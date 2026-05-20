# Stock Restô - Toma de Inventario

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_st3/guia_perfstock_st3/?p=26151/

## Contenido

# Stock Restô - Toma de Inventario

Desde este proceso es posible ingresar el conteo de inventario realizado en los diferentes depósitos.

De existir diferencias entre el stock real y el stock del sistema, podrá realizar un ajuste de inventario no valorizado. En el caso de necesitar que el ajuste sea valorizado, ingréselo desde el proceso Ajustes de inventario.  
El sistema sólo tomará como unidad de medida la unidad de stock.  
La toma de inventario es un comprobante independiente, que no conlleva movimiento de stock.

**Comando Agregar  
**Desde esta función sólo es posible ingresar comprobantes de toma de inventario, con los artículos y sus respectivos depósitos. El comprobante quedará con el estado 'Ingresado'.

**Comando Actualizar  
**Este comando permite modificar todos los comprobantes que estén con estado 'Ingresado' o 'En Proceso'.  
Para el estado 'En Proceso', sólo será posible agregar o eliminar artículos de los depósitos bloqueados, si el perfil así lo permite. Para el estado 'Ingresado' es posible modificar todos los campos.

**Comando Acciones asociadas  
**Detallamos en los siguientes ítems, las acciones asociadas a la toma de inventario.

  * **Comenzar Conteo de Inventario:** usted podrá, en primera instancia, bloquear los depósitos (en caso de no aceptar cargar las cantidades), sino se ingresarán las cantidades del recuento físico para los artículos inventariados, con sus partidas.  
No se calcularán las diferencias.  
Es posible agregar artículos de los depósitos bloqueados (si el perfil lo permite).  
Si no ingresa las cantidades en este proceso, deberá hacerlo desde el comando Actualizar.  
El comprobante quedará con estado 'En Proceso'.
  * **Procesar Diferencias:** se calcularán las diferencias existentes entre el stock real y el stock del sistema. También, se validarán las partidas cargadas con las existentes en el sistema.  
No es posible editar los datos.  
El comprobante quedará con estado 'Procesado'.
  * **Realizar Ajuste de Inventario:** de existir diferencias, tanto en las cantidades como en las partidas, se realizará el ajuste de inventario. Después de ajustar, se desbloqueará el o los depósitos.  
El comprobante quedará con estado 'Ajustado'.
  * **Anular Conteo de Inventario:** desde esta función cambiará el estado del comprobante, de 'En Proceso' a 'Ingresado', acarreando el desbloqueo del depósito.
  * **Anular Cálculo de Diferencias:** utilice esta función para cambiar el estado del comprobante, de 'Procesado' a 'En Proceso'.  
No se visualizarán las diferencias.
  * **Anular Toma de Inventario:** se anularán los comprobantes con estado 'Ingresado', 'En Proceso' o 'Procesado'.  
Si el comprobante está con estado 'En Proceso' o 'Procesado', se desbloquearán el o los depósitos.  
El comprobante quedará con estado 'Anulado'.



**Comando Importar  
**Mediante este comando, es posible importar la información generada por una colectora.  
Es necesario configurar, previamente, el formato del archivo (en el proceso Configuración de colectoras).

Origen: ingrese la ruta del archivo generado por la colectora.

Depósito: si en la configuración del formato del archivo no incluyó el depósito, ingréselo en forma manual. Caso contrario, se obtendrá automáticamente del archivo a importar.

Consideraciones para la toma de inventario registrada en el sistema:

Si la toma de inventario tiene información de artículos previamente cargada, es posible indicar cómo proceder en caso de importar información sobre artículos existentes. Puede reemplazar la información existente con la obtenida del archivo, o bien actualizarla, acumulando las cantidades.

Consideraciones para los artículos incluidos en el archivo:

Dependiendo de las características de la colectora que utilice, es posible que el archivo contenga sólo los artículos con cantidades inventariadas o bien, el maestro de artículos completo con cantidad cero en los artículos no inventariados. Según la información obtenida, es posible procesar los artículos con cantidad cero.

##### Datos del encabezado

Comprobante: indica el comprobante de la toma de inventario a utilizar.

Estado: muestra el nivel de avance de la toma de inventario. El estado puede variar entre 'Ingresado', 'En Proceso', 'Procesado', 'Ajustado' o 'Anulado'.

Depósito: indica el depósito donde se realizará el inventario. Si la cantidad de depósitos a inventariar es más de uno, podrá dejar en blanco este campo y completar este dato en el renglón del comprobante.

##### Conceptos generales

Mediante la función Agregar, el sistema permite seleccionar el tipo de comprobante de toma de inventario e ingresar los artículos y los Depósitos.  
Si indica el depósito en el encabezado, este dato no podrá modificarse en los renglones del comprobante.  
Al finalizar la carga, el comprobante quedará con estado 'Ingresado'.  
Invocando la opción 'Comenzar Conteo de Inventario' podrá cargar las cantidades y las partidas físicas existentes en el o los depósitos. Al ejecutar el conteo, el sistema bloqueará el artículo/depósito o el depósito, dependiendo de lo configurado en los parámetros generales.  
Si desde el proceso Perfiles de toma de inventario usted configura el parámetro Toma de inventario ciega = Sí, se exhibe el stock del sistema (en este estado no mostrará las diferencias) para cada uno de los artículos cargados en la toma de inventario.  
El stock del sistema es el saldo que podrá visualizar en el informe Saldos de stock por artículo o Saldos de stock por Depósito.  
Una vez finalizada la carga de las cantidades, el comprobante se guardará con el estado 'En Proceso'.  
Es posible eliminar o agregar renglones; para este último caso, sólo si el depósito a ingresar ya existe en el comprobante.  
Finalizada la carga de cantidades, podrá ejecutar la función 'Procesar diferencias'. El sistema calculará las diferencias entre el stock real (incluidas las partidas) y el stock del sistema.  
Si desde el proceso Perfiles de toma de inventario, usted configura el parámetro Toma de inventario ciega = No, el stock junto con las diferencias se podrán visualizar en pantalla. Si existieran diferencias (tanto entre los saldos o en las partidas), es posible realizar el ajuste de inventario (no valorizado) desde este proceso. De no realizarlo en este momento, lo podrá generar posteriormente desde este mismo proceso (mediante la función 'Realizar ajuste de inventario') o bien, desde el proceso Ajuste de inventario (en este caso, el ajuste podrá ser valorizado). Al realizar el ajuste, el sistema calculará el ingreso o el egreso para cada uno de los artículos cargados en el comprobante, posteriormente desbloqueará los artículos/depósitos o depósitos de la toma de inventario ajustada.  
Si en el proceso Parámetros generales indicó que las partidas en la toma de inventario serán automáticas, al ejecutar la función 'Procesar diferencias', el sistema realizará automáticamente el ingreso o egreso de partidas. Si necesita realizar un ingreso de partidas, éstas serán agregadas a la última partida ingresada al sistema, que esté relacionada con el artículo y el depósito indicado en el comprobante. Caso contrario, el egreso se realizará de la primera partida ingresada al sistema. No se tendrá en cuenta la modalidad de descarga de partidas.

Función | Estado | Funciones relacionadas  
---|---|---  
Agregar | Ingresado | Actualizar. Comenzar conteo. Anular toma de inventario.  
Comenzar conteo | En proceso | Actualizar. Procesar diferencias. Anular conteo de inventario. Anular toma de inventario.  
Procesar diferencias | Procesado | Actualizar. Realizar ajuste de inventario. Anular cálculo de diferencias. Anular toma de inventario.  
Realizar ajuste de inventario | Ajustado | Anular toma de inventario.  
Anular conteo de inventario | Ingresado | Función activa para el estado 'En Proceso'.  
Anular cálculo de diferencias | En Proceso | Función activa para el estado 'Procesado'.  
Anular toma de inventario | Anulado | Función activa para los estados 'Ingresado', 'En Proceso', 'Procesado' y 'Ajustado'.
