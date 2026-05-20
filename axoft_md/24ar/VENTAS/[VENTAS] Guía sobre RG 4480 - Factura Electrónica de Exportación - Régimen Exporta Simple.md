# Guía sobre RG 4480 - Factura Electrónica de Exportación - Régimen Exporta Simple

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_rg4480_gv/

## Contenido

# Guía sobre RG 4480 - Factura Electrónica de Exportación - Régimen Exporta Simple

Esta guía de implementación le indica los pasos a seguir para poner en marcha este circuito. La RG 4480 especifica los comprobantes de exportación bajo este régimen que se emitirán desde el Facturador.

Tenga en cuenta que para utilizar este régimen su empresa deberá revestir el carácter de Responsable Inscripto en el IVA (RI) o encontrarse adherido al Régimen Simplificado para Pequeños Contribuyentes (RS).

##### Puesta en marcha

Para comenzar a utilizar el circuito debe seguir los siguientes pasos:

  * Ingrese a [Parámetros de Ventas](?p=19401/#otras-resoluciones) y active la opción RG 4480 - Inscripto en el régimen de Exportación Simplificada que se encuentra en la solapa Comprobantes electrónicos, sub solapa Otras resoluciones.
  * Ingrese al proceso [Formularios](?p=11875) del módulo Procesos generales | Tablas generales | Formularios | Ventas y agregue las siguientes variables: 
    * **@DV:** representa el valor DES (Documento Exportación Simplificada) asociado al comprobante.
    * **@MF:** representa el monto FOB correspondiente al comprobante de exportación simplificada.
    * **@EP:** representa la descripción del tipo de comprobante de exportación. El resultado de esta variable será "EXPORTA SIMPLE".



##### Detalle del circuito

**Emisión de comprobantes**

Tenga en cuenta que al emitir un comprobante deberá ingresar la siguiente información:

  * Tipo de exportación "Bienes".
  * Valor DES (Documento de exportación simplificada).
  * Monto FOB.



__Nota

El valor DES no deberá ser informado en notas de débito o notas de crédito.

**Notas de crédito y notas de débito**

Para realizar una nota de crédito / nota de débito bajo el régimen de exportación simplificada, debe seleccionar como comprobante de referencia una factura aprobada por AFIP y que haya sido emitida bajo el mismo régimen.

**¿Dónde puedo consultar la información adicional ingresada en el comprobante?**  
Puede consultar la información ingresada desde los procesos [Modificación de comprobantes](?p=20552), [Consulta de comprobantes](?p=21172), y en ficha Live del comprobante.
