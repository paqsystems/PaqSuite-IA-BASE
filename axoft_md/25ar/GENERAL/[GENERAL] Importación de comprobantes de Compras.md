# Importación de comprobantes de Compras

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_rg3572_gla/?p=9412/

## Contenido

# Importación de comprobantes de Compras

Este proceso permite incorporar al módulo **Compras**(o **Proveedores**) información relacionada con facturas, notas de crédito y notas de débito, para agregarlas a la cuenta corriente y gestionar su pago centralizado.

El asistente de la importación lo guiará en este proceso. Para más información, consulte el tópico [Asistente para transferencias](?p=11934).  
Las validaciones de la importación son las siguientes:

  * El comprobante no debe existir para el proveedor.
  * El proveedor, tipo de comprobante y conceptos deben estar definido en el módulo Compra.
  * Los artículos asociados al comprobante deben estar definidos en el módulo Stock.
  * Si al exportar se informó la sucursal destino, serán considerados solo los comprobantes donde la sucursal destino coincida con la sucursal donde se realiza la importación.



##### Auditoría de importaciones

Cada vez que realice una importación de información, por ejemplo: tablas generales, comprobantes para informes y estadística, etc., se registra un detalle de auditoría con la información aceptada y rechazada.  
Puede consultar esta información desde Live utilizando la consulta Auditoría dentro de la rama Transferencias de los módulos Central y Procesos generales.  
Puede consultar información general: fecha, hora, usuario, etc. que realizó una importación, y además puede consultar un detalle completo de la información aceptada, rechazada y con advertencias.

##### Contenido dependiente

  * [Centralización de pagos](https://ayudas.axoft.com/25ar/ayudas/ct/transferencias_carp_ct/importacion_carp_ct/gestioncentral_carp_ct/compras_carp2_ct/importcomprobfacturcomp_ct/centralizpagos_ct/)
