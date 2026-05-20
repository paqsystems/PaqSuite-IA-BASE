# Guía sobre perfiles de compra

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_cp2/guia_perfiles_cp2/

## Contenido

# Guía sobre perfiles de compra

Los perfiles permiten adaptar el ingreso de datos a las necesidades de su empresa, como así también, determinar restricciones para algunos usuarios en particular, otorgando permisos sobre determinadas operaciones.

Usted puede definir distintos perfiles para los usuarios del sistema, de modo que, algunos procesos operen en base a diferentes parametrizaciones y permisos según el rol de la persona que los esté ejecutando.  
Cada perfil definido podrá tener asociado a uno o más usuarios.  
Al definir un perfil de usuario, es posible configurar los permisos sobre cualquiera de las siguientes operaciones:

  * [Solicitud de compra](https://ayudas.axoft.com/25ar/solicp_cp2)
  * [Orden de compra](https://ayudas.axoft.com/25ar/ordencpgeneracion_cp2)
  * [Factura de compra](https://ayudas.axoft.com/25ar/comprobfactura_cp2)
  * [Autorización de comprobantes](https://ayudas.axoft.com/25ar/ccorrautcomprpagar_cp2)



Cabe mencionar que la definición de perfiles no es obligatoria. Si un usuario no tiene asignado ningún perfil, entonces estarán disponibles las funciones del módulo Compras que se hayan configurado en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2).

__Nota

Recuerde que la tecla rápida <F3> permite realizar la búsqueda de un texto en el árbol de procesos de todos los módulos. Como resultado, se exhibirá el nombre de los procesos que incluyen el texto ingresado, con la indicación del módulo y carpeta en la que se encuentran.  


##### Puesta en marcha

Para definir que un determinado usuario opere bajo un perfil debe realizar el procedimiento detallado a continuación:

1) Desde Archivos | Carga Inicial | Perfiles elija una de las opciones:

  * de factura de compra
  * de autorización de comprobantes
  * de solicitud de compra
  * de orden de compra



2) Defina los parámetros correspondientes a ese perfil, para ello:

  1. Agregue un perfil.
  2. Defina un código para el nuevo perfil e ingrese una descripción. Complete el resto de los campos de las ventanas.



3) Luego de ingresar todos los valores necesarios, indique los usuarios que tendrán el perfil asociado.

__Nota

Tenga en cuenta que no es obligatorio que asigne usuarios en este momento.

Para más información sobre el alta y modificación de usuarios, consulte [la sección correspondiente](?p=9111).  
Recuerde que los distintos procesos de compras tienen operaciones en común, por lo tanto, al momento de asignar perfiles a una persona que utiliza varios procesos procure mantener una relación entre parámetros similares.

**Ejemplo de implementación  
**A continuación se expone un ejemplo en el que se detallan los parámetros más importantes a configurar en cada uno de los perfiles, definidos según el rol que desempeñan los usuarios: La empresa que representaremos utiliza el circuito de compras en forma completa para la adquisición de insumos de librería.  
Los empleados ingresan solicitudes de compras para los insumos que utilizan. Dependiendo del tipo de solicitud se asigna a un comprador u otro, quien emite las ordenes de compra necesarias para cumplir con los requerimientos (con previa autorización del Jefe de Compras). Luego se reciben las facturas y remitos del proveedor, las cuales son ingresadas al sistema por el operador de compras.

Antes de comenzar a crear los perfiles, deberemos dar de alta los usuarios, a los cuáles les asignaremos los perfiles.

**Perfiles de solicitud de compra  
**Es posible crear un perfil genérico, que sea utilizado para que todos los empleados ingresen [Solicitudes de compra](https://ayudas.axoft.com/25ar/perfsolicitudcp_cp2) correspondientes a los insumos de librería. Este perfil le permitirá agilizar y restringir la carga de datos, que realicen los usuarios para este tipo de solicitud.

_Perfil "Insumos de librería"  
_A continuación se detallan las funcionalidades disponibles para el usuario asociado a este perfil.

  * Edita la clasificación definiendo si la solicitud es, por ejemplo, de prioridad alta, media, urgente o baja. Consulte cómo definir una [clasificación](https://ayudas.axoft.com/25ar/clasificacion1_cp2) para cada tipo de comprobante.
  * Utiliza siempre "gastos de librería" como el tipo de gasto que corresponde a la imputación. Para este ejemplo el campo [clasificación de comprobantes](?p=11840) se ha definido con el comportamiento 'Muestra'.
  * Visualiza todos los ítems del encabezado menos aquellos que correspondan a datos propios del usuario, como es el caso de solicitante, sucursal y sector, los cuales se presentan en modo 'Edita'.
  * Ingresa el tipo de artículos y observaciones en el caso de ser necesario.



Para más información consulte el tópico [Perfiles de solicitud de compra](https://ayudas.axoft.com/25ar/perfsolicitudcp_cp2).

**Perfiles de orden de compra  
**Es posible crear un perfil que sea utilizado para el comprador, que realiza las compras de insumos de librería, y otro para el jefe de compras, responsable de autorizar todas las ordenes emitidas y de generar otros tipos de ordenes. De esta forma obtendremos para el primer caso, un ingreso de [orden de compra](https://ayudas.axoft.com/25ar/ordencpgeneracion_cp2) ágil y restrictivo, y para el segundo caso, una carga más completa y flexible.

_Perfil "Operador compras librería"_

  * Utiliza siempre el mismo talonario y solo podrá modificar la fecha de recepción.
  * Visualiza casi todos los datos de la compra, a excepción de la lista de precios que podrá editarse, y tendrá la clasificación de comprobante ya definida como gastos de librería.
  * Puede dar de alta artículos y editar plan de entrega, precio y bonificación.
  * Ingresa tipo de artículos y observaciones en el caso de ser necesario.
  * Siempre referencia solicitudes de compra y solo traslada plan de entrega y comprador a la orden de compra, ya que para realizar esta tarea es necesario que las ordenes que genere estén fundamentadas en una solicitud.
  * Ingresa observaciones en caso de ser necesario.



_Perfil "Jefe de compras"_

  * Selecciona talonarios y modifica fechas.
  * Edita todos los datos de la compra y la clasificación, no se han definido valores por defecto porque por su rol, debe poder dar de alta cualquier tipo de orden.
  * Puede dar de alta artículos y editar plan de entrega, precio y bonificación.
  * Ingresa tipo de artículos y observaciones para este, en caso de ser necesario.
  * Referencia flexiblemente las solicitudes de compra y no traslada los datos a la orden
  * Ingresa observaciones, leyendas y textos, en caso de ser necesario.



Para más información consulte el tópico [Perfil de Orden de Compras](https://ayudas.axoft.com/25ar/perfordencp_cp2).

**Perfiles de factura de compra  
**Se puede crear un perfil que sea utilizado para el operador que ingresa habitualmente todas las facturas de proveedores y otro para el jefe de compras quien tiene a cargo la supervisión del sector, de esta forma obtendremos para el primer caso una carga de [facturas de compra](https://ayudas.axoft.com/25ar/comprobfactura_cp2) mas ágil y restrictiva; y para el segundo caso, una carga completa y flexible.

_Perfil "Operador de facturación"_

  * Visualiza casi todos los datos del encabezado de la factura y sólo puede editar el número de comprobante, la fecha de emisión y contable, el concepto, la condición de compra y la [clasificación de comprobante](?p=11840).
  * Puede dar de alta proveedores e ingresar proveedores ocasionales.
  * Puede dar de alta artículos y editar unidad de medida, precio y bonificación.
  * Tiene un control de diferencias flexible, sin poder modificar IVA / Impuestos ni vencimientos.
  * Referencia ordenes de compra flexiblemente, ya que ingresa cualquier tipo de factura de proveedores.
  * No modifica imputaciones contables.



_Perfil "Jefe de compras"_

  * Edita todos los datos del encabezado de la factura.
  * Puede dar de alta proveedores e ingresar proveedores ocasionales.
  * Puede dar de alta artículos y editar unidad de medida, precio y bonificación.
  * Tiene un control de diferencias flexible, pudiendo editar IVA / Impuestos vencimientos y subtotales.
  * Referencia ordenes de compra flexiblemente y edita partidas y depósitos.
  * Modifica imputaciones contables, en caso de ser necesario, respetando la definición del tipo de asiento y verificando la existencia de cuentas contables.



Para más información consulte el tópico [Perfiles de factura de compra](https://ayudas.axoft.com/25ar/perffacturacp_cp2).

##### Contenidos relacionados

  * [Ayudas sobre Compras con Importaciones](https://ayudas.axoft.com/25ar/ayudas/cp2/)

  * [Video sobre parámetros de Compras](https://ayudas.axoft.com/25ar/videos/cp2_carp_vid/parametros_cp2_vid/)

  * [Video sobre usuarios, roles y permisos](https://ayudas.axoft.com/25ar/videos/operacion_carp_vid/perfiles_gral_vid/)

  * [Videos sobre remitos y facturas de compra](https://ayudas.axoft.com/25ar/videos/cp2_carp_vid/remitofactura_cp2_vid/)
