# Modelos de ingreso de comprobantes

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_iv/definiciones_guia_iva/?p=8418/

## Contenido

# Modelos de ingreso de comprobantes

Los modelos de ingreso de comprobante permiten definir las fórmulas y parametrizaciones contables que se utilizarán durante el ingreso de comprobantes.

Se entiende como "modelo" a la definición de un perfil o plantilla, el que busca agilizar la carga de los comprobantes, definiendo los datos que forman parte del comprobante, por ejemplo total gravado, IVA, retenciones, bonificaciones entre otros.  
En general, siempre se genera el mismo "perfil" de comprobante para el mismo cliente o recibimos el mismo "perfil" de comprobante de nuestro proveedor, entendiendo por perfil a los datos que forman parte del comprobante (por ejemplo total gravado, IVA, retenciones, bonificaciones, etc.). Es por eso que los modelos de ingreso están diseñados para representar ese perfil o plantilla y agilizar así la carga de comprobantes.  
Los modelos de ingreso pueden asociarse a clientes y proveedores para indicar cuál es la forma habitual en la que van a ingresar los datos al sistema para ese cliente / proveedor.

La definición de un modelo implica:

  * Ingresar el código de modelo y su nombre.
  * Indicar cuáles son los conceptos (fórmulas) que utiliza el modelo.
  * Indicar la secuencia de ingreso y el comportamiento de cada fórmula.
  * Definir la "parametrización contable" para el modelo.
  * Definir la apropiación por centros de costo correspondiente a cada cuenta del asiento definido en el paso anterior.



__Sugerencias

Es importante aclarar que, si bien un modelo puede utilizarse indistintamente para créditos o débitos de ventas y de compras, puede provocar inconsistencias con respecto a la integración contable ya que son diferentes los asientos que se deben generar. Existen dos alternativas para resolver esta situación:

  * Crear varios modelos similares en cuanto a los importes que intervienen, pero con distinta definición contable. Esta tarea la puede realizar fácilmente mediante el comando Copiar. Se crean todos los modelos necesarios para ventas y compras.
  * Modificar manualmente las imputaciones contables que se generan automáticamente en base al modelo. Obviamente esta tarea, si bien requiere menos modelos de ingreso, requiere un mayor trabajo cotidiano de su parte.



##### Principal

Los modelos de ingreso pueden habilitarse para comprobantes de ventas y compras, de esta forma estarán disponibles desde el proceso [Registración de comprobantes](?p=8433).  
La definición de un modelo implica:

  * Ingresar el código de modelo y su descripción.
  * Indicar si estará habilitado para ventas / compras o ambos.
  * Indicar cuáles serán las fórmulas que utilizará el modelo.
  * Indicar la secuencia de ingreso y el comportamiento de cada fórmula.
  * Definir el "asiento tipo" para el modelo.
  * Definir la regla de apropiación y los tipos de auxiliar correspondiente a cada cuenta del asiento definido en el paso anterior.



##### Fórmulas

###### Detalle del modelo

Fórmulas

Secuencia: indique el orden en que se ingresarán los datos (conceptos) durante la registración de comprobantes.

Fórmula: indique el concepto o fórmula a utilizar.

__Importante

La evaluación de las fórmulas se realiza respetando la secuencia definida y sólo se evalúan aquellas que están en orden creciente a partir del campo que está ingresando. Por ejemplo, no se puede evaluar el tercer concepto si hace referencia al cuarto (porque todavía no lo ha ingresado) pero puede evaluarse si referencia al primer o segundo concepto.

Comportamiento: el comportamiento en el ingreso está directamente relacionado con la forma en que prefiere ingresar la información.

  * Calcula: el sistema evalúa la fórmula, pero el resultado no se exhibe en pantalla. Puede ser utilizado para registrar valores internos. Un ejemplo de su utilización es la registración de la fecha en la que ingresó el comprobante. Esta fecha puede ser utilizada en listados de control.
  * Calcula y Muestra: se evalúa la fórmula asociada y su resultado se exhibe en pantalla. En este caso el resultado no es modificable. Un ejemplo es el total del comprobante.
  * Calcula e Ingresa: el sistema evalúa la fórmula asociada, su resultado se exhibe en pantalla y puede ser modificado.
  * Ingresa: en este caso debe ingresar el valor por pantalla y el sistema no aplica ningún tipo de cálculo ni validación.
  * Ingresa y Verifica: en este caso usted ingresa un valor por pantalla, luego se evalúa la fórmula asociada, y si no coinciden los resultados, se informa el resultado evaluado solicitando una confirmación o rechazo del ingreso.



##### Parametrización contable

Una vez definidos los conceptos a ingresar puede definir la imputación contable defecto que posee ese comprobante.

Orden: ingrese el orden de la cuenta dentro de la imputación contable.

Código de cuenta: indique la cuenta a la que se imputarán los importes. Si usted no informa una cuenta contable, el importe correspondiente a este renglón no formará parte del asiento a generar.

D/H: indique si la cuenta debe ser debitada (D) o acreditada (H). Esta columna se habilita si usted informa una cuenta contable para el renglón del modelo.

Origen: esta opción le permite indicar el origen de la cuenta contable. Esta columna se habilita si usted informa una cuenta contable para el renglón del modelo. Los valores posibles son:

**Código** | **Significado**  
---|---  
CP1 | Cuenta 1 del Proveedor  
CP2 | Cuenta 2 del Proveedor  
CC1 | Cuenta 1 del Cliente  
CC2 | Cuenta 2 del Cliente  
MIC | Modelo de Ingreso  
  
Las opciones 'CP1', 'CP2', 'CC1' y 'CC2' están pensadas para que pueda llevar la contabilidad por cliente/proveedor, rubro, etc.

__Nota

En caso que el proveedor / cliente no tengan asignada una cuenta contable, el sistema tomará la ingresada en el modelo de ingreso de comprobantes.

Leyenda: en esta columna puede ingresar una descripción sobre lo que representa la cuenta contable. Este concepto es el que se asignará por defecto a la leyenda del asiento en cada comprobante, asignando por defecto este dato como leyenda del asiento en cada comprobante. No es un valor obligatorio.

Edita cuenta: de manera predeterminada, este parámetro se encuentra activado. En el momento de generar el asiento en el ingreso del comprobante, permitirá cambiar la cuenta contable.

##### Detalle de apropiaciones

El ingreso de esta grilla es opcional y se habilita sólo si la cuenta contable usa auxiliares contables. Recuerde que al definir un tipo de auxiliar debe asociarle una regla de apropiación.

Tipo de auxiliar: ingrese o seleccione el código o descripción del auxiliar contable a utilizar en el modelo. Sólo se podrán asociar tipos de auxiliares manuales.

Regla de apropiación: ingrese o seleccione el código o descripción de la regla de apropiación habilitadas para el módulo Liquidador de IVA.  
La regla de apropiación de un modelo de ingreso tiene prioridad sobre la regla de apropiación por defecto asociada al tipo de auxiliar.  
Para más información, consulte en la ayuda del módulo Procesos Generales, las opciones de la carpeta Tipos de auxiliares, Reglas de apropiación y Actualización individual de auxiliares contables.

##### Elección del modelo de comprobante adecuado

Un modelo de ingreso de comprobante determina la forma en la que se ingresan los importes del comprobante. Dicha forma de ingreso está determinada por la secuencia de los datos a ingresar (por ejemplo, primero ingresa el neto gravado y luego el total) y por atributos o fórmulas (por ejemplo se debe ingresar el neto gravado, mientras que el IVA y el total del comprobante lo calcula el sistema automáticamente).

**Ejemplos de Modelos**

Los procesos donde puede elegir un modelo son los siguientes:

  * Actualización de clientes
  * Actualización de proveedores
  * Ingreso de comprobantes
  * Ingreso de clientes ocasionales
  * Ingreso de proveedores ocasionales



En principio, defina el modelo de ingreso que desea asociar a cada cliente / proveedor. Para ello tome en cuenta el tipo de operación que habitualmente realiza con su cliente / proveedor.

__Nota

Cuanto más preciso sea el modelo de ingreso habitual seleccionado, más ágil será su carga de datos.

Durante el ingreso de comprobantes, el sistema propone el modelo de ingreso habitual del cliente / proveedor. Si necesita seleccionar un modelo diferente debe pulsar la tecla <F3>.Recuerde que los modelos de ingreso y las fórmulas son totalmente parametrizables. Es su decisión definir más fórmulas y modelos de ingreso para agilizar la carga de comprobantes o si desea trabajar con modelos más generales pero menos ágiles durante el ingreso de comprobantes.

**Código** | **Descripción**  
---|---  
A y M | Para clientes y proveedores RI.  
B | Para clientes CF, INR, EX, RS, NC, PCE, RSS, PCS, EXE.  
C | Para proveedores INR, EX, RS, NC, PCE, RSS, PCS, EXE.  
EXENT | Para clientes exentos en la compra y proveedores exentos en las ventas.  
IMPOR | Para registrar importaciones.  
EXPORT | Para registrar exportaciones.  
RETEN | Para registrar retenciones.  
ANULA | Para registrar comprobantes anulados.  
  
##### Contenidos relacionados

  * [Videos sobre Liquidador de IVA](https://ayudas.axoft.com/25ar/videos/iva_carp_vid/)
