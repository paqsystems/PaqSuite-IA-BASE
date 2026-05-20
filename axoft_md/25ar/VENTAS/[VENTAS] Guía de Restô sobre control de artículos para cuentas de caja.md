# Guía de Restô sobre control de artículos para cuentas de caja

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv3/guia_controlart_gv3/

## Contenido

# Guía de Restô sobre control de artículos para cuentas de caja

Con Restô, es posible controlar los artículos asociándolos a una cuenta de caja, donde se podrá definir qué artículGuía de Restô sobre pago con QR de Mercado Pagoos son permitidos o cuáles están restringidos, para cobrar con una cuenta de caja configurada con un tipo de control de artículos.

El control de artículos para [cuentas de caja](?p=24601) está disponible para los circuitos:

  * Modalidad 1.
  * Modalidad 2.
  * Facturar Mesa.
  * Cobrar mesa.



##### Puesta en marcha

**¿Cómo parametrizar una cuenta de caja con control de artículos?**

  * Ingrese al Adicionista | Otros | Más acciones | Control de artículos para cuentas de caja.
  * Al presionar la opción Control de artículos para cuentas, se abrirá la vista del proceso de configuración.
  * Desde este proceso podrá parametrizar el control de artículos para la cuenta de caja seleccionada.



##### Parametrización

Seleccione la cuenta de caja sobre la que desea aplicar el control de artículos.  
Active la opción Control de artículos para habilitar la sección Tipo de control.  
En Tipo de control debe elegir entre las siguientes modalidades:

  * **Restringe:** permite definir los artículos que no podrán ser cobrados con la cuenta de caja seleccionada.
  * **Permite:** se usa para definir los artículos que solo podrán ser cobrados con la cuenta de caja seleccionada.



__Nota

Al seleccionar el control Permite, se habilitará la sección Modalidad de artículos permitidos.  


Dentro de la sección Modalidad de artículos permitidos puede configurar los siguientes parámetros:

  * **Por artículo:** marque esta opción si desea trabajar con un número limitado de artículos permitidos.
  * **Cantidad de artículos:** indique el número máximo de artículos que se podrán registrar en la comanda.  
El número máximo aplica al total de artículos de la comanda, no a cada artículo de manera individual.
  * **Por monto:** establezca un límite de monto a cobrar para los artículos permitidos.
  * **Monto máximo:** indique el valor tope que podrá alcanzar el total del monto a cobrar de la comanda.



__Nota

Tendrá la opción de configurar esta modalidad de artículos permitidos ('Por Artículo' - 'Por Monto' - 'Ambos').  
Para el tipo de control de artículos 'Permite', una vez seleccionada la Modalidad de artículos permitidos, también será posible configurar de manera individual los artículos por cantidad, por monto y/o por ambos, parametrizándolos desde la grilla de la sección Artículos con control en los campos Cantidad y Monto.  


Una vez definido el tipo de control de artículos para la cuenta de caja, debe indicar los artículos a los que se aplicará dicho control.  
En la sección Artículos, busque el artículo ingresando el código o la descripción en el campo de búsqueda.  
Se mostrará el artículo en la grilla y deberá marcar la casilla ubicada a la izquierda del código.  
Una vez seleccionados los artículos, utilice los botones centrales de desplazamiento:

  * (>>) para seleccionar de manera automática todos los artículos de la grilla de la sección Artículos y puedan moverse a la grilla de la sección Artículos con control.
  * (>) para mover los artículos seleccionados a la sección Artículos con control.
  * (<) para retirar artículos previamente asignados.
  * (<<) para seleccionar de manera automática todos los artículos de la grilla de la sección Artículos con control y puedan moverse a la grilla de la sección Artículos.



__Nota

Los artículos que se visualicen en la grilla Artículos con control serán los que quedarán vinculados bajo el control de artículos definido como ('Restringe' o 'Permite'). Si desea retirar algún artículo de la grilla Artículos con control, solo deberá marcar la casilla ubicada a la izquierda del código y con el botón central "<" retirará el articulo previamente asignado o con el botón "<<" para retirar todos los artículos.  


Adicionalmente, en la sección Gestión de parametrización tendrá la opción de exportar o importar configuraciones de control de artículos en cuentas de caja.

  * **Exportar:** seleccione esta opción para generar un archivo con la parametrización actual ('Origen'), que luego podrá ser utilizada en otra sucursal (Destino).
  * **Importar:** seleccione esta opción para cargar una parametrización previamente exportada en otra sucursal ('Origen').



__Nota

Durante el proceso de importación, puede ocurrir que en el destino no existan algunos de los artículos definidos en el origen. En ese caso, se mostrará un mensaje informando cuáles son los artículos faltantes y se detendrá el proceso de importación.  


##### Detalle del circuito

Una vez parametrizados los campos en el proceso Control de artículos para las cuentas de caja, al momento de realizar la cobranza de la comanda y seleccionar una cuenta de caja con control de artículos, el sistema aplicará automáticamente las validaciones correspondientes según el tipo de control de artículos definido como 'Restringe' o 'Permite'.

##### Preguntas frecuentes

**¿Puedo definir una cuenta de caja con el control de artículos como Restringe y Permite al mismo tiempo?  
**No. Solo es posible seleccionar un tipo de control de artículos por cuenta de caja.

**¿Qué tipo de cuentas de caja puedo parametrizar con el control de artículos?  
**Cualquier tipo de cuenta de caja puede parametrizarse con el control de artículos.

**¿Con qué circuitos de facturación puedo utilizar el control de artículos para cuentas de caja?  
**El control de artículos está disponible en los siguientes circuitos: Modalidad 1, Modalidad 2, Facturar Mesa y Cobrar Mesa, dentro de los módulos Adicionista (salón) y Mostrador (take away).

**¿Puedo seleccionar una cuenta de caja con control de artículos como cuenta habitual para un puesto de caja?  
**Sí. Cuando una cuenta de caja con control de artículos se configura como habitual en un puesto de caja, se aplicarán las validaciones correspondientes sobre los artículos de la comanda al momento de facturar.

**¿Puedo configurar simultáneamente las dos modalidades de artículos permitidos?  
**Sí. El sistema permite configurar ambas modalidades cuando el tipo de control de artículos está definido como 'Permite'. No obstante, también es posible utilizarlas por separado, según la necesidad de la configuración deseada.

**¿Qué ocurre si intento importar una parametrización en una cuenta de caja que ya tiene una configuración definida?  
**Al realizar el proceso de importación, el sistema mostrará un mensaje indicando que la cuenta de caja ya posee una parametrización previa. Si decide continuar, la configuración existente será reemplazada por la nueva.

**¿Puedo importar una parametrización a una sucursal destino que no tenga los mismos artículos?  
**No. Durante el proceso de importación se verificará que los artículos de la sucursal origen coincidan con los de la sucursal destino. Si existen artículos que no coincidan, se mostrará un mensaje indicando cuáles faltan y no será posible continuar con la importación.

__Importante

Recuerde que siempre tendrá la opción de realizar la parametrización manual del control de artículos para las cuentas de caja.  


**Si en la sucursal destino no existe la cuenta de caja de origen para parametrizar con el control de artículos, ¿puedo realizar la importación?  
**No. Al momento de importar la configuración de una cuenta de origen, se validará que dicha cuenta de caja exista en la sucursal destino. En caso de no existir, se mostrará un mensaje indicando que la cuenta de caja de origen no está definida en el destino.

**¿Puedo importar la parametrización de una cuenta de caja origen en una sucursal destino donde la cuenta de caja sea de un tipo distinto al de la cuenta de caja origen?  
**Sí. Durante la importación se verificará el código de la cuenta de caja origen contra el de la cuenta de caja destino y se validará el tipo de cuenta. Si en el destino el tipo de cuenta es diferente al de la cuenta de caja origen, se mostrará un mensaje informando esta diferencia y se consultará si desea continuar con la importación.

**Ejemplo:**  
La cuenta de caja XX es de tipo YYYY en el origen y en el destino está definida como tipo ZZZZ  


**¿****Puedo aplicar descuentos en una comanda con una cuenta de caja que tenga el control de artículos permitidos por monto máximo?  
**No se deben aplicar descuentos en comandas asociadas a cuentas de caja que usen este tipo de control. Ya que los artículos tienen un límite de monto máximo permitido por unidad, y los descuentos alterarían ese control.

**¿Se pueden configurar los artículos de manera individual por cantidad o monto cuando el control de artículos está definido como 'Restringe'?  
**No. Si el control está definido como 'Restringe', no se pueden asignar parámetros individuales de Cantidad ni de Monto. En este caso, Restô bloquea directamente el uso de los artículos marcados como restringidos para cobrar con esta cuenta de caja.

**¿Cómo agrego un control de artículos permitidos de forma individual?  
**En la grilla derecha de la vista Control de artículos para cuentas de caja, dentro de la sección Artículos con control, puede definir la cantidad máxima, el monto máximo o ambos para un artículo en particular, dando doble clic sobre la casilla del control que desee aplicar. Esto le permite aplicar un control individual dentro de la cuenta de caja.

**¿Qué pasa si no configuro cantidad ni monto máximo en un artículo permitido de forma individual?  
**El artículo quedará sin control individual. En ese caso, solo se aplicarán las restricciones generales definidas en el tipo de control de la cuenta de caja.

**¿Puedo editar los parámetros individuales de un artículo ya configurado?  
**Sí. En la sección Artículos con control puede modificar en cualquier momento la cantidad máxima, el monto máximo o ambos, dando doble clic sobre la casilla del control que desee aplicar.  
Recuerde que los cambios se guardan recién cuando presione el botón "Aceptar".

**¿Qué sucede si un artículo supera la cantidad o el monto máximo definido para la cuenta de caja?  
**Restô no permitirá cobrar la comanda con esa cuenta de caja. Aparecerá un mensaje de alerta indicando que el artículo no cumple con los parámetros configurados en Control de artículos para cuentas de caja.

**¿Puedo aplicar controles a todos los artículos de una cuenta de caja al mismo tiempo?  
**Sí. Puede usar los botones de selección masiva (>>) para mover artículos a la sección Artículos con control y configurar allí sus parámetros Cantidad y Monto máximo.

**¿Qué hago si quiero configurar un artículo de promoción variable que incluye categorías valorizadas bajo el control individual por monto máximo?  
**Debe ajustar el monto máximo permitido tomando en cuenta los valores de las categorías valorizadas. Si solo se considera el monto de la promoción, se mostrará un mensaje indicando que el artículo de promoción supera el límite permitido.

**Ejemplo:**  
Para el artículo "Café gourmet" de tipo 'Promoción', el subtotal del artículo es de $3.128.  
Si le agrega un artículo de categoría valorizado, por ejemplo "Leche de almendras" de $700, el total del artículo "Café gourmet" pasa a $3.828.  
Si el monto máximo configurado para el artículo era $3.128, al agregar la leche de almendras se supera el límite permitido.  
En ese caso, se mostrará un aviso en pantalla indicando que el artículo de promoción excede el monto máximo definido.
