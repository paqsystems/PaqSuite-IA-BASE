# Guía sobre creación, impresión y consulta de campos adicionales

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_guiacamposadicionales_gla/

## Contenido

# Guía sobre creación, impresión y consulta de campos adicionales

Es posible la creación, consulta e impresión de los campos adicionales utilizados en comprobantes referidos a clientes y artículos.

Los comprobantes que cuentan con la posibilidad de impresión de campos adicionales son los siguientes:

Ventas:

  1. Cotizaciones
  2. Pedidos
  3. Facturas
  4. Facturas Punto de Venta
  5. Notas de débito
  6. Notas de crédito
  7. Remitos
  8. Recibos (sólo clientes)



Stock:

  1. Ingreso de Stock.
  2. Egresos de Stock.
  3. Transferencias entre depósitos.
  4. Toma de inventario.
  5. Ajuste de inventario.
  6. Comprobantes de armado.



Compras e Importaciones:

  1. Solicitudes de compra.
  2. Orden de compra.
  3. Remitos.
  4. Carpetas de importación.
  5. Despachos.



##### Puesta en marcha

Defina los campos adicionales para artículos y clientes desde el [Administrador de empresas](?p=9067).  
socie el [campo adicional](?p=12000) a una variable de impresión.  
Agregue al formulario de impresión las variables configuradas en los módulos [Stock](?p=17309), [Ventas](?p=14483) y [Compras](?p=14699).

##### Preguntas frecuentes

El siguiente listado de respuestas a preguntas frecuentes le ayudará resolver aspectos de la operatoria referida a las funcionalidades propias de los campos adicionales.

**¿Cómo actualizar información de campos adicionales?**  
Para actualizar la información se debe ingresar Archivo | Actualizaciones | Clientes o Archivo | Actualizaciones | Artículos e ingresar a la solapa de campos adicionales para modificar los valores de los campos.

**¿Cómo imprimir los campos adicionales?**  
Configure la variable desde el proceso de actualización de variables de impresión para campos adicionales en el módulo Procesos generales. Luego modifique los formularios de cada comprobante al que se desea agregar el campo adicional.

**¿Puedo segmentar la información de la variable para que se imprima en más de un renglón?  
**No, estas variables no podrán ser divididas para que se imprima su contenido en más de un renglón.

**¿Cómo consultar información de campos adicionales?**  
Para consultar la información asociada a un campo adicional, puede utilizar las consultas y fichas de Live. Si la consulta incluye datos de clientes o artículos, en la sección "Columnas" se muestran los campos adicionales al final de la lista.  
También se muestran dentro de las fichas de clientes y artículos, como una solapa en el encabezado de las mismas.

##### Contenidos relacionados

  * [Video sobre Procesos generales](https://ayudas.axoft.com/24ar/videos/gla_carp_vid/)

  * [Videos sobre historial, vistas, apertura y campos adicionales](https://ayudas.axoft.com/24ar/videos/operacion_carp_vid/campoadic__oper_vid/)
