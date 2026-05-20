# CHATBOT_TANGO.md — Base de conocimiento Q&A (Tango Gestión / Axoft)

Este archivo sintetiza respuestas coherentes con la documentación de ayuda de **Tango Gestión** (referencia **24AR**) contenida en el repositorio bajo `.cursor/docs/axoft_md`. Sirve como material de entrenamiento o respuesta guiada para un chatbot sobre operativa del sistema.

**Nota:** Los nombres de menús y procesos corresponden a la ayuda oficial; en implementaciones concretas puede haber variaciones por versión o personalización.

---

## Preguntas y respuestas (50 + subpreguntas 7.a–7.c y 15.a)

### 1. ¿Qué recomienda la ayuda antes de operar Compras si la empresa usa Contabilidad?

Debe definir y completar la configuración contable **antes** de operar en Compras: monedas (corriente y extranjera contable), cuentas contables, tipos de asiento, auxiliares, reglas de apropiación, parámetros contables de Compras, modelos de asiento y parametrización por tipo de comprobante (y opcionalmente por proveedor, artículo, conceptos o tipo de gasto).

### 2. ¿Cuáles son los escenarios típicos de integración contable entre Compras y Contabilidad?

Hay cuatro variantes principales: (1) asiento al ingresar el comprobante y exportación a la **misma** base; (2) sin asiento al ingresar, generación masiva posterior y exportación a la misma base; (3) asiento al ingresar y exportación a **otra** base con importación en Contabilidad; (4) sin asiento al ingresar, generación masiva, exportación a otra base e importación.

### 3. Si activo “Genera asiento en el ingreso del comprobante” en Compras, ¿cuándo se genera el asiento?

Al ingresar factura, nota de débito o nota de crédito se genera el asiento correspondiente. Si el perfil o tipo de comprobante permite modificar el asiento en el ingreso, al finalizar la carga se abre la pantalla del asiento; si no, el asiento se genera igualmente pero sin abrir esa pantalla.

### 4. ¿En qué moneda se genera el asiento de compras respecto del comprobante?

El asiento se genera **siempre en la moneda del comprobante**: si el comprobante es en moneda corriente, el asiento en moneda corriente; si es en moneda extranjera, en moneda extranjera (la extranjera contable es la definida como habitual en Procesos generales).

### 5. ¿Puedo grabar un asiento de compras desbalanceado?

No. El sistema **no permite grabar asientos desbalanceados**, esté o no abierta la pantalla de asiento en el ingreso.

### 6. Si no genero asiento al ingresar el comprobante en Compras, ¿cómo genero los asientos pendientes?

Se debe ejecutar el proceso **Generación de asientos contables**, que filtra comprobantes sin asiento y los procesa masivamente según modelo y parametrización. Al finalizar muestra cantidad generada y una grilla con comprobantes con problemas; con doble clic se accede a modificación de comprobantes para corregir y volver a intentar.

### 7. ¿Dónde puedo modificar o completar el asiento de un comprobante de compras ya ingresado?

Desde **Modificación de comprobantes** puede modificar el asiento generado, generar el asiento pendiente o ajustar lo necesario según permisos y configuración.

### 7.a) ¿Qué pasos debo seguir para que al cargar una factura de conceptos ya aparezca el asiento contable y balanceado al terminar la carga?

Según la guía de integración contable en Compras: **(1)** En Procesos generales, definir **monedas** (corriente y extranjera contable donde aplique), **parámetros contables** con moneda extranjera habitual, y cargar **cuentas**, **tipos de asiento**, **auxiliares** y **reglas de apropiación** habilitadas para Compras. **(2)** En **Parámetros contables de Compras**, activar **Genera asiento en el ingreso del comprobante** (si no está activo, la factura se graba sin asiento y habría que usar Generación de asientos contables después). **(3)** Definir **modelos de asiento** y **parametrización contable por tipo de comprobante** que use la factura de conceptos. **(4)** Completar parametrización por **conceptos** y, si corresponde, por **proveedor** (el asiento se arma desde modelo y/o conceptos y proveedor; si el renglón reemplaza cuenta, usa la del concepto o proveedor). **(5)** Si el **perfil de facturación** o **tipo de comprobante** permiten modificar el asiento en el ingreso, al terminar la carga se abre la pantalla del asiento para completar **auxiliares/apropiaciones** cuando la cuenta lo exija; si no lo permiten, el asiento se genera igual pero sin abrir esa pantalla. **(6)** El sistema **solo permite grabar asientos balanceados**; debe completarse lo que falte hasta cuadrar.

### 7.b) ¿Cómo se completa un modelo de asiento de Compras en la solapa “Cuentas contables”?

En **Parametrización contable en Compras – Modelos de asientos**, esa solapa define el **cuerpo del asiento** (renglones). El sistema **habilita los tipos contables** según el **tipo de comprobante** elegido en la solapa Principal. En **Detalle del modelo**: **Nro** de renglón (no editable); **Código de cuenta** (cuenta habilitada para Compras); **Descripción** automática; **D/H** (debe/haber habitual, por defecto según saldo habitual de la cuenta); **Tipo contable** propuesto por el sistema; **Leyenda** automática del tipo contable (opcional, editable); **Reemplaza** (solo tipos que lo permitan; en Compras la ayuda cita **TO**, **SB** y **EX**) para tomar cuenta del proveedor / artículos / conceptos al generar el asiento; **Edita cuenta** (por defecto no) para poder cambiar la cuenta al generar el asiento en el ingreso. Si la cuenta usa auxiliares, en **Detalle de apropiaciones** (opcional) se cargan tipo de auxiliar **manual** y **regla de apropiación** para Compras; la regla del modelo prevalece sobre la del tipo de auxiliar.

### 7.c) ¿Qué “tipos contables” pueden existir en modelos de asiento de Compras?

La ayuda indica que **el sistema habilita y propone** los tipos contables **según el tipo de comprobante** asociado al modelo (factura, nota de débito y/o nota de crédito en Principal); **no trae en estos extractos una tabla cerrada de todos los códigos** posibles por cada combinación — conviene ver la columna en el proceso **Modelos de asientos** o la ayuda en línea vinculada a ese proceso.

Con texto explícito en la documentación mirrorada para Compras: **TO**, **SB** y **EX** son los tipos para los que puede activarse **Reemplaza** (reemplazo de cuenta por proveedor / artículos / conceptos). Además: si el **artículo o concepto no tienen cuenta** definida para Compras y está activo el parámetro correspondiente, se usa la cuenta del modelo en tipo **SB** o **EX**; para **proveedor ocasional** sin datos completos, el asiento puede tomar la cuenta genérica del tipo **TO** según el tipo de asiento utilizado (**Parámetros de Compras**).

### 8. ¿Los movimientos de tesorería de Compras usan la parametrización de Compras o de Tesorería?

Los movimientos de tesorería (órdenes de pago, cancelación de documentos, cancelación de facturas de crédito) toman la parametrización establecida en el módulo **Tesorería**.

### 9. ¿Qué pasos previos ante AFIP exige la ayuda para comprobantes electrónicos en Ventas?

Gestionar **clave fiscal nivel 3**, obtener **certificado digital** (se sugiere el asistente Pedido de certificado digital / AxCertSetup en la carpeta de instalación) y completar la **configuración en el sitio de AFIP** (punto de venta, administración de certificados, relación certificado–webservice).

### 10. El asistente de certificado genera archivos; ¿cuál se sube a AFIP como pedido?

Se indica como nombre de archivo el que tiene extensión **.req** (Request). Si AFIP devuelve error de Request inválido, la guía sugiere reinstalar OpenSSL, evitar espacios en nombre/alias y regenerar el .req.

### 11. ¿Qué valida el sistema antes de permitir cambiar la versión de webservices de facturación electrónica?

Valida que **no existan comprobantes electrónicos pendientes de obtener CAE**. Si los hay, debe usarse **Administración de Comprobantes Electrónicos** para obtener CAE de pendientes/rechazados; recién después cambiar la versión en Parámetros de Ventas.

### 12. Al pasar a versión 2 de webservices, ¿qué datos hay que codificar en el sistema?

Además del cambio en Parámetros de Ventas, desde **Alícuotas** debe indicarse el código de tributo AFIP por alícuota y, si aplica **Percepciones definibles**, el código habilitado por AFIP para cada una.

### 13. ¿Para qué sirve el circuito de “comprobantes con diferencias” en Compras?

Detecta diferencias por **precio** (facturado mayor al de lista o bonificación menor) y por **cantidad** (cantidad facturada mayor a la recepcionada en Factura-Remito o remitos), para evitar pagar de más si no se corrige.

### 14. ¿Qué diferencia hay entre control “Flexible” y “Estricto” de diferencias?

**Flexible**: avisa la diferencia y permite seguir (el comprobante puede quedar marcado con diferencia). **Estricto**: avisa y **no permite continuar** hasta salvar/corregir la diferencia.

### 15. ¿Una factura con diferencias puede pagarse?

**No.** Mientras tenga diferencia de precio o cantidad **no podrá ser pagada**; al intentar pagar el sistema informa la situación.

### 15.a) Hay una factura de compras que figura pendiente de cancelar, pero en Pagos no aparece. ¿Por qué puede ser?

La ayuda no enumera una única causa; conviene revisar según la documentación de Compras y cuenta corriente: **(1)** Si tiene **diferencias** de precio o cantidad, **no puede pagarse** hasta resolverlas (coherente con la pregunta 15). **(2)** Con **“Requiere autorización para el pago”** activo, puede hacer falta autorizar en **Autorización de comprobantes a pagar** y los **perfiles** limitan por importes antes de que el comprobante siga el circuito habitual de **Pagos**. **(3)** Si la factura se cargó como **contado** (p. ej. condición sin el vencimiento mínimo que la ayuda asocia a cuenta corriente), el circuito no es el mismo que **Pagos** para cuenta corriente. **(4)** Si entrás a **Pagos** con **perfil para pagos**, las cuentas de tesorería del proveedor deben estar **habilitadas en ese perfil**; si no, puede impedirse operar con ese perfil. **(5)** En **factura de crédito electrónica** puede exigirse **aceptación** y pasos en AFIP antes del pago. **(6)** En **gestión central/sucursales**, el comprobante puede estar en otra sucursal y debiera exportarse/importarse (p. ej. Tangonet o transferencias) para pagarlo donde corresponda.

### 16. ¿Cómo se pueden resolver diferencias en facturas según la guía?

Una vía es el reclamo de **nota de crédito** del proveedor; también pueden eliminarse manualmente las diferencias desde **Modificación de comprobantes**. Las de remitos asociados pueden tratarse con la función **Dif. en Remitos**.

### 17. ¿Qué necesito para que el control de diferencias por precio funcione?

Debe existir **lista de precios** para el proveedor y artículos involucrados y el comprobante debe usar esa lista.

### 18. ¿Qué hace el proceso “Depreciación de bienes” en Activo Fijo?

Calcula la depreciación por tipo de valoración para los bienes seleccionados; permite definir ejercicio, período y, si se activa “Genera movimiento de depreciación”, el tipo de movimiento interno Depreciación y si la generación es **según frecuencia** del bien o **según fecha del proceso**.

### 19. ¿Qué condiciones exige Activo Fijo para generar movimientos de depreciación?

Ejercicio **abierto**, período dentro del ejercicio, bienes parametrizados para depreciar y con movimientos en el período según corresponda.

### 20. ¿Qué permite modificar “Modificación de comprobantes de Ventas” en todos los tipos?

Entre otros (según tipo y restricciones): **observaciones**, **código de vendedor**; en facturas/créditos/débitos no electrónicos la **fecha de emisión** si no afectaron stock y cumplen fechas de cierre; en electrónicos hay reglas adicionales según stock y PPP.

### 21. ¿Cómo accedo al asiento contable desde la modificación de un comprobante de ventas?

Con **Ctrl + F5** se accede a modificar el asiento contable cuando integra con Contabilidad y las condiciones lo permiten (por ejemplo asiento no transferido según campo).

### 22. ¿Qué ocurre si cambio la condición de venta en una factura modificada?

Si pasa de una condición que **no** genera fechas alternativas de vencimiento a una que **sí**, el sistema solicitará las fechas adicionales; si es al revés, al confirmar se **borran** las fechas alternativas de las cuotas.

### 23. ¿Qué es la Generación del pago masivo en Compras?

Lista pagos masivos ingresados/autorizados y parcialmente pagados; con doble clic se ve el detalle; el hipervínculo **Pagar** abre la generación que crea **una orden de pago por cada proveedor**, actualiza cuenta corriente, cancela/imputa comprobantes y genera movimientos en Tesorería si está instalado.

### 24. ¿Puedo usar distinto medio de pago por proveedor en el pago masivo?

Sí. Si tiene Tesorería puede elegir un medio único para todo el pago o **Ingresa medio de pago por proveedor** usando lo definido en Actualización de proveedores.

### 25. ¿Qué pasa si incluyo facturas con diferencias en el pago masivo?

Se cancelan igualmente en esa instancia. Si está activo **Elimina Diferencia al Pagar**, pasan a “Sin diferencias”; si no, la diferencia queda como **Resuelta**.

### 26. Si uso retenciones automáticas en pago masivo, ¿qué debo tener configurado en códigos de retención?

Debe definirse la **Cuenta de Tesorería por defecto** para cada retención; si no, el total puede asignarse a la cuenta configurada como **Medio de pago habitual**.

### 27. ¿El pago masivo respeta los perfiles de Tesorería?

La ayuda indica que el sistema **no tiene en cuenta** en este proceso los perfiles de Tesorería definidos.

### 28. ¿Qué tipos de impuesto pueden parametrizarse en el proceso Retenciones?

IVA, Ganancias, Ingresos brutos y Otras; para algunos tipos interviene código de provincia y régimen AFIP según corresponda.

### 29. ¿Sobre qué calcula la retención de IVA según la guía?

Se calcula sobre el total de IVA o importes gravados de cada factura imputada en los pagos (con posibilidad de agregar otros comprobantes en la orden de pago); el régimen contemplado corresponde a la **RG 3125** de DGI.

### 30. ¿Qué significa “Acumula pagos” en retenciones de Ganancias?

Con **‘S’** el cálculo considera pagos **acumulados del mes** por proveedor según RG 2784; con **‘N’** se calcula sobre cada pago sin acumular (RG 4343 Facturas de Crédito).

### 31. ¿Para qué sirve el vínculo entre retención RG 830 y RG 5762?

Cuando corresponda, el sistema calcula ambas retenciones de ganancias, **compara importes** y aplica **la mayor**, dejando la otra en cero.

### 32. ¿Qué es el CAEA y cuándo se usa?

El **CAEA** es autorización electrónica **anticipada** (contingencia: sin Internet o caída AFIP). Se solicita por **quincena** y el mismo número sirve para todas las facturas del período de vigencia; luego debe **informarse** a AFIP el detalle emitido.

### 33. ¿Cómo habilito CAEA en talonarios?

En definición de talonarios, solapa Comprobantes electrónicos, tipo de autorización **CAEA**. Se recomienda asociar un talonario CAEA a cada talonario CAE para cambiar rápido en contingencia.

### 34. ¿Qué hace la opción “CAEA activo”?

Asigna automáticamente el talonario CAEA vinculado al CAE habitual y muestra solo talonarios CAEA; para revertir, poner CAEA activo en No y puede usarse **Probar conexión** antes.

### 35. ¿Debo informar a AFIP si tuve CAEA pero no emití comprobantes?

Sí. Si solicitó CAEA **también debe informar** si en ese período no hubo emisión (CAEA no utilizado).

### 36. ¿Cuántos CAEA hay por contribuyente por quincena?

La AFIP otorga **un número CAEA por contribuyente**, no por punto de venta; todos los puntos usan el mismo número.

### 37. ¿Cuál es el circuito de Mis comprobantes AFIP en Compras?

Descargar desde AFIP los recibidos en Excel, importar en **Compras | Procesos periódicos | Mis comprobantes AFIP**, comparar con lo cargado en el sistema y obtener listados por estado; los pendientes de registrar y los con diferencia en fecha/monto quedan seleccionados para ayudar al alta desde facturas (menú Comprobantes AFIP o Ctrl+F11 si está habilitado por parámetros y perfil).

### 38. ¿Qué activo para ver Comprobantes AFIP en el alta de facturas?

En Parámetros de Compras: **Muestra comprobantes AFIP pendientes de registrar**; y si hay perfiles de factura, el mismo parámetro en cada perfil que corresponda.

### 39. ¿Qué logra “Generación de asientos contables de Activo Fijo”?

Genera asientos de movimientos de bienes en un rango de fechas para tener **subdiario de Activo Fijo** antes de exportar a Contabilidad; permite seleccionar sin contabilizar, contabilizados o transferidos y tipo de asiento (registración/anulación).

### 40. Si regenero asientos de Activo Fijo desde este proceso, ¿qué pierdo?

Si hubo cambios manuales en el mini-asiento desde **Registración de movimientos**, **se pierden** al regenerar desde este proceso (salvo las consideraciones específicas de cada caso según ayuda).

### 41. ¿Cómo prioriza Activo Fijo la cuenta contable al generar asientos?

Se usa el modelo del movimiento; si una cuenta tiene **Reemplaza**, se busca la cuenta particular del bien para ese tipo contable; si no hay reemplazo o cuenta en el bien, se usa la del modelo.

### 42. ¿Dónde se transfieren los asientos de Activo Fijo a Contabilidad?

Desde **Exportación de asientos contables de Activo Fijo**, individual por movimiento o resumidos por fecha/modelo/resumen según opciones.

### 43. ¿Qué métodos HTTP expone el API REST de Tango según la documentación?

**GET** consultar/leer, **POST** crear, **PUT** editar, **DELETE** eliminar; el intercambio en JSON.

### 44. ¿Cómo obtengo el token para llamar al API?

En **Menú web > Menú de usuario > Desarrollador**, botón **Generar**; el token va en el header como **ApiAuthorization** junto con **Company** (ID empresa) y Accept application/json.

### 45. ¿Cómo identifico el número de empresa para el API?

Por la URL (`company/` seguido del número) o consultando en base **Diccionario** tabla **Empresa**, campo ID_Empresa.

### 46. ¿Dónde veo los métodos disponibles de cada proceso?

En cada proceso: **Apertura > API**, documentación autogenerada con ejemplos y botón ejecutar en consultas.

### 47. ¿Qué permite Gestión de solicitudes de compras?

Administrar solicitudes pendientes: filtrar por múltiples criterios, indicar cantidades a **comprar**, **entregar** desde stock o **cerrar** con motivo, generar órdenes de compra con asistente y usar detalle por renglón para imputar por solicitud.

### 48. ¿Qué estados de solicitud pueden gestionarse según la guía?

**Ingresado** (sin autorización de solicitudes), **Autorizado / Autorizado Parcial** (con circuito de autorización), o **En curso** para renglones con cantidades autorizadas pendientes de comprar.

### 49. ¿Qué es el Libro de sueldos digital (LSD) en relación con Tango?

Es la aplicación AFIP para Libro de Sueldos y DDJJ F.931; en Tango se activa **Usa Libro de Sueldos Digital** en Parámetros de Sueldos y se completan conceptos y datos de legajos/categorías; puede combinarse generación automática con **conceptos auxiliares** manuales.

### 50. ¿Qué valor debe tener “Días Base” en topes para bases imponibles para LSD?

Debe estar **Base 30**, porque AFIP considera todos los meses con **30 días**. Además, para legajos por horas hay que informar horas y equivalente en días según registros 02 y 04 que describe la guía.

---

## Uso recomendado para el chatbot

- Ante preguntas normativas recientes (AFIP/ARBA), contrastar siempre con normativa vigente y con la versión instalada del producto.
- Para rutas exactas de menú en instalaciones locales vs. web, indicar que el usuario puede buscar texto con **F3** en el menú global según recomendación de la ayuda de Compras.

---

*Fuente interna del proyecto: fragmentación de ayudas Axoft/Tango en `.cursor/docs/axoft_md/` (metadata Producto: Tango, Versión documentada: 24AR).*
