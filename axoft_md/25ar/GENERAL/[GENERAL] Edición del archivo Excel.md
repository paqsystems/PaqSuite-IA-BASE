# Edición del archivo Excel

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Operación
- URL: https://ayudas.axoft.com/25ar/documentos/operacion/apertura_oper/excel_oper/excel_edicion_oper/

## Contenido

# Edición del archivo Excel

Lo primero que encontrarás al abrir el archivo generado es una solapa denominada “Ayuda” en la que te explicamos los principales conceptos para trabajar con el archivo Excel.  
Además de la solapa de ayuda, encontrarás otras en las que vas a trabajar con la información a importar. En la solapa denominada "Principal" encontrarás los datos propios del registro (por ejemplo, de un cliente) y a continuación podrás encontrar solapas adicionales con más información del mismo registro (por ejemplo, direcciones de entrega, contactos, datos impositivos, etc.). La existencia o no de solapas adicionales depende de cada proceso.  
El título de cada columna se encuentra inmovilizado de forma que no lo pierdas de vista al desplazarte verticalmente en las filas.  
Cada celda valida la información que puede contener. Por ejemplo, validamos la longitud de los campos y en el caso que existan valores posibles podrás seleccionarlos desde una lista desplegable.  
Como mencionamos en los párrafos anteriores, tené en cuenta que la información de un mismo registro (por ejemplo, cliente) se encuentra distribuida en varias solapas, por lo que deberás editarla en la solapa correspondiente.  
Para incorporar la información a Tango, volvé a la pantalla de exportación y pulsá [el botón "Importar"](https://ayudas.axoft.com/25ar/excel_import_oper). Si ya cerraste esa ventana, podés importarlo ingresando a esta opción Apertura > Excel > Importar y seleccionando este archivo para procesarlo.  
Si durante el procesamiento surgiera algún problema, generaremos un nuevo archivo con el sufijo "_problemas_importación" detallando en la última columna los motivos por los que no se actualizó cada registro. Podés corregirlos en ese mismo archivo e importarlo nuevamente al sistema.

##### ¿Qué acciones podés realizar?

Podés agregar, modificar o eliminar registros.

  * Para agregarlo, solo tenés que crear una fila y completar al menos la información obligatoria. Tené en cuenta que si existen varias solapas deberás completar al menos la información obligatoria de cada una de ellas.
  * Para eliminarlo, solo tenés que indicar 'Sí' en la última columna. Esta columna se llama "Eliminar" y está resaltada con fondo rojo. Tené en cuenta que si querés eliminar un registro (por ejemplo, un cliente) solo debés indicar 'Sí' en la columna "Eliminar" de la solapa Principal; no hace falta que hagas lo propio en el resto de las solapas. Por el contrario, si querés eliminar información relacionada con el cliente (pero no el cliente propiamente dicho) -como ser un contacto-, deberás indicar 'Sí' en la columna "Eliminar" de esa solapa.
  * Para modificarlo, basta con que cambies el valor de cada celda que requieras.



##### ¿Qué representa cada color de las celdas?

Las celdas resaltadas con amarillo son aquellas que debes completar en forma obligatoria. Tené cuenta que en algunos casos pueden existir celdas que no estén resaltadas como obligatorias, pero pueden volverse requeridas según el valor de otros campos. Por ejemplo, en el caso de artículos, la información relacionada con unidades de medida de compras sólo es requerida cuando el artículo tiene asignado el perfil "Compras" o "Compraventa". En esos casos, validaremos la consistencia del registro durante la importación del archivo.  
Los valores identificados con letra azul representan a los campos clave, generalmente denominados "Código". No deberías modificar estos valores a menos que quieras copiar registros. Para más información consultá el ítem que sigue a continuación.

##### ¿Qué consideraciones debés tener al modificar un campo clave?

Como te mencionamos en el ítem anterior, estas celdas están identificados con color azul. Tené en cuenta que si modificás el valor de estos campos no actualizaremos el registro original, sino que crearemos uno nuevo con los valores de la fila.  
Por ejemplo, suponé que exportás a Excel un grupo de artículos correspondientes a tornillos.

Y luego modificás el código del segundo registro (0200100010) y le asignás por ejemplo el valor 0200100012 con descripción "TORNILLO 1/2"x4mm".

En ese caso generaremos un nuevo artículo con código 0200100012 y descripción "TORNILLO 1/2"x4mm", pero mantendremos sin cambios el artículo original (0200100010).

En el caso de registro que representan un detalle de un registro principal, si querés modificar un registro de este detalle, deberías poner en el registro a modificar la columna "Eliminar" igual a 'Sí' y agregar un nuevo registro con los datos modificados  
Por ejemplo, suponé que exportás a Excel un pedido con un renglón de un artículo con cantidad pedida 20 unidades, que tiene en la solapa Fecha de entregas los siguientes registros.

**Identificador** | **Nro.** | **Fecha de entrega** | **Cantidad pedida** | **Eliminar**  
---|---|---|---|---  
1 | 1 | 10/08/2026 | 10,000 |   
2 | 1 | 20/08/2026 | 10,000 |   
  
Si necesitás modificar la fecha de entrega de alguno de estos registros deberías proceder de la siguiente manera: poner en la columna "Eliminar" del registro que deseo modificar igual 'Sí', y agregar un nuevo registro en fechas de entrega con la fecha modificada, cómo se muestra a continuación.

**Identificador** | **Nro.** | **Fecha de entrega** | **Cantidad pedida** | **Eliminar**  
---|---|---|---|---  
1 | 1 | 10/08/2026 | 10,000 |   
2 | 1 | 20/08/2026 | 10,000 | Sí  
3 | 1 | 25/08/2026 | 10,000 |   
  
El resultado de la importación será el siguiente:

**Identificador** | **Nro.** | **Fecha de entrega** | **Cantidad pedida** | **Eliminar**  
---|---|---|---|---  
1 | 1 | 10/08/2026 | 10,000 |   
3 | 1 | 25/08/2026 | 10,000 |   
  
__Importante

Modificar un campo clave es similar a la función "Copiar registro". Tené en cuenta que si ese campo clave está en varias solapas deberás actualizar su valor en todas ellas.

##### ¿Cuáles son los valores posibles de una celda?

Cada celda valida la información que puede contener. Por ejemplo, si ingresas un texto cuya longitud es superior a la esperada por **Tango** te mostraremos el siguiente mensaje:

Si la celda solo acepta un conjunto de valores posibles, lo podrás seleccionar desde una lista desplegable, ya sea que se trate de una lista definida por el sistema (por ejemplo, el perfil del artículo) o de una lista definida por vos (unidades de medida).

|   
---|---  
  
##### Temas relacionados

  * [Consideraciones para los procesos Clientes, Artículos, Proveedores, Legajos, Cuentas contables y Cuentas de Tesorería](https://ayudas.axoft.com/25ar/excel_consideracion_oper)
  * [Posibles problemas que pueden surgir en la importación de archivos](https://ayudas.axoft.com/25ar/problemasexcel_import_oper)
