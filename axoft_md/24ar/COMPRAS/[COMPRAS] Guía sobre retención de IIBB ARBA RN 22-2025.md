# Guía sobre retención de IIBB ARBA RN 22/2025

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp2/guia_retencarba222025_cp2/

## Contenido

# Guía sobre retención de IIBB ARBA RN 22/2025

Esta guía de implementación detalla la configuración y los pasos a seguir para poner en marcha la [Resolución Normativa 22/2025](https://www.arba.gov.ar/archivos/Tramites/RN 22-2025.pdf), referida a la emisión de comprobante de retención de IIBB de ARBA.

Esta normativa estable modificaciones para los agentes de retención en la generación de los comprobantes de retención y en las declaraciones juradas del impuesto a los Ingresos Brutos. La modificación principal establece que el único comprobante válido de retención es el generado desde la página de ARBA.

Para operar bajo este régimen:

  * La empresa debe estar inscripta como agente de retención de ARBA.
  * Debe contar con acceso al servicio A122R para operar (no solo de consultas).
  * Las retenciones deben corresponder a Ingresos Brutos con padrón ARBA.



##### Puesta en marcha

Para solicitar autorización y obtener el comprobante de retención de ARBA configure previamente en Parámetros de Compras: en la solapa Retenciones | Retenciones de ARBA - A 122R.

  1. Tilde el parámetro RN 22/2025 Agente de retención IIBB ARBA A122R.
  2. Agregue el o las actividades para clasificar las retenciones de ARBA.
  3. Complete los parámetros de Servicio de ARBA. el método de conexión, el CUIT y la clave CIT esto le permitirá autorizar la retención y obtener el PDF de Arba.



Con esta configuración; cuando realice una factura de contado, un pago o pago masivo que genere un comprobante de retención de Ingresos Brutos de ARBA, el sistema solicitará autorización y obtendrá el PDF que entrega ARBA. Si la DDJJ no existe, previo al pedido de autorización va a crearla.
