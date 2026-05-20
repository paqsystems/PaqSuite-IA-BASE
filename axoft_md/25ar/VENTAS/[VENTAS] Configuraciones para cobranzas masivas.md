# Configuraciones para cobranzas masivas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_cuentcorr_gv/?p=19256/

## Contenido

# Configuraciones para cobranzas masivas

Este proceso permite definir los datos a tener en cuenta para la generación masiva de recibos.

Tenga en cuenta que cuando el origen sea [Tango Cobranzas](?p=12425), se requerirá el ingreso de la forma de cobro asociada, el talonario, el vendedor, el concepto, la cuenta principal y la contracuenta.  
Para más información consulte la [Guía de implementación sobre cuentas corrientes](?p=26557).

##### Principal

Código: identifique mediante un código alfanumérico, cada configuración a utilizar en la generación masiva de recibos.

Descripción: asocie un texto o descripción a cada código ingresado. Este dato no es obligatorio.

Origen de las cobranzas: indique si la configuración se aplicará a las cobranzas provenientes de una entidad (Pagomiscuentas®, Pago Fácil® o Rapipago®), [Tango Cobranzas](?p=12425) u otro origen: 'Manual' o 'Formato Tango' (*.xls).

A continuación, detallamos sus opciones disponibles:

  * Datos para el origen: [Tango Cobranzas](?p=12425)  
Si su empresa realiza cobros electrónicos con sistemas de pago en línea, deberá ingresar:  
Forma de cobro asociada: permite asociar un sistema de pagos a dicha configuración. El sistema valida que sólo pueda existir una única configuración por cada forma de cobro asociada.
  * Datos para entidades recaudadoras  
Si su empresa opera con una entidad recaudadora (Pagomiscuentas®, Pago Fácil® o Rapipago®) para la cobranza de sus facturas:  
1\. Ingrese como Identificación, el número que la entidad le asignó a su empresa. Este dato es obligatorio.  
2\. Ingrese la Ubicación del archivo de cobranzas a recibir por la entidad.
  * Datos para _Pagomiscuentas_  
Modalidad de identificación de clientes: seleccione la modalidad a aplicar para identificar sus clientes ante la entidad recaudadora. Por defecto, el sistema propone utilizar el Código de cliente Tango, pero es posible optar por el Número de pago electrónico.  
Ubicación archivo de facturas a exportar: ingrese la carpeta donde se guardará el archivo a exportar a la entidad recaudadora o bien, selecciónela usando el botón "Examinar".
  * Datos para el origen: Formato Tango (*.xls)  
Ingrese la Ubicación del archivo de cobranzas (con formato .xls) a procesar. Puede seleccionarlo utilizando el botón "Examinar".



##### Datos para recibos

Ingrese los datos generales que se aplicarán a los recibos que genere en forma masiva usando esta configuración.

  * Talonario
  * Fecha del recibo (la 'Del día' o la 'De cobro').
  * Vendedor ('Del cliente' u 'Otro').
  * Forma de envío ('Impresión', 'Por correo electrónico' o 'Por WhatsApp').



__Nota

Para el origen [**Tango Cobranzas**](?p=12425), el talonario no debe permitir la edición del número de comprobante durante su ingreso.

##### Datos para Tesorería

Defina el concepto y la clasificación que llevarán los comprobantes a generar. Este último dato es obligatorio si el origen es [Tango Cobranzas](?p=12425) y la empresa clasifica recibos de cobranzas siempre o con confirmación.  
Indique la cuenta principal (de tipo 'Otra' y la contracuenta (de tipo 'Otra' o 'Banco'). Si el origen es [Tango Cobranzas](?p=12425), como contracuenta, sólo mostrará aquellas que tengan asociada la forma de cobro elegida en la primera solapa, y si su leyenda se deja en blanco, el sistema grabará en dicho campo el número de transacción del sistema de pago.  
Ambas cuentas no deben asociar unidades y deben estar habilitadas para los módulos Ventas y Tesorería.  
También, es posible ingresar los códigos de operación, leyendas y clasificaciones.

##### Comprobantes de ajuste

Esta solapa estará visible sólo cuando el origen sea [Tango Cobranzas](?p=12425).  
Defina si desea generar automáticamente los ajustes por cobro en fechas alternativas. La definición de esta opción depende del valor del [parámetro de venta](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes) que indica si se generan ajustes automáticamente al cobrar.  
Indique también los tipos de comprobantes, talonarios, generación de asientos y cálculo de impuestos para la generación de dichos ajustes.

##### Contenidos relacionados

  * [Video sobre cobranzas masivas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/cobramasiva_gv_vid/)

  * [Videos sobre cuentas corrientes](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/cuentacorriente_gv_vid/)

  * [Videos sobre integración con Mercado Pago®](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/marcadopago_gral_vid/)
