# Problemas al importar

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Operación
- URL: https://ayudas.axoft.com/24ar/documentos/operacion/apertura_oper/excel_oper/excel_import_oper/problemasexcel_import_oper/

## Contenido

# Problemas al importar

Hay dos razones por las que podés estar leyendo este capítulo:

  * Sos un usuario previsor y te gusta entender los procesos antes de ejecutarlos.
  * Hemos detectado un problema durante la importación de tu archivo Excel.



Si perteneces al primer grupo te felicitamos por eso, ¡nos encanta conocer usuarios proactivos y seguramente te ayudará a acotar los problemas al procesar el archivo Excel!  
Si tuviste un problema durante la importación de tu archivo este capítulo te ayudará a resolverlo lo antes posible.

##### ¿Cómo consultás los problemas detectados?

Ingresá a la segunda solapa del archivo de errores (la primera es siempre la de "Ayuda") y consultá la última columna denominada "Problemas detectados durante la importación".  
Recordá que al detectar un problema en la importación generamos un nuevo archivo con el detalle de los temas a revisar. Ese archivo se llama "XXXX_problemas_importación" siendo "XXXX" el nombre del proceso, por ejemplo "Artículos_problemas_importación.xlsx".  
Podés corregir los problemas directamente en este archivo. Tené en cuenta que ya importamos los registros que no tuvieron inconvenientes. En este archivo solo encontrarás los registros que debés revisar.

##### ¿Cuáles son los errores más comunes y cómo podés solucionarlos?

**Problema detectado** | **Posibles causas y soluciones**  
---|---  
Clave duplicada (XXXXX) | El valor del campo XXXXX ya existe en el sistema. Normalmente estos campos tienen el título de la columna en color azul.  
Para solucionarlo debés ingresar otro código (si es que aún querés ingresarlo al sistema)  
El archivo a importar no es válido. | Quisiste importar un archivo con el formato de una versión anterior a Tango Delta.  
Para solucionar este problema debés generar la plantilla desde el proceso de Tango Delta, completarlo e importarlo nuevamente.  
El campo XXXXX es requerido. | Debes ingresar algún valor en este campo. Normalmente esta columna estará resaltada en color amarillo, pero en determinados casos puede que no figure de esta forma; uno de esos casos es cuando el campo se transforma en obligatorio a consecuencia del valor de otro campo. Por ejemplo, el código de alícuota a aplicar en compras es obligatorio solo cuando el perfil del artículo es igual a "Compra" o de "Compra - Venta".  
Formato inválido de columna: XXXXXX | Verificá que el tipo de dato ingresado sea correcto. Por ejemplo, que no hayas ingresado letras en un campo de tipo numérico.  
Revisá también las Consideraciones sobre Copiar y Pegar.  
La estructura del archivo (XXXX) fue modificada. No es posible importar esta planilla. | Eliminaste alguna solapa o columna de la plantilla generada.  
Para solucionar este problema debés generar la plantilla desde el proceso de Tango Delta, completarlo e importarlo nuevamente.  
No es posible actualizar los datos debido a que fueron modificados por otro usuario. | Estos problemas se producen cuando varias personas trabajan sobre el mismo registro. Por ejemplo, después de que exportaste la información de los empleados para actualizar su domicilio otra persona actualizó el sueldo de 10 personas.  
Si al importar el archivo destildaste la opción Modificaciones: Prioriza la información del archivo a importar (no verifica que los datos a procesar hayan tenido cambios desde su exportación a Excel) el sistema rechazará tu registro para no perder los cambios realizado por el otro usuario (en nuestro caso los cambios de sueldos).Si considerás que en tu archivo se encuentra la información con la que debe actualizarse el sistema, dejá tildada la opción de la que hablamos en el párrafo anterior.  
Otros mensajes | En general, una vez superadas las validaciones anteriores solo restan las verificaciones propias de cada proceso, por lo que los mensajes y soluciones dependen del tema en cuestión. Algunos ejemplos pueden ser:  
"El campo XXXXX no es un e-mail válido", por ejemplo, cuando la dirección de correo electrónico que ingresaste no tiene un formato similar a xxxx@xxx.xxx  
"Código de artículo existente como sinónimo o código de barras".  
Valor inexistente o inválido en el campo XXXXX. | Verificá que el valor ingresado exista en el proceso XXXXX. Por ejemplo, puede ser que el código de provincia que le asociaste al cliente no exista dentro del sistema.  
Revisá también las Consideraciones sobre Copiar y Pegar.  
XXXXX: Valor fuera de dominio. | El valor que ingresaste en el campo XXXXX no pertenece a lista de valores posibles.  
Revisá también las Consideraciones sobre Copiar y Pegar.  
  
Tené en cuenta que en caso de detectar más de un tipo de error los mostraremos en la misma columna separados por el caracter "|". Por ejemplo "El campo Perfil es requerido | Valor inexistente o inválido en el campo Escala". Sin embargo, algunos errores recién podrán ser detectados cuando se solucionen otros en forma previa. Por ejemplo, si no completás el campo Perfil en la importación de Artículos no podremos indicarte si te falta completar alguno de los datos correspondiente a la configuración de ventas o compras y por lo tanto algunos errores te los informaremos una vez resuelto el incidente previo y vuelvas a procesar la importación.

##### Consideraciones sobre Copiar y Pegar

Al generar el archivo Excel asignamos a cada celda los siguientes atributos:

  * Formato (numérico, texto, etc.).
  * Validación de longitud de caracteres.
  * Lista de valores posibles, ya sea que se trate de una lista de valores fijos (por ejemplo, masculino, femenino) o dinámicos (por ejemplo, lista de unidades de medida definidas en tu sistema).



Todos estos atributos facilitan la carga de datos en archivo Excel ya que no tenés que recordarlos porque los podés seleccionar de la lista de valores. Sin embargo, **es muy importante** que sepas que **al copiar y pegar celdas, estos atributos no se conservan** ya que al pegar Excel traslada a la celda nueva no solo el contenido sino también el formato y validaciones de la celda de origen.  
Si habitualmente copias la información desde un archivo generado por otro sistema, seguramente la celda origen no tendrá validaciones asociadas (lista de valores posibles) y por lo tanto al pegarlos sobre la plantilla generada por Tango Delta no sabrás si son válidos hasta que proceses el archivo.  
Si tenés dudas sobre las validaciones o los valores posibles de una celda, te recomendamos que siempre lo verifiques sobre una fila en blanco (es decir una fila que no hayas editado). Obviamente que si no copias y pegas podés verificarlo sobre cualquier celda.

##### ¿Cómo continuas con la importación?

Para incorporar la información a Tango, volvé a la pantalla de exportación y pulsá el botón "Importar". Si ya cerraste esa ventana, podés importalo ingresando a esta opción Apertura |Excel | Importar y seleccioná este archivo para procesarlo.  
Si durante el procesamiento surgiera algún problema, generaremos un nuevo archivo en el que deberás repetir lo explicado anteriormente.
