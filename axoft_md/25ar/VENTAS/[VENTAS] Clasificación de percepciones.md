# Clasificación de percepciones

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_alicuotiibbsantafe_gv3/?p=19231/

## Contenido

# Clasificación de percepciones

Este proceso permite agregar clasificaciones de clientes, así como también consultar, listar, modificar y dar de baja clasificaciones existentes.

Estas clasificaciones pueden utilizarse desde los procesos [Clientes,](https://ayudas.axoft.com/25ar/clientes_carp_gv) [Artículos](?p=17035), [Percepciones definibles](https://ayudas.axoft.com/25ar/percepcdefin_gv).  
Para poder eliminar una clasificación, la misma no debe estar utilizada en otros procesos.  
Para más información consulte el tópico [¿Para qué se utiliza la clasificación para percepciones definibles?](?p=27041/#puesta-en-marcha)

Clientes ocasionales

Clasificación para Percepciones Definibles: este campo permite asignar una clasificación especial para ser utilizada en el cálculo de la percepción definible.  
Si se completa este campo, la percepción sólo se calculará para aquellos clientes y artículos que tengan definida la misma clasificación.

Percepciones definibles: si el cliente liquida percepciones definibles es necesario asociarle un código previamente definido en el proceso [Clasificación Percepciones Definibles](https://ayudas.axoft.com/25ar/clasifpercepdefin_gv).

Alícuota: este campo no es dato un obligatorio. Pero si no se completa, para liquidar el impuesto se considerará el código que tenga asignado en el artículo.  
Si se completa el código de alícuota, ésta será considerada en los comprobantes, independientemente de la alícuota ingresada para los artículos (salvo en aquellos artículos en los que no se parametrice la percepción definible y que en ningún caso calcularán percepción).

Si se asignó una clasificación al cliente para calcular la percepción, el artículo deberá tener parametrizada la misma percepción-clasificación.

##### Contenidos relacionados

  * [Guía sobre percepciones definibles](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_percepdefin_gv/)

  * [Videos sobre retenciones y percepciones impositivas](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/retencpercep_gral_vid/)
