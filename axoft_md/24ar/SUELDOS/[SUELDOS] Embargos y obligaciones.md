# Embargos y obligaciones

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sua/guia_emboblig_sua/?p=13077/

## Contenido

# Embargos y obligaciones

Administre los embargos y obligaciones vinculadas a los legajos del sistema de sueldos.

Para dar de alta una nueva obligación, seleccione primero el legajo y luego el tipo de obligación. Las opciones son 'Cuota alimentaria', 'Embargo' y 'Otro'.  
Para el correcto cálculo de las obligaciones de tipo 'Embargo' verifique que en los [Parámetros de Sueldos](?p=13208), en la solapa Principal se encuentren cargados los topes mínimo y máximo para embargos en 10% y 20% respectivamente, según los valores vigentes.

##### Principal

Para dar de alta una nueva obligación, seleccione primero el legajo y luego el tipo de obligación.

Tipo de Obligación: en este caso las opciones son 'Cuota alimentaria', 'Embargo' y 'Otro'.

Estado: el estado inicial de una obligación es 'Activo', salvo que se trate de un segundo embargo, en cuyo caso se le aplicará el estado de 'Pendiente', una vez finalizada la obligación, debe cambiar el estado a 'Cancelado'.

Concepto: se solicita un concepto para la liquidación de la obligación, en el caso de los embargos y las cuotas alimentarias, los conceptos sugeridos son del tipo 'Retención', en cambio para el tipo 'Otro' podrán ser 'Retención' o 'No remunerativo'.

Importante:

Los conceptos a utilizar deben ser dados de alta utilizando las variables especialmente diseñadas para cada tipo de obligación: **CUOTALIM** , para cuota alimentaria; **EMBARGO** , para embargos y **CALCOTRO** para el tipo 'Otro', o bien utilizar formulas armadas con los resultados parciales de las mismas. Para más información, vea [Variables](?p=13245) de **Sueldos**.

Más información:

Los conceptos utilizados en algún tipo de obligación con las variables antes mencionadas no pueden reutilizarse para otro tipo de cálculo. En caso de ser necesario se deberá crear un concepto nuevo, no asociado a ninguna obligación.  


Motivo: permite dejar constancia, en forma opcional, del origen de la obligación.

Parámetros de cálculo

Total: informa el importe total a retener en los casos de 'Embargo' u 'Otros'.

Saldo inicial: en este campo pueden cargarse un valor para los casos en que ya se hubieran practicado retenciones que hayan disminuido la deuda original (importes ya descontados).

Cantidad de cuotas: es un número entero por el cual dividir el total para obtener el valor de las cuotas en el caso de obligaciones del tipo 'Otros'.

Importe de cuota fija: en una obligación de tipo 'Cuota alimentaria', permite ingresar el valor de la parte fija a retener, si la hubiera; para el caso del tipo 'Otros' se puede ingresar el valor final de la cuota.

Porcentaje: en el caso de las cuotas alimentarias, permite ingresar el porcentaje a retener, puede usarse en forma conjunta a Importe de cuota fija. También puede utilizarse en una obligación de tipo 'Otros'.

Incluye conceptos no remunerativos: tilde esta opción para indicarle al cálculo que contemple los conceptos de tipo 'No remunerativo' (tipo 4) para la base de cálculo de la retención.

Calcula sobre sueldo neto: tilde en los casos donde a la base de cálculo se le deba restar las retenciones.

Descuenta cuota alimentaria: indica si para los embargos se debe descontar de la base de cálculo, las cuotas alimentarias que se estén liquidando simultáneamente.

##### Expediente

Fecha: permite ingresar la fecha de recepción del Oficio judicial.

Nro. de expediente, Fuero, Nro. de juzgado, Nro. de secretaria: indica el número de expediente, a que fuero corresponde el juzgado del cual proviene el Oficio, número de juzgado, número de secretaria.

Correo electrónico: correo electrónico de contacto con el juzgado.

Autos: título del juicio.

Datos bancarios

Banco, Sucursal: entidad y sucursal bancaria donde se deben depositar los montos retenidos.

Tipo de cuenta: tipo de cuenta en la que se deben realizar los depósitos.

Nro. de cuenta: número de la cuenta del expediente.

CBU: número de CBU de la cuenta.

Fecha de vencimiento

Tipo: tipo de días para el cálculo del vencimiento pueden ser corridos o hábiles.

Cantidad de días: cantidad de días de plazo para realizar el depósito de los importes retenidos.

##### Oficio

En esta solapa usted podrá pegar el texto del expediente, si lo recibió en formato electrónico.

##### Contenidos relacionados

  * [Guía sobre embargos y obligaciones](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sua/guia_emboblig_sua/)

  * [Video sobre embargos, préstamos y cuotas alimentarias](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/embargos_sua_vid/)
