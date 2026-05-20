# Importación de órdenes de Compras

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_rg3572_gla/?p=9415/

## Contenido

# Importación de órdenes de Compras

Este proceso incorpora las órdenes de compra generadas y exportadas desde una sucursal, para su gestión centralizada.

El asistente de importación lo guiará en el ingreso de los datos necesarios para este proceso. Para más información sobre el asistente de importación, consulte el tópico [Asistente para transferencias](?p=11934).  
Para que una orden de compra sea incorporada correctamente, se realiza una serie de validaciones. Si existiera alguna anomalía, la orden se rechaza informando en el detalle de auditoría los motivos de rechazo.  
Las validaciones de la importación son las siguientes:

  1. El número de orden de compra no debe existir en los archivos correspondientes. Este control no permite que se importe dos veces el mismo comprobante.
  2. Los códigos de comprador, condición de compra y talonario deben existir en el módulo Compras.
  3. En caso de tener configurada una lista de precios, ésta debe estar definida. Si la misma no existe la orden de compra no se rechaza (se importa sin lista de precios) ya que no es un dato obligatorio.
  4. Cada uno de los artículos y sus unidades de medida de compras, así como también, los depósitos de entrada asociados a la orden de compra deben estar definidos en el módulo Stock.
  5. Si en el módulo Compras está activa la autorización de órdenes de compra, según se haya configurado el parámetro Estado de las órdenes de compra al importar (en [Parámetros de transferencia de gestión central](?p=9434)), podrán importar las órdenes de compra con estado: 'Autorizada', 'Ingresada' o 'Respetar el estado que tenían al ser exportadas'.  
Si en el módulo Compras no está activa la autorización de órdenes de compra, aquellas que en la empresa origen figuran con estado "Ingresadas" serán importadas con estado 'Autorizada'.
  6. Si al exportar se informó la sucursal destino, serán considerados solo las órdenes de compra donde la sucursal destino coincida con la sucursal donde se realiza la importación.



Si todas las validaciones son correctas, se da de alta la orden de compra y se actualiza el inventario pendiente de recepción de los artículos.

##### Auditoría de importaciones

Cada vez que realice una importación de información, por ejemplo: tablas generales, comprobantes para informes y estadística, etc., se registra un detalle de auditoría con la información aceptada y rechazada.  
Puede consultar esta información desde Live utilizando la consulta Auditoría dentro de la rama Transferencias de los módulos Central y Procesos generales.  
Puede consultar información general: fecha, hora, usuario, etc. que realizó una importación, y además puede consultar un detalle completo de la información aceptada, rechazada y con advertencias.
