# Guía de Punto de Venta sobre RG 3711/15

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv2/guia_rg3711_gv2/

## Contenido

# Guía de Punto de Venta sobre RG 3711/15

Con el fin de cumplimentar las disposiciones establecidas por la RG 3711/15, referida a la Determinación del IVA según la actividad declarada; se requiere parametrizar la base de datos como se detalla a continuación.

Siga los siguientes pasos para configurar el circuito completo.

##### Puesta en marcha

**Única actividad**

Si la empresa desarrolla una única actividad:

  1. Defina la actividad principal -en la solapa Más Datos\- del menú [Datos de la Empresa](?p=11851).
  2. Asigne la actividad económica en cada uno de los artículos. Este campo estará disponible en la solapa [Datos Legales](https://ayudas.axoft.com/25ar/articulo_carp_st), sección AFIP-Siap.  
Recuerde que este dato puede actualizarlo mediante el proceso [Actualización masiva de artículos](?p=17026).  
En caso de no tenerlo completo, asumirá la actividad que fue definida como principal en el punto anterior.
  3. Complete la actividad económica en aquellos los tipos de comprobantes de generación automática. Por ejemplo: diferencias de cambio, comprobantes de ajuste, interés por mora y descuento / recargo por fecha alternativa.  
Este dato lo encontrará en la solapa Principal de [Tipos de Comprobantes](https://ayudas.axoft.com/25ar/tipocomprobante_gv2), en la sección AFIP-SIAp.



**Múltiples actividades**

Si la empresa desarrolla una más de una actividad:

  1. Defina la actividad principal -en la solapa Más Datos\- del menú [Datos de la Empresa](?p=11851).  
Complementariamente, en la solapa Otras actividades; consigne cada una de las actividades complementarias que se desarrollan en su empresa.
  2. Asigne la actividad económica en cada uno de los artículos. Este campo estará disponible en la solapa [Datos Legales](https://ayudas.axoft.com/25ar/articulo_carp_st), sección AFIP-SIAp. Sólo podrá seleccionar alguno de los valores definidos en [Datos de la Empresa](?p=11851) (solapa Más datos y Otras actividades).  
Recuerde que este dato puede actualizarlo mediante el proceso [Actualización masiva de artículos](?p=17026).  
En caso de no tenerlo completo, asumirá la actividad que fue definida como principal en el punto anterior.
  3. Complete la actividad económica en aquellos los tipos de comprobantes de generación automática. Por ejemplo: diferencias de cambio, comprobantes de ajuste, interés por mora y descuento / recargo por fecha alternativa.  
Este dato lo encontrará en la solapa Principal de [Tipos de Comprobantes](https://ayudas.axoft.com/25ar/tipocomprobante_gv2), en la sección AFIP-SIAp.  
Sólo podrá seleccionar alguno de los valores definidos en [Datos de la Empresa](?p=11851) (solapas Más datos y Otras actividades).



##### Generación de información para F2002

La parametrización sugerida, le permitirá obtener información para completar el formulario F2002.

  * Para emitir el reporte sobre sus ventas, ingrese a Informes - Archivos DGI - Informes para F2002 - IVA por Actividad.
  * Para emitir el reporte sobre sus compras, ingrese a Informes - Archivos DGI - Informes para F2002.



Para mayor información sobre el los alcances del proceso, le sugerimos consultar [Informes para F2002 - IVA por Actividad](?p=21480/#informacion-para-f2002-iva-por-actividad).
