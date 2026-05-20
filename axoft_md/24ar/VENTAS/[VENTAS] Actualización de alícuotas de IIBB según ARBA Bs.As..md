# Actualización de alícuotas de IIBB según ARBA Bs.As.

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_alicuotarba_gv/?p=21126/

## Contenido

# Actualización de alícuotas de IIBB según ARBA Bs.As.

Este asistente le permitirá actualizar la alícuota de ingresos brutos que se debe aplicar a cada cliente, teniendo en cuenta el padrón emitido por Rentas de la provincia de Buenos Aires (Disposición Normativa 01/04, modificatorias y complementarias).

Para más información sobre este tema consulte: Régimen de percepción por sujeto (Rentas provincia de Bs.As.)

__Nota

Tenga en cuenta que antes de utilizar por primera vez este asistente debe obtener el padrón de Rentas que corresponda al período en curso.

El sistema utiliza como carpeta por defecto para la lectura del padrón el directorio comunes ubicado en el servidor del sistema (NombreDelServidorCOMUN#########, donde ######### representa el número de llave de su sistema).

__Nota

Sólo es necesario que tilde la opción _Actualizar el padrón del sistema_ cuando obtenga un nuevo padrón generado por Rentas.

Finalmente, seleccione la información que desea consultar al terminar el asistente.

  * Clientes con cambio de alícuota: tilde esta opción para conocer los clientes que cambiaron de grupo de percepción.
  * Clientes no actualizados por no estar incluidos en el padrón: seleccione esta opción para conocer los clientes a los que no se les actualizaron las alícuotas de ingresos brutos por no figurar en el padrón de Rentas. Esta opción esta visible únicamente cuando tenga configurados los impuestos de ARBA con alícuotas comunes.
  * Clientes no actualizados por tener definida una provincia distinta a la asociada al padrón: seleccione esta opción para conocer los clientes a los que no se les actualizaron las alícuotas de ingresos brutos por no coincidir la provincia con la asociada al padrón.
  * Alícuotas de ingresos brutos actualizadas: marque esta opción para visualizar las alícuotas de ingresos brutos cuyo porcentaje fue modificado en base a la información existente en el padrón.
  * Grupos de Rentas no definidos en el sistema: tilde esta opción para conocer los grupos de Rentas no asociados a una alícuota de ingresos brutos del sistema. En caso de existir grupos no asociados a una alícuota es necesario que los defina y vuelva a ejecutar este proceso para actualizar la información de los clientes que pertenecen a dicho grupo.
  * Clientes actualizados con la alícuota especial por estar fuera del padrón: tilde esta opción para conocer los clientes que no están en el padrón de ARBA y que fueron actualizados con el impuesto especial configurado en los [parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv/#parametros-para-padrones) para aquellos clientes estén fuera del padrón de ARBA.



El sistema busca si existe al menos una percepción definible con alguna alícuota que tenga asociada un grupo de ARBA. Si la encuentra, la actualización se hará utilizando sólo percepciones definibles, de lo contrario, la hará utilizando los códigos de impuestos definidos en el proceso [Alícuotas](https://ayudas.axoft.com/24ar/alicuota_gv).  
Si el porcentaje registrado en el padrón de Rentas no coincide con el porcentaje de la alícuota registrada en el sistema, se actualizará dicho porcentaje en base a la información del padrón.  
Para cada cliente que posea CUIT definido y exista en el padrón de Rentas, el sistema actualizará el código de alícuota correspondiente al grupo indicado en el padrón.  
En caso de que no se encuentre una alícuota asociada al grupo de Rentas, no se actualizará la información del cliente. Al parametrizar la actualización por [Alícuotas](https://ayudas.axoft.com/24ar/alicuota_gv), y si el cliente está configurado para que no se le liquiden percepciones de ingresos brutos, pero figura en el padrón de Rentas, el sistema actualizará los datos del cliente para que se le comience a liquidar la percepción.  
Si no tiene configurada una alícuota especial de ARBA para clientes no estén en el padrón, y el cliente no existe en el padrón de Rentas, entonces el sistema lo informará al terminar el asistente. Recuerde que si corresponde que liquide percepciones de ingresos brutos, deberá configurar manualmente la alícuota de percepción que se le deba aplicar.  
Caso contrario, si tiene configurada una alícuota especial a aplicar a clientes que no estén en el padrón, al finalizar el proceso el sistema informará sobre dichos clientes que fueron actualizados con el impuesto especial configurado para estos casos, y liquidará las percepciones de ingresos brutos con el porcentaje configurado en dicha alícuota.

Más información:

Tenga en cuenta que sólo se actualiza la alícuota general correspondiente a la percepción de ingresos brutos del cliente (en modo [Alícuotas](https://ayudas.axoft.com/24ar/alicuota_gv)) o las alícuotas definibles (en modo [Percepciones definibles](https://ayudas.axoft.com/24ar/percepcdefin_gv)). No se actualiza la alícuota adicional ni la alícuota correspondiente a percepciones de la provincia de Bs.As. de acuerdo a la Disposición Normativa 59/98.

##### ¿Qué problemas se pueden presentar en la importación de padrones de ARBA?

Si esta ejecutando el proceso de actualización del padrón de ARBA y se presentan errores durante la actualización del padrón o la actualización de las alícuotas en su empresa se sugiere realizar las siguientes tareas:

  1. Controlar que el padrón se importe directamente como se descargó de la Web del organismo (el archivo no debe ser descomprimido ni modificado).
  2. Revisar los logs del sistema buscando errores alcanzados en los archivos de registro del sistema.
  3. Verificar los permisos del usuario sobre las carpetas comunes que usa el sistema para copiar y descomprimir el archivo conteniendo los datos del padrón.
  4. Verificar que el usuario posea permisos sobre las carpetas comunes que usa el sistema para copiar y descomprimir el archivo que contiene los datos del padrón.
  5. Revisar las características del entorno de ejecución del proceso, algunos de los aspectos que pueden generar problemas en la importación son:  
• Verificar la existencia de suficiente espacio disponible en la ubicación donde se almacena físicamente el MSSQLServer.  
• Verificar que las propiedades Maxisize de los archivos .MDF y .LOG la base de datos de la empresa se encuentren configurados como Unlimited.  
• Verificar la performance del servidor, la ejecución de otros procesos que pudieran ejecutarse en paralelo con la actualización del proceso de ARBA.



##### Contenidos relacionados

  * [Guía sobre actualización de alícuotas definibles de IIBB según ARBA](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_alicuotarba_gv/)

  * [Videos sobre retenciones y percepciones impositivas](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/retencpercep_gral_vid/)
