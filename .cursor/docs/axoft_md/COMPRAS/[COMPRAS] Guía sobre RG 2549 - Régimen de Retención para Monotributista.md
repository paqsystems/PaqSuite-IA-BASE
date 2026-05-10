# Guía sobre RG 2549 - Régimen de Retención para Monotributista

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp2/guia_rg2549_cp2/

## Contenido

# Guía sobre RG 2549 - Régimen de Retención para Monotributista

Esta guía es de utilidad para implementar las retenciones a Monotributistas

La RG 2549/09 define un régimen de retención de Ganancias e IVA a contribuyentes monotributistas.  
La normativa establece que cuando se comercializan bienes y alguno de los que integran el comprobante que se cancela tiene un precio unitario superior a $870, corresponde realizar la retención sobre el importe que cancela.  
O bien, cuando en el transcurso de los últimos DOCE (12) meses al momento del pago se hubieran efectuado operaciones con un mismo sujeto y superen la suma de $72.000.- (si se factura servicios) o $144.000.- .(si se factura bienes).  
A continuación, puede observar las distintas etapas que componen el circuito.

##### Puesta en marcha

Para implementar el circuito de Retenciones establecido por la RG 2549/2009, siga los siguientes pasos:

  1. A través del proceso [Parámetros Retenciones](https://ayudas.axoft.com/24ar/paramgrales_cp2/#parametros-para-retenciones) defina las retenciones que se calcularán en el momento de pago.
  2. Defina un talonario para Retenciones desde carga inicial de [Talonarios.](https://ayudas.axoft.com/24ar/talonario_cp2) Tenga en cuenta que deben generarse con numeración propia, consecutiva y progresiva.
  3. Desde el proceso [Actualización de Retenciones](https://ayudas.axoft.com/24ar/actualretencion_cp2) ingrese en cada uno de los códigos de retención. Para cumplimentar con la RG. 2549/2009, es necesario definir dos bases de análisis; una como "A - Importe total Acumulado 12 meses" y otra como "U – Precio unitario" con sus respectivos importes 'Supera'.
  4. Desde el proceso [Actualización de Proveedores](https://ayudas.axoft.com/24ar/proveedores_cp2) asigne el código de las Retenciones de Monotributista.



Cuando se realice el pago de un comprobante o un pago a cuenta, el sistema calculará las retenciones asignadas a cada proveedor.
