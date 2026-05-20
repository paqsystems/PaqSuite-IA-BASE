# Percepciones (Restô)

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv3/guia_percepdefin_gv3/?p=13099/

## Contenido

# Percepciones (Restô)

Usted puede definir distintos tipos de percepciones, obteniendo una mayor flexibilidad y la posibilidad de asociarles un modelo de formato adecuado para la generación de soportes magnéticos.

Este proceso permite agregar, modificar y eliminar tipos de percepción con distintas bases de cálculo y alícuotas. Para definir adecuadamente las percepciones, es recomendable que revise la [Guía de implementación sobre percepciones definibles](?p=14409).

Para cada código de percepción definible se ingresarán los siguientes datos:

##### Principal

Código y Descripción de la percepción: permite identificar los distintos tipos, bases y alícuotas de percepciones posibles.

Tipo de impuesto: en este campo se parametriza el tipo de impuesto de la percepción definible.  
Los valores posibles son:

  * IVA
  * Ingresos Brutos
  * Impuestos Internos
  * Otros impuestos



Código de régimen: ingrese el código asignado por la AFIP u otro organismo para la Percepción indicada.

Jurisdicción: ingrese en este campo a qué Jurisdicción pertenece la percepción.  
Los valores posibles son:

  * Nacional
  * Provincial
  * Municipal
  * Otra



Si se selecciona una Jurisdicción Provincial se habilitará el campo Código de Provincia para poder seleccionarla.

Leyenda: leyenda general que será posible utilizar en la generación de ASCII.

Código de modelo ASCII: ingrese el código de modelos de formatos de generación de archivos ASCII con el cual se informará la percepción. Los formatos de archivos de texto (ASCII) se definen y parametrizan en el proceso [Definición de Formato ASCII](https://ayudas.axoft.com/24ar/percepdefin_carp_gv) (opción Procesos periódicos | Percepciones definibles del menú principal).  
Cada formato está identificado bajo un código de modelo, el que puede ser asociado a percepciones. La información referida al formato del archivo deberá ser provista por el organismo al que se le hará la presentación.

##### Parámetros para el cálculo

Mínimo no imponible: es de utilidad para el caso de percepciones que se calculan sólo a partir de un importe determinado.  
En este campo se consigna el importe mínimo gravado a partir del que se calculará la sobretasa correspondiente.

Mínimo de percepción: es el importe mínimo de percepción a partir del que se realizará la percepción.

Método para la evaluación del mínimo de percepción: este parámetro permite definir si el mínimo de percepción se analizará por cada alícuota o en forma global por toda la percepción.  
Este parámetro permite cumplir con la RG 5329/2023 y su modificatoria RG 5334/2023, la cual establece que corresponde efectuar la percepción cuando se supere el mínimo de percepción en la transacción, es decir considerando todas las alícuotas del comprobante que corresponden a esta percepción.  
Los valores posibles son:

  * Aplica por cada alícuota (A).
  * Aplica en forma global para toda la percepción (G).



**Ejemplo...**  
Si la percepción tiene parametrizado el monto mínimo de percepción es $3000, y tiene dos alícuotas, una del 3% y una 1,5%.  
Al generar una factura con el siguiente detalle:

  * Artículo 1 x $80.000 de neto gravado, se le aplica un 3% de percepción y da $2400.
  * Artículo 2 x $50.000 de neto gravado, se le aplica un 1.5% de percepción y da $750.



Si se parametrizó que se aplica el mínimo por alícuota, se evalúa por separado la percepción correspondiente a cada alícuota ($2400 y $750) contra el mínimo de percepción ($3000) y al ser menores no lo aplica.  
Si se parametrizó que el mínimo se aplica en forma global para toda la percepción, se sumaran los importes calculados por cada alícuota ($2400 + $750) y este nuevo valor ($3150) se compara con el mínimo de percepción. Al superar dicho importe se aplica la percepción.

Código AFIP: si usted emite comprobantes electrónicos para el mercado interno, indique para cada una de las alícuotas, el código de tributo definido por AFIP.  
Según el Tipo de percepción y la Jurisdicción, los valores posibles de selección (establecidos por AFIP) son los siguientes:

  * 01 (para Impuestos nacionales)
  * 02 (para Impuestos provinciales)
  * 03 (para Impuestos municipales)
  * 04 (para Impuestos Internos)
  * 99 (para Otros)



Método de acumulación de la base de cálculo: indica si la acumulación es:

  * **Mensual:** indica que el cálculo de la percepción se realiza sobre el total de la base imponible acumulados del mes, en el caso que ingrese
  * **Anual**
  * **Ninguno:** el cálculo de la percepción se realizará sobre cada comprobante que se efectúa, sin considerar las percepciones anteriores.



Esta opción solo será tenida en cuenta en aquellos comprobantes generados desde Facturador y para aquellas percepciones con base de cálculo 'Neto gravado + Exento'.

##### Bases de cálculo

Base de cálculo: se podrán seleccionar las bases de cálculo para una misma percepción, las bases de cálculo disponibles son:

  * Neto Gravado
  * Neto Gravado + Exento
  * Neto Gravado + IVA
  * Neto Gravado + Exento + IVA
  * Neto Gravado + IVA + Imp. Int.
  * Neto Gravado + Exento + IVA + Imp. Int.
  * Neto Gravado + IVA + Imp. Int. + IB
  * Neto Gravado + Exento + IVA + Imp. Int. + I.B.
  * Total del Comprobante
  * Otra Percepción Definible (1)
  * Importe Fijo por Cantidad (2)
  * Neto Gravado + Exento + Imp. Int
  * Neto Gravado + Exento + Ing. Brutos
  * Neto Gravado + Exento + Imp. Int + IB



(1) El campo _Percepción relacionada_ se habilitará cuando la base de cálculo sea 'Otra Percepción Definible'. No se podrá asociar una percepción definible cuya base de cálculo sea distinta a 'Otra percepción definible'.  
(2) El campo _Importe_ se habilitará cuando la base de cálculo sea 'Importe Fijo por Cantidad'. En el momento de facturar un artículo que tenga definido este código de impuesto, el proceso de facturación requerirá el importe unitario que corresponda para el código de percepción, tomando por defecto el que se encuentre definido para esa percepción.

Mínimo: se podrá ingresar el monto mínimo que deberá tener la base de cálculo para realizar la percepción.

Importe: se podrá ingresar el monto fijo percibir.

Percepción relacionada: se habilitará cuando la base de cálculo sea 'Otra Percepción Definible'. No se podrá asociar una percepción cuya base de cálculo sea distinta a 'Otra percepción definible'.

Clasificación: al completar estos campos, la percepción sólo se calculará para aquellos clientes y artículos que tengan definida la misma clasificación y de corresponder la misma alícuota.

Si usted utiliza el padrón Régimen General de AGIP, es recomendable crear distintas clasificaciones para poder establecer diferentes bases de cálculo en la percepción. Por ejemplo, la base de cálculo para clientes exentos utiliza el importe total del comprobante, y es diferente a la base de cálculo para clientes responsables inscriptos que utilizan el importe neto gravado más los importes exentos del comprobante. Entonces, la clasificación de la percepción en un cliente exento es distinta a la clasificación de la percepción para un cliente responsable inscripto.

__Nota

Para que el importe de la percepción se calcule es necesario que al mismo tiempo la clasificación de la percepción definible esté asignada en la percepción propiamente, en el cliente y en el artículo. Si la clasificación no está relacionada a la percepción, al cliente y al artículo no se calculará el importe de la percepción en el comprobante.

Para ello, se deben definir con anterioridad las clasificaciones desde el proceso [Clasificación para percepciones definibles](?p=13094).

##### Alícuotas

Es posible definir distintas alícuotas para una misma percepción, y para cada una es necesario definir el porcentaje y, de corresponder, el grupo de AGIP o ARBA.

Grupos AGIP para padrones

En el caso de que desee asignar en forma automática la alícuota de ingresos brutos correspondiente a cada cliente de acuerdo a las Resoluciones de AGIP se publican en la web de Rentas ([www.agip.gob.ar)](http://www.agip.gob.ar), complete el grupo de AGIP al que pertenece la alícuota que está definiendo según el padrón al que pertenezca.

__Nota

Los campos _Grupo AGIP_ son excluyentes entre sí.

Código y Descripción de la percepción: se podrán ingresar el código y descripción de las alícuotas de la percepción.

Porcentaje: ingrese el porcentaje asignado a cada alícuota:

Padrón: seleccione el padrón de percepciones que le corresponde a la alícuota, las opciones disponibles son:

  * Sin padrón
  * ARBA
  * AGIP - Riesgo fiscal
  * AGIP - Regímenes particulares
  * AGIP - Régimen general



Grupo: ingrese el grupo del padrón que le corresponde a la alícuota.

Para mayor información consulte el ítem [Puesta en marcha en la Guía sobre actualización de alícuotas de IIBB según AGIP Bs.As.](?p=14420)

Grupo ARBA para padrones

En el caso de que desee asignar en forma automática la alícuota de ingresos brutos que le corresponde a cada cliente según lo especificado en la Disposición Normativa 1/04, modificatorias y complementarias de Rentas de la Provincia de Buenos Aires, complete el grupo de ARBA al que pertenece la alícuota que está definiendo según el padrón publicado.

Grupo ARBA: indica el grupo de percepción de ARBA vinculado con la alícuota de percepción de Ingresos Brutos. Cada grupo cuenta con una alícuota diferente según la disposición de ARBA. Si la alícuota configurada corresponde a la alícuota a utilizar con los clientes que están fuera del padrón, entonces esta columna debe estar vacía.  
Para mayor información puede consultar [Guía de Implementación sobre actualización de alícuotas definibles de IIBB según ARBA](?p=14434).

##### Contenidos relacionados

No se ha encontrado ninguno
