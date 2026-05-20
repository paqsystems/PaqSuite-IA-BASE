# Exportación a Excel

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Operación
- URL: https://ayudas.axoft.com/25ar/documentos/operacion/apertura_oper/excel_oper/excel_export_oper/

## Contenido

# Exportación a Excel

Para generar el archivo Excel con el que vas a trabajar debés ingresar a la opción Apertura > Excel > Exportar que se encuentra en la barra de herramientas del proceso con el que estás trabajando.  
A continuación, ingresarás a un asistente que te guiará en la generación del archivo.  
Este asistente se encuentra dividido en los siguientes pasos:

  * **Tipo de exportación:** indicá que tipo de exportación querés realizar: 
    * **Sin datos:** utilizá este criterio cuando solo quieras importar nuevos registros. Esta opción de suma utilidad cuando tenés que migrar información de otro sistema o cuando tenés que crear muchos registros en forma masiva.
    * **Con datos:** seleccioná esta opción cuando necesitás actualizar o eliminar información del sistema. También te permite generar nuevos registros.
  * **Datos de las tablas relacionadas:** utilizá esta opción para indicar si querés emplear listas desplegables para seleccionar códigos de tablas relacionadas en el archivo generado. 
    * Te recomendamos 'Utilizar lista desplegable' cuando realizás una edición manual del archivo Excel y no recordás los códigos de las tablas relacionadas, por ejemplo, en el caso de una exportación de clientes algunas de las tablas relacionadas son vendedor, zona, depósito, transportistas, etc.
    * Si, en cambio, recordás los códigos relacionados o solés trabajar con la opción "copiar y pegar" desde otros registros (o incluso desde otro archivo) te recomendamos utilizar la opción 'Ingresar manualmente los valores'.  
Tené en cuenta que si trabajás con tablas relacionadas muy grandes (por ejemplo, artículos) el ingreso manual de códigos te permitirá mejorar la performance de la exportación e importación, así como también el tamaño del archivo generado.
  * **Registros a enviar:** este paso solo está disponible cuando seleccionaste la opción 'con datos' en el paso anterior. Para seleccionar los registros a enviar podés utilizar alguna de las [vistas](https://ayudas.axoft.com/25ar/vistas_oper) ya definidas o utilizar la [búsqueda avanzada](https://ayudas.axoft.com/25ar/buscar_oper#buscavanzado) para aplicar un criterio específico para esta exportación. Si necesitás utilizar este último criterio seleccioná la opción "Búsqueda avanzada" dentro del botón "Más opciones".
  * **Campos a enviar:** te recomendamos que solo envíes los campos que necesitás actualizar, de esta forma la actualización de información será mucho más rápida. Tené en cuenta que los campos obligatorios no se pueden destildar. Los campos no enviados mantendrán su valor en caso de que modifiques un registro o se completarán con el valor por defecto en el caso de uno nuevo.
  * **Confirmación:** antes de que generemos el archivo Excel deberás confirmar que toda la información seleccionada es correcta.



Tené en cuenta que, siempre que sepas que todas las actualizaciones son registros nuevos (o sea, cuando no hay modificaciones de datos ya existentes, sino nueva información), te conviene generar una exportación solo con altas, de esa manera evitarás que el sistema analice todos y cada uno de los registros innecesariamente. Esta opción es de suma utilidad cuando deseas migrar toda la información o luego de crear muchos registros que necesitás exportar de forma masiva.  
Para ello, desde el apartado ¿Qué tipo de exportación querés realizar? seleccioná la opción 'Sin datos (recomendado para registros nuevos)'. En cambio, si necesitás trabajar con información ya existente en Tango, seleccioná la opción 'Con datos (recomendado para modificación o eliminación)'.
