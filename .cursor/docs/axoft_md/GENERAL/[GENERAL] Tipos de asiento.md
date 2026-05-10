# Tipos de asiento

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_integrcont_gla/?p=11994/

## Contenido

# Tipos de asiento

Defina tipos de asiento de manera que luego, puedan ser agrupados, filtrados y controlados con algún criterio especial.

Todos los asientos pertenecen a un tipo. Los tipos de asiento responden a una clasificación arbitraria, definida por usted. Cuanto más amplia es la definición de tipos de asiento, más específica será la información a analizar.  
La clasificación puede ser tan simple, como tener un tipo de asiento de diario o más particular, como tener un tipo de asiento para cada operación.

**Condiciones para eliminar un tipo de asiento**

  * No es posible eliminar un tipo de asiento utilizado en movimientos de asientos registrados.
  * No es posible eliminar un tipo de asiento utilizado en modelos de asientos para Contabilidad.
  * No es posible eliminar un tipo de asiento reservado para operaciones automáticas.
  * Si el tipo de asiento a eliminar está referenciado en unidades adicionales, monedas o cuentas que usan unidades adicionales (cuentas cotizables), el sistema solicita su confirmación para realizar la operación.



Para más información, consulte las opciones [Unidades adicionales](?p=9824), [Monedas contables](?p=9806) y [Cuentas contables](?p=9774) en el módulo Contabilidad.

##### Principal

Código: ingrese un código que identifique al tipo de asiento. El sistema valida que el código indicado sea único. Su ingreso es obligatorio.

Descripción: indique una descripción para el tipo de asiento. Su ingreso es opcional.

Habilitado: por defecto este parámetro se presenta activado. Destíldelo para inhabilitar el tipo de asiento en pantalla.

Genera asiento resumen: este parámetro está disponible sólo si en el proceso Parámetros de Contabilidad está activo el parámetro Utiliza asiento resumen.  
Si activa este parámetro, el sistema valida que el tipo de asiento no se utilice en operaciones automáticas (cierre, apertura, refundición de cuentas, pasaje a resultados acumulados, ajuste por inflación, resultado por tenencia). Para más información, consulte en la opción Parámetros de Contabilidad, la solapa Tipos de asiento para procesos automáticos.  
Si usted desactiva este parámetro, el sistema valida que no existan asientos analíticos pendientes de generar resumen. En ese caso, genere los asientos resumen correspondientes y vuelva a intentar.

Estado inicial para asientos: es el estado que se asignará a los asientos en el momento de ser ingresados. Los valores posibles son los siguientes: 'Borrador', 'Ingresado' o 'Registrado'. Por defecto, se propone el estado 'Ingresado'. El ingreso de este dato es obligatorio.

Edita estado de los asientos: indique si es posible cambiar el estado de los asientos. Por defecto, este parámetro no está activo.

Agrupación: es posible asignar, de manera opcional, un código de [agrupación de tipos de asiento](?p=11830) para clasificar los tipos de asiento definidos y utilizar esta clasificación en los listados.

##### Módulos

En esta solapa se indican los módulos en los que está habilitado el tipo de asiento.  
Desafecte o destilde el o los módulos para los que no desea habilitar el tipo de asiento.

##### Leyendas

En esta solapa, usted define las leyendas a utilizar para los encabezados de los asientos asociados al tipo de asiento en edición.  
Elija una de ellas como leyenda por defecto.

##### Contenidos relacionados

  * [Video sobre imputación contable Sueldos](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/imputcontsueldos_gral_vid/)

  * [Videos sobre asientos contables](https://ayudas.axoft.com/24ar/videos/cna_carp_vid/asientocontabl_cna_vid/)

  * [Videos sobre parametrización contable](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/paramcontab_gral_vid/)
