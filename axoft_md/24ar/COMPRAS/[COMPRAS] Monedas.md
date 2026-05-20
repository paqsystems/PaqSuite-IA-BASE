# Monedas

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp/guia_integrcontabl_cp/?p=11956/

## Contenido

# Monedas

Invoque esta opción para especificar las distintas monedas posibles de utilizar en la carga de asientos.

Podrá definir una única moneda corriente (o local) y múltiples monedas extranjeras y otras monedas. Los datos de definición de una moneda se organizan en dos solapas: Principal y Observaciones.

##### Principal

Código: se utiliza para identificar a cada moneda. El sistema valida que no existan códigos repetidos. Su ingreso es obligatorio.

Descripción: si lo desea, ingrese una referencia o texto para el código de moneda.

Tipo: elija una de las siguientes opciones: 'Corriente', 'Extranjera contable' ,'Otra moneda'. No es posible modificar este dato.  
La moneda del tipo 'Corriente' corresponde a la moneda local de presentación de información contable.  
La moneda del tipo 'Extranjera contable' es la moneda utilizada para la reexpresión de los asientos contables. El sistema tomará solo la moneda definida como 'Moneda extranjera contable habitual' en los parámetros contables.

Símbolo: ingrese, de manera obligatoria, una sigla representativa de la moneda.

Cantidad de decimales: ingrese un valor comprendido entre cero y cuatro (0-4). Por defecto, se propone utilizar dos (2) decimales.  
No será posible modificar la cantidad de decimales desde este proceso. Para ello deberá ir al proceso [Administrar decimales](?p=9120#amindecimal) del Administrador del sistema. 

Habilitada desde ejercicio: para las monedas de tipo 'Extranjera contable', indique el ejercicio a partir del cual la moneda en edición está habilitada. El sistema valida que no existan asientos en el ejercicio seleccionado ni en ejercicios posteriores.  
Para las monedas de tipo 'Corriente' y de tipo 'Otras monedas', este campo no es editable -por defecto, están habilitadas para todos los ejercicios.

__Nota

El sistema por defecto provee de una moneda del tipo _Corriente_ y una moneda del tipo _Extranjera contable_. Usted puede modificar el código de la moneda en caso de no ajustarse a la definición de la empresa.

La moneda 'Extranjera contable' definida como habitual en los [parámetros contables](?p=12044), es la moneda que se utiliza en la integración entre el módulo Contabilidad y los módulos Compras, Ventas, Tesorería, etc.

**Codificación según AFIP**

Código moneda RG 1547: si usted con la RG 1547 de la AFIP asigne el código de moneda requerido para la generación del archivo según el Anexo de la mencionada resolución. Para más información, consulte la ayuda del módulo Compras / Proveedores.

Código moneda Comp Elec: si usted emite comprobantes electrónicos para el mercado interno y/o de exportación, ingrese la clasificación que la AFIP asigna a cada unidad monetaria.

Para más información, consulte la Guía sobre comprobantes electrónicos del módulo Ventas.

**Parámetros de cotización  
**Sólo para las monedas de tipo 'Otras monedas' y 'Extranjera', defina los siguientes parámetros:

Tipo de cotización: elija el [tipo de cotización](?p=11995) a considerar por defecto en la carga de asientos u operaciones en esta moneda y en la opción remito del módulo Contabilidad.

Edita tipo de cotización: indica si el tipo de cotización puede ser modificado en la carga de asientos. Por defecto, este parámetro está activo.

Edita cotización: indica si la cotización puede modificarse en la carga de asientos y en la opción resultado por tenencia del módulo Contabilidad. Por defecto, este parámetro está activo.

Cantidad de decimales para cotización: ingrese un valor comprendido entre cero y siete (0-7). Por defecto, se propone utilizar cuatro (4) decimales.  
No será posible modificar la cantidad de decimales desde este proceso. Para ello deberá ir al proceso [Administrar decimales](?p=9120#amindecimal) del Administrador del sistema.

**Aclaraciones sobre tipos de monedas  
**A continuación explicamos cada uno de los tipos posibles de monedas:

  * Corriente: es la moneda de curso legal en el país. Por ejemplo, en Argentina es Pesos. Es la moneda que se utiliza para la presentación de estados contables.  
El sistema valida que exista sólo una moneda clasificada como moneda corriente.
  * Extranjera contable: son monedas extranjeras que además, se utilizan para llevar saldos contables. Por ejemplo: Dólares.
  * Otras monedas: se utilizan para las unidades adicionales monetarias o para ingresar valorizaciones de unidades adicionales no monetarias, para valuar a los bienes, y para definir en las cuentas de Tesorería si asociada unidades. Por ejemplo, Yenes, Euros, etc.



Llevar los saldos en moneda extranjera contable significa que cada vez que se registre una operación en la contabilidad, también se guardará el importe en moneda extranjera contable -utilizando para el cambio, el tipo de cotización definido por defecto para la moneda y la cotización que corresponda a la fecha del asiento.  
El [tipo de cotización](?p=11995) y/o la [cotización](?p=11848) puede modificarse, si está activo el parámetro Edita tipo de cotización y/o Edita cotización de la moneda y además, el usuario cuenta con la habilitación correspondiente.

**Condiciones para eliminar una moneda  
**Es posible eliminar una moneda sólo si:

  * no existen asientos analíticos ni asientos resúmenes;
  * no existen cuentas que lleven saldo en unidades adicionales en esa moneda;
  * no existen tipos de valorización que tengan asociada la moneda como moneda de ingreso de las valorizaciones.
  * no existen bienes o tipos de valoración asociados a la moneda.
  * no existen cuentas de tesorería asociadas a la moneda.



Al eliminar una moneda, se borrarán también las cotizaciones definidas. En este caso, el sistema solicita su confirmación.

##### Contenidos relacionados

  * [Video sobre ajustes en Compras](https://ayudas.axoft.com/24ar/videos/cp2_carp_vid/ajustes_cp2_vid/)

  * [Video sobre ajustes en Ventas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/ajustes_gv_vid/)

  * [Video sobre diferencia de cambio en Compras](https://ayudas.axoft.com/24ar/videos/cp2_carp_vid/diferenciacambio_cp2_vid/)

  * [Video sobre diferencia de cambio en Ventas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/diferenciacambio_gv_vid/)

  * [Video sobre parámetros de Tesorería](https://ayudas.axoft.com/24ar/videos/sb_carp_vid/parametrosb_sb_vid/)
