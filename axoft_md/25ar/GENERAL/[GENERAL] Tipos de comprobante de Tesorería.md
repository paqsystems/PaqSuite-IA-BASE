# Tipos de comprobante de Tesorería

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_rg3685_gla/?p=10253/

## Contenido

# Tipos de comprobante de Tesorería

Todo movimiento que ingresa al módulo tiene asociado un tipo de comprobante. Este proceso permite actualizar, consultar y listar los tipos de comprobante a utilizar.

Los datos asociados a un tipo de comprobante se presentan en tres solapas: [Principal](?p=10253#principal), [Módulos](?p=10253#modulos) y Observaciones:

##### Principal

Tipo de comprobante: es el código (de hasta tres caracteres) con el que se identifica un comprobante, por ejemplo: 'ING', 'REC', 'VAL', etc.

Tipo de comprobante de reversión  
Existe un tipo de comprobante fijo, provisto con el sistema, que se utiliza para realizar reversiones o anulaciones de comprobantes. El código de este comprobante es 'REV'.  
No puede eliminarse y sólo son modificables algunos datos: Concepto, Descripción y Orden, siendo automático el tipo de numeración.

Tipos de comprobante para integraciones con otros módulos  
Si el sistema trabaja en forma integrada, debe definir los siguientes tipos de comprobante para que sea factible el enlace:

  * FAC: para facturas al contado del módulo Ventas.
  * REC: para cobranzas en cuenta corriente.
  * O/P: para pagos a proveedores.
  * Sin restricción de nombre, los comprobantes a utilizar para las cancelaciones de documentos en los módulos Ventas y Compras / Proveedores, y para facturas al contado de Compras / Proveedores.
  * Créditos: los tipos de comprobante créditos contado definidos en el módulo Ventas.
  * Débitos: los tipos de comprobante débitos contado definidos en el módulo Ventas.



Descripción: este campo permite ingresar el nombre completo del comprobante.

Clase: es posible definir la clase habitual asociada al tipo de comprobante. La clase aquí definida será la propuesta por defecto al utilizar el tipo de comprobante en el ingreso de movimientos de tesorería.

Edita clase en el ingreso de movimientos: si este parámetro está tildado le permitirá modificar la clase en el momento de ingresar un movimiento de tesorería. Por defecto, está tildado. Para su modificación, el sistema controla que no existan [modelos de ingreso](?p=10275) asociados al tipo de comprobante.

Clasificación habitual: si está activo el [Parámetros de Tesorería](?p=10293) Utiliza clasificación es posible indicar una clasificación habitual para cada tipo de comprobante.

Controla clasificación: si utiliza clasificación, elija una modalidad para su aplicación. Las opciones posibles son las siguientes:

  * Siempre: el ingreso de un código de clasificación es obligatorio.
  * A confirmar: el ingreso de una clasificación es optativo, pero en el caso de no especificar un valor, el sistema solicita su confirmación.
  * A pedido: el ingreso de una clasificación no es obligatorio, el sistema no solicita su confirmación ante la omisión de este dato.



Los campos anteriores (para la clasificación de comprobantes) estarán disponibles si en el proceso [Parámetros de Tesorería](?p=10293) está habilitado el parámetro Utiliza clasificación y la Operación a clasificar correspondiente a la clase del comprobante.

Número de orden: este número permite dar un ordenamiento a los tipos de comprobante para el análisis en algunos informes.  
Es un campo obligatorio.

__Nota

Este número es modificable, permitiendo reagrupar de distintas maneras a los comprobantes.

##### Informes basados en rangos de comprobantes

Para los informes, al requerir rangos de comprobantes, el sistema considera los números de orden de comprobantes asignados a los tipos de comprobante. Si desea variar el ordenamiento debe modificar este valor.  
Cada tipo de comprobante puede tener asignado un número de orden, o bien varios comprobantes pueden tener un mismo número de orden asociado.

**Ejemplo...**

**Tipo Comprobante** | **Nro. de orden**  
---|---  
REC (Recibos) | 1  
ING (Otros Ingresos) | 1  
O/P (Ordenes de Pago) | 2  
VAL (Vales al personal) | 3  
  
Al solicitar rangos, si se ingresa desde número de orden 2 hasta número de orden 3, sólo se listarán órdenes de pago y vales.

Valores habituales

Modelo de impresión: es posible asociar a cada tipo de comprobante un modelo de impresión habitual. Los modelos de impresión se encontrarán previamente definidos.

Imprime comprobante en el ingreso de comprobantes: tilde este parámetro para imprimir los comprobantes generados desde el proceso [Movimientos de Tesorería](?p=10296).

Cuenta principal: ingrese el código de cuenta que habitualmente es única en un movimiento.

##### Estructura del comprobante

Es necesario que al cargar cada comprobante, usted defina sólo una cuenta deudora o acreedora (es decir, que el asiento posea una sola cuenta debitada y una o varias acreditadas o viceversa). Habrá entonces, sólo una cuenta deudora o acreedora y una o varias contracuentas de esa cuenta principal.  
Por ello, al definir un comprobante, es posible ingresar la estructura habitual que tendrán los movimientos asociados a ese comprobante.  
Según sea la clase del comprobante, la cuenta principal tiene condiciones, ya que cada [clase](?p=10296) representa un tipo de transacción y la cuenta debe ser del tipo apropiado.

Tipos de imputación: si habitualmente la cuenta principal se asocia a un débito, el valor a ingresar será 'D', y si se asocia a un crédito será 'H'.  
Sólo se puede definir en los casos donde la clase permita indistintamente ambos valores para la cuenta principal, de lo contrario este valor es asignado en forma automática.

__Nota

Durante el ingreso de una operación al referenciar un tipo de comprobante, si estos campos están definidos, se exhiben por defecto pero ambos pueden ser modificados.

Concepto: este concepto se utiliza en dos momentos:

  * Se exhibe por defecto como concepto, al ingresar un comprobante asociado al tipo de comprobante.
  * Se toma como concepto del asiento resumen que agrupa los movimientos del tipo de comprobante.



Numeración

Primer número habilitado / Último número habilitado: es posible ingresar un rango de números habilitados para cada tipo de comprobante.

Controlar el ingreso de movimientos  
Estos campos permiten el control en el ingreso de movimientos. Sólo podrán ingresarse comprobantes cuyo número pertenezca al rango habilitado para ese tipo de comprobante.

__Nota

Estos campos no son obligatorios. Sirven para establecer controles.

El sistema realizará el control en caso de existir estos topes. Si no existen, acepta el ingreso de cualquier número de comprobante. El usuario autorizado podrá modificar los topes en cualquier momento, a medida que se realicen habilitaciones de talonarios para los distintos comprobantes utilizados.

__Nota

Puede ser ingresado un solo tope (primero o último), y en este caso la validación se realizará con respecto al valor existente.

Cuando el tipo de comprobante se utiliza para movimientos de integración con Ventas o Compras / Proveedores, no hay que definir rangos de habilitación, ya que éstos están controlados desde los módulos de origen.

Tipo de numeración: puede optar por automática o manual.

  * Automática: en cada ingreso de este tipo de comprobante el sistema propondrá el próximo número correlativo, en base al último que se encuentre registrado para el mismo tipo de comprobante.
  * Manual: el número se debe ingresar directamente. En general, se recomienda este tipo de numeración para aquellos comprobantes que no son internos de la empresa y donde los números no siguen un orden correlativo.



Edita cuenta principal en el ingreso de movimientos: si este parámetro está tildado, usted podrá modificar la cuenta principal en los [movimientos de Tesorería](?p=10296).

Edita número de comprobante: si la numeración se define como 'Automática', puede indicar si el número propuesto por el sistema será modificable.

##### Módulos

Desde esta solapa defina en qué módulo (Ventas, Compras, Tesorería) es posible utilizar el comprobante en edición.  
Los tipos de comprobante reservados 'FAC' y 'REC' están disponibles en el módulo Ventas. El tipo de comprobante 'O/P' está disponible en el módulo Compras y el tipo de comprobante 'REV' en Tesorería. Esta configuración no puede ser modificada.  
La parametrización de los tipos de comprobante restantes es totalmente libre.

##### Contenidos relacionados

  * [Video sobre multicaja en Ventas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/multicaja_gv_vid/)

  * [Video sobre notas de crédito](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/nc_gral_vid/)

  * [Video sobre parámetros de Compras](https://ayudas.axoft.com/25ar/videos/cp2_carp_vid/parametros_cp2_vid/)

  * [Video sobre parámetros de Tesorería](https://ayudas.axoft.com/25ar/videos/sb_carp_vid/parametrosb_sb_vid/)

  * [Video sobre recibos y notas de débito](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/recibosnd_gral_vid/)

  * [Videos sobre cuentas corrientes](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/cuentacorriente_gv_vid/)

  * [Videos sobre el Facturador](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/facturador_gv_vid/)

  * [Videos sobre parámetros de Ventas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/parametros_gv_vid/)

  * [Videos sobre seguimiento de cheques de terceros](https://ayudas.axoft.com/25ar/videos/sb_carp_vid/chequetercero_sb_vid/)

  * [Videos sobre transferencia de valores](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/transfvalor_gral_vid/)
