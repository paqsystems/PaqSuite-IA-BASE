# Guía de Proveedores sobre actualización de alícuotas de IIBB según AGIP Bs.As.

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp/guia_actualalicagipbsas_cp/

## Contenido

# Guía de Proveedores sobre actualización de alícuotas de IIBB según AGIP Bs.As.

Las Resoluciones AGIP 251/08, 816/14, 177/09, 364/16 y 421/16 han implementado un procedimiento que implica la generación de padrones por parte de AGIP en donde se especifican las alícuotas de percepción y retención que se deberá aplicar a cada contribuyente del Impuesto sobre los Ingresos Brutos, por parte de los agentes de recaudación en cada transacción comercial que se practique con ellos.

Por tal motivo, todos los agentes de retención / percepción de ingresos brutos de la ciudad de Buenos Aires deben consultar los archivos ASCII emitidos por la autoridad municipal para determinar la alícuota que deben retener o percibir a sus proveedores o clientes respectivamente.  
Los padrones se publican en la web de Rentas ([www.agip.gob.ar](http://www.agip.gob.ar)).

__Nota

Recuerde que la tecla rápida _< F3>_ permite realizar la búsqueda de un texto en el árbol de procesos de todos los módulos. Como resultado, se exhibirá el nombre de los procesos que incluyen el texto ingresado, con la indicación del módulo y carpeta en la que se encuentran.

Se recomienda conocer las consideraciones dispuestas por AGIP para los agentes de recaudación del impuesto sobre los ingresos brutos a partir del 01/11/2016. Para más información consulte en el sitio de AGIP este [documento](http://www.agip.gob.ar/filemanager/source/Agentes/De%20Recaudacion/Ingresos%20brutos/Considerac%20de%20AR%20ISIB%20hasta%20Res%20%20486-2016%20AMPLIADO.pdf).

##### Puesta en marcha

A continuación se detallan los pasos a seguir para la asignación de códigos de retención de ingresos brutos en base a los padrones de Rentas.

  1. Decida cómo prefiere implementar el impuesto a los ingresos brutos en el sistema. Para más información consulte ¿Cómo me conviene implementar las retenciones de ingresos brutos?.
  2. Ingrese al proceso [Códigos de retención para Ingresos Brutos](?p=14619#ib) o [Códigos de retención definibles](?p=14619#definibles) según lo definido en el punto anterior y complete para cada código de retención los campos de Grupo AGIP. Para más información sobre estos campos consulte Consideraciones sobre los campos de Grupo AGIP.  
Cada padrón deberá tener dadas de altas las alícuotas de IIBB y los grupos que corresponda para los regímenes alcanzados, es decir que si la empresa está alcanzada por el régimen general y/o el particular de AGIP, deberá tener configuradas las alícuotas propias de cada régimen en el sistema.
  3. Ingrese a la siguiente página de Internet de Rentas para obtener los padrones actualizados de contribuyentes: <http://www.agip.gob.ar/agentes/agentes-de-recaudacion-e-informacion>.  
Utilice los archivos de los padrones sin modificar los nombres originales que tienen al ser descargados de la página de Rentas de la Ciudad de Buenos Aires.
  4. Copie los padrones en el directorio comunes del servidor (NombreDelServidor_______#########, donde ######### representa el número de llave de su sistema).
  5. Ingrese al proceso [Actualización de alícuotas de IIBB según AGIP Bs.As.](https://ayudas.axoft.com/24ar/actalicibagpbsas_cp) para actualizar el padrón del sistema y los códigos de retención de ingresos brutos asociados a cada uno de sus proveedores.



Tenga en cuenta que también puede clasificar a los proveedores desde el proceso [Proveedores](https://ayudas.axoft.com/24ar/proveedores_cp). Desde el botón "Actualizar según padrones" asignará en forma automática el código de retención de ingresos brutos que le corresponda de acuerdo al padrón.  
Para configurar las alícuotas de percepciones de IIBB para AGIP en el módulo Ventas, consulte la puesta en marcha de la [Guía de implementación sobre actualización de alícuotas de IIBB según AGIP Bs.As.](?p=26538/#puesta-en-marcha)

##### ¿Cómo me conviene implementar las retenciones de ingresos brutos?

Usted puede implementar las retenciones de ingresos brutos mediante alguna de las siguientes opciones:

  * [Códigos de retención para Ingresos Brutos](?p=14619#ib): es la forma básica de definir retenciones de ingresos brutos. Aunque cubre la mayor parte de las necesidades de este impuesto posee algunas limitaciones con respecto a las retenciones definibles.
  * [Códigos de retención definibles](?p=14619#definibles): esta opción permite definir distintos tipos de retenciones. Su beneficio radica en su mayor flexibilidad (más bases de cálculo y posibilidad de configurar bases de análisis) y la oportunidad de asociarle un modelo de formato de archivo ASCII para la generación de soportes magnéticos requeridos por la autoridad de aplicación del impuesto.



Importante:

Tenga en cuenta que si decide modificar la forma de implementar retenciones debe modificar la parametrización de ingresos brutos de todos sus proveedores. Por ejemplo, si trabajaba con retenciones de ingresos brutos y ahora decide trabajar con retenciones definibles no basta con agregar el código de retención definible sino que debe eliminar la retención de ingresos brutos; de lo contrario, se liquidará dos veces el impuesto.

##### Consideraciones sobre los campos del Grupo AGIP

Para trabajar con los padrones es necesario que asigne ciertos códigos de grupo a las alícuotas de percepción y a los códigos de retención.

  * **Grupo "1":** asigne este valor al código de retención / percepción que representa a la alícuota de porcentaje cero. El código de retención / percepción que tenga asociado este grupo será asignado al proveedor cuando éste figure en el padrón con porcentaje de alícuota en cero, o haya dejado de figurar en el padrón durante el período anterior y no esté presente en los padrones actuales.
  * **Grupo "2":** asigne este valor al código de retención / percepción que represente a la alícuota de exento o de magnitud superada del impuesto. El código de retención / percepción que tenga asociado este grupo será asignado al proveedor cuando éste resulte incluido en los padrones.
  * **Grupo "3":** asigne este valor al código de retención / percepción que representa a la alícuota con mayor porcentaje del padrón exento y alícuotas diferenciales. El código de retención / percepción que tenga asociado este grupo será asignado al proveedor cuando éste resulte incluido en los padrones.



**Códigos de grupo para riesgo fiscal  
**A partir de la Resolución N° 52/2018 de AGIP, se establece la "Matriz de Perfiles de Riesgo Fiscal" mediante la cual se categorizará a los contribuyentes y/o responsables del Impuesto sobre los Ingresos Brutos de acuerdo a su conducta tributaria en 5 niveles:  


**Nivel** | **Riesgo**  
---|---  
0 | MUY BAJO  
1 | BAJO  
2 | MEDIO  
3 | ALTO  
4 | MUY ALTO  
  
  * **Grupo "1":** asigne este valor al código de retención / percepción que represente a la alícuota general del impuesto. El código de retención / percepción que tenga asociado este grupo será asignado al proveedor cuando éste haya figurado en el padrón durante el trimestre anterior y no esté presente en el padrón actual; es decir dejó de ser catalogado como de riesgo fiscal.
  * **Grupo "2":** asigne este valor al código de retención / percepción que representa al nivel de riesgo fiscal con menor porcentaje (distinto de cero). El código de retención / percepción que tenga asociado este grupo será asignado al proveedor cuando éste resulte incluido en los padrones y tenga asignado dicho porcentaje.
  * **Grupo "3" y "4":** asigne números de grupo incrementales a los códigos de retención / percepción que representen los siguientes niveles de la matriz.



**Ejemplo...  
**A la fecha de publicación de la resolución, la asignación de grupos sería:

**Nivel** | **Alícuta de retención** | **Alícuota de percepción** | **Número de grupo**  
---|---|---|---  
0 |  |  | 1  
1 |  |  | 1  
2 | 4 | 5 | 2  
3 | 4.5 | 6 | 3  
4 | 4.5 | 6 | 3  
  
Más información:

Se recomienda conocer las consideraciones dispuestas por AGIP para los agentes de recaudación del impuesto sobre los ingresos brutos a partir del 01/11/2016. Para más información consulte en el sitio de AGIP [este documento](http://www.agip.gob.ar/filemanager/source/Agentes/De%20Recaudacion/Ingresos%20brutos/Considerac%20de%20AR%20ISIB%20hasta%20Res%20%20486-2016%20AMPLIADO.pdf).  
Usted podrá verificar si fue nominado como agente para un régimen especial de ingresos brutos o para el régimen general o en ambos regímenes. Para verificar esto, deberá consultar el "Universo de agentes de recaudación" – Anexo II, III, IV o V, de la Resolución N° 939/2013 y sus modificatorias desde el [sitio web de AGIP](http://www.agip.gob.ar).

**Códigos de grupos para el padrón régimen general  
**Si usted utiliza el padrón de régimen general, asigne los códigos de grupo para alícuotas de percepción y códigos de retención de acuerdo a la disposición de AGIP.

**Alícuotas de retenciones**

**Grupo** | **Porcentaje**  
---|---  
1 | 0,00%  
2 | 0,10%  
3 | 0,20%  
4 | 0,50%  
5 | 0,75%  
6 | 0,90%  
7 | 1,00%  
8 | 1,25%  
9 | 1,50%  
10 | 1,75%  
11 | 2,00%  
12 | 2,50%  
13 | 2,75%  
14 | 3,00%  
15 | 4,00%  
16 | 4,50%  
  
Las cantidades de grupos y los porcentajes de las alícuotas de retenciones podrán variar de acuerdo a disposiciones de AGIP.

Más información:

Si usted realiza una operación alcanzada por este régimen general de Ingresos Brutos con un proveedor pasible de retención y que no esté incluido en el archivo del padrón de régimen general, tendrá que retener el impuesto aplicando sobre el monto el porcentaje de alícuota del 4,50% (porcentaje puede variar de acuerdo a disposición de AGIP artículo 12 Resolución 421/16).  
Configure este porcentaje en un código de retención especial que no está en el archivo del padrón y asigne grupo 0. Mantenga actualizado el porcentaje de este código de retención en forma manual.

**Alícuotas de percepciones**

**Grupo** | **Porcentaje**  
---|---  
1 | 0,00%  
2 | 0,10%  
3 | 0,20%  
4 | 0,30%  
5 | 0,50%  
6 | 1,00%  
7 | 1,50%  
8 | 2,50%  
9 | 2,60%  
10 | 2,70%  
11 | 3,00%  
12 | 3,20%  
13 | 3,50%  
14 | 4,00%  
15 | 5,00%  
16 | 6,00%  
  
Los códigos de retenciones y de alícuotas de percepciones de los anexos I y II de la Resolución 364/16 (anexos VI y VII Resolución 939/13) se tendrán que configurar, asignar y mantener de forma manual.

**Proveedores que pueden estar en más de un padrón al mismo tiempo  
**Un mismo CUIT puede encontrarse en los padrones de "alto riesgo fiscal" y "exentos y alícuotas diferenciales" al mismo tiempo y en el mismo período. De acuerdo a la normativa vigente, el porcentaje de alícuota predominante para ese contribuyente será la alícuota que corresponda al padrón de exentos y alícuotas diferenciales, eso hasta tanto el contribuyente regularice su situación con AGIP.  
Además, un mismo CUIT puede encontrarse al mismo tiempo en los padrones de "alto riesgo fiscal" y "magnitudes superadas" en el mismo período. En ese caso, se agregarán las alícuotas de los dos padrones hasta tanto el contribuyente regularice su situación con AGIP.  
También, un mismo CUIT puede hallarse al mismo tiempo en los padrones de "exentos y alícuotas diferenciales" y de "magnitudes superadas" en el mismo período. Se agregará la alícuota del padrón de magnitudes superadas hasta tanto el contribuyente normalice su situación con AGIP.  
Un mismo CUIT puede encontrarse al mismo tiempo en los padrones de "alto riesgo fiscal" y de "régimen general" en el mismo período. En ese caso, el porcentaje de alícuota predominante para ese contribuyente será la alícuota que corresponda al padrón de riesgo fiscal.  
Un mismo CUIT puede encontrarse al mismo tiempo en los padrones de "exentos y alícuotas diferenciales" y de "régimen general" en el mismo período. En ese caso, el porcentaje de alícuota predominante para ese contribuyente será la alícuota que corresponda al padrón de exentos y alícuotas diferenciales.  
Un mismo CUIT puede hallarse al mismo tiempo en los padrones de "magnitudes superadas" y de "régimen general" en el mismo período. Se agregará la alícuota del padrón de magnitudes superadas como porcentaje de alícuota predominante.

##### Contenidos relacionados

No se ha encontrado ninguno
