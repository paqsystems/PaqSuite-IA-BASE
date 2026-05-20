# Guía sobre comparación de comprobantes con Mis comprobantes AFIP

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_cp2/guia_miscomprobantesafip_cp2/

## Contenido

# Guía sobre comparación de comprobantes con Mis comprobantes AFIP

Esta guía lo ayudará ha comparar comprobantes recibidos en la AFIP con los ingresados en el módulo Compras, con el objetivo de detectar comprobantes pendientes de registrar y comprobantes con diferencias en la fecha de ingreso o en el importe total.

##### Puesta en marcha

Para poder cruzar la información de los comprobantes que están declarados en la AFIP con los comprobantes que usted tiene en el módulo Compras debe realizar los siguientes pasos:

  1. **Parámetros de Compras:** active el parámetro Muestra comprobantes AFIP pendientes de registrar para habilitar la opción de menú Comprobantes AFIP a fin de consultar los comprobantes pendientes desde el ingreso de facturas, notas de crédito y notas de débitos.
  2. **Perfiles de factura de compras:** si en la empresa utilizan perfiles de facturación, debe activar en los perfiles que corresponda el parámetro Muestra comprobantes AFIP pendientes de registrar para habilitar para cada perfil la posibilidad de acceder a la opción de menú Comprobantes AFIP durante el ingreso de facturas de compras.



##### Detalle del circuito

Para realizar la comparación entre los comprobantes que tiene registrados en la AFIP y los comprobantes cargados en el sistema debe realizar los siguientes pasos:

  1. Ingrese a la web de AFIP con clave fiscal y acceda a la aplicación Mis comprobantes, seleccione Comprobantes recibidos para realizar una consulta de los comprobantes recibidos y descargarlos en una planilla Excel.
  2. En el sistema, acceda al proceso Compras | Procesos periódicos | Mis comprobantes AFIP y realice la importación de la planilla Excel que se descargó de AFIP o que generó manualmente. Seleccione los comprobantes a incluir y continúe.
  3. En este paso, el sistema realizará la comparación de los datos entre ambos sistemas y como resultado del procesamiento mostrará un listado de comprobantes agrupado y ordenado por estado y fecha de emisión, conteniendo todos los comprobantes analizados de la planilla Excel y mostrando el estado actual en el sistema.  
Al mostrar el listado de comprobantes, el proceso marca como seleccionados los comprobantes pendientes de registrar y los comprobantes con diferencia en la fecha y/o en el monto, dejándolos disponibles en la consulta en el ingreso de comprobantes.  
Los comprobantes que están registrados en el sistema, de forma predeterminada aparecen sin seleccionar, y al presionar el botón "Actualizar" serán eliminados del proceso, preservando solo aquellos comprobantes que utilizará en el ingreso de comprobantes, o que necesite para realizar algún seguimiento.



Durante el ingreso de facturas, notas de créditos y notas de débito puede consultar los comprobantes que están en la AFIP que faltan registrar en el sistema, para ello seleccione en la barra de menú la opción Comprobantes AFIP (o <Ctrl + F11>).

Para consultar y buscar información de Mis comprobantes AFIP:

  1. Diríjase a Compras | Procesos periódicos | Mis comprobantes AFIP.
  2. En Configuración del procesamiento de la información, seleccione la opción 'Consultar comprobantes' y elija el estado de los comprobantes a incluir.
  3. En la Selección de comprobantes puede ingresar los criterios de búsqueda a aplicar.  
Si no ingresa ningún criterio, el proceso le mostrará el listado conteniendo todos los comprobantes existentes en proceso.
  4. El proceso mostrará el listado de comprobantes clasificado, agrupado y ordenado por estado, considerando los criterios seleccionados.



##### Contenidos relacionados

  * [Mis comprobantes AFIP](https://ayudas.axoft.com/25ar/ayudas/cp2/procesoperiodico_carp_cp2/miscomprobafip_cp2/)

  * [Video sobre Mis comprobantes AFIP](https://ayudas.axoft.com/25ar/videos/cp2_carp_vid/miscomprobantesafip_cp2_vid/)
