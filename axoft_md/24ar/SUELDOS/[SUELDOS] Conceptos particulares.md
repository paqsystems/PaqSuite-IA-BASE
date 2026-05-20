# Conceptos particulares

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sua/guia_puestamarcha_sua/?p=13036/

## Contenido

# Conceptos particulares

Puede asociar determinados conceptos de liquidación a un legajo de sueldos. Llamamos concepto a todo ítem que interviene en una liquidación.

__Nota

Los conceptos particulares intervienen siempre en liquidaciones futuras, no intervienen en liquidaciones ya realizadas.  


Este grupo de conceptos asociados se define como conceptos particulares del legajo y son evaluados en el momento de liquidar el legajo, lo que evita que sean ingresados cada vez que se liquide.  
Los conceptos particulares pueden tener definidos rangos de fechas de vigencia de aplicación.  
Es posible especificar sólo la Fecha Desde, sólo la Fecha Hasta, ambas fechas o bien, ninguna. Si las dos fechas quedan en blanco, el concepto se liquidará siempre. De otro modo, el concepto se liquidará evaluando las vigencias parciales; es decir, siempre que haya intersección entre el rango de fechas de la liquidación y el rango de fechas del concepto.

Gráficamente  
Suponiendo que los datos fijos contienen la siguiente información:

_Fecha de liquidación: 28/08/2026_  
_Desde: 01/08/2026_  
_Hasta: 30/08/2026_

En este caso el concepto se liquida para esta liquidación.  
Para su mejor comprensión, presentamos dos casos en los que el concepto automático no se liquida:

CASO 1:

CASO 2:

En los procesos [Liquidación de conceptos individual](?p=13156) y [Liquidación de conceptos global](?p=13167), cuando liquide con la opción Conceptos a procesar Particulares, Sueldos evalúa el conjunto de conceptos particulares asociados al legajo, validando si el concepto está habilitado para el tipo de la liquidación del dato fijo y validando fechas de vigencia contra las fechas Desde y Hasta de la liquidación en curso.

Más información:

Tenga en cuenta que no es posible asociar a un legajo, conceptos de tipo _[axvar variable=gan_impunico]_ (_Tipo 5-Retención de ganancia_ y _Tipo 6-Devolución de ganancia_), puesto que éstos son generados automáticamente desde el proceso Liquidación de conceptos o desde Liquidación de ganancias.

La actualización de conceptos puede realizarse en forma individual para cada empleado, o bien en forma global, si elige un conjunto de conceptos y selecciona el grupo de empleados a los que se asignarán los conceptos elegidos.

##### Contenido dependiente

  * [Actualización individual de conceptos particulares](https://ayudas.axoft.com/24ar/ayudas/sua/archivos_carp_sua/archempl_carp_sua/conceppartic_sua/actindividconcpart_sua/)
  * [Actualización global de conceptos particulares](https://ayudas.axoft.com/24ar/ayudas/sua/archivos_carp_sua/archempl_carp_sua/conceppartic_sua/actglobalconceppart_sua/)
