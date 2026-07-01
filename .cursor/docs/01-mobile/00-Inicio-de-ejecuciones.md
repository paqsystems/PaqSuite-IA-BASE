# Inicio de ejecuciones — versión Mobile (PedidosWeb)

Checklist rápido tras **reiniciar la PC** o iniciar una sesión de prueba. Detalle completo en los runbooks BASE.

| Documento | Uso |
|-----------|-----|
| [05-runbook-primera-prueba-android-emulador.md](./05-runbook-primera-prueba-android-emulador.md) | Smoke app + backend |
| [06-instalacion-emulador-android-studio.md](./06-instalacion-emulador-android-studio.md) | Device Manager, credenciales §10 |

---

## 1. Prerrequisitos

- [ ] **VPN** conectada si el SQL Server está en red privada (login requiere SQL; health no).
- [ ] Emulador **Pixel 6 API 34** encendido (Device Manager → ▶ Play) **o** usar Run ▶ de Android Studio.
- [ ] Proyecto abierto: `{repo}/frontend/android`.

---

## 2. Terminal A — Backend (dejar abierta)

```powershell
cd C:\Programacion\PaqSuite-IA-PedidosWeb\backend
php artisan serve --host=0.0.0.0 --port=8088
```

Verificar en navegador PC: `http://localhost:8088/api/v1/health` → `"status":"up"`.

> **Error frecuente:** «No se pudo conectar» en la app con la base OK → falta este servidor HTTP (no es lo mismo que SQL).

---

## 3. Terminal B — Frontend (solo si hubo cambios de código)

```powershell
cd C:\Programacion\PaqSuite-IA-PedidosWeb\frontend
npm run build:mobile
npx cap sync android
```

---

## 4. Android Studio

1. Gradle sync terminado.
2. Dispositivo: **Pixel 6 API 34** (o el AVD creado).
3. **Run ▶** verde (`Shift+F10`) — no usar solo el botón Power del panel emulador.

---

## 5. Config API (si no quedó guardada)

1. Pantalla login → **engranaje**.
2. URL: `http://10.0.2.2:8088/api/v1`
3. **Probar conexión** → éxito → **Guardar**.

---

## 6. Login

| Campo | Valor |
|-------|--------|
| Empresa (tenant) | `desarrollo` |
| Usuario | `supervisor.mvp` |
| Contraseña | `ChangeMeInLocalEnv` |

---

## 7. Qué validar en la app (v1 + v2)

### Base (v1)

- [ ] Landing en **Consulta de stock** (kardex).
- [ ] Filtro: escribir texto → **Enter** → resultados y «Mostrando X de Y».
- [ ] **Scroll** de la lista: en emulador, clic + arrastrar (la rueda del mouse suele no funcionar).
- [ ] Menú **☰** en el **header derecho** → backdrop cierra el menú.
- [ ] Tap en tarjeta → detalle popup.

### v2 (`v1.2.1-mobile`) — si el build incluye menú ampliado

- [ ] Menú muestra **consultas y listados** según permiso (no solo Stock).
- [ ] Probar al menos: **Deuda**, **Pedidos ingresados**, **Presupuestos ingresados**.
- [ ] **Parámetros** y **Logs integración** si aparecen en menú.
- [ ] **Carga pedidos** no debe estar en menú (v3).

---

## 8. Referencias cierre F

| Release | F1 / D | F formal |
|---------|--------|----------|
| v1 `v1.2.0-mobile` | [D-VERIFICACION v1](../../04-tareas/101-PedidosWeb/D-VERIFICACION-101-17-mobile-v1.md) | [F-101-17-cierre-formal](../../04-tareas/101-PedidosWeb/F-101-17-cierre-formal.md) |
| v2 `v1.2.1-mobile` | [D-VERIFICACION v2](../../04-tareas/101-PedidosWeb/D-VERIFICACION-101-17-mobile-v2.md) | [F-101-17-cierre-formal-v2](../../04-tareas/101-PedidosWeb/F-101-17-cierre-formal-v2.md) |

Tags Git pendientes smoke **iOS**.
