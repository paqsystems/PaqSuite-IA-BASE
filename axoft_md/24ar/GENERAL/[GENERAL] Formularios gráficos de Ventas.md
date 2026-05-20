# Formularios gráficos de Ventas

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_formgrafico_gla/?p=9218/

## Contenido

# Formularios gráficos de Ventas

Este proceso permite configurar los formularios gráficos para pedidos de ventas utilizando una fuente de datos o diccionario con los campos disponibles relacionados con el pedido.

##### Principal

Código: cada modelo que usted defina se identificará por este código. Será posible ingresar hasta 10 caracteres.  
El sistema valida que sea único, es decir, que no se repita en dos formularios.

Descripción: en este campo podrá ingresar una descripción o referencia. Su ingreso es opcional.

Habilitado: esta opción indica si el formulario está habilitado o no para generación de pdf. Por defecto estará activado.

Tipo de formulario: esta opción indica que el formulario pertenece a Pedidos. Por defecto estará desactivado.

Agrupa artículos iguales: esta opción indica si agrupa artículos iguales en la generación del PDF, según los campos incluidos en el formulario en el detalle de renglones.  
A continuación, mostramos algunos ejemplos de aplicación del parámetro:

**Ejemplo 1:**

_Pedido original_

**Nro** | **Código artículo** | **Descripción** | **Descripción adicional** | **UM** | **Cantidad  
pedida** | **Precio** | **Bonificación** | **Total renglón**  
---|---|---|---|---|---|---|---|---  
1 | Artículo 1 | BARRA DE SONIDO MARCA TCL | Con garantía | UN | 1,00 | 49200,00 | 10,00 | 44280,00  
2 | Artículo 1 | Barra de sonido | POTENCIA RMS 250 W | UN | 1,00 | 49200,00 | 0,00 | 49200,00  
3 | Artículo 1 | Barra de sonido |  | UN | 1,00 | 49200,00 | 0,00 | 49200,00  
4 | Artículo 1 | Barra de sonido |  | UN | 1,00 | 49200,00 | 0,00 | 49200,00  
  
_Resultado al agrupar_

**Nro** | **Código artículo** | **Descripción** | **Descripción adicional** | **UM** | **Cantidad  
pedida** | **Precio** | **Bonificación** | **Total renglón**  
---|---|---|---|---|---|---|---|---  
1 | Artículo 1 | BARRA DE SONIDO MARCA TCL | Con garantía | UN | 1,00 | 49200,00 | 10,00 | 44280,00  
2 | Artículo 1 | Barra de sonido | POTENCIA RMS 250 W | UN | 3,00 | 49200,00 | 0,00 | 147600,00  
  
**Ejemplo 2:**

_Pedido original_

**Nro** | **Código artículo** | **Descripción** | **Descripción adicional** | **UM** | **Cantidad  
pedida** | **Precio** | **Bonificación** | **Total renglón**  
---|---|---|---|---|---|---|---|---  
1 | Artículo 2 | KIT VARIABLE VIDEO  
30/04/2025 | COMPLETO | UN | 1,00  
1,00 | 316000,00 | 0,00 | 316000,00  
2 | Artículo 2 | KIT VARIABLE VIDEO  
30/04/2025  
05/05/2025 | COMPLETO |  | 2,00  
1,00  
1,00 | 316000,00 | 0,00 | 632000,00  
  
_Resultado al agrupar_

**Nro** | **Código artículo** | **Descripción** | **Descripción adicional** | **UM** | **Cantidad  
pedida** | **Precio** | **Bonificación** | **Total renglón**  
---|---|---|---|---|---|---|---|---  
1 | Artículo 2 | KIT VARIABLE VIDEO  
30/04/2025  
05/05/2025 | COMPLETO | UN | 3,00  
2,00  
1,00 | 316000,00 | 0,00 | 948.000,00  
  
**Ejemplo 3:**

_Pedido original_

**Nro** | **Código artículo** | **Descripción** | **Descripción adicional** | **UM** | **Cantidad  
pedida** | **Precio** | **Bonificación** | **Total renglón**  
---|---|---|---|---|---|---|---|---  
1 | Artículo 3 | PROYECTOR FULL HD PHANTOM  
1028p  
Proyector HD | Alta definición | UN | 1 | 161250,00 |  | 161250,00  
2 | Artículo 3 | PROYECTOR FULL HD PHANTOM  
Proyector HD | Alta definición | UN | 2 | 161250,00 |  | 161250,00  
  
_Resultado al agrupar_

**Nro** | **Código artículo** | **Descripción** | **Descripción adicional** | **UM** | **Cantidad  
pedida** | **Precio** | **Bonificación** | **Total renglón**  
---|---|---|---|---|---|---|---|---  
1 | Artículo 3 | PROYECTOR FULL HD PHANTOM  
1028p  
Proyector HD | Alta definición | UN | 3 | 161250,00 |  | 322500,00  
  
##### Diseño

En esta sección usted puede configurar el formulario gráfico que se utilizará en la generación de PDF con los datos relacionados con el pedido.  
Los campos disponibles se muestran agrupados, según las secciones del reporte como ser Encabezado, Renglones, Totales, etc.  
Para más información, puede consultar los [campos disponibles para pedidos](?p=14445).

Botón Modelos<Alt + M>  
Al presionar "Nuevo" se habilita un botón en la barra de botones en el encabezado llamado Modelos. Esta opción le permite seleccionar un modelo de formulario gráfico, ya armado, provisto por el sistema, que le sirve como plantilla para luego modificarlo según lo que necesite.

##### Contenidos relacionados

  * [Emisión de cotizaciones](https://ayudas.axoft.com/24ar/ayudas/gv/cotizacion_carp_gv/emisioncotizacion_gv/)

  * [Generación / Modificación de cotizaciones](https://ayudas.axoft.com/24ar/ayudas/gv/cotizacion_carp_gv/genermodificotizacion_gv/)

  * [Gestión masiva de pedidos](https://ayudas.axoft.com/24ar/ayudas/gv/pedido_carp_gv/masivapedidos_gv/)

  * [Guía sobre formularios gráficos](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_formgrafico_gla/)

  * [Pedidos](https://ayudas.axoft.com/24ar/ayudas/gv/pedido_carp_gv/ingresopedido_gv/)

  * [Remitos](https://ayudas.axoft.com/24ar/ayudas/gv/procesofacturacion_gv/remito_carp_gv/)

  * [Talonarios de Ventas](https://ayudas.axoft.com/24ar/ayudas/gv/archivos_carp_gv/cargainicial_carp_gv/talonario_gv/)

  * [Video sobre Reemplazo Factura 'M' - Retención IVA e IIGG](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/facturam_gv_vid/)

  * [Video sobre formularios gráficos en pedidos](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/formgrafpedido_gv_vid/)
