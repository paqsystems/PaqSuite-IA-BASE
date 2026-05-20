# Herramientas para integración contable

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_integrcont_gla/?p=11936/

## Contenido

# Herramientas para integración contable

Este asistente lo ayuda a definir el módulo contable a utilizar por los módulos Compras, Ventas y Tesorería.

En los siguientes ítems explicamos cada una de las operaciones disponibles en esta herramienta.

**Módulo contable a utilizar  
**Si ingresó a este proceso es para migrar la información contable de los módulos comerciales (Ventas, Compras, Tesorería, etc.) al módulo Contabilidad.

__Importante. Leer antes de ejecutar este proceso

Este proceso completa toda la configuración necesaria para poder trabajar con la nueva integración contable, tomando los datos de la configuración contable de cada módulo comercial y migrándolos al formato utilizado por **Contabilidad**.  
Una vez finalizado este proceso, debe salir del sistema y volver a ingresar para poder acceder a las nuevas opciones de menú relacionadas con la integración contable. Es importante que además de salir del menú principal, cierre el servidor de accesos.  
Tenga en cuenta que si para definir nuevos auxiliares contables, reglas de apropiación y tipos de asientos, debe utilizar el módulo **Procesos generales**. Tenga en cuenta que también puede crear los datos básicos de una cuenta contable desde el mencionado módulo.

**Recomendaciones previas al cambio de módulo contable**

  * Lea la [guía de implementación y operación](?p=11899) que se encuentra en la ayuda del módulo Procesos generales. Esta guía está orientada a detallar cómo es la nueva forma de trabajo, las nuevas opciones menú y mejoras que ofrece este tipo de integración. Le recomendamos conocer la nueva operatoria en una empresa de prueba (le sugerimos utilizar un backup de la empresa con la que trabaja habitualmente).
  * Si realiza el cambio de módulo para poder consultar un subdiario (en los módulos comerciales) ya sea de un periodo en particular o del ejercicio actual, deberá generar o migrar los asientos de los comprobantes ya contabilizados como los no contabilizados con la vieja Contabilidad. Para eso puede ejecutar este mismo proceso utilizando la segunda opción Migrar o generar asientos de los módulos.
  * Ejecute este proceso cuando los usuarios no estén trabajando, ya que puede demorar varios minutos dependiendo de la información contable a migrar.
  * Tenga en cuenta que anteriormente ejecutó el proceso de migración a Contabilidad y lo vuelve a ejecutar nuevamente, se perderán los datos anteriormente migrados.



**Migrar o generar asientos de los módulos  
**Esta opción se habilita si usted integra con el módulo Contabilidad.  
Permite migrar los asientos de Compras generados en Tango y permite generar los asientos de los módulos Ventas y Tesorería.  
Por defecto se propone la fecha del ejercicio actual de Contabilidad o el año actual, es posible modificar esta fecha.  
Cada vez que se ejecute esta operación se perderá la información anteriormente migrada o generada.  
Le recomendamos que revise los datos contables de la parametrización contable antes de ejecutar este proceso.  
Al ejecutar la opción de módulo a utilizar cuando cambia de Tango a Tango Astor, le permite ejecutar en el mismo paso la operación migrar o generar asientos de los módulos. Si usted posee gran volumen de información es conveniente ejecutar estas operaciones por separado.

##### Contenidos relacionados

  * [Guía sobre integración contable desde Procesos generales](https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_integrcont_gla/)

  * [Jerarquías de plan de cuentas](https://ayudas.axoft.com/25ar/ayudas/cna/archivos_carp_cna/cuentas_cna/jerarquas_cna/)
