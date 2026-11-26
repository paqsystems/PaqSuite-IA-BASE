# Coordinación de concurrencia — ERP ↔ sistemas externos

| Campo | Valor |
|-------|--------|
| **Ámbito** | PaqSuite-IA-BASE — patrón reutilizable |
| **Aplica a** | Integraciones bidireccionales (portal, TMS, etc.), procesos manuales + GEN-13 |
| **Tenancy** | Estado de coordinación **por empresa** (`companyId` / `X-Company-Id`) |
| **Implementación de referencia** | PedidosWeb → `docs/02-producto/PedidosWeb/Integracion-con-Pedidos-Web.md` (TANGO) |

---

## 1. Problema

En integraciones ERP ↔ producto externo suelen coexistir:

- Varios **operadores** en el ERP (misma empresa).
- **Jobs** programados (GEN-13).
- **Usuarios** en el sistema remoto editando los mismos datos.
- Procesos **largos** (lotes, ack por API) que superan ventanas de tiempo fijas.

Los antipatrones (semáforos en parámetros globales, bloqueo SQL directo, un solo timer para todo) generan carreras, locks colgados y ventanas mal calculadas al entrar tarde a una pantalla.

Este documento define un **modelo de tres mecanismos** + **vencimiento efectivo** + **liberación explícita**, reutilizable por cada módulo.

---

## 2. Tres mecanismos (separar siempre)

| ID | Nombre | Propósito | Típicamente inicia |
|----|--------|-----------|-------------------|
| **M1** | **Ventana de coordinación remota** | Señal al sistema externo de que el ERP está en fase de **consulta/descarga** de datos sensibles | Primera **bajada** exitosa (HTTP/API) del ciclo |
| **M2** | **Lease de escritura** | Un solo **writer** en el ERP (grabación, mutación local) | Confirmación **Procesar** o inicio de fase de grabación del job |
| **M3** | **Inactividad de UI** | No dejar pantallas abiertas sin uso; **no** sustituye M1 ni M2 | Última acción del operador en la pantalla (excepto durante M2 activo) |

Además, en el **sistema remoto** pueden existir reglas propias (p. ej. estado “en edición”, timeouts de sesión). El ERP **debe respetarlas** además de M1–M3.

**Persistencia MUST:** M1 y M2 en tablas/servicio backend por **empresa** (no en `PQ_PARAMETROS_GRAL` como semáforo único).

---

## 3. Ciclo de vida (estado por empresa)

```text
IDLE ──(primera bajada)──► COORDINACION_ABIERTA ──(Procesar)──► GRABACION (lease)
     ◄──(liberación)───────                    ◄──(fin ack)────
```

| Estado | M1 activo | M2 activo | Cómo se entra | Cómo se sale |
|--------|-----------|-----------|---------------|--------------|
| **IDLE** | No | No | Inicial; tras liberación completa | Primera bajada → COORDINACION_ABIERTA |
| **COORDINACION_ABIERTA** | Sí (hasta `venceEfectivo`) | No | Primera bajada del ciclo | Procesar → GRABACION; o **liberar** (§5) |
| **GRABACION** | Sí (extendido) | Sí | Lease adquirido | Fin fase importación (§6); o abortar + liberar |

---

## 4. Ventana de coordinación (M1)

### 4.1 Inicio

- Se fija `fechaInicioControl` en la **primera bajada exitosa** del ciclo (no al abrir pantalla, no al **Procesar**).
- **Alcance:** una fila (o registro equivalente) **por empresa**.

### 4.2 Ancla fija (entrar tarde)

Mientras el ciclo siga vigente:

```text
venceNominal = fechaInicioControl + MinutosBloqueo
restanteUI   = venceEfectivo > ahora ? (venceEfectivo - ahora) : 0
             // solo si la ventana sigue vigente; nunca reiniciar Bloqueo completo al entrar tarde
```

Bajadas/refrescos posteriores **no** mueven `fechaInicioControl`. Si `venceEfectivo <= ahora` **sin** lease M2, tratar ventana vencida y **liberar** M1 (§5); la UI muestra **0** o estado “vencido”, no valores negativos.

### 4.3 Vencimiento efectivo (grabación larga)

Durante **M2 (lease)**:

```text
venceEfectivo = max(venceNominal, finFaseImportacionEstimado)
```

Al adquirir lease, el backend **prorroga** M1 hasta el fin de la fase de importación definida en el módulo (§6). Así no expone el remoto mientras el ERP sigue grabando/ack.

**Durante M2:** **no** aplicar M3 (aviso/cierre por inactividad de pantalla).

### 4.4 Nuevo ciclo (sin la regla “A4” problemática)

**No** abrir un ciclo nuevo solo porque pasó `venceNominal` y alguien refrescó en background.

Nuevo `fechaInicioControl` solo si:

1. Estado empresa = **IDLE** (M1 y M2 liberados según §5), **y**
2. El usuario o job ejecuta una **bajada** intencional (carga/refresco que llama al remoto).

Tras fin de importación de A, si B baja 2 minutos después → nuevo ciclo (nuevo `fechaInicioControl`).

---

## 5. Liberación de M1 (obligatoria)

Limpiar coordinación remota **y** pasar a IDLE cuando ocurra cualquiera de:

| Evento |
|--------|
| Fin normal de la **fase de importación** del módulo (§6) |
| Cierre de pantalla / **navegación fuera** del proceso |
| Cierre de **browser** o pérdida de sesión (backend detecta desconexión o TTL de pantalla) |
| **Cancelación** explícita |
| Aborto de grabación con política de liberación acordada en el módulo |
| Expiración de `venceEfectivo` **sin** lease activo (solo consulta colgada) |

**No** dejar M1 activo indefinidamente tras cerrar la pantalla (decisión BASE).

Liberar M2 en `finally` al terminar o abortar grabación.

---

## 6. Fase de importación vs fases posteriores

Cada módulo **MUST** declarar qué incluye la fase que extiende M1 bajo lease:

| Incluir en fase importación (ejemplo PedidosWeb) | Excluir (proceso aparte) |
|------------------------------------------------|-------------------------|
| Grabación en ERP (Tango, etc.) | Reconciliaciones masivas de estados tardíos |
| **Ack** al remoto por ítem (estado 1/2, ids, etc.) | Jobs de sync que no compiten con “ingresados” |
| Idempotencia pre-commit por clave de negocio | |

PedidosWeb: **1/2 → 3** según `GVA21` = **otro menú**, GEN-13 propio, invocable desde botón en importación **sin** prolongar M1/M2 del lote actual.

---

## 7. Lease de escritura (M2)

| Regla |
|-------|
| Un lease **activo por empresa** para la operación de grabación acordada |
| Segundo **Procesar** (u operación equivalente) → rechazo con titular y hora |
| Consulta/refresco **sin** lease → permitido salvo restricción propia del módulo |
| Job vs manual: mismo lease; excluyentes |
| Pre-commit **por ítem** antes de persistir (idempotencia) |
| Resultado **por fila** en UI manual |

---

## 8. Inactividad de pantalla (M3)

Solo en fase **sin lease** (COORDINACION_ABIERTA o pantalla previa a Procesar):

- **Inactividad** = no **Procesar**, no **salir**, sin acciones que reinician el timer (refrescar, tildar, etc.).
- Tras `MinutosBloqueo` de inactividad → aviso `MinutosAviso` → cierre de pantalla.
- Cierre por M3 debe disparar **liberación M1** si no hay lease (§5).

**Procesar** (éxito o “otro procesando”) reinicia M3.

---

## 9. Matriz de situaciones (plantilla — gate SPEC)

**Prerrequisito Open-Spec:** ningún SPEC/TR que implemente M1–M3 en un módulo puede abrirse hasta tener la matriz del producto **cerrada** en este formato (copiar filas S1–S16 y completar columnas portal y UX).

Columnas obligatorias: **Situación → Acción ERP → Acción portal/remoto → Qué ve el usuario** (operador ERP; si aplica, operador remoto entre paréntesis).

Estado / M1 / M2: derivar de §3 (no repetir en la tabla salvo anotaciones en Acción ERP).

| # | Situación | Acción ERP | Acción portal / remoto | Qué ve el usuario |
|---|-----------|------------|-------------------------|-------------------|
| S1 | Abre pantalla de integración, **sin** primera bajada | Montar UI; no crear/actualizar registro de coordinación | Sin cambio en señal de “descarga/consulta activa” | Grilla vacía o datos locales; **sin** cuenta regresiva ni bloqueo remoto |
| S2 | Primera bajada exitosa del ciclo (IDLE → COORD) | `fechaInicioControl = T0`; activar **M1**; persistir por empresa; exponer `venceEfectivo` / `restanteUI` | Activar regla remota equivalente a §21 (descarga ERP en curso) | Grilla cargada; **countdown** = `venceEfectivo - ahora` si `venceEfectivo > ahora`; aviso de ventana activa |
| S3 | **Refrescar** / bajada repetida con M1 vigente | `GET` datos; **no** mover `inicio`; recalcular `restanteUI` | Mantener señal M1 | Datos actualizados; **mismo** tiempo restante |
| S4 | Segundo operador entra **tarde** al mismo ciclo | Leer mismo registro empresa; **no** reiniciar `MinutosBloqueo` | Igual que S3 | Mismos pedidos; countdown **residual** (ej. 15 min, no 30) |
| S5 | **Procesar** con lease libre | Adquirir **M2**; `venceEfectivo = max(T0+Bloqueo, finFase)`; **desactivar M3** | Mantener/fortalecer protección sobre ítems en conflicto | Barra de lote; titular del lease; **sin** cierre por inactividad de pantalla |
| S6 | **Procesar** con lease de otro | Rechazar grabación (409/conflict); **no** tomar M2; reiniciar **M3** del solicitante | Sin cambio | Mensaje “otro usuario/job procesando” + identificación; puede refrescar |
| S7 | Grabación supera `T0 + MinutosBloqueo` | M1 sigue hasta fin fase; M2 hasta ack; sin M3 | Señal vigente hasta liberación post-ack | Countdown alineado a `venceEfectivo` extendido; (web) no editar ingresados bloqueados |
| S8 | **Fin** fase definida (ack remoto OK del lote) | Liberar **M1+M2**; resultado **por fila**; estado IDLE | Estados contrato (ej. 1/2); quitar señal descarga | Resumen de lote; iconos/estados por fila; **sin** countdown M1 |
| S9 | Cierre pantalla / cambio de ruta / cierre browser | `finally` + beacon: liberar M1; liberar M2 solo si no grababa; limpiar señal remota | Fin inmediato de §21 / equivalente | Al salir: —; otros en empresa: pueden abrir nuevo ciclo |
| S10 | Tras liberación (IDLE), **nueva** bajada intencional | Nuevo `T0`; nuevo M1 (no reutilizar ciclo anterior) | Nueva ventana remota | Countdown **desde cero** |
| S11 | Job GEN-13 vs operador manual | **Mismo** lease por empresa; exclusión mutua | Según contrato | Manual: mensaje si job tiene lease; job: skip o error programado claro |
| S12 | Ítem ya persistido (idempotencia) | Pre-commit: omitir; código `omitidoYaIngresado` | Sin ack duplicado | Fila marcada con motivo; lote continúa |
| S13 | Proceso **posterior** al ingreso (reconciliación, otro estado) | Menú/job **aparte**; lease/coord **propio**; **no** extender M1/M2 del ingreso | Actualizar estados remotos (ej. 3) | Botón/menú dedicado; importación en curso **no** depende de este paso |
| S14 | `venceEfectivo <= ahora` **sin** M2 | Liberar M1; limpiar señal; IDLE; `restanteUI = 0` | Fin protección descarga | Aviso “ventana vencida”; **no** valores negativos en UI |
| S15 | **Refrescar** tras S14 (bajada explícita en IDLE) | Tratar como **S2** (nuevo ciclo); **no** abrir ciclo solo por timer JS automático | Nueva señal según S2 | Nuevo countdown; regla A4 descartada |
| S16 | **M3** inactividad (solo COORD, sin M2) | Tras `MinutosBloqueo` inactivo → aviso `MinutosAviso` → cerrar pantalla → **S9** | Liberar señal con S9 | Modal de aviso; cierre si no hay acción válida (Procesar/refrescar/etc. reinicia M3) |

---

## 10. Contratos técnicos (checklist implementación)

- [ ] Tabla `*CoordinationControl` por `companyId` (`inicio`, `venceEfectivo`, `leaseHolder`, `estado`, `modo`, `ultimoHeartbeat` si aplica).
- [ ] Endpoint o mecanismo para que el **remoto** consulte “descarga activa” (parametro §21, header, API dedicada).
- [ ] API pantalla: `restanteSegundos`, `estado`, `leaseHolder`.
- [ ] Liberación en `finally` + hooks cierre SPA (`beforeunload` / beacon).
- [ ] Tests: dos operadores, grabación larga, cierre browser, idempotencia.

---

## 11. Referencias por producto

| Producto | Documento |
|----------|-----------|
| PedidosWeb (TANGO) | `PaqSuite-IA-TANGO` → `docs/02-producto/PedidosWeb/Integracion-con-Pedidos-Web.md` |
| PedidosWeb (portal §21) | `PaqSuite-IA-PedidosWeb` → definición conceptual §21 |

Al abrir una épica de integración, el TR **MUST** enlazar este documento y **adjuntar o citar** la matriz §9 del producto (4 columnas) como artefacto validado **antes** del SPEC.