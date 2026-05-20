# Reglas de apropiación habituales

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_integrcont_gv/?p=12997/

## Contenido

# Reglas de apropiación habituales

##### Actualización individual de reglas de apropiación habituales

En este proceso puede ingresar individualmente, el detalle de auxiliares contables a asociar a un legajo, para ser tenido en cuenta en la generación de asientos contables.

Se generarán los auxiliares contables y los porcentajes definidos para el legajo, que estén habilitados para la cuenta del movimiento del asiento. Aquellos que estén en la regla y no estén habilitados se descartan en la generación de asientos.

Tenga en cuenta que si desea modificar el "Tipo de regla" de un auxiliar contable de "Manual" a "Otra regla", deberá eliminar el mismo y agregarlo nuevamente seleccionando la opción que corresponda.

**Ejemplo...**

En el módulo Procesos generales por cada cuenta contable del modelo de asiento se tiene una configuración general. Recuerde que si al generar un asiento no se encuentra la configuración de auxiliares particular del legajo, el sistema buscará la configuración general de los auxiliares para la cuenta. Para más información consulte [Actualización individual de auxiliares contables](?p=11827).

En este ejemplo, se consulta la cuenta contable Sueldos y Jornales a Pagar del modelo de asiento de sueldos.

En el módulo Sueldos se configura para el legajo 1 la siguiente regla: 'Manual' para el tipo de auxiliar **CCOSTO**.

En el momento de generar los asientos contables de Sueldos y en el caso de no haber definido apropiaciones habituales u ocasionales para algún legajo, se tomará la configuración general de la cuenta contable.

##### Actualización global de reglas de apropiación habituales

Actualice los auxiliares contables en forma masiva, para un grupo de legajos de sueldos, automatizando el control sobre grupos de legajos de similares características de generación de asientos de liquidación.

Modalidad de actualización: este tipo de actualización le permite elegir la modalidad a aplicar. Las opciones posibles son: 'Agregar', 'Eliminar' o 'Reemplazar' los auxiliares contables para los legajos seleccionados.

##### Contenidos relacionados

  * [Videos sobre asientos contables en Sueldos](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/asientocontabl_sua_vid/)
