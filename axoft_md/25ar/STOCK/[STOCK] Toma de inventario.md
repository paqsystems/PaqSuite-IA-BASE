# Toma de inventario

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_st/gua_perfil_st/?p=17358/

## Contenido

# Toma de inventario

Desde este proceso es posible ingresar el conteo de inventario realizado en los diferentes depósitos.

De existir diferencias entre el stock real y el stock del sistema, podrá realizar un ajuste de inventario no valorizado. En el caso de necesitar que el ajuste sea valorizado, ingréselo desde el proceso [Ajuste de inventario](https://ayudas.axoft.com/25ar/ajusteinventario_st).  
En caso de tener activo el parámetro general Lleva doble unidad de medida desde el proceso [Parámetros de Stock](https://ayudas.axoft.com/25ar/parametrogeneral_st) y para artículos que llevan doble unidad de medida, la toma de inventario se podrá realizar para las dos unidades de medida de stock.  
Si el artículo usa el control entre las unidades de stock durante el ingreso de comprobantes, en la toma de inventario no se aplica el control.

Tenga en cuenta:

  * La toma de inventario es un comprobante independiente, que no conlleva movimiento de stock.
  * No se tendrán en cuenta las series.



##### Comandos

Agregar  
Desde esta función sólo es posible ingresar comprobantes de toma de inventario, con los artículos y sus respectivos depósitos. El comprobante quedará con el estado 'Ingresado'.

Actualizar  
Este comando permite modificar todos los comprobantes que estén con estado 'Ingresado' o 'En Proceso'.  
Para el estado 'En Proceso', sólo será posible agregar o eliminar artículos de los depósitos bloqueados, si el perfil así lo permite. Para el estado 'Ingresado' es posible modificar todos los campos.

Acciones asociadas  
Detallamos en los siguientes ítems, las acciones asociadas a la toma de inventario.

Comenzar Conteo de Inventario  
Usted podrá, en primera instancia, bloquear los depósitos (en caso de no aceptar cargar las cantidades), sino se ingresarán las cantidades del recuento físico para los artículos inventariados, con sus partidas.  
No se calcularán las diferencias.  
Es posible agregar artículos de los depósitos bloqueados (si el perfil lo permite).  
Si no ingresa las cantidades en este proceso, deberá hacerlo desde el comando Actualizar.  
El comprobante quedará con estado 'En Proceso'.

Procesar diferencias  
Se calcularán las diferencias existentes entre el stock real y el stock del sistema. También, se validarán las partidas cargadas con las existentes en el sistema.  
No es posible editar los datos.  
El comprobante quedará con estado 'Procesado'.

Realizar Ajuste de Inventario  
De existir diferencias tanto en las partidas como en las cantidades, se realizará el ajuste de inventario.  
Después de ajustar, se desbloqueará el o los depósitos.  
El comprobante quedará con estado 'Ajustado'.

Consultar Ajustes de Inventario

De existir registros asociados a la toma de inventario se visualiza una ventana con los de los datos 'Tipo de comprobante' y 'Número de comprobante' de los resultados obtenidos. De no existir registrados asociados se visualiza el mensaje "No hay ajustes de inventario asociados a esta toma".

Anular Conteo de Inventario  
Desde esta función cambiará el estado del comprobante, de 'En Proceso' a 'Ingresado', acarreando el desbloqueo del depósito.

Anular Cálculo de Diferencias  
Utilice esta función para cambiar el estado del comprobante, de 'Procesado' a 'En Proceso'.  
No se visualizarán las diferencias.

Anular Toma de Inventario  
Se anularán los comprobantes con estado 'Ingresado', 'En Proceso' o 'Procesado'.  
Si el comprobante está con estado 'En Proceso' o 'Procesado', se desbloquearán el o los depósitos.  
El comprobante quedará con estado 'Anulado'.

Comando Importar  
Mediante este comando, es posible importar la información generada por una colectora.  
Es necesario configurar, previamente, el formato del archivo (en el proceso Configuración de colectoras).

Origen: ingrese la ruta del archivo generado por la colectora.

Depósito: si en la configuración del formato del archivo no incluyó el depósito, ingréselo en forma manual. Caso contrario, se obtendrá automáticamente del archivo a importar.

Consideraciones para la toma de inventario registrada en el sistema:

Si la toma de inventario tiene información de artículos, previamente cargados, será posible indicar la forma de proceder en caso de importar información de éstos. También, puede reemplazar la información existente con la obtenida en el archivo, o bien actualizarla acumulando las cantidades.

Consideraciones para los artículos incluidos en el archivo:

Dependiendo de las características de la colectora que utilice, es posible que el archivo contenga sólo los artículos con cantidades inventariadas o bien, el maestro de artículos completo con cantidad cero en los artículos no inventariados. Según la información obtenida, es posible procesar los artículos con cantidad cero.

##### Datos del encabezado

Comprobante: indica el comprobante de la toma de inventario a utilizar.

Estado: muestra el nivel de avance de la toma de inventario. El estado puede variar entre 'Ingresado', 'En proceso', 'Procesado', 'Ajustado' o 'Anulado'.

Depósito: indica el depósito donde se realizará la toma de inventario. Si la cantidad de depósitos a inventariar es más de uno, podrá dejar en blanco este campo y completar este dato en el renglón del comprobante. No es posible seleccionar un depósito que se encuentre inhabilitado.

##### Conceptos generales

Mediante la función 'Agregar', el sistema permite seleccionar el tipo de comprobante de toma de inventario e ingresar los artículos y los depósitos.  
Si indica el depósito en el encabezado, no será posible modificar este dato en los renglones del comprobante.  
Al finalizar la carga, el comprobante quedará con estado 'Ingresado'.  
Invocando la función 'Comenzar Conteo de Inventario' será posible cargar las cantidades y las partidas físicas existentes en el o los depósitos y, dependiendo de lo configurado en el proceso [Parámetros de Stock](https://ayudas.axoft.com/25ar/parametrogeneral_st), el sistema bloqueará el artículo/depósito o el depósito.  
Si desde el proceso Perfiles de toma de inventario, usted configura el parámetro Toma de Inventario Ciega = Sí, se exhibirá el stock del sistema (en este estado no mostrará las diferencias) para cada uno de los artículos cargados en la toma de inventario.  
El stock del sistema es el saldo que se visualizará en el informe Saldos de Stock por artículo o Saldos de Stock por depósito.  
Una vez finalizada la carga de las cantidades, el comprobante se guardará con el estado 'En Proceso', mediante el comando' Actualizar' será posible eliminar o agregar renglones en dichos comprobantes. También será posible ejecutar la función 'Procesar diferencias'. En el cual el sistema calculará las diferencias entre el stock real (incluidas las partidas) y el stock del sistema.  
Si desde el proceso Perfiles de toma de inventario, usted configura el parámetro Toma de inventario ciega = No, el stock del sistema y las diferencias se visualizarán en pantalla. En el caso que existieran diferencias (entre los saldos o en las partidas), es posible realizar el ajuste de inventario (no valorizado) desde este proceso. De no realizarlo, será posible generarlo en otro momento desde este mismo proceso (mediante la función 'Realizar ajuste de inventario') o bien, desde el proceso Ajuste de inventario (en este caso, el ajuste podrá ser valorizado). Al realizar el ajuste, el sistema calculará el ingreso o el egreso para cada uno de los artículos cargados en el comprobante, posteriormente desbloqueará los artículos/depósitos o depósitos de la toma de inventario ajustada.

Si en el proceso [Parámetros de Stock](https://ayudas.axoft.com/25ar/parametrogeneral_st) indicó que las partidas sean automáticas en la toma de inventario, el sistema realizará automáticamente el ingreso o egreso de partidas al ejecutar la función 'Procesar diferencias'. En el caso de realizar un ingreso de partidas, éstas serán agregadas a la última partida ingresada al sistema que se encuentre relacionada con el artículo y el depósito indicado en el comprobante; caso contrario, el egreso se realizará a la primera partida ingresada al sistema, y no se tendrá en cuenta el parámetro Descarga Partidas según Antigüedad.  
Además es posible ingresar partidas existentes en un despacho de importación; pero tenga en cuenta que no afectará al costo de la partida.

<tdActualizar, Comenzar Conteo, Anular Toma de Inventario

**Función** | **Estado** | **Funciones relacionadas**  
---|---|---  
Agregar | Ingresado  
Comenzar conteo | En Proceso | Actualizar. Procesar diferencias. Anular conteo de inventario. Anular toma de inventario.  
Procesar diferencias | Procesado | Actualizar. Realizar ajuste de inventario, Anular cálculo de diferencias. Anular toma de inventario.  
Realizar ajuste de inventario | Ajustado | Anular toma de inventario anulando el ajuste generado desde el proceso de [anulación de movimientos de stock](https://ayudas.axoft.com/25ar/anulacionmovimstock_st).  
Anular conteo de inventario | Ingresado | Función activa para el estado 'En Proceso'.  
Anular cálculo de diferencias | En Proceso | Función activa para el estado 'Procesado'.  
Anular toma de inventario | Anulado | Función activa para los estados 'Ingresado', 'En Proceso' y 'Procesado'.  
  
##### Contenidos relacionados

  * [Video sobre administración de stock](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/adminstock_gral_vid/)

  * [Video sobre artículos Doble Unidad de Medida (DUM)](https://ayudas.axoft.com/25ar/videos/st_carp_vid/dum_st_vid/)

  * [Videos sobre artículos simples y escalas](https://ayudas.axoft.com/25ar/videos/st_carp_vid/articulos_st_vid/)

  * [Videos sobre series y partidas](https://ayudas.axoft.com/25ar/videos/st_carp_vid/seriepartida_st_vid/)

  * [Videos sobre toma de inventario](https://ayudas.axoft.com/25ar/videos/st_carp_vid/tomainventario_st_vid/)
