# Alícuotas de Ventas

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_alicuotarba_gv/?p=19193/

## Contenido

# Alícuotas de Ventas

Este proceso le permite definir las tasas correspondientes a cada tipo de impuestos, que luego se aplicarán a los artículos y a los clientes.

Cada tipo de impuesto tiene un rango válido de códigos. Esto permite que sean diferenciados por el sistema.  
Defina por lo menos un código de cada tipo. Para aquellos tipos de impuesto no requeridos (debido a la naturaleza de los artículos que comercializa y las normas legales), defina un solo código con porcentaje cero.  
Las tasas o porcentajes pueden ser también valores negativos. Esto se utilizará, fundamentalmente, para definir subtasas. Para el caso de códigos de IVA, es recomendable definir como código '1' a la tasa general de IVA.  
Las sobretasas de IVA se aplican sobre el total gravado del comprobante , ya que se utilizan para registrar las percepciones que incluyen los grandes contribuyentes en sus facturas. Las sobretasas y subtasas de Impuestos Internos se calculan sobre el importe de impuesto interno del comprobante. 

Importe mínimo: este campo es de utilidad para el caso de percepciones que se calculan sólo a partir de un importe determinado. En este campo se consigna el importe mínimo gravado a partir del que se calculará la sobretasa correspondiente.

##### Especificaciones referidas a los códigos

Dentro de los códigos habilitados para impuestos internos, los códigos '40' y '82' se utilizan únicamente para el caso que el impuesto interno no surja de un porcentaje, es decir, que sea un importe fijo y particular en cada artículo. Por ello, al ingresar este código el sistema asume un porcentaje nulo.  
En el momento de facturar un artículo que tenga definido este código de impuesto, el proceso de facturación requerirá el importe unitario que corresponda para el impuesto interno, tomando por defecto el que se encuentre definido para el artículo.  
Los códigos '51' a '80' permitirán definir alícuotas para el cálculo de percepción de Ingresos Brutos en la facturación. Para estos códigos usted puede indicar, opcionalmente, el código de provincia al que corresponda cada alícuota. Este código podrá ser utilizado en el informe Impuestos Registrados para obtener las percepciones calculadas por cada provincia.

Grupo ARBA: indica el grupo de percepción ARBA vinculado con el código de alícuota de tipo percepción de Ingresos Brutos.  
Tenga en cuenta que si existe al menos una alícuota de [Percepciones definibles](https://ayudas.axoft.com/24ar/percepcdefin_gv) con un grupo de ARBA asociado, durante el proceso de actualización de alícuotas de percepción de IIBB según el padrón de ARBA, no serán tenidas en cuenta las alícuotas definidas en este proceso.

Grupo AGIP - Riesgo fiscal: indica el grupo de percepción AGIP vinculado con el código de alícuota de tipo percepción de Ingresos Brutos, ingrese '1' para identificar a los contribuyentes normales, e ingrese '2', '3' o '4' para contribuyentes que se encuentren dentro del padrón de contribuyentes con riesgo fiscal.

__Nota

Fuera de vigencia a partir del 01/01/2020 según Resolución Nº 296/AGIP/2019.  


Grupo AGIP - Magnitudes superadas: indica el grupo de percepción AGIP vinculado con el código de alícuota de tipo percepción de Ingresos Brutos, ingrese '1' para identificar a los contribuyentes normales, e ingrese '2' para contribuyentes que se encuentren dentro del padrón de contribuyentes con magnitudes superadas.

__Nota

Fuera de vigencia a partir del 01/01/2020 según Resolución Nº 296/AGIP/2019.  


Grupo AGIP - Exentos y alícuotas diferenciales: indica el grupo de percepción AGIP vinculado con el código de alícuota de tipo percepción de Ingresos Brutos, ingrese '1' para identificar a los contribuyentes normales, e ingrese '2' o '3' para contribuyentes que se encuentren dentro del padrón de contribuyentes exentos y alícuotas diferenciales.

__Nota

Fuera de vigencia a partir del 01/01/2020 según Resolución Nº 296/AGIP/2019.  


Grupo AGIP - Régimen general: indica el grupo de percepción AGIP vinculado con el código de alícuota de tipo percepción de Ingresos Brutos. Ingrese '0' para identificar a los contribuyentes que no están dentro del padrón de régimen general. Ingrese los números de grupo desde '1' a '16' para los contribuyentes que se encuentren dentro del padrón. Cada grupo cuenta con una alícuota diferente según la disposición de AGIP.

Para mayor información consulte el ítem [Puesta en marcha en la Guía sobre actualización de alícuotas de IIBB según AGIP Bs.As](?p=26538).

En el caso que desee asignar en forma automática la alícuota de ingresos brutos que le corresponda a cada cliente de acuerdo a las Resoluciones AGIP 251/08, AGIP 816/14, AGIP 177/09, AGIP 364/16, AGIP 421/16, 296/19 y 352/23 de la Ciudad de Bs. As. complete el grupo de Rentas al que pertenece la alícuota que está definiendo (campos Grupo AGIP).  
Los campos Grupo ARBA y de Grupo AGIP son excluyentes entre sí. El código '91' será definido en el caso de operar con clientes que posean la característica de 'IVA Liberado'. El porcentaje de liberación no es solicitado en este proceso, ya que es propio de cada cliente y se lo ingresa en el proceso [Clientes](https://ayudas.axoft.com/24ar/clientes_carp_gv). 

##### Señas

Si está activo el parámetro general Utiliza el sistema de facturación con señas, es posible modificar las alícuotas definidas en el proceso [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-clientes) para la generación de señas, sólo si no existen señas con estado 'Ingresado'.  
Los campos Porcentaje e Importe mínimo no son editables, si usted está modificando los datos de una alícuota para la que existen señas pendientes.

##### Comprobantes electrónicos para el mercado interno

Código AFIP: si usted emite comprobantes electrónicos para el mercado interno, indique para cada una de las alícuotas, el código de tributo definido por AFIP.  
Los valores posibles de selección (establecidos por AFIP) son los siguientes:

  * Para informar códigos de IVA: 
    * 3 (para 0%). El código **3** (para 0%) no está habilitado por AFIP para la versión de Webservice: Notificación Juez ('J').  
Si usted emite comprobantes electrónicos de turismo, defina una alícuota de IVA (con código de alícuota del 1 al 10), con porcentaje del 21% y asígnele el Código AFIP 10 (para 21% Aplica reintegro).
    * 4 (para 10.5%)
    * 5 (para 21%)
    * 6 (para 27%)
  * Para informar códigos de tributos: 
    * 01 (para Impuestos nacionales)
    * 02 (para Impuestos provinciales)
    * 03 (para Impuestos municipales)
    * 04 (para Impuestos Internos)
    * 99 (para Otros)



##### Contenidos relacionados

  * [Guía sobre actualización de alícuotas de IIBB según AGIP Bs. As. ](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_alicuotiibb_gv/)

  * [Video sobre regímenes de facturación](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/regfact_gral_vid/)

  * [Videos sobre gestión impositiva](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/gestimpositiva1_gral_vid/)
