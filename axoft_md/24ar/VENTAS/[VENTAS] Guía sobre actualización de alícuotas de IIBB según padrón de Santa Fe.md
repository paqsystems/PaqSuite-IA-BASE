# Guía sobre actualización de alícuotas de IIBB según padrón de Santa Fe

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_alicuotiibbsantafe_gv3/

## Contenido

# Guía sobre actualización de alícuotas de IIBB según padrón de Santa Fe

Esta guía le permitirá configurar las alícuotas de ingresos brutos necesarias para utilizar el padrón de alícuotas de retenciones y percepciones, de acuerdo con la Resolución 37/2025 emitida por la Administración Provincial de Impuestos (en adelante API) de la provincia de Santa Fe.

Dicho padrón estará a disposición en forma mensual para los agentes de percepción y retención en la página web de la API.  
Si su empresa fue designada como agente de percepción y/o retención de Ingresos Brutos para la provincia de Santa Fe, debe disponer del padrón, de acuerdo al artículo 2 de la Resolución 37/2025 (API).  
Para realizar los cálculos de percepciones, usted deberá utilizar el proceso [Percepciones](?p=19407).

##### Puesta en marcha

Para la implementación de alícuotas de percepción definible de ingresos Brutos de Santa Fe, realizar los siguientes pasos:

  1. Si desea utilizar distintas bases de cálculo según el tipo de cliente, tendrá que dar de alta las [Clasificaciones para percepciones definibles](?p=19231) que vaya a necesitar.
  2. Verifique el código de modelo de SIPRIB - Santa Fe para la generación del archivo de texto de percepciones, a importar en aplicativo SIPRIB, desde el proceso [Definición de formato ASCII para percepciones definibles](?p=21184).
  3. Agregue la percepción definible con las alícuotas a aplicar para clientes incluidos en el padrón y, de corresponder, con la alícuota a aplicar para clientes fuera del padrón. En este punto debe configurar, en Tipo de impuesto la opción 'Ingresos brutos', el Código de provincia correspondiente (Santa Fe) y asignar el Modelo ASCII indicado en el paso anterior.  
Respecto a las alícuotas, debe configurarlas para cada uno de los 23 grupos especificados en el Anexo II de la Resolución 37/2025 de API, indicando en todas ellas el valor 'Santa Fe - Régimen general' en el campo Padrón. Tenga en cuenta que, si no completa todos los grupos antes de procesar el padrón, el asistente de actualización de alícuotas de IIBB le informará aquellos para los cuáles no hay alícuota definida.  
Si configura una alícuota general para clientes fuera del padrón, debe indicar el valor 'Sin padrón' en el campo Padrón.  
**Nota:** en el campo Método de acumulación de la base de cálculo de "Acumulación" indique el valor Diario, lo cual permite que el sistema calcule la percepción sobre el total de la base imponible acumulada en el día, respetando los mínimos no imponibles de la normativa vigente ($360.000 general o $650.000 para productos cárnicos).
  4. Desde el proceso [Parámetros de Ventas](?p=19401), dentro la solapa Santa Fe de Padrones, podrá definir, para los clientes incluidos en el padrón, si desea actualizar la alícuota considerando la provincia de la dirección de entrega o el CUIT del cliente. Si selecciona la opción por provincia, deberá indicar el código de provincia correspondiente a Santa Fe.  
Además, podrá definir si se asigna una alícuota general a los clientes fuera del padrón. En caso afirmativo, deberá establecer el criterio de actualización considerando la provincia de la dirección de entrega o el CUIT del cliente, y seleccionar el código de percepción y el código de alícuota configurados en el paso anterior.
  5. Agregue, en los [Modelos de percepciones](?p=13058) que correspondan, las alícuotas de la percepción de ingresos brutos de la provincia de Santa Fe.  
En caso de que el modelo de percepción no exista, debe crearlo.



__Nota

Utilice [Clasificación de percepciones definibles](?p=19231) cuando necesite aplicar distintas bases de cálculo o alícuotas según el tipo de cliente; para ello, en el cliente se define la clasificación y en el artículo se configuran, mediante el modelo de percepciones, todas las combinaciones posibles de grupos y clasificaciones. Tenga en cuenta que, en percepciones, cada base de cálculo debe estar asociada a una clasificación (recomendándose definir una sin clasificación como general) y que la percepción solo se calculará si existe coincidencia entre cliente y artículo.  


##### Tabla de grupos y alícuotas Santa Fe (percepciones y retenciones)

Asigne los siguientes códigos de grupo a las alícuotas de percepción y/o retención de acuerdo al anexo II de la Resolución 37/2025 de API – Santa Fe.

**Grupo** | **Alícuota de Retención (%)** | Alícuota de Percepción (%)  
---|---|---  
1 | 0,00 | 0,00  
2 | 0,01 | 0,01  
3 | 0,05 | 0,05  
4 | 0,10 | 0,10  
5 | 0,20 | 0,20  
6 | 0,30 | 0,30  
7 | 0,35 | 0,35  
8 | 0,40 | 0,40  
9 | 0,50 | 0,50  
10 | 0,60 | 0,60  
11 | 0,70 | 0,70  
12 | 0,80 | 0,80  
13 | 1,00 | 1,00  
14 | 1,25 | 1,25  
15 | 1,50 | 1,50  
16 | 2,00 | 2,00  
17 | 2,50 | 2,50  
18 | 2,75 | 3,00  
19 | 3,00 | 3,50  
20 | 3,50 | 4,00  
21 | 4,00 | 4,50  
22 | 4,50 | 5,00  
23 | 5,00 | 6,00  
  
Más información:

Si usted es agente de percepción por este régimen general de Ingresos Brutos con un cliente pasible de percepción, y que no esté incluido en el archivo del padrón de percepciones de Santa Fe, tendrá que percibir el impuesto aplicando sobre el monto el porcentaje de alícuota del 6,00% (según Artículo 11 Resolución 37/2025 de API – Santa Fe). Configure este porcentaje en una alícuota especial dentro de la percepción definible que incluyo las alícuotas correspondientes a los 23 grupos, con la diferencia, que en columna Padrón, le asigna el valor Sin padrón. Mantenga actualizado el porcentaje de esta percepción en forma manual.  


##### Detalle del circuito

  1. En forma mensual, se debe disponer del padrón de alícuotas de retenciones y percepciones (PARP), de acuerdo al artículo 2 de la Resolución 37/2025 (API), y guardarlo en el directorio comunes del servidor (NombreDelServidorCOMUN#########, donde ######### representa el número de llave de su sistema).
  2. Desde el proceso [Actualización de alícuotas de IIBB según padrón Santa Fe](?p=18476) puede: 
     1. Importar el padrón mensual en formato .zip al sistema.
     2. Actualizar las alícuotas asociadas a los clientes. Tenga en cuenta que, al actualizar alícuotas, los comprobantes emitidos utilizarán la nueva alícuota del padrón. Es recomendable ejecutar el proceso de actualización de alícuotas el último día hábil del mes (al terminar la jornada) o el primer día hábil antes de ingresar comprobantes.  
Al finalizar, el sistema le mostrará un detalle de la información actualizada.
     3. Actualizar las alícuotas asociadas a los proveedores. Tenga en cuenta que, al actualizar alícuotas, los comprobantes emitidos utilizarán la nueva alícuota del padrón. Es recomendable ejecutar el proceso de actualización de alícuotas el último día hábil del mes (al terminar la jornada) o el primer día hábil antes de ingresar comprobantes.  
Al finalizar, el sistema le mostrará un detalle de la información actualizada.
     4. Al ingresar o modificar un cliente, puede asignar en forma automática la alícuota asociada al grupo de Santa Fe que le corresponda al cliente, o de corresponder, asignarle la alícuota por fuera del padrón, pulsando la opción Actualizar según padrones de la solapa Direcciones (o la tecla <F9>).
     5. Al ingresar un cliente ocasional en una cotización, puede asignar en forma automática la alícuota asociada al grupo de Santa Fe que le corresponda al cliente, o de corresponder, asignarle la alícuota por fuera del padrón, pulsando la opción Actual. s/ padrones de la ventana Percepciones Definibles (o la tecla <F8>).
     6. Al ingresar un cliente ocasional en un pedido o desde el Facturador, puede asignar en forma automática la alícuota asociada al grupo de Santa Fe que le corresponda al cliente, o de corresponder, asignarle la alícuota por fuera del padrón, pulsando la opción Actualizar según padrones (o la tecla <Alt + P>).
     7. Al ingresar un cliente potencial, puede asignar en forma automática la alícuota asociada al grupo de Santa Fe que le corresponda al cliente, o de corresponder, asignarle la alícuota por fuera del padrón, pulsando la opción Actual. s/ padrones de la ventana Datos Adicionales (o la tecla <F8>).
     8. Al completar un período (quincenal o según lo indique 'API - Santa Fe'), deberá generar un archivo de texto con todas las percepciones efectuadas, para ser importado en el aplicativo de SIRPIB.



Si la parametrización la realizó desde [Percepciones definibles](?p=19407), utilice los procesos [Definición de formato ASCII](?p=21184) y [Generación del archivo ASCII](?p=21458).
