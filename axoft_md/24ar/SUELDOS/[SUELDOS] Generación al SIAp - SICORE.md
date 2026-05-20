# Generación al SIAp - SICORE

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sua/guia_puestamarcha_sua/?p=13102/

## Contenido

# Generación al SIAp - SICORE

Utilice el asistente para generar el archivo ASCII, que posteriormente puede ser importado desde la versión 6.1 del sistema SIAp - SICORE Este archivo contiene la información de liquidaciones con importes liquidados que correspondan al impuesto a las ganancias 4ª categoría.

Recuerde especificar las codificaciones para SICORE en el proceso [Parámetros de Sueldos](?p=13208) antes de generar el archivo ASCII.

__Nota

Se excluirán los empleados que no tengan ingresado un número de CUIL en su legajo o bien, tengan un número incorrecto. En este caso, el sistema emitirá un informe a fin de corregir los números y luego, volver a generar.

Determine la información a generar. Las opciones posibles son: 'Generación de retenciones' o 'Generación de datos de empleados'.

##### Generación de retenciones

Para incorporar en forma automática al SIAp - SICORE, los importes correspondientes a la liquidación del impuesto a las ganancias, utilice el formato de importación "retenciones".  
El archivo resultante contiene información de aquellas liquidaciones con importes de conceptos de Tipo 5 - Retención de ganancias o de Tipo 6 - Devolución de ganancias.

Período de generación: elija el mes y año liquidado que abarca la generación de información a presentar para el SIAp - SICORE Todos los datos fijos de liquidaciones existentes en ese período (según la modalidad de generación) deben tener estado 'Cerrada' o 'Transferida', es decir, el período ya no es operativo y está listo para generar la información legal.

Incluye ajuste de liquidación año anterior: elija esta opción si usted desea generar la información para presentar una liquidación anual para el SIAp - SICORE.

Fecha de retención: existen dos posibilidades para su generación: automática o manual.

  * Automática: el sistema toma, por defecto, la fecha de pago ingresada en el momento de la carga de los datos fijos de cada liquidación que corresponda al período de presentación. Sin embargo, si existiera alguna liquidación que por su definición en los datos fijos corresponda al período de presentación pero que la fecha de pago ingresada fuera posterior al período, entonces el sistema asigna automáticamente una fecha de retención correspondiente al último día del período.
  * Manual: en este caso, la fecha de retención a informar será la fecha solicitada por pantalla. Por lo tanto, todas las liquidaciones existentes dentro del período seleccionado se informarán con la misma fecha de retención, independientemente de la fecha de pago definida en los datos fijos.



Tipo de generación: indique la forma de realizar la generación del archivo. Las opciones posibles son: por período de la liquidación o bien, por fecha de pago de la liquidación.

  * **Por período de la liquidación:** incluye las liquidaciones cuyo período de liquidación corresponda al ingresado.
  * **Por fecha de pago de la liquidación:** incluye las liquidaciones que correspondan a datos fijos cuya fecha de pago corresponda al período ingresado.



Modalidad de generación: es posible generar el archivo ASCII y/o generar un reporte de retenciones y devoluciones.

__Nota

En el caso de haber datos fijos en estado ‘Abierto’, el sistema le preguntará si quiere cerrar los datos fijos de manera masiva. Indique ‘Sí’ si quiere que el sistema cierre y controle los datos fijos a tener en cuenta para el informe. Si el sistema detecta alguna anormalidad que impida el cierre, lo indicará con el número de dato fijo a revisar.

##### Genera archivo ASCII

Indique el nombre del archivo ASCII a generar. Por defecto, se propone SUSICORE.TXT.  
A continuación, ingrese el directorio donde grabará el archivo a generar. Para su comodidad, utilice el botón 'Examinar'.  
La generación del archivo ASCII se realiza de la siguiente manera:

Código de comprobante: el código de comprobante se crea en base a la naturaleza del concepto liquidado y a la parametrización efectuada en el proceso [Parámetros de Sueldos](?p=13208).  
Si el concepto es de Tipo 5 - Retención de ganancias, se genera como código de comprobante, el parametrizado para código de retención.  
Si el concepto es de Tipo 6 - Devolución de ganancias, se genera el parametrizado para código de devolución.

Si anteriormente usted selecciono la opción de Incluye ajuste de liquidación año anterior, estos códigos son reemplazados por código 61 cuando el concepto sea de Tipo 5 - Retención de ganancias y código 62 cuando el concepto sea de Tipo 6 - Devolución de ganancias.

Fecha de emisión del comprobante: se genera de la misma manera que la fecha de emisión de la retención.

Número del comprobante: se genera el número de recibo de liquidación como referencia de número de comprobante.

Importe del comprobante: el importe del comprobante se informa en cero.

Código de impuesto: todos los registros se generan con el código de impuesto para sueldos (por impuesto a las ganancias), parametrizado en el proceso [Parámetros de Sueldos](?p=13208).

Código de régimen: todos los registros se generan con el código de régimen para sueldos (parametrizado en el proceso [Parámetros de Sueldos](?p=13208)), correspondiente a sueldos, jubilaciones y otros réditos de carácter periódico del trabajo personal.

Código de operación: todos los registros se generan con el código de operación parametrizado en el proceso [Parámetros de Sueldos](?p=13208), correspondiente a retención.

Fecha de emisión de la retención: se genera la fecha de pago, según la parametrización: 'Automática' o 'Manual'.

Código de condición: todos los registros se generan con el código de condición parametrizado en el proceso [Parámetros de Sueldos](?p=13208).

Base de cálculo, Importe de la retención: si el concepto es de Tipo 5 - Retención de ganancias, la base de cálculo se genera con ceros y en el importe de la retención, se genera el importe liquidado para el concepto.  
Si el concepto es de Tipo 6 - Devolución de ganancias, en la base de cálculo se genera el importe liquidado por devolución y el importe de retención se genera con ceros.

Tipo de documento del retenido: todos los registros se generan con el tipo de documento correspondiente al código de CUIL parametrizado en el proceso [Parámetros de Sueldos](?p=13208).

Número de documento del retenido: se informa el número de CUIL del empleado.

Porcentaje de exclusión, Fecha de emisión del boletín, Número certificado original, Denominación del ordenante, Acrecentamiento, CUIT del país del retenido y CUIT del ordenante: estos datos se generan en cero o caracteres en blanco (según los tipos de datos).

##### Formato de archivo ASCII (retenciones)

La siguiente tabla resume el formato del archivo ASCII para SIAp – SICORE versión 9.8.

**Nro.** | **Desde** | **Hasta** | **Long.** | **Tipo dato** | **Descripción**  
---|---|---|---|---|---  
1 | 1 | 2 | 2 | Entero | Código del comprobante  
2 | 3 | 12 | 10 | Fecha | Fecha de emisión del comprobante (DD/MM/AAAA)  
3 | 13 | 28 | 16 | Texto | Número del comprobante  
4 | 29 | 44 | 16 | Decimal | Importe del comprobante  
5 | 45 | 48 | 4 | Entero | Código de impuesto  
6 | 49 | 51 | 3 | Entero | Código de régimen  
7 | 52 | 52 | 1 | Entero | Código de operación  
8 | 53 | 66 | 14 | Decimal | Base de cálculo  
9 | 67 | 76 | 10 | Fecha | Fecha de emisión de la retención  
10 | 77 | 78 | 2 | Entero | Código de condición  
11 | 79 | 79 | 1 | Entero | Retención practicada a sujetos suspendidos según:  
12 | 80 | 93 | 14 | Decimal | Importe de la retención  
13 | 94 | 99 | 6 | Decimal | Porcentaje de exclusión  
14 | 99 | 109 | 10 | Fecha | Fecha de emisión del boletín  
15 | 110 | 111 | 2 | Entero | Tipo de documento del retenido  
16 | 112 | 131 | 20 | Texto | Número de documento del retenido  
17 | 132 | 145 | 14 | Entero | Número certificado original  
  
Para más información acerca de los campos que componen esta tabla, consulte el ítem Genera archivo ASCII.  
Recuerde especificar las codificaciones para SICORE en el proceso [Parámetros de Sueldos](?p=13208) antes de generar el archivo ASCII.

##### Genera reporte de retenciones y devoluciones

Ejecute esta opción para obtener un reporte con información detallada de las retenciones y devoluciones practicadas en el período de generación seleccionado.

Configurar reporte  
Desde esta opción, accede a la configuración del reporte. Defina el formato de los reportes mediante el Administrador de reportes. (Esta opción está dentro del administrador general del sistema)

##### Generación de datos de empleados

Permite generar un archivo ASCII con los datos de los empleados, que posteriormente puede ser incorporado en forma automática al sistema SIAp - SICORE, mediante el formato de importación 'Sujetos Retenidos'.  
Recuerde especificar las codificaciones para SICORE en el proceso [Parámetros de Sueldos](?p=13208) y los datos legales para Provincias, antes de ejecutar la generación del archivo ASCII. Si no especifica un código para SICORE para una provincia, se informa el código "99".  
Indique el nombre del archivo ASCII a generar. Por defecto, se propone LEGAJOS.TXT.  
A continuación, ingrese el directorio donde grabará el archivo a generar. Para su comodidad, utilice el botón "Examinar".

##### Formato de archivo ASCII (datos de empleados)

**Nro.** | **Desde** | **Hasta** | **Longitud** | **Descripción**  
---|---|---|---|---  
1 | 1 | 11 | 11 | Número de documento del retenido  
2 | 12 | 31 | 20 | Apellido y Nombre  
3 | 32 | 51 | 20 | Domicilio  
4 | 52 | 71 | 20 | Localidad  
5 | 72 | 73 | 2 | Provincia  
6 | 74 | 81 | 8 | Código postal  
7 | 82 | 83 | 2 | Tipo de documento del retenido  
  
##### Contenidos relacionados

  * [Videos sobre modernización laboral - Cambios en Sueldos](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/modernlaboral_sua_vid/)
