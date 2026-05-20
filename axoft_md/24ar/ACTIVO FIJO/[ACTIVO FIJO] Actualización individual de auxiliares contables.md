# Actualización individual de auxiliares contables

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Activo Fijo
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_afa/guia_administracionbienes/?p=11827/

## Contenido

# Actualización individual de auxiliares contables

Este proceso habilita los tipos de [auxiliares contables](?p=11835) por cuenta, para la apertura de los importes de los movimientos en subimputaciones.

Cuenta: seleccione una [cuenta contable](?p=11850). Para más información, consulte el ítem [Selección de una cuenta contable](?p=11882/#definiciones-previas). El sistema valida que la cuenta elegida esté habilitada y use auxiliares contables.

Información del detalle de tipos de auxiliares: la grilla está compuesta por dos sectores: Tipo de auxiliar y Regla de apropiación por defecto.

Código y Descripción del tipo de auxiliar: estos campos no son editables en renglones existentes de la grilla.

Origen: esta columna no se puede modificar, indica si el tipo de auxiliar es de origen 'Manual' o 'Automático'.

Subauxiliares: esta columna no se puede modificar, indica si el tipo de auxiliar tiene apertura en subauxiliares.

Edita regla: si elige la opción 'N', debe seleccionar una regla de apropiación por defecto. Caso contrario, la elección de la regla de apropiación por defecto es opcional. Para los tipos de auxiliares automáticos este dato siempre es 'N' y no podrá ser modificado.

Apropiación 100%: indica si se valida, en el ingreso de asientos, que el importe del movimiento contable se apropie en forma total.

Auxiliares: es posible indicar a la relación cuenta - tipo auxiliar si maneja apropiaciones en todos los auxiliares definido, o bien sólo para una selección. Este detalle se habilita cuando el tipo de auxiliar es de origen 'Manual'.

Esta configuración se utiliza en los asientos del módulo Contabilidad y desde los módulos Ventas, Compras, Tesorería y Activo Fijo cuando no se aplique una regla de apropiación.

**Validaciones que realiza el sistema**

Si usted agrega o elimina un tipo de auxiliar para la cuenta contable, y si la cuenta contable posee asientos generados en los módulos Activo Fijo, Compras, Contabilidad, Sueldos, Tesorería, Ventas y Liquidador de IVA el sistema actualiza esta información para la relación cuenta - tipo auxiliar. Antes de empezar la grabación de datos, el proceso mostrará una pantalla con el resumen de las modificaciones a realizar en cada módulo y para cada proceso involucrado.

__Nota

Se recomienda que antes se ejecutar este proceso, realice una copia de seguridad de la empresa.

Tenga en cuenta que para poder mantener la consistencia de los asientos generados en cada uno de los módulos, las fechas de cierre deben estar en blanco o ser menores a la fecha de los asientos a modificar. El proceso en este aspecto es estricto y no le permite seguir adelante con la actualización.  
Si elimina un tipo de auxiliar para una cuenta contable, en los asientos generados se eliminará no sólo el tipo de auxiliar sino también las apropiaciones relacionadas con la cuenta contable.  
Si en cambio, agrega un tipo de auxiliar para la cuenta contable, el proceso agrega el 100% de la apropiación al auxiliar/subauxiliar 'SinAsignar' para la cuenta contable y el tipo de auxiliar que se está agregando.  
El sistema solicita su confirmación más de una vez para continuar.

##### Contenidos relacionados

  * [Videos sobre asientos contables en Sueldos](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/asientocontabl_sua_vid/)

  * [Videos sobre auxiliares contables y contabilidad por proyectos](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/conproyectos_cna_vid/)
