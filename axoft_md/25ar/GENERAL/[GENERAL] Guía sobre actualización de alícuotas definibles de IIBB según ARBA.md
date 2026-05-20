# Guía sobre actualización de alícuotas definibles de IIBB según ARBA

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_guiagenerarchpdf_gla/?p=26537/

## Contenido

# Guía sobre actualización de alícuotas definibles de IIBB según ARBA

Esta guía le permitirá configurar las alícuotas de ingresos brutos necesarias para utilizar el Padrón de Recaudación por sujeto emitido por Rentas de la provincia de Buenos Aires.

La Disposición Normativa 1/04, que fue modificada por la Disposición Normativa 39/18 establece que se pondrá a disposición un padrón de contribuyentes de la Provincia de Buenos Aires, en el cual se especifica la alícuota y el porcentaje de percepción que corresponde aplicar. Dicho padrón estará a disposición de los agentes de percepción en la página web de esta Agencia de Recaudación y su actualización se realizará mensualmente.  
Si su empresa fue designada como agente de percepción de Ingresos Brutos para la provincia de Buenos Aires, debe consultar el padrón, ya sea en forma manual (desde el sitio web de ARBA) o mediante un archivo ASCII.  
Para realizar los cálculos de percepciones, usted podrá optar por utilizar el proceso [Alícuotas](https://ayudas.axoft.com/25ar/alicuota_gv) o [Percepciones definibles](?p=19407). La principal diferencia es que, en la primera modalidad, la cantidad de alícuotas aplicables para percepciones es limitada.

Más información:

Tenga en cuenta que no se pueden usar ambas modalidades simultáneamente. Si el sistema detecta la existencia de al menos una percepción definible con grupo de ARBA asignado, la actualización de alícuotas se realizará con la modalidad de [Percepciones definibles](?p=19407).

##### Puesta en marcha

Para la implementación de alícuotas de IIBB para ARBA con percepciones definibles debe realizar los siguientes pasos:

  1. Desde el proceso [Parámetros de Ventas](https://ayudas.axoft.com/25ar/paramgrales_gv), dentro la solapa ARBA de [Padrones](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-padrones), podrá definir si desea actualizar la alícuota teniendo en cuenta la provincia de la dirección de entrega o el CUIT del cliente. Si selecciona la primera opción, deberá indicar el código de provincia correspondiente a Buenos Aires.
  2. Si desea utilizar distintas bases de cálculo según el tipo de cliente, tendrá que dar de alta las [Clasificaciones para percepciones definibles](https://ayudas.axoft.com/25ar/clasifpercepdefin_gv) que vaya a necesitar.
  3. Defina un modelo para la generación de ASCII desde el proceso [Definición de formato ASCII para percepciones definibles](https://ayudas.axoft.com/25ar/definmodarchascii_gv).
  4. Agregue las [percepciones definibles](https://ayudas.axoft.com/25ar/percepcdefin_gv). En este punto debe configurar las alícuotas para cada uno de los grupos especificados en la Disposición 39/18 de ARBA y asignar el Modelo ASCII creado en el paso anterior. Si no define todos los grupos antes de procesar el padrón, el asistente de actualización de alícuotas de IIBB le informará aquellos para los cuáles no hay alícuota definida.
  5. Asocie las alícuotas definidas en el punto anterior a los artículos que deban liquidar percepción de IIBB a través del proceso [Actualización masiva de artículos](?p=17026): 
     1. Seleccione Percepciones definibles dentro de la sección Impuestos y pulse el botón "Siguiente".
     2. Agregue las alícuotas en la grilla de percepciones definibles y deje el Tipo de actualización con la opción 'Agregar'. Para más información consulte la ayuda de [Percepciones definibles](https://ayudas.axoft.com/25ar/percepcdefin_gv).Tenga en cuenta que si utiliza [Clasificación de percepciones definibles](https://ayudas.axoft.com/25ar/clasifpercepdefin_gv), tendrá que repetir estas alícuotas por cada clasificación, de manera de cubrir todas las posibilidades.
  6. Si anteriormente utilizaba [Alícuotas](https://ayudas.axoft.com/25ar/alicuota_gv), deberá blanquear las mismas en cada cliente. Para mayor conveniencia, puede hacerlo desde el proceso [Actualización masiva de clientes](https://ayudas.axoft.com/25ar/actualizacionmasivacliente_gv).



Más información:

Para evitar la doble imposición, al ejecutar la actualización de alícuotas de clientes desde el proceso [Actualización de alícuotas de IIBB según ARBA Bs.As.](https://ayudas.axoft.com/25ar/actalicibpadronrentabsas_gv), si existe al menos una alícuota de percepción definible asociada a un grupo de ARBA, el sistema asignará el porcentaje "0" (cero) a todas las [Alícuotas](https://ayudas.axoft.com/25ar/alicuota_gv) que tengan asociadas un grupo de ARBA.

**Ejemplo de Modelo ASCII para percepciones de ARBA**

A continuación, se detalla un ejemplo de modelo para la [Generación de archivo ASCII para percepciones definibles](https://ayudas.axoft.com/25ar/generarchasciipercepdefin_gv).

El archivo generado puede ser incorporado en los aplicativos SIAp Agente de Recaudación Provincia de Buenos Aires y Agente de Recaudación Sirft Baires.

Sección: 1 - ARBA

**Columna** | **Leyenda** | **Comienzo** | **Longitud** | **Tipo**  
---|---|---|---|---  
@CU | CUIT | 1 | 13 | C  
@FO | FECHA | 14 | 10 | F  
@TC | TIPO | 24 | 1 | C  
@LC | LETRA | 25 | 1 | C  
@NS | SUCURSAL | 26 | 4 | N  
@NC | COMPROB | 30 | 8 | N  
@II | MONTIMP | 38 | 12 | N  
@IR | IMPRET | 50 | 11 | N  
@LY | a | 61 | 1 | C  
  
Parametrización general

Separa Campos: | N | Símbolo: | N | Completa caracteres con: | N  
---|---|---|---|---|---  
Separa Decimales: | S | Símbolo: | . | Decimales p/importes: | 2  
Separa Miles: | N | Símbolo: |  | Créditos en negativo: | S  
Separa Fecha: | S | Símbolo: | / | Máscara para Fechas: | DD/MM/AAAA  
Separa CUIT/CUIL: | S | Símbolo: | - | Completa números con: | C  
Separa Nro. Comp: | N | Símbolo: |  | Decimales p/  
alícuotas: | 0  
  
Clasificación de comprobantes

| **A** | **B** | **C** | **M** | **E**  
---|---|---|---|---|---  
**Facturas** | F | F | F | F | F  
**Débitos** | D | D | D | D | D  
**Créditos** | C | C | C | C | C  
  
##### Detalle del circuito

  1. Mensualmente se debe acceder al sitio web de ARBA para obtener el Padrón de Recaudación por sujeto y guardarlo en el directorio comunes del servidor (\NombreDelServidorCOMUN#########, donde ######### representa el número de llave de su sistema).
  2. Desde el proceso [Actualización de alícuotas de IIBB según ARBA Bs.As.](?p=21126) puede: 
     1. Actualizar el padrón del sistema.
     2. Actualizar las alícuotas asociadas a los clientes. Tenga en cuenta que, al actualizar alícuotas, los comprobantes emitidos utilizarán la nueva alícuota del padrón. Es recomendable ejecutar el proceso de actualización de alícuotas el último día hábil del mes (al terminar la jornada) o el primer día hábil antes de ingresar comprobantes.  
Al finalizar, el sistema le mostrará un detalle de la información actualizada.
     3. Al ingresar o modificar un cliente, puede asignar en forma automática la alícuota asociada al grupo de ARBA que le corresponda al cliente, pulsando la tecla <F8>: 
        1. Si está ingresando o modificando un cliente habitual y presiona la tecla de función dentro de la grilla de [Percepciones definibles](?p=19407), se actualizará automáticamente la alícuota indicada en el padrón. Para más información consulte la información de la parametrización de [clientes](?p=19401/#parametros-para-clientes).
        2. Si está ingresando un cliente ocasional y presiona la tecla de función en la sección de [Percepciones definibles](?p=19407), se insertará automáticamente la alícuota indicada en el padrón. Para más información consulte Clientes ocasionales.
        3. Si está ingresando o modificando un cliente potencial y presiona la tecla de función, se actualizará automáticamente la alícuota indicada en el padrón. Para más información consulte la información del proceso [Clientes potenciales](?p=19238).
     4. Al completar un período (mensual o según lo indique ARBA), deberá presentar un soporte magnético con todas las percepciones efectuadas, a fin de generar un archivo ASCII para ser importado por el aplicativo de ARBA.  
Si la parametrización la realizó en el proceso [Alícuotas](?p=19193), utilice el proceso [Generación Archivo Percepciones IB Bs.As.](?p=21480/#generacion-archivo-percepciones-ib-bs-as)  
Si la parametrización la realizó desde [Percepciones definibles](?p=19407), utilice los procesos [Definición de formato ASCII](?p=21184) y [Generación del archivo ASCII](?p=21458).



Para más información, consulte la ayuda de [Actualización de alícuotas de IIBB según ARBA Bs.As.](?p=21126)

Clientes ocasionales:

A través del proceso Facturación es posible emitir facturas a clientes no habituales, en cuyo caso no se desea asignar un código de identificación. Para ello se ingresará, en el campo Código de cliente, un código de cliente ocasional. 

Para ingresar facturas de clientes ocasionales, ingrese '000000' en el campo Código de cliente. En este caso, se visualizará una ventana para cargar los datos necesarios del cliente. Estos datos saldrán impresos en la factura y en el subdiario de IVA ventas.

__Nota

A los clientes ocasionales se les asigna un código '000000' para diferenciarlos de los clientes habituales. Siempre corresponde realizarles facturas de venta al contado, ya que no se les registra deuda en cuenta corriente. Si no se editan los datos, el comprobante queda registrado como una venta a consumidor final, sin detallar los datos del cliente.  


Si se encuentra habilitada la opción Edita percepciones definibles en la solapa Impuestos de Parámetros de Ventas será posible agregar o eliminar los códigos de percepción parametrizados en el cliente o cambiar la alícuota asignada. Estas modificaciones pueden realizarse desde los procesos Facturación, Notas de crédito y Notas de débito.

**Asignación de alícuota de IB según padrones de Rentas Bs.As.  
**Pulse <F8> para consultar el padrón de Rentas (Provincia de Bs.As.) y asignar en forma automática la alícuota que se le debe aplicar al cliente.  
Podrá asignar la alícuota desde el campo Alícuota fija o desde la grilla de [Percepciones definibles](https://ayudas.axoft.com/25ar/percepcdefin_gv). Para más información sobre este tema consulte la [Guía de Implementación sobre actualización de Alícuotas Definibles de IIBB según ARBA](?p=26537).

**Asignación de alícuotas de IB de acuerdo a padrones de AGIP  
**Pulse <F9> para consultar los padrones (Ciudad de Bs. As.) y asignar en forma automática los códigos de retenciones que se le debe aplicar al cliente.  
Podrá asignar la alícuota desde la columna "Cód" en la grilla de Percepciones definibles. Para más información sobre este tema consulte [Actualización de alícuotas de IIBB según AGIP Bs.As. (Rentas Ciudad de Bs.As.)](?p=26538)

##### Contenidos relacionados

  * [Actualización de alícuotas de IIBB según ARBA Bs.As.](https://ayudas.axoft.com/25ar/ayudas/gv/procperiodico_carp_gv/actalicibpadronrentabsas_gv/)

  * [Video sobre regímenes de facturación](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/regfact_gral_vid/)

  * [Videos sobre configuración impositiva](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/configimpositiva_gral_vid/)

  * [Videos sobre gestión impositiva](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/gestimpositiva1_gral_vid/)

  * [Videos sobre retenciones y percepciones impositivas](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/retencpercep_gral_vid/)
