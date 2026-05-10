# Importación desde Excel

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Operación
- URL: https://ayudas.axoft.com/24ar/documentos/operacion/apertura_oper/excel_oper/excel_import_oper/

## Contenido

# Importación desde Excel

Para incorporar la información a Tango, volvé a la pantalla de exportación y pulsá el botón "Importar". Si ya cerraste esa ventana podés importarlo ingresando a esta opción Apertura > Excel > Importar y seleccioná este archivo para procesarlo.  
Si durante el procesamiento surgiera algún problema, generaremos un nuevo archivo con el sufijo "_problemas_importación" detallando en la última columna los motivos por los que no se actualizó cada registro. Podés corregirlos en ese mismo archivo e importarlo nuevamente al sistema.  
Tené en cuenta que sólo actualizaremos los registros que tuvieron algún cambio, ya sean nuevos registros, eliminados o modificados. Esta información quedará registrada en el [Historial de cambios](https://ayudas.axoft.com/24ar/historial_oper) como cualquier otra modificación que realizás en forma manual, pero identificando que el origen fue un archivo Excel.

__Importante

También te recomendamos que tengas en cuenta el campo Manejo de errores. Utilizalo para detener la importación cuando la cantidad de fallos detectados son numerosos. Por ejemplo, suponé que vas a importar 10.000 registros y completaste mal el valor de una columna (por ejemplo, con un valor incorrecto).  
Qué opciones podés elegir:

  * **Proceso todo el archivo:** opción predeterminada, que procesará todo el archivo e importará los registros que sean correctos, descantando aquellos con errores. En este caso el sistema va a rechazarte los 10.000 registros pero con un demora de procesamiento mayor (como si realmente importara los registros).
  * **Detengo la inspección al detectar errores:** esta alternativa te permite definir una determinada cantidad de fallos en el campo Cantidad de errores tolerados antes de suspender. Sobrepasado ese umbral, el proceso se detendrá y te informará de su suspensión para que puedas corregir la causa del problema. Bajo este criterio, el sistema detendría la importación después de procesar los primeros 100 registros (suponiendo que cada fila tuviera un error) y podrías darte cuenta que tuviste un error "genérico" al completar el Excel.



Siempre te sugerimos que si vas a importar un archivo con muchas filas, hagas un lote de muestreo para verificar que no existan errores repetitivos entre las filas. En función a este y a la confianza que tengas a la consistencia de tu archivo será la opción que selecciones para el manejo de errores.

Existen casos puntuales, como el de clientes y artículos, en los que permitimos utilizar una plantilla para completar la información pendiente. De esta forma no es necesario que la completes todos los campos en el archivo Excel en forma manual, sino que los completaremos con los valores asignados en la plantilla de [clientes](?p=19466) o [artículos](?p=17230).  
Al finalizar la importación te informaremos la cantidad de registros nuevos, modificados y eliminados.

Consideraciones sobre concurrencia:

Tené en cuenta que pueden existir problemas de concurrencia al importar un archivo Excel. Estos problemas se producen cuando varias personas trabajan sobre el mismo registro. Por ejemplo, después de que exportaste la información de los empleados para actualizar su domicilio otra persona actualizó el sueldo de 10 personas. Cuando importes el archivo sobrescribirás los cambios que hizo esa persona a menos que destildes la opción Modificaciones: Prioriza la información del archivo a importar (no verifica que los datos a procesar hayan tenido cambios desde su exportación a Excel). Cuando destildes esta opción el sistema verificará que el registro no haya tenido cambios posteriores a la exportación, y en caso de tenerlos rechazará el registro y deberás exportarlo nuevamente para realizar allí los cambios de domicilio.

##### Contenido dependiente

  * [Problemas al importar](https://ayudas.axoft.com/24ar/documentos/operacion/apertura_oper/excel_oper/excel_import_oper/problemasexcel_import_oper/)
