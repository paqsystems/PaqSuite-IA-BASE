# Monedas contables

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp/guia_integrcontabl_cp/?p=9806/

## Contenido

# Monedas contables

Invoque esta opción para especificar las distintas monedas posibles de utilizar en la carga de asientos. Podrá definir una única moneda corriente (o local) y múltiples monedas extranjeras contables y otras monedas.

Contabilidad divide los datos de definición de una moneda en cuatro solapas.

##### Principal

Código: se utiliza para identificar a cada moneda. El sistema valida que no existan códigos repetidos. Su ingreso es obligatorio.

Descripción: si lo desea, ingrese una referencia o texto para el código de moneda.

Tipo: elija una de las siguientes opciones: 'Otra moneda', 'Extranjera contable' o 'Corriente'. No es posible modificar este dato.

Símbolo: ingrese, de manera opcional, una sigla representativa de la moneda. Su ingreso es obligatorio.

Cantidad de decimales: el valor puede estar comprendido entre cero y cuatro (0-4). Por defecto, se propone utilizar dos (2) decimales. No es posible modificar en este proceso este dato.

Más información:

Para poder modificar la cantidad de decimales para los importes o para las cotizaciones deberá hacerlo desde el proceso [Administrador de decimales](?p=9120) del **Administrador del sistema**.

Habilitada desde ejercicio: para las monedas de tipo 'Extranjera contable', indique el [ejercicio](?p=9778) a partir del cual la moneda en edición está habilitada. El sistema valida que no existan asientos en el ejercicio seleccionado ni en ejercicios posteriores.  
Para las monedas de tipo 'Corriente' y de tipo 'Otra moneda', este campo no es editable -por defecto, están habilitadas para todos los ejercicios.

**Aclaraciones sobre tipos de monedas**  
A continuación explicamos cada uno de los tipos posibles de monedas:

Corriente: es la moneda de curso legal en el país. Por ejemplo, en Argentina es el PESO. Es la moneda que se utiliza para la presentación de estados contables.  
El sistema valida que exista sólo una moneda clasificada como moneda corriente.

Otra moneda: son monedas extranjeras que no se utilizan para llevar saldos contables, sino como monedas para las [unidades adicionales](?p=9824) (de cuentas monetarias) o como monedas de ingreso de [valorizaciones](?p=9821) de unidades adicionales.

Extranjera contable: son monedas extranjeras que además, se utilizan para llevar saldos contables.  
Llevar los saldos en moneda extranjera contable significa que cada vez que se registre una operación en la contabilidad, también se guardará el importe en moneda extranjera contable, utilizando para el cambio el tipo de cotización definido por defecto para la moneda y la cotización que corresponda a la fecha del asiento.  
El tipo de cotización y/o la cotización puede modificarse, si está activo el parámetro Edita tipo de cotización y/o Edita cotización de la moneda y además, el usuario cuenta con la habilitación correspondiente.  
Para más información sobre tipos de cotización y cotizaciones, consulte estas opciones en la carpeta Monedas del ítem [Tablas generales](?p=11991) en el módulo Procesos generales.

**Parámetros de cotización  
**Sólo para las monedas de tipo 'Otra moneda' y 'Extranjera contable', defina los siguientes parámetros:

Tipo de cotización: elija el tipo de cotización a considerar por defecto en la carga de [asientos](?p=9755) u operaciones en esta moneda y en la opción [Resultado por tenencia](?p=9817).  
Para más información sobre tipos de cotización, consulte esta opción en la carpeta Monedas del ítem Tablas generales en el módulo Procesos generales.

Edita tipo de cotización: indica si el tipo de cotización puede ser modificado en la carga de [asientos](?p=9755). Por defecto, este parámetro está activo.

Edita cotización: indica si la cotización puede modificarse en la carga de [asientos](?p=9755) y en la opción [Resultado por tenencia](?p=9817). Por defecto, este parámetro está activo.

Cantidad de decimales para cotización: ingrese un valor comprendido entre cero y siete (0-7). Por defecto, se propone utilizar cuatro (4) decimales.

##### Parametrización contable

Esta solapa sólo está disponible para las monedas de tipo 'Otra moneda' o de tipo 'Extranjera contable'.

Resultado por tenencia positivo: ingrese o seleccione la [cuenta contable](?p=9774) para el resultado positivo de la opción [Resultado por tenencia](?p=9817).

Resultado por tenencia negativo: ingrese o seleccione la [cuenta contable](?p=9774) para el resultado negativo de la opción [Resultado por tenencia](?p=9817).  
El sistema valida que para la cuenta elegida no esté activo el parámetro Usa unidad adicional.

Traslación monetaria: sólo para monedas de tipo 'Extranjera contable', ingrese o seleccione la [cuenta contable](?p=9774) para el cálculo automático de la traslación monetaria.

Resultado por tenencia: indique el tipo de asiento a considerar por defecto en la opción [Resultado por tenencia](?p=9817).  
Para más información sobre tipos de asiento, consulte la [ayuda](?p=11994) del módulo Procesos generales.

Conversión a monedas extranjeras contables: indique el tipo de asiento a considerar por defecto en la opción [Conversión a moneda extranjera contable](?p=9772).  
Para más información sobre tipos de asiento, consulte la [ayuda](?p=11994) del módulo Procesos generales.

##### Datos legales

Código de moneda RG 1547: indique el dato equivalente a la moneda según la RG 1547.

Código de moneda AFIP: indique el dato equivalente a la moneda según AFIP.

**Condiciones para eliminar una moneda contable**  
Es posible eliminar una moneda sólo si:

  * no existen asientos analíticos ni asientos resúmenes;
  * no existen cuentas que lleven saldo en unidades adicionales en esa moneda;
  * no existen tipos de valorización que tengan asociada la moneda como moneda de ingreso de las valorizaciones.



Al eliminar una moneda, se borrarán también las cotizaciones definidas. En este caso, el sistema solicita su confirmación.

##### Contenidos relacionados

  * [Videos sobre parametrización contable](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/paramcontab_gral_vid/)
