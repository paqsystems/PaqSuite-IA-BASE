---
name: generar-fixtures-postman-integracion
description: Genera cuerpos JSON reales para probar en Postman las APIs de importación de maestros y transacciones de PedidosWeb, leyendo la base configurada en backend/.env y separando los archivos por empresa activa y recurso. Usar cuando se solicite preparar datos reales de DEMO para probar altas, bajas, modificaciones, snapshots o deltas.
disable-model-invocation: true
---

# Generar fixtures reales para Postman

## Objetivo

Preparar payloads JSON de prueba con los datos actualmente existentes en la base configurada por `backend/.env`. Los payloads son cuerpos HTTP para:

- `POST /api/v1/integracion/maestros/{recurso}`;
- `POST /api/v1/integracion/transacciones/{recurso}`.

La skill solo lee datos y escribe archivos locales. No modifica la base, no llama los endpoints de importación y no altera empresas, maestros ni transacciones.

## Carpeta de salida

Usar siempre:

```text
backend/storage/app/postman/integracion/
```

Cada ejecución debe crear una subcarpeta nueva:

```text
backend/storage/app/postman/integracion/<YYYYMMDD-HHmmss>/
├── manifest.json
└── <empresa>/
    ├── maestros/
    │   ├── provincias-001.json
    │   ├── condventa-001.json
    │   └── ...
    └── transacciones/
        ├── stock-001.json
        ├── deuda-001.json
        └── ...
```

El nombre de `<empresa>` debe ser seguro para Windows. Preferir el código de `X-Paq-Cliente`; si no existe, usar un identificador compuesto estable y documentarlo en `manifest.json`.

Al terminar **siempre** informar textualmente:

```text
Carpeta generada: backend/storage/app/postman/integracion/<YYYYMMDD-HHmmss>/
```

También informar la cantidad de empresas, recursos y archivos generados, además de los recursos omitidos y el motivo.

## Flujo obligatorio

### 1. Confirmar alcance y entorno

1. Leer `backend/.env` sin imprimir secretos.
2. Identificar `DB_CONNECTION`, `DB_HOST`, `DB_PORT`, `DB_DATABASE` y el esquema configurado.
3. Verificar que la base sea la que el usuario pidió usar. Si el nombre parece una base compartida o de producción, pedir confirmación antes de extraer datos.
4. No ejecutar comandos destructivos ni de bootstrap. Esta skill nunca necesita `DROP`, `TRUNCATE`, `migrate:fresh`, `bootstrap-pedidosweb-dev` ni seeds.
5. No imprimir `DB_PASSWORD`, tokens, claves de API ni contenido completo de `.env`.

### 2. Descubrir empresas activas

Consultar de forma segura la tabla/catálogo de empresas usado por el proyecto y determinar:

- código de tenant que debe viajar en `X-Paq-Cliente`;
- descripción/nombre para el `manifest.json`;
- estado activo;
- base/conexión asociada, si el modelo la utiliza;
- si la empresa pertenece al entorno DEMO.

Si el catálogo no tiene un campo inequívoco para “activa” o “DEMO”, detenerse y pedir el criterio exacto. No asumir que una empresa es activa por tener filas en tablas de negocio.

La extracción debe hacerse para **cada empresa activa**. Si las empresas están separadas por conexión, cambiar únicamente la conexión indicada por el catálogo; no reutilizar datos de una empresa en otra.

### 3. Obtener contrato vigente

Antes de extraer datos, leer:

- `backend/config/integracion_maestros.php`;
- `backend/config/integracion_transacciones.php`;
- handlers y requests de integración;
- documentación `docs/02-producto/PedidosWeb/APIs-Importacion-datos-maestros.md` y `APIs-Importacion-transacciones.md`.

Usar el contrato vigente del código como autoridad para:

- recursos habilitados;
- nombres camelCase;
- campos requeridos;
- claves naturales;
- modo permitido;
- orden de carga;
- campos que no deben viajar.

No inventar propiedades a partir de columnas SQL. Si una columna no tiene mapeo contractual, no incluirla.

### 4. Leer datos sin modificar la base

Usar el acceso SQL configurado en `backend/.env` y consultas parametrizadas de solo lectura. Aplicar `READ UNCOMMITTED`/`NOLOCK` únicamente para esta extracción si es compatible con la configuración del proyecto; registrar en el manifest que la lectura fue no bloqueante.

Reglas:

- nunca concatenar valores del usuario en SQL;
- nunca ejecutar `INSERT`, `UPDATE`, `DELETE`, `MERGE`, `TRUNCATE`, `DROP`, DDL ni procedimientos de escritura;
- no usar `WHERE IN` con listas de tamaño incierto;
- para relaciones grandes, usar `JOIN`, `EXISTS`, paginación o consultas por clave;
- verificar el conteo y las claves naturales antes de serializar;
- respetar el tenant/empresa al consultar;
- si la tabla o campo esperado no existe, marcar el recurso como `omitido` y explicar el motivo.

Si el repositorio dispone de un procedimiento almacenado oficial de lectura/exportación para un recurso, preferirlo. No crear ni desplegar procedimientos desde esta skill.

### 5. Construir lotes

Cada archivo debe tener la forma contractual:

```json
{
  "modo": "delta",
  "fechaProceso": "YYYY-MM-DDTHH:mm:ss-03:00",
  "origen": "postman-fixture-db",
  "items": []
}
```

Reglas de generación:

- `fechaProceso` es la fecha/hora de generación en zona `America/Argentina/Buenos_Aires`;
- usar `snapshot` para recursos cuyo contrato lo permita y cuyo contenido represente el universo actual;
- usar `delta` para `historial-ventas` y para relaciones o recursos sin snapshot;
- no generar snapshot vacío;
- no generar un recurso con `items` vacío salvo que el usuario lo pida expresamente para probar el rechazo;
- respetar el máximo vigente de `1500` ítems por lote;
- si un recurso supera el máximo, dividirlo en `-001`, `-002`, etc.;
- preservar el orden contractual de carga;
- conservar fechas, decimales, booleanos y valores nulos con tipos JSON correctos;
- no incluir `codLogin`, credenciales, tokens, contraseñas ni datos que el contrato prohíba;
- no modificar ni anonimizar los valores: el objetivo es reproducir el estado real de la base para DEMO.

Para recursos relacionados, mantener únicamente filas que tengan sentido para la empresa y conservar las claves naturales tal como están en la base. En escalas, respetar la estructura anidada `valores[]` definida por el contrato.

### 6. Validar antes de finalizar

Para cada archivo:

1. validar sintaxis JSON;
2. validar que exista `modo`, `fechaProceso` e `items`;
3. validar que `items` sea un array;
4. validar el máximo de 1500;
5. validar campos requeridos y tipos;
6. validar unicidad de la clave natural dentro del archivo y entre sus partes;
7. comprobar que el recurso y la empresa del path coincidan con el manifest;
8. comparar el conteo extraído con el conteo serializado;
9. comprobar que no se haya escrito fuera de la carpeta de salida.

Si existen filas inválidas, no corregirlas silenciosamente. Generar el archivo solo con filas contractualmente válidas y registrar en `manifest.json`:

- cantidad total leída;
- cantidad exportada;
- cantidad omitida;
- claves o índices omitidos;
- motivo de cada omisión.

### 7. Manifest

Crear `manifest.json` con:

- timestamp de generación;
- base usada, sin contraseña;
- conexión y host, sin credenciales;
- empresas activas consideradas;
- código tenant por empresa;
- recursos generados;
- modo y cantidad de ítems por archivo;
- SHA-256 de cada archivo;
- omisiones y advertencias;
- confirmación de que la operación fue de solo lectura.

No incluir en el manifest el contenido de `DB_PASSWORD`, tokens ni headers `Authorization`.

## Referencia de recursos

Maestros esperados:

`provincias`, `condventa`, `transportes`, `perfiles`, `vendedores`, `listaprecios`, `escalas`, `articulos`, `listaprecios-articulos`, `descuentocantidad`, `clientes`, `clientes-direcciones`, `clientes-contactos`, `parametros`.

Transacciones esperadas:

`stock`, `deuda`, `cheques`, `historial-ventas`.

La lista real siempre debe salir de los archivos de configuración y handlers vigentes. Si un recurso está configurado pero no puede mapearse de forma segura a datos existentes, informarlo como omitido; no fabricar ejemplos.

## Resultado al usuario

La respuesta final debe ser breve y contener:

1. estado de generación;
2. empresas procesadas;
3. recursos y archivos creados;
4. advertencias/omisiones;
5. la ruta exacta, recordada obligatoriamente:

```text
Carpeta generada: backend/storage/app/postman/integracion/<YYYYMMDD-HHmmss>/
```

No afirmar que los JSON fueron probados contra la API si la skill solo los generó. La prueba en Postman queda a cargo del usuario.
