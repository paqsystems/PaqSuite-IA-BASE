# Actualización de alícuotas de IIBB según padrón Santa Fe

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_alicuotiibbsantafe_gv3/?p=18476/

## Contenido

# Actualización de alícuotas de IIBB según padrón Santa Fe

Este asistente le permitirá actualizar la alícuota de ingresos brutos que se debe aplicar a cada cliente y a cada proveedor, teniendo en cuenta el padrón emitido por la Administración Provincial de Impuestos (API) de la provincia de Santa Fe (Resolución 37/2025).

Más información:

Antes de utilizar por primera vez este asistente le recomendamos leer la [Guía de implementación de actualización de alícuotas de IIBB según padrón API - Santa Fe](?p=10177).  


**Pasos a seguir para actualizar las alícuotas**

  1. Obtenga el padrón a utilizar desde API.
  2. Ingrese a este asistente y tilde las opciones: 
     * **Actualizar el padrón de Santa Fe - Régimen general:** este paso sólo es necesario cuando obtenga un nuevo padrón.
     * **Actualizar alícuotas de clientes:** este paso sólo es necesario cuando desee aplicar la alícuota de percepción de ingresos brutos a las direcciones de entrega de cada cliente habitual y/o potencial.
     * **Actualizar alícuotas de proveedores:** este paso sólo es necesario cuando desee aplicar la alícuota de retención de ingresos brutos a cada proveedor.
  3. Seleccione el archivo .zip desde su directorio. Solo disponible si tildó Actualizar el padrón de Santa Fe - Régimen general.
  4. Visualice los filtros aplicados.
  5. Visualice los resultados que se mostrarán en el archivo que se generará por la actualización de alícuotas de clientes. Solo disponible si tildó Actualizar alícuotas de clientes. 
     * **Clientes con alícuotas del padrón:** listado de clientes que fueron actualizados con la alícuota de percepción correspondiente según padrón.
     * **Clientes no incluidos en el padrón:** listado de clientes no incluidos en el padrón que fueron actualizados con la alícuota de percepción correspondiente según configuración general.
     * **Alícuotas de percepción de ingresos brutos actualizadas:** listado de alícuotas de ingresos brutos cuyo porcentaje fue modificado en base a la información existente en el padrón.
     * **Grupos API - Santa Fe no definidos en percepciones:** listado de grupos no asociados a una alícuota. Es necesario que los defina y vuelva a ejecutar este proceso para actualizar la información de los clientes que pertenecen a dicho grupo.
  6. Visualice los resultados que se mostrarán en el archivo que se generará por la actualización de alícuotas de proveedores. Solo disponible si tildó Actualizar alícuotas de proveedores. 
     * **Proveedores con alícuotas del padrón:** listado de proveedores que fueron actualizados con la alícuota de retención correspondiente según padrón.
     * **Proveedores no incluidos en el padrón:** listado de proveedores no incluidos en el padrón que fueron actualizados con la alícuota de retención correspondiente según configuración general.
     * **Alícuotas de retención de ingresos brutos actualizadas:** listado de alícuotas de ingresos brutos cuyo porcentaje fue modificado en base a la información existente en el padrón.
     * **Grupos Santa Fe no definidos en retenciones:** listado de grupos no asociados a una alícuota. Es necesario que los defina y vuelva a ejecutar este proceso para actualizar la información de los proveedores que pertenecen a dicho grupo.
  7. Haga clic en el botón "Terminar".



**¿Cómo se actualizan las alícuotas asociadas a cada cliente?**

El sistema verifica si el CUIT del cliente se encuentra en el padrón.

  * **Si el cliente está en el padrón:** se toma la alícuota del padrón y se actualiza el porcentaje en la percepción definible de ingresos brutos de Santa Fe. Según el criterio definido en el proceso [Parámetros de Ventas](?p=19401/#padrones-agip) la alícuota se actualiza en todas las direcciones de entrega del cliente o únicamente en aquellas ubicadas en la provincia de Santa Fe.
  * **Si el cliente no está en el padrón:** se evalúa si corresponde aplicar la alícuota general definida en el proceso [Parámetros de Ventas](?p=19401/#padrones-agip). En este caso, la actualización se realiza según el criterio configurado.



__Nota

En el caso de clientes potenciales, la actualización se realiza en función de la provincia de entrega informada. Si la provincia corresponde, se actualizan las percepciones definibles.  


__Nota

En la percepción definible de ingresos brutos de Santa Fe solo se actualizan los grupos necesarios según las alícuotas informadas en el padrón. Por ejemplo, si la percepción tiene definidos 23 grupos y el padrón informa 21 alícuotas, solo se actualizan los primeros 21 grupos.  


**¿Cómo se actualizan las alícuotas asociadas a cada proveedor?  
**El sistema verifica si el CUIT del proveedor se encuentra en el padrón.

  * **Si el proveedor está en el padrón:** se toma la alícuota del padrón y se actualiza el porcentaje en la retención de tipo 'Otras' correspondiente a ingresos brutos de Santa Fe.
  * **Si el proveedor no está en el padrón:** se evalúa si corresponde aplicar la alícuota general definida en el proceso [Parámetros de Compras](?p=14676). En ese caso, la actualización se realiza según el criterio configurado.



__Nota

En la retención de tipo 'Otras' solo se actualizan los grupos necesarios según las alícuotas informadas en el padrón. Por ejemplo, si la retención tiene definidos 23 grupos y el padrón informa 21 alícuotas, solo se actualizan los primeros 21 grupos.  


##### Contenidos relacionados

  * [Guía sobre actualización de alícuotas de IIBB según padrón de Santa Fe](https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_alicuotiibbsantafe_gv3/)
