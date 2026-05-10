# Registración de comprobantes

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_rg3572_gla/?p=8433/

## Contenido

# Registración de comprobantes

Mediante este proceso se puede ingresar los comprobantes de ventas y compras, ya sean facturas, notas de crédito, notas de débito o cualquier tipo de comprobante que se haya definido en el proceso [Tipos de comprobantes](?p=8444).

Las características de edición de cada comprobante dependerán del tipo de comprobante, el modelo de ingreso y la configuración de parámetros definida.

Barra de herramientas y teclas de función

La información que se detalla a continuación es de aplicación en el proceso Registracion de comprobantes.

**Comando** | **Descripción**  
---|---  
Aceptar | Confirma la edición y graba.  
Cancelar | Cancela el paso en ejecución y remite el sistema al estado anterior.  
Agregar | Permite el ingreso de un nuevo movimiento.  
Alta continua | Permite realizar el ingreso sucesivo de comprobantes  
Eliminar | Permite eliminar el comprobante en pantalla.  
Modificar registro activo | Permite modificar el movimiento en pantalla.  
Actualizar | Actualiza la información en pantalla.  
Ir al primer registro | Accede al primer movimiento (con fecha más reciente).  
Ir al registro anterior | Accede al movimiento que precede al movimiento en pantalla.  
Ir al siguiente registro | Accede al movimiento posterior al que se muestra en pantalla.  
Ir al último registro | Accede al último movimiento (con fecha más lejana).  
Buscar | Obtiene un movimiento determinado a través de la ventana Buscar, haciendo uso de una o más claves de ordenamiento.  
Aplicar filtro | Permite filtrar los movimientos que cumplen determinadas condiciones.  
Cambiar vista | Permite cambiar la forma de ver la información en pantalla (modo Formulario o modo Grilla).  
Ordenar por | Permite definir un ordenamiento para navegar entre los movimientos.  
Opciones | Lista de accesos directos a otros procesos o funciones relacionados.  
Ayuda | Invoca la ayuda del proceso.  
  
##### Encabezado del comprobante

Comprobante: abarca el tipo y número de comprobante.

Tipo de comprobante: es el código del tipo de comprobante que está ingresando.

Número: es el que corresponde al comprobante que está ingresando. Si el tipo de comprobante permite ingreso por lote, el número ingresado en este campo será considerado como el comienzo del lote.

Hasta comprobante: si el tipo de comprobante permite ingreso por lote, debe ingresar el último número de comprobante del lote.

La numeración de los comprobantes, admitirá el ingreso de caracteres alfanuméricos, según lo definido en [Tipos de comprobantes](?p=8443).

Proveedor: en esta sección deberá seleccionar el proveedor al que pertenece el comprobante si el tipo de comprobante seleccionado en el ingreso es de Compras. Si especifica que se trata de un proveedor ocasional (código '000000'), se habilitará el botón para que ingrese los datos del mismo.

__Importante

Desde el proceso [Proveedores](?p=8430) usted cuenta con la posibilidad de predeterminar datos, para agilizar la carga de comprobantes correspondientes a proveedores ocasionales.

Cliente: en esta sección deberá seleccionar el cliente al que pertenece el comprobante si el tipo de comprobante seleccionado en el ingreso es de Ventas. Si especifica que se trata de un cliente ocasional (código '000000'), se habilitará el botón para que ingrese los datos del mismo.

__Importante

Desde el proceso [Clientes](?p=8349) usted cuenta con la posibilidad de predeterminar datos, para agilizar la carga de comprobantes correspondientes a clientes ocasionales.

Pulsando la tecla <F6> desde el campo Código podrá acceder al proceso asociado, y agregar un nuevo cliente / proveedor al sistema, o bien modificar uno existente.

Fecha: es la fecha de emisión del comprobante que está ingresando.

El sistema valida que la fecha sea posterior a la Fechas de cierre para el ingreso de comprobantes de compras o ventas, según sea el caso, definidas en el proceso Fechas de cierre en Procesos generales.

Modelo de ingreso: el modelo define qué datos deben ingresarse en el ingreso de comprobantes, la secuencia y la forma de cálculo. También puede tener definida la parametrización contable para la generación del asiento.

Cotización: en el alta de un nuevo registro, se propone la cotización de la moneda extranjera contable para la fecha y hora del comprobante.

Los comprobantes son expresados en pesos al tipo de cambio correspondiente, al igual que el asiento que tenga asociado.  
En todos los casos se informa la moneda de origen del comprobante.

Fecha contable: es aquella que tomará el sistema para registrar los comprobantes en el Subdiario de IVA.  
En el caso de comprobantes de ventas, este campo no es editable, debido a que los comprobantes de ventas deben registrarse con su fecha de origen.  
En el caso de comprobantes de compras, el campo es editable. El sistema valida que esta fecha no sea inferior a la fecha de emisión.

Actividad: ingrese la actividad que realiza la empresa al emitir el comprobante, si el tipo de comprobante interviene en ingresos brutos, el sistema propondrá la actividad por defecto de la empresa.  
Si ingresa una actividad, el sistema calcula automáticamente el importe gravado para ingresos brutos. Esto puede visualizarse desde la solapa Jurisdicciones y Actividades IIBB en la sección de Detalle de actividades, y si lo considera necesario puede desglosar el neto gravado en varias actividades para el mismo comprobante.  
Para proponer la actividad por defecto, el sistema tiene en cuenta el criterio de cálculo de la base imponible configurado en Actividades. El mismo puede ser 'Sobre las ventas' o bien 'Sobre la diferencia entre compras y ventas'. En el primer caso sólo va a proponer la actividad para los comprobantes de ventas, mientras que en el segundo caso la va a proponer tanto para comprobantes de compras y ventas.

Origen: este campo es completado en forma automática por el sistema. Los valores posibles son 'IVA', propios del módulo, o bien 'Ventas' o 'Compras', en caso de que el comprobante sea importado desde Ventas o Compras. Este campo no es editable.

Clasificación: ingrese la clasificación del comprobante para el sistema AFIP - SIAp El sistema propone la clasificación habitual del tipo de comprobante ingresado.  
Seleccione 'Venta mixta' o 'Compra mixta' según se trata de un comprobante de Ventas o Compras, cuando el comprobante ingresando responde a más de una clasificación. En este caso, complete la clasificación proporcionando los distintos conceptos según su clasificación en la solapa Clasificación de comprobantes.  
Seleccione 'Sin Clasificar' si desea que el comprobante no sea considerado por AFIP - SIAp

__Importante

Para poder cumplir con lo estipulado en la RG 3711 e informar el F2002, debe completar la actividad principal y las actividades secundarias de la empresa desde proceso Datos de la empresa. En la clasificación del comprobante tenga en cuenta que por defecto se asignará la actividad principal para la clasificación SIAp, modifíquela si es necesario. Desde la consultas live podrá visualizar la determinación de los débitos fiscales por actividad y de los créditos fiscales.

Es importante que haya completado el significado de las fórmulas para un correcto funcionamiento del sistema en lo referido a SIAp - IVA.  
Sólo son consideradas los siguientes tipos de fórmulas:

**Tipo de fórmula** | **Ventas** | **Compras**  
---|---|---  
GR - Gravado | X |   
NG - No gravado | X | X  
EX - Exento | X | X  
IG - IVA general |  | X  
ID - IVA diferencial |  | X  
  
Operación sujeto vinculado: ingrese la operación del comprobante según lo establecido en la RG 3572 para el cliente o proveedor que estén definidos como sujetos vinculados y siempre que la empresa informe sobre operaciones de mercado interno - sujeto vinculados. El sistema propone por defecto la operación habitual definida en el cliente/proveedor.

Para más información consulte la [Guía sobre implementación RG 3572 - Sujetos vinculados](?p=11911).

Tipo comprobante AFIP: indique el valor según el tipo de comprobante de la operación. Esta opción se habilita cuando en la carga del comprobante esté completa el tipo y letra del comprobante. Por defecto se le asignará el valor definido utilizando para esto el tipo de comprobante interno definido en el [tipo de comprobante](?p=8443), el mismo puede ser modificado. Este es un dato que va a tenerse en cuenta en el archivo generado para RG 3685.

Operación AFIP: indique el valor según la operación del comprobante, por defecto se le asignará el valor definido como operación habitual en el [cliente](?p=8350) o [proveedor](?p=8431), sino asignará el valor definido en el proceso [parámetros](?p=8426) del módulo, el mismo puede ser modificado. Este es un dato que va a tenerse en cuenta en el archivo generado para RG 3685.

Interviene en RG 3685 / 3711 / 4597: por defecto toma el valor definido en el tipo de comprobante. Los comprobantes que no participen en el libro de IVA no van a ser tenidos en cuenta en el archivo generado para RG 3685 / 3711 / 4597.

IVA no computable: se habilita para comprobantes de compras. Estos comprobantes no van a ser tenidos en cuenta en el archivo generado para RG 3685.

Nro de despacho: se habilita para comprobante de compras. Este es un dato que va a tenerse en cuenta en el archivo generado para la RG 3685

Comprobante electrónico: utilice esta opción para indicar que si el comprobante es electrónico.

CAE/CAI: ingrese el código de autorización electrónico para cada comprobante, o el código de autorización de impresión para el talonario en caso de no ser un comprobante electrónico, ambos otorgados por AFIP. Este es un dato que va a tenerse en cuenta en el archivo generado para RG 3685.

Fecha vencimiento CAE/CAI: si el código de autorización electrónico o de impresión está completo, el sistema requiere que complete la fecha de vencimiento, y valida que la fecha ingresada sea mayor o igual que la fecha de emisión del comprobante. Este es un dato que va a tenerse en cuenta en el archivo generado para la RG 3685.

Operación con intermediario: se habilita para comprobantes de compras.

CUIT intermediario: indique la clave única del intermediario, este dato es obligatorio si en la operación interviene un intermediario. Este es un dato que va a tenerse en cuenta en el archivo generado para RG 3685.

Denominación intermediario: ingrese la razón social del intermediario, este dato es opcional. Este es un dato que va a tenerse en cuenta en el archivo generado para RG 3685.

##### Datos contables del comprobante

Genera asiento: indica si el comprobante genera asiento. Por defecto se propone el definido en el proceso [Tipos de comprobantes](?p=8444). Su edición también dependerá de lo configurado en el tipo de comprobante.  
El asiento se puede generar al ingresar el comprobante, configuración que se realiza desde [Parámetros contables](?p=8424) o podrá generarlo posteriormente en forma manual desde el proceso [Generación de asientos contables](?p=8390).  
Si el tipo de comprobante fue configurado para modificar el asiento en el ingreso del comprobante, al procesar el alta del mismo, se abrirá la pantalla del asiento contable.

Si en [Parámetros contables](?p=8424) se activa la marca Respeta definición del modelo de ingreso, no tendrá la posibilidad de modificar la estructura del asiento definida en la parametrización del modelo de ingreso. Puede informar el detalle de auxiliares.

  * Para consultar el asiento de registración generado para el comprobante utilice <Ctrl + S>.
  * Para consultar información de control acerca del ingreso y la última modificación del asiento de registración utilice <Ctrl + U>. Se exhibe el usuario, fecha y terminal en la que se realizó la operación.



Si se trata de un asiento exportado a Contabilidad o a otro sistema, se exhiben otros datos referidos al origen de la exportación (origen, número de lote de exportación, usuario, fecha y terminal).

Estado del asiento: informa si el asiento se encuentra sin generar, está generado o exportado. Este dato no es editable.

###### Funcionalidad de las grillas

Al operar con la grilla de renglones de movimientos, de asientos, están disponibles las siguientes funciones:

  * Primero (ir a la primera fila)
  * Anterior (ir a la fila anterior)
  * Siguiente (ir a la fila siguiente)
  * Último (ir a la última fila)
  * Insertar nueva fila <Ins>
  * Eliminar fila actual <Del>
  * Mover al principio
  * Mover renglón hacia arriba <Alt + Up>
  * Mover renglón hacia abajo <Alt + Down>Mover al final.



**En la grilla de renglones de asiento se agrega:**

  * Invertir importes (cambia de columna el importe) <F4>
  * Asignar importe por la diferencia <F9>
  * Apertura automática / manual de auxiliares.



Para acceder a estas funciones, haga clic en el botón correspondiente que se exhibe en el encabezado de la grilla en movimientos, en asientos y en el detalle de auxiliares.

###### Datos de los renglones del asiento

Los datos se exhiben en formato grilla, de acuerdo a la definición de la parametrización contable en el modelo de ingreso.  
Al pie de la grilla, se exhibe la suma de los importes en la columna "Debe", la suma de los importes en la columna "Haber" y la diferencia entre ambas.  
Cada renglón se compone de los siguientes datos:

Número: es el número de renglón del asiento. Este dato no es editable.

Código de cuenta: ingrese o seleccione el código de cuenta contable. Este dato es de ingreso obligatorio. En caso de poder editar la cuenta o de poder agregar más renglones usted puede seleccionar una cuenta contable habilitada para el módulo.

Descripción de cuenta: este dato se completa automáticamente al completar la columna "Código de cuenta".

Debe / Haber: por defecto el importe se completará automáticamente de acuerdo al movimiento. Usted puede editar el importe. El sistema realiza los siguientes controles: el asiento deberá tener dos líneas como mínimo, el asiento deberá balancear, no se permite ingresar importes negativos, ni dejar renglones con importe en cero, los importes del asiento deben coincidir con los valores ingresados en el movimiento. El ingreso de este dato es obligatorio.  
Si ingresa el importe en la columna "Debe", se deshabilita la edición de la columna "Haber" y viceversa.  
Haga clic en "..." para abrir la calculadora.

###### Detalle de auxiliares

Auxiliares: el valor de este campo depende de la definición del parámetro Usa auxiliares contables en la cuenta contable.  
Haga clic en "..." para ingresar o consultar las imputaciones a auxiliares y subauxiliares contables de la cuenta contable en la que está posicionado. Las imputaciones pueden ser manuales o bien, basadas en reglas de apropiación automáticas asociadas a la cuenta - tipo de auxiliar.  
Es posible ingresar el Porcentaje y que se calcule en forma automática el Importe, o viceversa. Si la imputación a auxiliares contables queda pendiente por el total del importe de la línea o renglón del asiento, el Porcentaje será igual a 100% para el auxiliar 'Sin Asignar'.  
Usted puede seleccionar una regla de apropiación, puede elegir una regla que esté habilitada para el módulo.

Leyenda: el sistema exhibe la leyenda definida en el modelo de asiento, será posible modificarla.

##### Renglones del comprobante

En la parte inferior de la pantalla, ingrese los importes correspondientes a los conceptos definidos en [Modelos de ingreso de comprobantes](?p=8418).  
El modelo de ingreso define qué datos debe ingresar, su secuencia, y su forma de cálculo.  
Tenga en cuenta que el modelo de ingreso define qué datos debe ingresar, su secuencia, y su forma de cálculo.

##### Comprobantes relacionados

Comprobante de origen de retención: esta sección permite asociar una factura 'M' en el ingreso de comprobantes de retención. Se habilitará cuando se esté ingresando un tipo de comprobante de origen Ventas.  
Haga clic sobre el botón "Buscar" para acceder a una búsqueda de comprobantes a referenciar.  
Seleccione un renglón de la consulta de comprobantes y haga doble clic o presione "Aceptar" para asociar el comprobante.  
Con el botón "Limpiar" podrá desasociar un comprobante asociado previamente.

Comprobante de origen de la retención IIBB: haga clic sobre el botón "Buscar" para acceder a una búsqueda consultando los comprobantes del cliente o proveedor, para asociar el comprobante que dio origen a la retención.  
Seleccione un renglón de la consulta de comprobantes y haga doble clic o presione "Aceptar" para asociar el comprobante.  
Con el botón "Limpiar" podrá desasociar un comprobante asociado previamente.

Comprobante de origen de la retención SICORE: esta sección sólo se habilitará cuando se esté ingresando un tipo de comprobante de origen Compras.  
Usted debe activar esta opción para ingresar los datos que dieron origen a la retención de SICORE que desea asociar al comprobante.  
Los datos a completar son:

  * Comprobante
  * Fecha
  * Importe
  * Base de cálculo



##### Modificación de un comprobante

Para poder modificar datos puntuales del comprobante que está en pantalla. Sólo podrá modificar comprobantes con fechas posteriores a las fechas de cierre definidas en Fechas de cierre o cuyo asiento no haya sido transferido a contabilidad.  
Para el caso de comprobantes que hayan sido importados desde Gestión, si tiene activo el parámetro Permite modificación de comprobantes de Tango Gestión en los [Parámetros de Liquidador de IVA](?p=8426), se aplicará del mismo modo que en los comprobantes ingresados desde el Liquidador de IVA. Caso contrario, no podrán modificarse.  
Una vez localizado el comprobante a modificar, se editarán los siguientes datos:

Datos del cliente / proveedor ocasional: haga clic en este botón, el cual estará habilitado si el comprobante corresponde a un cliente / proveedor ocasional, para modificar datos del mismo.

Fecha de emisión: el sistema valida que la fecha del comprobante a modificar sea posterior a la fecha de cierre definida en el proceso Fechas de cierre.

Fecha contable: el sistema valida que la fecha del comprobante a modificar sea posterior a la fecha de cierre definida en el proceso Fechas de cierre.  
La fecha contable sólo será posible editarla si el comprobante es de Compras.

Modelo de ingreso: al modificar este valor se conservarán los renglones del comprobante en los cuales haya ingresado valores, y tendrá a su disposición los demás renglones del modelo de ingreso para realizar las modificaciones que considere necesarias.

Cotización: sólo podrá modificar la cotización de los comprobantes en moneda corriente.

Actividad: si modifica la actividad desde la solapa principal, el sistema pedirá confirmación para recalcular el neto gravado para ingresos brutos. También podrá modificar lo que se considere necesario desde la solapa 'Jurisdicciones y actividades IIBB'.

Clasificación para AFIP - SIAp: en caso de modificar la clasificación, el sistema comunicará si no coincide con el valor original del comprobante, y solicitará confirmación para realizar la distribución correspondiente, la cual se podrá observar en la solapa Clasificación de comprobantes.

Genera asiento: si el comprobante tiene el asiento en estado sin generar o generado, podrá modificar esta marca. Si destilda esta opción y tenía el asiento generado, el sistema solicitará confirmación para eliminarlo.

Auxiliares: puede modificar la distribución de los importes de los auxiliares contables, siendo válidas las consideraciones mencionadas para la [Registración de comprobantes](?p=8433).

Solapa comprobantes relacionados: podrá modificar los comprobantes seleccionados o ingresados en dicha solapa.

##### Eliminación de un comprobante

Sólo se podrán eliminar comprobantes con fechas posteriores a las fechas de cierre definidas en Fechas de cierre o cuyo asiento no haya sido transferido a contabilidad.  
El sistema solicitará confirmación para la eliminación del registro.

##### Contenidos relacionados

  * [Videos sobre Liquidador de IVA](https://ayudas.axoft.com/24ar/videos/iva_carp_vid/)
