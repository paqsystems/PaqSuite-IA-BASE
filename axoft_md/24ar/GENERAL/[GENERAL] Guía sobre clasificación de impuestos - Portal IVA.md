# Guía sobre clasificación de impuestos - Portal IVA

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_iv/clasifimpuesto_guia_iva/

## Contenido

# Guía sobre clasificación de impuestos - Portal IVA

A través de este asistente usted tiene la posibilidad de reclasificar percepciones (Ingresos Brutos, Ganancias e IVA) e impuestos internos de manera masiva para comprobantes importados en el proceso de [importación de comprobantes desde Portal IVA](https://ayudas.axoft.com/desarrollo/documentos/guias/guias_carp_iv/afipportaliva_guia_iva/).

El proceso se divide en dos etapas:

  * **Exportación:** en Excel de los comprobantes a reclasificar,
  * **Importación:** de ese mismo archivo con los importes ya clasificados.



#### Puesta en marcha

##### Parámetros de Liquidador de IVA

Para parámetros del módulo debemos tener en cuenta que dentro de la solapa [Parámetros Portal IVA](?p=66908) tanto para Ventas como para Compras, hay que tener configuradas las fórmulas dentro de Fórmulas para percepciones y otros tributos, que define la relación entre las fórmulas del modelo de ingreso de comprobantes (**PIVAV** , **PIVAC** , **PIVAVCRED** y **PIVACCRED**) y los importes que se encuentran dentro del archivo csv de Portal IVA.

Tenga en cuenta:

No es posible asignar una misma fórmula para diferentes tributos.  


Las fórmulas aquí configuradas son las que, en el Excel, aparecerán como las fórmulas a reclasificar. Si faltara la asignación de alguna de ellas el proceso lo validará y se detendrá en ese punto.

__Nota

Las relaciones que se parametrizan en la solapa _"Parámetros Portal IVA"_ dentro de _"Fórmulas para percepciones y otros tributos"_ tienen relación a los tipos de fórmula de la siguiente manera:

  * "Importe de percepciones. o pagos a cuenta de otros impuestos nacionales" con Percepción ganancias.
  * "Importe de percepciones de ingresos brutos" con Percepción IB.
  * "Importe de percepciones o pagos a cuenta de IVA" con Percepción IVA.
  * "Importe de impuestos internos" con Impuesto interno.



##### Fórmulas

A las fórmulas de los modelos utilizados para Portal IVA (**PIVAC** , **PIVAC** , **PIVAVCRED** y **PIVACCRED**), se les puede modificar la descripción y el tipo de fórmula para que luego en el Excel descargado aparezcan como una columna que sirva para ser clasificada.

#### Detalle del circuito

##### Clasificación de impuestos

**Selección de acción**

Usted debe seleccionar primero la acción a realizar, es decir, 'Exportar archivo con importes a clasificar' o 'Importar archivo con importes clasificados'.

#### Exportación

Este proceso permite exportar a Excel aquellos comprobantes, importados desde Portal IVA de acuerdo con los parámetros: Origen (Ventas o Compras), intervalo de fechas, y selección de importes a clasificar.  
Podemos elegir que importes queremos reclasificar en Excel:

  * Importe de percepciones. o pagos a cuenta de otros impuestos nacionales.
  * Importe de percepciones de ingresos brutos.
  * Importe de percepciones o pagos a cuenta de IVA.
  * Importe de impuestos internos.



Vendrán activas las opciones que posean relación en parámetros con fórmulas que sean de tipo sin definir. Caso contrario, estarán inactivas.

###### Validaciones

  * Desde las opciones seleccionadas debe existir una asignación a alguna fórmula dentro de los parámetros para el Portal IVA que se encuentre en los Parámetros de Liquidador de IVA.
  * Deben existir fórmulas con estos tipos asociados: 
    * Percepción de IVA.
    * Percepción de Ganancias.
    * Percepción de Ingresos Brutos.
    * Impuestos Internos.



##### Estructura del Excel descargado

El Excel posee la siguiente estructura:

  * **Datos identificatorios del comprobante:** se encuentran entre la columna "A" y la "G", además se encuentran griseadas. Se recomienda no modificar estos datos.
  * **Importes por clasificar:** la planilla se completa dinámicamente dependiendo de las opciones seleccionadas. Es decir, si tengo activo Importe de per. o pagos a cuenta de otros impuestos nacionales esta columna se visualizará de color amarillo, y los importes a clasificar se obtendrán de las fórmulas asignadas en los parámetros. Seguidamente a esta columna, vendrán las fórmulas pertenecientes al modelo de Porta IVA que posean el tipo de fórmula Percepción de Ganancias (columnas en blanco). Hay que tener en cuenta que se debe asignar un importe al menos a una de esas fórmulas. También es necesario que el importe distribuido en una o más fórmulas sea igual al importe que figura en la columna amarilla a clasificar.
  * **Orden de las columnas:**
    * Importe de per. o pagos a cuenta de otros impuestos nacionales + fórmulas de Percepción de Ganancias.
    * Importe de percepciones de ingresos brutos + fórmulas de Percepción de Ingresos Brutos.
    * Importe de percepciones o pagos a cuenta de IVA + fórmulas de Percepción de IVA.
    * Importe de impuestos internos + fórmulas de impuestos internos.



Tenga en cuenta:

  * No debe modificar la estructura de la planilla descargada, es decir, agregar o eliminar columnas, modificar datos de cabecera del Excel, modificar el importe que viene en las columnas amarillas.
  * En el caso que la columna a reclasificar tenga sólo una columna para clasificar, esta vendrá asignada (con importe) por defecto.



##### Importación

Una vez reclasificados los importes en la planilla descargada, podrá importarlos.  
Aquí algunas validaciones, previas a ejecutar el proceso:

  * **Errores de estructura:**
    * Añadir o eliminación de columnas.
    * Cambiar alguna descripción de la columna cabecera.
    * El archivo debe contener al menos 1 comprobante a modificar.
    * Valide que sea un archivo Excel.
  * **Asiento generado:** si algún comprobante del archivo posee asiento generado, se solicita confirmación, dado que se eliminará dicho asiento si se continúa con el proceso.



Una vez ejecutado el proceso, obtenemos una planilla Excel cono el resultado de la importación.

Validaciones que se aplican en el archivo Excel:

  * **Existencia del comprobante importado:** verifica que exista el número interno del comprobante a modificar.
  * **Que el importe a clasificar sea efectivamente el previamente registrado:** verifica que no se haya modificado los importes de la columna amarilla.
  * **Que los importes clasificados sean igual al importe a clasificar:** verifica que los importes distribuidos entre las diferentes fórmulas que pertenecen al mismo concepto sumen la totalidad del importe a clasificar.
  * **Comprobante con asiento exportado o transferido:** no se pueden modificar estos comprobantes.



#### Preguntas frecuentes

**¿Puedo modificar las fórmulas de los modelos de ingreso de comprobantes PIVAV, PIVAVCRED, PIVAC o PIVACCRED?**  
Sí, pero sólo es posible modificar la descripción y el tipo de fórmula, además de la configuración de las cuentas contables sobre dichos modelos. Esto serviría si desea reemplazar un concepto no utilizado por otro de mayor valía para el usuario.

**¿El proceso genera automáticamente el asiento contable por cada comprobante?**  
No, se debe generar a través del proceso Generación de asientos contables.  
La posibilidad de generar asiento o no depende de la configuración del tipo de comprobante utilizado como equivalencia para la importación de comprobantes.

**¿Qué sucede con el importe de la columna a reclasificar?**  
El proceso modifica el comprobante y reasigna el importe a la nueva fórmula en el archivo Excel, quedando la fórmula original con valor cero.

**¿Qué pasa si hay fórmulas en los comprobantes con importe previo a la exportación (fórmulas que no son las parametrizadas)?**  
Esta situación revela que el comprobante ha sido modificado manualmente.  
En este caso, se sumarán los importes de aquellas fórmulas a clasificar en el archivo Excel, cuando contengan un valor previo en el comprobante.

##### Contenidos relacionados

  * [Guía sobre importación de comprobantes AFIP - Portal IVA](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_iv/afipportaliva_guia_iva/)

  * [Importación de comprobantes desde AFIP - Portal IVA](https://ayudas.axoft.com/24ar/ayudas/iv/comprobantes_carp_iva/portaliva_carp_iva/importportaliva_iva/)
