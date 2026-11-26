# HU-PQ-MOB-04 — Menú API y exclusiones mobile (shell piloto)

| Campo | Valor |
|-------|--------|
| **ID** | HU-PQ-MOB-04 |
| **Depende de** | [HU-PQ-MOB-03](./HU-PQ-MOB-03-kardex-demo-api-mono.md) |
| **Estado** | **Pendiente de Revisión** |
| **TR** | [TR-PQ-MOB-04-menu-exclusiones-shell.md](./TR-PQ-MOB-04-menu-exclusiones-shell.md) |

## Narrativa

Como **usuario mobile autenticado**, quiero **ver el menú del backend sin opciones prohibidas en mobile** (admin, pivot, excel), para **navegar solo a procesos piloto permitidos**.

## Criterios de aceptación

- [x] **CA-01:** `GET /api/v1/user/menu` con Bearer + tenant + company.
- [x] **CA-02:** Filtro client-side exclusiones GEN-22 (admin, pivot, excel-import).
- [x] **CA-03:** Drawer con `data-testid` equivalentes (`menuDrawer`, `menuItem-*`).
- [x] **CA-04:** Ruta `/demo-grid` abre kardex piloto.