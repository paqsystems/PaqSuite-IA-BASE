# Guía de Punto de Venta sobre RG 5616/2024

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv2/guia_rg5616_gv2/

## Contenido

# Guía de Punto de Venta sobre RG 5616/2024

Esta guía de implementación le indica los pasos a seguir para poner en marcha la RG 5616/2024, referida a la emisión de comprobantes manuales y electrónicos.

Las nuevas disposiciones alcanzan a los comprobantes clase 'A', 'B', 'C', 'E' y 'T', y establece que en las operaciones realizadas en moneda extranjera que se cancelen en la misma moneda, se deberá considerar el tipo de cambio vendedor divisa que informa el Banco de la Nación Argentina, correspondiente al día hábil anterior al de la fecha de la factura pertinente.  
Quienes utilicen controladores fiscales de nueva tecnología, para documentar operaciones en moneda extranjera que se cancelen en la misma moneda podrán utilizar «comprobantes en línea», el facturador web gratuito de ARCA para emitir los comprobantes electrónicos.

__Nota

Para más información referida a este tema, consulte la reglamentación en  
<https://servicios.infoleg.gob.ar/infolegInternet/anexos/405000-409999/407369/norma.htm>  
y  
<https://servicioscf.afip.gob.ar/publico/sitio/contenido/novedad/ver.aspx?id=4468>  


##### Puesta en marcha

  1. **[Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv2)  
**En la solapa Comprobantes, subsolapa General, sección Resoluciones AFIP, tilde el parámetro RG 5616 - Emisión de comprobante.  
Si genera comprobantes en moneda extranjera, configure el comportamiento del parámetro Pago en la misma moneda del comprobante, siendo sus opciones 'Sí', 'No' o 'Confirma'. Por defecto, la opción propuesta es 'Confirma'. El valor que seleccione será tenido en cuenta en la generación de facturas desde el Facturador.
  2. [**Cotizaciones**](?p=11848)  
Al generar facturas en moneda extranjera que se cancelen en la misma moneda, será necesario que utilice la cotización del Banco de la Nación Argentina correspondiente al día hábil anterior a la fecha del comprobante.  
Puede registrar la cotización en forma manual desde el proceso [Cotizaciones](?p=11848) para el tipo de cotización RG 5616, o el sistema lo puede realizar automáticamente.  
Para que la cotización se actualice en forma automática, se requiere establecer conexión con los servidores de ARCA, y por lo tanto será necesario que tenga cargado al menos un [certificado](?p=24053) habilitado para la emisión de los comprobantes habituales.
  3. **[Formulario de Ventas](?p=11875)  
**Si emite comprobantes electrónicos o pre-impresos, ingrese al proceso [Formulario de Ventas](?p=11875) del módulo Procesos generales para adaptar los formularios que utilice para la generación de comprobantes.



**Variable de impresión** | **Significado**  
---|---  
@CO | Muestra el valor de la cotización  
@LY | Muestra la leyenda de la cotización  
@LM | Muestra la moneda de emisión del comprobante  
@CI | Muestra la categoría de IVA del cliente  
  
##### Detalle del circuito

Realizada la puesta en marcha, el circuito se compone de las siguientes operaciones.

  * **Emisión de facturas:** en el proceso de facturación, cuando genere un comprobante en moneda extranjera, deberá indicar si lo cancela en la misma moneda. En caso afirmativo, el sistema obtendrá la cotización correspondiente al día hábil anterior al de la fecha de la factura pertinente.  
Si el sistema no logra obtener automáticamente la cotización, se le notificará el inconveniente y podrá ingresarla manualmente.  
Recuerde que, si emite la factura desde el Facturador, puede definir un valor por defecto para la opción Pago en la misma moneda del comprobante desde Parámetros de Ventas | General | Comprobantes sección Resoluciones AFIP.  
Para más información consulte [Cotización en comprobantes en moneda extranjera según RG 5616](?p=13075).
  * **Emisión de débitos y créditos:** los débitos y créditos en moneda extranjera que referencien una factura que fue cancelada en misma moneda, utilizarán la cotización del comprobante de referencia.



Consideración general:

Entre las restricciones establecidas en la RG 5616, se especifica que ARCA no permite la generación de comprobantes electrónicos de clase B de un 'Responsable Inscripto' a otro 'Responsable Inscripto'. Por lo tanto, ante esta situación, desde el Facturador se le dará la opción de considerar al cliente Responsable Inscripto como un Consumidor Final para ese comprobante.  
Para más información consulte [Emisión de comprobantes B a Responsables Inscriptos](?p=13061).

##### Preguntas frecuentes

Consulte en esta sección las respuestas a las preguntas más frecuentes que puede tener sobre la aplicación de la RG5616 en la emisión de comprobantes.

**¿Tengo que realizar cambios si no genero comprobantes en moneda extranjera?  
**No debe realizar cambios si sólo genera comprobantes en moneda corriente.

**¿Qué tipo de comprobante son afectados por la RG5616?  
**Son afectadas las facturas, notas de crédito y notas de débito preimpresas y electrónicas emitidas en moneda extranjera que se cancelen en la misma moneda.  
Las facturas deben utilizar la cotización del día hábil anterior a la fecha del comprobante y las notas de débito y notas de crédito que referencien una factura cancelada en la misma moneda, deben utilizar la cotización del comprobante de referencia.

**¿Qué cotización debo utilizar si la factura es en moneda extranjera y no se cancela en la misma moneda?  
**Si indica que la factura no se cancela en la misma moneda, no habrá cambios en la operatoria y se utilizará la cotización general de ventas o del comprobante de referencia según configuración y la podrá modificar si los permisos definidos en el perfil se lo permiten.

**¿Cómo ingresar manualmente una cotización para la RG5616 desde el proceso de Cotizaciones?  
**En Procesos generales | Moneda | Cotizaciones puede ingresar manualmente una cotización seleccionando el código del tipo de cotización 'RG5616', con la moneda y fecha correspondiente de la cotización.  
Para ejemplificar un caso de uso, si ingresa manualmente una cotización para el tipo de cotización 'RG5616' con fecha del 28/04/2026; esta cotización será utilizada por el sistema para todas las facturas en moneda extranjera que se cancelen en la misma moneda el día 29/04/2026.

**¿Cómo parametrizo el sistema para que consulte la cotización en forma automática?  
**Cuando active la opción RG 5616 - Emisión de comprobante en la solapa Comprobantes en [Parámetros de Ventas](?p=19401/#parametros-para-comprobantes), el sistema va a obtener la cotización automáticamente en las facturas generadas en moneda extranjera que se cancelen en la misma moneda.  
El sistema buscará la cotización para el día hábil anterior a la fecha del comprobante desde el proceso [Cotizaciones](?p=11848) y si no la encuentra se conectará a los servidores ARCA, por lo tanto, será necesario que tenga cargado al menos un [certificado](?p=24053) en Procesos generales, habilitado para la emisión de los comprobantes habituales.

**Si genero una factura en moneda extranjera con fecha superior a la fecha actual ¿que cotización se debe utilizar?  
**Una factura con fecha futura debe utilizar la cotización del día hábil anterior a la fecha de emisión.  
Por ejemplo, si está emitiendo un comprobante el 29/04/2026 con fecha del 30/04/2026, la cotización a utilizar debe ser la indicada por el Banco Nación para la moneda correspondiente el día 28/04/2026.

**¿Si existen varias cotizaciones de la RG5616 para un mismo día, cuál utiliza el sistema?  
**Si existen varias cotizaciones de la RG 5616 para una misma fecha y moneda, el sistema utilizará la última ingresada en base a su horario de registración. Tengo en cuenta que desde el proceso [Cotizaciones](?p=11848), puede gestionar las cotizaciones añadiendo una nueva o eliminando una que considere que no corresponda.

##### Contenidos relacionados

No se ha encontrado ninguno
