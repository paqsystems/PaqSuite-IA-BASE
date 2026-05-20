# Guía sobre integración contable desde Procesos generales

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_cp/guia_integrcontabl_cp/?p=11899/

## Contenido

# Guía sobre integración contable desde Procesos generales

A través de esta guía, usted obtendrá los lineamientos necesarios para la implementación de la parametrización contable, reutilizando información del módulo Procesos generales.

Esta configuración será válida para aquellos sistemas que se integran con el módulo Contabilidad, y puede abarcar los siguientes módulos: Activo Fijo, Compras, Ventas, Sueldos, Tesorería y CashFlow.

**Introducción a la integración contable  
**Realizar la integración contable con Tango Astor pone a su disposición utilidades y procesos que optimizan funcionalmente la información de su empresa entre los módulos comerciales, Procesos Generales, Sueldos y Activo Fijo.  
De esta forma los datos ingresados en Procesos Generales son utilizados por los módulos que integran con Contabilidad. Posibilitando entre otros el uso de auxiliares y subauxiliares, los que se utilizan para clasificar la información contable según distintos criterios de agrupación por ejemplo: Centros de costo, Proyectos, etc.  
Integrando sus módulos con Contabilidad puede obtener información contable gracias a la trazabilidad con que cuenta en esta versión, es decir desde los módulos consultando desde la consulta Live de Contabilización de comprobantes, podrá ver los asientos ingresados a Contabilidad, o desde el asiento contable consultando el detalle de comprobantes.  
En esta guía usted encontrará una descripción de las funcionalidades que se suman al realizar dicha integración, contemplando los nuevos cambios que aporta la versión y los posibles escenarios en los cuales su empresa puede encontrarse.

**¿Qué funcionalidades se obtienen al integrar con el módulo Contabilidad?**

  * Utilizar los [auxiliares y subauxiliares](?p=11835) definidos en Contabilidad desde los módulos comerciales.
  * Definir y trabajar con auxiliares automáticos, evitando así la necesidad de definir cuentas por artículos, clientes, proveedores y legajos.
  * Optar por generar asientos para los módulos Ventas, Compras y Tesorería junto al comprobante, o hacerlo en forma diferida (*).
  * Consultar o modificar en el propio módulo los asientos ya generados utilizando el proceso Modificación de comprobantes.
  * Obtener información contable desde los propios módulos de Ventas, Compras y Tesorería.
  * Exportar asientos a Contabilidad en una sola operación. La exportación de asientos se encargará de grabar los asientos en Contabilidad sin necesidad de ejecutar la importación.
  * Obtener información de trazabilidad desde los asientos registrados en Contabilidad. Desde cada asiento (incluyendo asientos resumen) se podrá conocer sus comprobantes relacionados.
  * Clasificar los asientos generados mediante un tipo de asiento.
  * Para los asientos el estado 'Contabilizado' es reemplazado por dos valores posibles: 
    * Asiento generado: cuando el comprobante tiene un asiento generado al ingreso del mismo o en forma diferida.
    * Asiento exportado: cuando el asiento ya fue exportado a la contabilidad.



(*) No disponible para los módulos **Ventas Restô** ni para el módulo **Ventas Punto de Venta** , que si bien podrán utilizar auxiliares siguen generando sus asientos en forma diferida.

##### Detalle del circuito

En este esquema de describe el flujo de información, que nace con el ingreso de los comprobantes de las distintas operaciones en los módulos, pasando por la generación y exportación de asientos, hasta llegar a Contabilidad, al que se podrá acceder desde la solapa del comprobante de Live.

**Primer escenario:**

  * Generación de asientos junto con el ingreso de comprobante
  * Exportación de asiento a Contabilidad a la misma base de datos.



**Segundo escenario:**

  * No existe generación de asientos con el ingreso del comprobante.
  * Generación de asientos contable.
  * Exportación de asientos a Contabilidad a la misma base de datos.



**Tercer escenario:**

  * Generación de asientos junto al ingreso de comprobante.
  * Exportación de asiento a Contabilidad a otra base de datos.
  * Importación de asiento a Contabilidad.



**Cuarto escenario:**

  * No hay generación de asientos con el ingreso del comprobante.
  * Generación de asientos contables.
  * Exportación de asientos a Contabilidad a otra base de datos.
  * Importación de asiento a Contabilidad.



De esta manera, usted puede obtener información contable desde el módulo Contabilidad a través del detalle de comprobantes del asiento contable, y desde allí acceder a la solapa del comprobante del módulo comercial en Tango Live. O puede acceder al asiento importado en el módulo Contabilidad desde del módulo comercial, a través de la consulta Contabilización de comprobantes de Tango Live.

__Nota

El circuito contable es prácticamente igual para todos los módulos que pueden generar asientos contables.  


Al ingresar un comprobante en cualquiera de los módulos mencionados, si el mismo está habilitado para generar asiento, puede generarlo en el ingreso del comprobante o luego desde el proceso masivo de generación de asientos.  
Luego del ingreso de comprobante, y en caso de tener los permisos necesarios, aparecerá la pantalla del asiento del comprobante.  
A continuación se muestra un ejemplo de factura de proveedores:

En ese momento usted puede consultar esta información desde la consulta o modificación de comprobantes, desde el subdiario de asientos, desde las consultas Live de contabilidad o desde la solapa Tango Live de comprobantes.  
El asiento generado del comprobante quedará almacenado en el módulo. Para transportar esta información a contabilidad debe realizar una exportación de asientos. Usted tiene dos posibilidades:

  * Si posee el módulo Contabilidad puede optar por transportarlos a la misma base de datos, con lo cual la importación en contabilidad es automática;
  * Puede trasportarlos a otra base de datos. En este caso, se generará un archivo ZIP que deberá ser importado desde el proceso Importación de asientos en la llave correspondiente.



En el caso de agrupar más de un comprobante por asiento exportado, viajará junto con el asiento el detalle de esos comprobantes. Usted puede consultar esta información desde el asiento de contabilidad, en la solapa Comprobantes.  
Cuando los módulos comerciales y el módulo Contabilidad se encuentran en una misma empresa, será posible acceder a la solapa Live del comprobante al que corresponde el asiento, a partir de los asientos contables importados.  
Desde la solapa Tango Live usted puede consultar los datos del comprobante y el asiento generado para éste.  
Para obtener más información sobre los circuitos posibles, consulte las guías de implementación para integración contable para cada módulo:

  * Compras
  * Proveedores
  * Ventas
  * Punto de Ventas
  * Tesorería
  * Ventas Restô



##### Puesta en marcha de la integración

Para poder empezar con la configuración en cada módulo, previamente debe realizar algunas definiciones obligatorias:

  * Si usted no posee el módulo Contabilidad entonces puede crear [cuentas contables](?p=11850) desde el módulo Procesos generales. Una vez creada la cuenta, puede habilitarla sólo para los módulo que necesiten utilizarla.
  * Puede definir si en la cuenta va utilizar apertura en [auxiliares contables](?p=11835). Las aperturas sirven para clasificar la información contable según distintos criterios de agrupación, como por ejemplo: Centros de costo, Proyectos, Canal de ventas, etc. Las mismas pueden tener hasta dos niveles de agrupación, las de primer nivel se llaman auxiliares y las de segundo nivel subauxiliares (*).
  * Los auxiliares contables pueden ser de origen manual o de origen automático. La diferencia entre ambos reside en que este último se completa en forma automática con información suministrada por la operación o el movimiento. Los auxiliares automáticos en el sistema pueden ser: 'Legajos', 'Clientes', 'Proveedores' y 'Artículos'.
  * A los auxiliares de origen manual, usted puede asociarles una [regla de apropiación](?p=11974). Esto permitirá completar los auxiliares por medio de una distribución de porcentajes. La aplicación de la regla aplica el porcentaje al importe del movimiento.
  * Una vez definidas todas las cuentas y todos los auxiliares contables, usted debe relacionarlos accediendo al proceso [Actualización individual de auxiliares contables](?p=11827).
  * Otro dato importante que debe definir para la generación de asientos desde los módulos, son los [tipos de asientos](?p=11994). Estos forman parte del encabezado del asiento a generar y sirven para agrupar y/o filtrar información similar desde los procesos, consultas e informes (desde el módulo de Contabilidad). También debe habilitar el tipo de asiento según el módulo.



**(*) Ejemplo...  
**Tomemos en cuenta el caso de un tipo de auxiliar llamado "Bienes" con dos niveles, en que podemos tener definidos los auxiliares "Muebles y útiles", "Rodados", "Inmuebles", etc. Para el auxiliar "Muebles y útiles" tenemos los subauxiliares 'Escritorio' y 'Silla' , en "Rodados" tenemos los subauxiliares 'Sedan 5 puertas' y 'Camioneta', etc. Por cada compra de bienes realizadas se apropiará el importe del movimiento según una asignación manual.

Tomemos en cuenta otro caso: un tipo de auxiliar llamado "Canal de ventas" con dos niveles, en que tenemos definido los auxiliares "Zona norte" y "Zona sur", y para el auxiliar "Zona norte" tenemos los subauxiliares 'Vicente López' y 'San Isidro', y en la "Zona sur" tenemos los subauxiliares 'Quilmes' y 'Avellaneda'. Por cada venta realizada se apropiará el importe del movimiento según una asignación manual.

**Consideraciones generales  
**El objetivo de este tópico es el de asistir a usuarios que utilizaban la integración contable con Contabilidad de versiones anteriores o que comienzan a utilizar la integración contable con Contabilidad.  
A continuación desarrollaremos los distintos escenarios posibles que se pueden presentar para los usuarios de Contabilidad que operan con los módulos comerciales (Ventas, Compras, Tesorería, etc.) y necesitan contabilizar información.

__Nota

Si va a contabilizar su información a través del módulo **Contabilidad** , le recomendamos la lectura de las siguientes consideraciones de implementación para una correcta integración de datos.

Los módulos comerciales se integran con Contabilidad de la siguiente manera:

  * Para generar asientos a contabilizar.
  * Para incorporar en Contabilidad los asientos generados por los módulos.
  * Para indicar y validar cuentas, auxiliares, reglas y tipos de asientos en los diferentes procesos del sistema que utilizan estas funcionalidades.



A continuación mencionamos los diferentes escenarios de integración y cómo debe proceder para integrar los módulos Tango (pertenecientes a su sistema Gestión, Punto de Venta, Estudios contables o Restô.

###### Integración de los módulos con Contabilidad

Esta documentación está dirigida a los usuarios de Tango Astor que operan módulos comerciales (Ventas, Compras, Tesorería etc.) y necesitan contabilizar información.  
Usted puede integrar sus módulos Tango (Ventas, Ventas Restô, Compras / Proveedores, Tesorería, etc.) con Contabilidad.

__Nota

Si elige contabilizar su información a través del módulo **Contabilidad** , recomendamos la lectura de las siguientes consideraciones de implementación para una correcta integración de datos.

Los módulos comerciales se integran con Contabilidad de la siguiente manera:

  * Para generar los asientos a contabilizar.
  * Para incorporar en Contabilidad los asientos generados por los módulos.
  * Para indicar y validar cuentas, auxiliares y subauxiliares en los diferentes procesos del sistema que utilizan esta funcionalidad.



A continuación, mencionamos los diferentes escenarios de integración y cómo debe proceder para integrar los módulos Tango (pertenecientes a su sistema Gestión, Punto de Venta o Estudios Contables) con Contabilidad.

###### Escenarios de integración

Teniendo en cuenta la nueva integración pueden presentarse las siguientes situaciones.

Sus módulos Tango y el módulo Contabilidad están en una misma base de datos  
En este caso, lleve a cabo los siguientes pasos:

  1. Ejecute el proceso [Herramientas para integración contable](?p=11936) y seleccione el módulo contable de Tango Astor Se ejecutará el proceso de migración de para traspasar la configuración contable. Leer atentamente las recomendaciones antes de continuar.
  2. Al presionar "Terminar", el sistema quedará automáticamente integrado, compartiendo [cuentas contables,](?p=11850) [auxiliares contables,](?p=11835) [reglas de apropiación](?p=11974) y [tipos de asientos](?p=11994) creados en el módulo Procesos generales.
  3. Usted puede generar información contable con formato Tango Astor y exportar los asientos contables a la misma base de datos (la importación será automática).



Para más información sobre este escenario vea la [Guía de Integración contable](?p=11899).

Sus módulos Tango y el módulo Contabilidad están en bases de datos diferentes  
En este escenario, la contabilidad se registra en otra instalación. Pueden presentarse los siguientes casos:

  * Usted no posee el módulo contable pero genera asientos para una instalación externa.
  * Usted posee el módulo contable pero exporta la información a otra instalación externa.



En los dos casos mencionados, lleve a cabo los siguientes pasos, según sea el caso:

  1. El encargado de operar el módulo Contabilidad (su estudio contable, su casa central, etc.) debe ejecutar el proceso de Transferencia del módulo Procesos generales para la [Exportación de datos contables](?=11859).  
Ejecute estos pasos cada vez que modifique cuentas, auxiliares, reglas o tipos de asientos.
  2. Si usted no opera con Contabilidad debe ejecutar el proceso de Transferencias del módulo Procesos generales para la [Importación de Tablas generales](?p=11992).  
Ejecute estos pasos cada vez que modifique cuentas, auxiliares, reglas o tipos de asientos.
  3. Para realizar la exportación e la importación de datos contables es necesario previamente identificar a cada empresa con una sucursal diferente en los [Datos de la empresa](?p=11851).



###### Fin del circuito de integración

Realizados los pasos de integración, se completa el circuito con las siguientes acciones:

  * Se exportan los asientos contables desde los módulos Tango (Ventas, Compras o Proveedores, Tesorería, etc.)
  * Se importan los asientos contables en el módulo Contabilidad.



###### Puesta en marcha en cada módulo

Para poder generar asientos desde los módulos luego de definir cuentas contables, auxiliares contables, reglas de apropiación y tipos de asientos, usted debe completar la información necesaria en cada módulo.

**Módulo Activo Fijo  
**En este módulo, los maestros que tienen información contable a completar son los siguientes:

  * **[Modelos de asientos](?p=5933):** debe definir un modelo de asiento, asociando los tipos contables definidos para cada operación. Este modelo se utiliza en la generación del asiento. Esta información es requerida.
  * **[Parámetros de Activo Fijo](?p=5948):** usted tiene la posibilidad de generar el asiento con el ingreso del comprobante, o por medio del proceso de generación de asientos contables.
  * **[Tipos de comprobantes](?p=5954):** usted necesita definir si el tipo de comprobante puede generar asiento, y el modelo de asiento predetermiando. Esta información es requerida.
  * **[Bienes](?p=5033):** usted puede indicar cuentas particulares para cada bien, y para cada tipo de movimiento interno. Esta información es opcional.
  * **[Tipos de bienes](?p=5955):** si desea una configuración genérica, indique las cuentas por cada tipo de bien y tipo de movimiento interno. Esta información es opcional.
  * **[Actualización individual de apropiaciones de bienes](?p=5897):** desde este proceso usted puede asociar los tipos de auxiliares relacionados con los bienes. En la generación de asientos de cada movimiento, se tomará la información de acuerdo a las cuentas y tipos de auxiliares utilizados en el asiento generado. Esta información es opcional.



**Módulo Compras  
**Al integrar con el módulo Contabilidad, usted debe definir algunos datos necesarios y obligatorios. Otros valores son opcionales, aunque ayudan a que la información contable sea más rica a la hora de realizar análisis contables. Antes de comenzar la puesta en marcha, le recomendamos leer el tópico [Detalle del circuito](?p=14453) del módulo Compras.

  * Indique desde la [opción monedas](?p=11956), la moneda corriente y la moneda extranjera contable, necesarias para la integración con el módulo de Contabilidad y para la integración con otros módulos como Activo Fijo y Tesorería.
  * Defina en [parámetros contables](?p=12044) del módulo Procesos generales la moneda extranjera contable habitual.
  * Ingrese los datos contables necesarios [cuentas contables](?p=11850), [tipos de asientos](?p=11994), [auxiliares contables](?p=11835), [reglas de apropiación](?p=11974) para poder crear modelos de asientos de compras. Tenga en cuenta que debe habilitar las cuentas, los tipos de asientos y las reglas de aplicación o de apropiación para el módulo Compras.
  * Complete los [parámetros contables](?p=14658) del módulo Compras, si genera asiento con el ingreso del comprobante o lo genera luego, etc.
  * Ingrese los [modelos de asientos](?p=14664) y la parametrización contable de los tipos de comprobantes.
  * En forma opcional, usted puede definir parámetros contables para [proveedores](?p=14686), [artículos](https://ayudas.axoft.com/25ar/articulo_carp_st), [conceptos](?p=14661) o para [tipo de gastos](?p=14663).



Luego de completar los pasos anteriores, usted está en condiciones de comenzar a generar asientos contables para las operaciones de Compras.

**Módulo Ventas  
**Al integrar con el módulo Contabilidad, usted debe definir algunos datos necesarios y obligatorios. Otros valores son opcionales, aunque ayudan a que la información contable sea más rica a la hora de realizar análisis contables. Antes de comenzar la puesta en marcha, le recomendamos leer el tópico [Detalle del circuito](?p=27201) del módulo Ventas.

  * Indique desde la [opción monedas,](?p=11956) la moneda corriente y la moneda extranjera contable, necesarias para la integración con el módulo de Contabilidad y para la integración con otros módulos como Activo Fijo y Tesorería.
  * Defina en [parámetros contables](?p=12044) del módulo Procesos generales la moneda extranjera contable habitual.
  * Ingrese los datos contables necesarios [cuentas contables](?p=11850), [tipos de asientos](?p=11994), [auxiliares contables](?p=11835), [reglas de apropiación](?p=11974) para poder crear modelos de asientos de ventas. Tenga en cuenta que debe habilitar las cuentas, los tipos de asientos y las reglas de aplicación o de apropiación para el módulo Ventas.
  * Complete los [parámetros contables](?p=19399) del módulo Ventas, si genera asiento con el ingreso del comprobante o lo genera luego, etc.
  * Ingrese los [modelos de asientos](?p=19368) y la parametrización contable de los tipos de comprobantes.
  * En forma opcional, usted puede definir parámetros contables para [clientes](?p=19444) o [artículos](https://ayudas.axoft.com/25ar/articulo_carp_st).



Luego de completar los pasos anteriores, usted está en condiciones de comenzar a generar asientos contables para las operaciones de Ventas.

**Módulo Tesorería  
**Al integrar con el módulo Contabilidad, usted debe definir algunos datos necesarios y obligatorios. Otros valores son opcionales, aunque ayudan a que la información contable sea más rica a la hora de realizar análisis contables. Antes de comenzar la puesta en marcha, le recomendamos leer el tópico [Detalle del circuito](?p=10450) del módulo Tesorería.

  * Indique desde la [opción monedas,](?p=11956) la moneda corriente y la moneda extranjera contable, necesarias para la integración con el módulo de Contabilidad y para la integración con otros módulos como Activo Fijo y Tesorería.
  * Defina en [parámetros contables](?p=12044) del módulo Procesos generales la moneda extranjera contable habitual.
  * Ingrese los datos contables necesarios [cuentas contables](?p=11850), [tipos de asientos](?p=11994), [auxiliares contables](?p=11835), [reglas de apropiación](?p=11974) para poder crear modelos de asientos de tesorería. Tenga en cuenta que debe habilitar las cuentas, los tipos de asientos y las reglas de aplicación o de apropiación para el módulo Tesorería.
  * Complete los [parámetros contables](?p=10832) del módulo Tesorería, si genera asiento con el ingreso del comprobante o lo genera luego, etc.
  * Ingrese la parametrización contable de los [tipos de comprobantes](?p=10279).
  * En forma obligatoria, usted debe definir parámetros contables para [cuentas de tesorería](?p=10204).



Luego de completar los pasos anteriores, usted está en condiciones de comenzar a generar asientos contables para las operaciones de Tesorería.

**Módulo Sueldos  
**En este módulo, los maestros que tienen información contable a completar son los siguientes:

  * **[Modelos de asientos](?p=13179):** defina un modelo de asiento, asociando los distintos conceptos que conforman la liquidación. Este modelo se utilizará en la generación del asiento. Esta información es requerida.
  * **[Datos fijos](?p=13052):** puede definir un modelo de asiento según cada dato fijo.
  * **[Actualización individual de apropiaciones habituales](?p=12997):** puede asociar los tipos de auxiliares relacionados a los legajos. Esta información se utilizará en la generación de asiento, la misma es opcional.
  * **[Actualización individual de apropiaciones ocasionales](?p=12999):** puede asociar los tipos de auxiliares relacionados a los legajos para un periodo en particular. Esta información se utilizará en la generación de asiento, la misma es opcional.
  * **[Tipos de liquidación](?p=13241):** puede definir un modelo de asiento por cada tipo de liquidación.
  * **[Legajos](?p=13153):** puede definir un modelo de asiento particular para el legajo.



##### Contenidos relacionados

  * [Herramientas para integración contable](https://ayudas.axoft.com/25ar/ayudas/gla/datoscontabl_carp_gla/herramientasintcontable_gla/)

  * [Video sobre Procesos generales](https://ayudas.axoft.com/25ar/videos/gla_carp_vid/)

  * [Video sobre automatización contable](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/automcontable_gral_vid/)

  * [Video sobre imputación contable Sueldos](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/imputcontsueldos_gral_vid/)

  * [Videos sobre auxiliares contables y contabilidad por proyectos](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/conproyectos_cna_vid/)
