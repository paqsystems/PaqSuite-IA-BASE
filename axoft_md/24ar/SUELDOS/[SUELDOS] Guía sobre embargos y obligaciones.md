# Guía sobre embargos y obligaciones

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sua/guia_emboblig_sua/

## Contenido

# Guía sobre embargos y obligaciones

Esta funcionalidad le permite calcular en forma automática distintos tipos de obligaciones que pudieran afectar a los legajos de la nómina.

Aquí le facilitamos una guía con los pasos necesarios para realizar estos cálculos y los controles posteriores a la liquidación.

##### Puesta en marcha

###### Alta de conceptos para cálculo de obligaciones

Para el cálculo de las obligaciones deben generarse los conceptos que luego serán asociados desde el proceso [Embargos y obligaciones](?p=13077).

Para ello, debe dar de alta un concepto de tipo '2 - Retención', que será utilizado para los tipos de obligación 'Cuota alimentaria', 'Embargo' y 'Otro'; o uno tipo '4 - No remunerativo' (únicamente para el caso de 'Otro').

Para los casos de cuota alimentaria se podrán crear tantos conceptos como cuotas alimentarias simultáneas se deseen liquidar.

Más información:

Los conceptos utilizados en algún tipo de obligación con las variables antes mencionadas no pueden reutilizarse para otro tipo de cálculo. En caso de ser necesario se deberá crear un concepto nuevo, no asociado a ninguna obligación.  


Los conceptos deberán crearse de la siguiente forma:

Cuota alimentaria: crear un nuevo concepto de tipo '2 - Retención' y crear una formula nueva, en lo posible con el mismo número del concepto que estamos creando, en el 'Importe' utilizaremos solamente la variable CUOTALIM.

Embargo: dar de alta un nuevo concepto de tipo '2 - Retención' y crear una formula a la cual se le asignara en importe la variable EMBARGO.

Otro: se debe generar un concepto de tipo '2 - Retención' o tipo '4 - No remunerativo' y asociarle una fórmula que contenga únicamente la variable CALCOTRO.

Todos los conceptos creados para obligaciones deben estar parametrizados como Afecta impuesto a las ganancias = No.

###### Alta de obligaciones

Para dar de alta una nueva obligación recurra al proceso [Embargos y obligaciones](?p=13077), allí se solicitaran los valores para el nuevo cálculo.

Nro. de obligación: es un número que genera el sistema para identificar unívocamente una obligación independientemente del tipo que se trate.

Legajo: número de legajo al que afecta la obligación.

Tipo de obligación: las opciones son 'Cuota alimentaria', 'Embargo', 'Otro'.

Estado: las opciones son 'Pendiente', 'Activo', 'Cancelado'. La opción por defecto es 'Activo', la modificación para pasar a otro estado dependerá de distintos factores, por ejemplo, en el caso de 'Embargo' el sistema sugerirá el estado 'Pendiente' si detecta que ya hay una obligación activa del mismo tipo para el legajo actual.

Concepto: seleccione el concepto (previamente generado) con el cual desea liquidar la obligación.

Motivo: para el caso de obligaciones de tipo Otro este campo permite introducir un motivo descriptivo.

###### Parámetros de cálculo

Total: indique el importe total de la deuda, este campo se utiliza tanto para Embargo como para Otro.

Saldo inicial: permite ingresar un monto ya retenido para continuar el cálculo.

Cantidad de cuotas: en el caso de obligaciones de tipo 'Otro', se utiliza para indicar la cantidad de cuotas por la cual dividir el importe ingresado en Total.

Importe de cuota fija: se utiliza para cargar el valor de una cuota tanto en 'Cuota alimentaria' como en 'Otro'.

Porcentaje: en el caso de la cuota alimentaria indica el porcentaje a retener.

Incluye conceptos no remunerativos: tilde esta opción para incluir en la base de cálculo los conceptos de tipo 4 - No remunerativo.

__Nota

Tenga en cuenta que al utilizar las variables específicas para cada tipo de obligación (CUOTALIM, EMBARGO, CALCOTRO) las retenciones podrán ser liquidadas en cualquier dato fijo del período, ya que aunque varíe la base de cálculo, la retención se ajustará automáticamente, pudiendo incluso realizar la devolución de lo retenido en exceso.

##### Detalle del circuito

**Base de cálculo**

Podrá determinar si un concepto del tipo 1 o tipo 4 forma parte de la base de cálculo de embargos y obligaciones, activando la marca Afecta base de cálculo de embargo y obligaciones en la definición de [conceptos de liquidación](?p=13165/#conceptos-y-totales-liquidados).

**Liquidación de conceptos**

En la liquidación de conceptos, tanto individual como global, el sistema calculará para los legajos que tengan vinculada una obligación, la retención correspondiente.

En los casos de obligaciones que se encuentren activas y ya hayan sido saldadas, el sistema emitirá un mensaje en Temas a revisar donde avisará de esta situación y sugerirá el cambio de estado a 'Cancelada'.

**Listados de control**

A través de las [consultas Live](?p=9203) el sistema le permitirá llevar un control de las retenciones practicadas y los próximos vencimientos de las mismas.

  * **Embargos y obligaciones:** es la consulta en donde se detallan las obligaciones contraídas por el legajo, por otro lado posibilita llevar un control del saldo pendiente de la misma.
  * **Vencimiento de embargos y obligaciones:** es la consulta en donde se detallan los vencimientos de las obligaciones contraídas. Se especifica además el detalle de la cuenta bancaria donde es depositado el importe retenido.



Ambas consultas son configurables y pueden combinarse los campos entre las mismas.

##### Contenidos relacionados

  * [Embargos y obligaciones](https://ayudas.axoft.com/24ar/ayudas/sua/novedades_carp_sua/emboblig_sua/)

  * [Video sobre embargos, préstamos y cuotas alimentarias](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/embargos_sua_vid/)
