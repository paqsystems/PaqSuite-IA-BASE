# Guía sobre actualización de alícuotas de IIBB según AGIP Bs. As.

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_alicuotiibb_gv/

## Contenido

# Guía sobre actualización de alícuotas de IIBB según AGIP Bs. As. 

AGIP genera periódicamente padrones (archivos de texto) conteniendo listados de contribuyentes con ciertas características, y para cada uno se especifican las alícuotas de percepción y retención que se deberá aplicar sobre los Ingresos Brutos, por parte de los agentes de recaudación en cada transacción comercial que se practique con ellos.

Por tal motivo, todos los agentes de retención / percepción de ingresos brutos de la Ciudad de Buenos Aires deben consultar los archivos ASCII emitidos por la autoridad municipal para determinar las alícuotas que deben retener o percibir a sus proveedores o clientes, respectivamente.  
Los padrones se publican en la web de Rentas ([www.agip.gob.ar](http://www.agip.gob.ar)).

__Nota

Recuerde que la tecla rápida <F3> permite realizar la búsqueda de un texto en el árbol de procesos de todos los módulos. Como resultado, se exhibirá el nombre de los procesos que incluyen el texto ingresado, con la indicación del módulo y carpeta en la que se encuentran.

Se recomienda conocer las consideraciones dispuestas por AGIP para los agentes de recaudación del impuesto sobre los ingresos brutos a partir del 01/11/2016. Para más información consulte en el sitio de AGIP este [documento](http://www.agip.gob.ar/filemanager/source/Agentes/De%20Recaudacion/Ingresos%20brutos/Considerac%20de%20AR%20ISIB%20hasta%20Res%20%20486-2016%20AMPLIADO.pdf).

##### Puesta en marcha

A continuación se detallan los pasos a seguir para la asignación de códigos de percepción de ingresos brutos en base al padrón de Rentas.

  1. Decida como prefiere implementar el impuesto a los ingresos brutos en el sistema. Para más información consulte [¿Cómo me conviene implementar las percepciones de ingresos brutos?](https://ayudas.axoft.com/24ar/guia_pm1_alicuotiibb_gv)
  2. Ingrese al proceso [Alícuotas](https://ayudas.axoft.com/24ar/alicuota_gv) o [Percepciones definibles](https://ayudas.axoft.com/24ar/percepcdefin_gv) según lo definido en el punto anterior y complete para cada percepción el campo Grupo AGIP Para más información sobre este campo consulte [Consideraciones sobre el campo Grupo AGIP](https://ayudas.axoft.com/24ar/guia_pm2_alicuotiibb_gv).  
Cada padrón deberá tener dadas de altas las alícuotas de IIBB y los grupos que corresponda para los regímenes alcanzados, es decir que si la empresa está alcanzada por el régimen general y/o el particular de AGIP, deberá tener configuradas las alícuotas propias de cada régimen en el sistema.
  3. Ingrese a la siguiente URL en la web de Rentas para obtener el padrón actualizado de contribuyentes:  
<http://www.agip.gob.ar/agentes/agentes-de-recaudacion-e-informacion>  
Utilice los archivos de los padrones sin modificar los nombres originales que tienen al ser descargados de la página de Rentas de la Ciudad de Buenos Aires.
  4. Copie el padrón en el directorio comunes del servidor (_NombreDelServidorCOMUN#########_ , donde ######### representa el número de llave de su sistema).
  5. Ingrese al proceso [Actualización de alícuotas de IIBB según AGIP Bs.As.](?p=26538) para actualizar el padrón del sistema y los códigos de percepción de ingresos brutos asociados a cada uno de sus clientes.



Tenga en cuenta que también puede clasificar a los clientes desde los procesos [Clientes](https://ayudas.axoft.com/24ar/clientes_carp_gv) , [Clientes potenciales](https://ayudas.axoft.com/24ar/clientepotencial_gv) y [Clientes ocasionales](?p=19271#clientesocasionales). Seleccione "Actualizar según padrones" para asignar en forma automática el código de percepción de ingresos brutos que le corresponda de acuerdo al padrón.  
Para configurar las alícuotas de retenciones de IIBB para AGIP en el módulo Compras, consulte la puesta en marcha de la [Guía de implementación sobre actualización de alícuotas de IIBB según AGIP Bs.As](?p=14406/#puesta-en-marcha).

###### ¿Cómo me conviene implementar las percepciones de ingresos brutos?

Usted puede implementar las percepciones de ingresos brutos mediante alguna de las siguientes opciones:

  * [Alícuotas](https://ayudas.axoft.com/24ar/alicuota_gv): es la forma básica de definir percepciones de ingresos brutos. Aunque cubre la mayor parte de las necesidades de este impuesto posee algunas limitaciones con respecto a las percepciones definibles.
  * [Percepciones definibles](https://ayudas.axoft.com/24ar/percepcdefin_gv): esta opción permite definir distintos tipos de percepciones. Su beneficio radica en su mayor flexibilidad (más bases de cálculo, asignación de alícuotas o bases de cálculo de acuerdo a distintas clases de clientes) y la oportunidad de asociarle un modelo de formato de archivo ASCII para la generación de soportes magnéticos requeridos por la autoridad de aplicación del impuesto.



Importante:

Tenga en cuenta que si decide modificar la forma de implementar percepciones debe modificar la parametrización de ingresos brutos de todos sus clientes y artículos. Por ejemplo, si trabajaba con percepciones asociadas a alícuotas y ahora decide trabajar con percepciones definibles no basta con agregar el código de percepción definible, y su correspondiente alícuota sino que debe indicar 'N' en el campo Percepción ingresos brutos tanto a nivel cliente como artículo; de lo contrario, se liquidará dos veces el impuesto.

###### Consideraciones sobre el campo Grupo AGIP

Para trabajar con los padrones es necesario que asigne ciertos códigos de grupo a las alícuotas de percepción y a los códigos de retención.

  * **Grupo "1":** asigne este valor al código de retención / percepción que representa a la alícuota de porcentaje cero. El código de retención / percepción que tenga asociado este grupo será asignado al proveedor cuando éste figure en el padrón con porcentaje de alícuota en cero, o haya dejado de figurar en el padrón durante el período anterior y no esté presente en los padrones actuales.
  * **Grupo "2" a "99":** asigne este valor al código de retención / percepción que represente a la alícuota del impuesto. El código de retención / percepción que tenga asociado este grupo será asignado al proveedor cuando éste resulte incluido en los padrones.



Códigos de grupos para el padrón régimen general  
Si usted utiliza el padrón de régimen general, asigne los códigos de grupo para alícuotas de percepción de acuerdo a la disposición de AGIP.  
Alícuotas de percepciones:

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
  
Más información:

Si usted realiza una operación alcanzada por este régimen general de Ingresos Brutos con un cliente pasible de percepción y que no esté incluido en el archivo del padrón de régimen general, tendrá que percibir el impuesto aplicando sobre el monto el porcentaje de alícuota del 6,00% (porcentaje puede variar de acuerdo a disposición de AGIP artículo 16 Resolución 421/16).  
Configure este porcentaje en una percepción especial que no está en el archivo del padrón y asigne grupo 0. Mantenga actualizado el porcentaje de esta percepción en forma manual.  
Configure la provincia asociada al padrón de régimen general, para más información consulte el proceso [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-impuestos).

__Nota

Las percepciones del anexo II de la Resolución 364/16 (anexo VII Resolución 939/13) se tendrán que configurar, asignar y mantener de forma manual.

##### Contenidos relacionados

  * [Actualización de alícuotas de IIBB según AGIP Bs. As.](https://ayudas.axoft.com/24ar/ayudas/gv/procperiodico_carp_gv/actaliciibbagipbsas_gv/)

  * [Alícuotas de Ventas](https://ayudas.axoft.com/24ar/ayudas/gv/archivos_carp_gv/actualizacion_carp_gv/alicuota_gv/)

  * [Guía sobre actualización de alícuotas de IIBB según AGIP Bs.As. (Compras)](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp2/guia_actualalicagipbsas_cp2/)

  * [Video sobre regímenes de facturación](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/regfact_gral_vid/)

  * [Videos sobre gestión impositiva](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/gestimpositiva1_gral_vid/)

  * [Videos sobre retenciones y percepciones impositivas](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/retencpercep_gral_vid/)
