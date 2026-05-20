# Ayudas sobre Stock

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_ivasimple_gv/?p=17254/

## Contenido

# Ayudas sobre Stock

Este módulo fue diseñado para cubrir las necesidades operativas y gerenciales de la gestión de stock, y también está orientado a la gestión de comercios minoristas por su agilidad y funciones de facturación rápida. Permite generar movimientos de stock en forma independiente a las gestiones de compra y venta. Contempla entradas, salidas, transferencias y ajustes. Concentra las funciones de costos y valorizaciones. Permite la carga y descarga de producto e insumos en base a fórmulas de composición de producto

Comprende las parametrizaciones y definiciones referentes al manejo de stock y funciona como módulo centralizador de las operaciones que involucren movimientos de productos e insumos.Se integra con Ventas y Compras en forma automática, recibiendo las transacciones que involucran movimientos de stock. Además, brinda las funciones necesarias para registrar las novedades de stock que no están relacionadas en forma directa con comprobantes de compra y venta.  
En resumen, las novedades de stock podrán tener origen en los siguientes módulos:

  * Ventas, que actualizará los movimientos de stock que se producen por comprobantes de la gestión de ventas (remitos y facturas, débitos y créditos que afecten stock).
  * Compras, que actualizará los movimientos de stock que se producen por comprobantes de la gestión de compras (remitos y facturas, débitos y créditos que afecten stock).



Por otra parte, permite exportar el archivo maestro de artículos. De la misma manera, permite crear archivos con comprobantes generados por egresos de stock, para que puedan ser incorporados automáticamente en otro sistema.

##### Características generales

A continuación, realizamos una breve descripción de los archivos y procesos que componen el módulo.

**Archivos**

Incluye la parametrización del módulo y la actualización de los archivos maestros del sistema. Todos estos datos son los que permitirán trabajar con las registraciones y operaciones de los módulos Ventas, Compras y Stock.

**Movimientos**

Abarca la generación de todos los movimientos de stock que no surgen en forma automática de los módulos Compras y Ventas.

**Procesos Periódicos**

Comprende los procesos que corresponden a funciones de cierta periodicidad, como el cálculo del precio promedio ponderado y la depuración de información, entre otros.

**Informes**

Concentra una amplia gama de reportes y estadísticas con toda la información sobre saldos y movimientos de stock, valorización, costos de mercadería, armado de producto, etc.

**Análisis Multidimensional**

Abarca la generación de información en formato multidimensional y la integración automática con tablas dinámicas de Excel.

**Integración con Central**

Incluye los procesos de exportación para la generación de informes y estadísticas; procesos de emisión de informes de auditoría y de importación de datos provenientes del módulo Central.

##### Consideraciones de implementación

Para implementar el sistema es importante la correcta definición de los parámetros de stock y archivos maestros. Es conveniente realizar un análisis global de todas las alternativas y adoptar la que sea más favorable para la modalidad de trabajo de su empresa.

**Parámetros:** un parámetro es un dato que influye en el comportamiento del sistema.  
Por ejemplo: en la definición de un artículo, el parámetro Lleva Stock Asociado provocará en el sistema un funcionamiento diferente; en cambio, la Descripción de un artículo si bien es un dato importante, no cambia el funcionamiento del sistema cualquiera fuere su valor.

Parámetros de tipo general y particular:

Hay parámetros que son de tipo general, es decir únicos para todo el sistema, y otros que son a nivel particular. Por ejemplo, un parámetro general corresponderá si el sistema [axvar variable=intermod_st-manejapart-llevaescalas], mientras que un parámetro particular corresponderá si un artículo "X" maneja [axvar variable=intermod_st-partidas-escalas]. Este último parámetro afecta únicamente a ese artículo "X" mientras que el primero habilita el manejo de [axvar variable=intermod_st-partidas-escalas] en general.

Si se implementan varios módulos, y por ser Tango un sistema integrado, los parámetros influyen en algunos casos en el resto de los módulos.

Instalación:

Al instalar el módulo Ventas o Compras el módulo Stock estará automáticamente presente en la instalación. Por ello, para comenzar a trabajar en Ventas y Compras la puesta en marcha también involucra la puesta en marcha conjunta del módulo Stock.

Hay parámetros y datos que se definen en el módulo Stock y que afectan al resto del sistema.  
A continuación, se enumeran los procesos que contienen este tipo de información y una breve referencia general. Para conocer en profundidad el detalle de cada parámetro o dato, opciones y restricciones puede recurrir a la explicación particular del proceso que lo contiene.

##### Definiciones en Stock que afectan al resto de los módulos

Los siguientes ítems afectan al resto de los módulos de su sistema.

###### Definición de parámetros generales

Los parámetros Lleva partidas y Lleva series determinan si todos o algunos artículos se administrarán por partida y si se manejan números y datos especiales por unidad de stock. De manejarse estos conceptos, tanto en Ventas como en Compras, los procesos que involucren artículos (ingresos o egresos, facturación) tendrán activados los comandos referidos a la administración de partidas y/o series. Los impuestos por defecto son una ayuda útil y totalmente opcional, para asignar durante el alta de artículos, las referencias impositivas habituales. Pueden consignarse valores diferentes para las operaciones de Ventas y las de Compras. 

###### Definición de artículos

Los artículos tienen su definición en este módulo. Tanto Ventas como Compras utilizan esta información para registrar sus transacciones y generar informes. El módulo Stock se alimenta de transacciones de Ventas y Compras que afectan stock, más todos los movimientos previstos en este módulo (movimientos que no surgen de los otros módulos). El parámetro Lleva stock asociado será tenido en cuenta al realizar operaciones con un artículo tanto en Ventas como en Compras y Stock, con el fin de generar el movimiento de stock correspondiente.  
Los parámetros Lleva partidas y Lleva series determinan, tanto en Ventas como en Compras y Stock, la activación de los comandos referidos a la administración de partidas y/o series al utilizar el artículo.  
El parámetro Equivalencia permite indicar la unidad alternativa de compra. Puede utilizar las equivalencias en los comprobantes que actualizan stock en el módulo Compras. El parámetro Perfil para un artículo, indica si un artículo es de venta, compra o compraventa. De acuerdo a este parámetro, se visualizarán en cada módulo sólo los artículos que correspondan al tipo de operación.  
Los campos Cuenta ventas y Cuenta compras, podrán ser utilizados opcionalmente para la contabilización de transacciones de los respectivos módulos.  
Los porcentajes de Comisión venta, Bonificación y Utilidad son datos que se utilizan en el módulo Ventas para el cálculo de comisiones por artículo, bonificación por artículo en las facturas y actualización de listas de precios con margen de utilidad sobre costo, respectivamente.  
El Porcentaje de desvío es un dato utilizado en el módulo Compras para dar por cumplida la recepción de mercaderías vinculadas a una orden de compra, dentro de un margen establecido por artículo. 

###### Definición de depósitos

Los depósitos tienen su definición en este módulo. Tanto Ventas como Compras y Stock utilizan esta información para registrar sus transacciones y generar informes por depósito.

##### Diferencias entre Punto de Venta y Gestión

Diferencias entre el módulo Ventas - Ventas Punto de Venta:

El módulo Ventas Punto de Ventas:

  * No maneja pedidos.
  * No maneja recargos (ni de transporte ni de interés).
  * No calcula ninguna percepción, salvo la del Responsable No Inscripto y la del Sujeto No Categorizado.
  * La lista de precios debe ser siempre utilizada con impuestos incluidos.
  * No incluye riesgo crediticio.
  * No incluye la Consulta Integral de Clientes (disponible en Ventas de Tango Gestión).
  * No maneja comprobantes electrónicos.
  * No maneja cotizaciones.
  * No genera notas de débito de interés por mora.
  * No maneja facturas de crédito.
  * No genera remitos valorizados.
  * Es únicamente para ser utilizado con controlador fiscal y bajo modalidad concomitante. No es posible otro tipo de modalidad.



Diferencias entre el módulo Stock - Stock Punto de Venta:

El módulo Stock Punto de Ventas:

  * No maneja series ni partidas.



##### Puesta en marcha

La implementación sigue un orden de pasos. Hay pasos necesarios y hay pasos optativos (no obligatorios para comenzar a trabajar con las funciones básicas), los que pueden implementarse con posterioridad cuando lo considere oportuno.  
A continuación, sugerimos el orden correcto de carga:

  1. [Parámetros de Stock](https://ayudas.axoft.com/24ar/parametrogeneral_st)
  2. Alícuotas: las alícuotas para el cálculo de impuestos se definen en los módulos Ventas y Compras. Esta información es necesaria en el momento de definir todos los artículos en el módulo Stock.
  3. [Longitud de agrupaciones](https://ayudas.axoft.com/24ar/longitagrupacion_st)
  4. [Agrupaciones de artículos](https://ayudas.axoft.com/24ar/agrupacionartic_st)
  5. [Escalas](?p=17077)
  6. [Artículos](https://ayudas.axoft.com/24ar/articulo_carp_st)
  7. [Depósitos](https://ayudas.axoft.com/24ar/deposito_st)
  8. [Talonarios](?p=17309): Definir el formato de los comprobantes que puede emitir el sistema. Dentro de la definición de un talonario se encuentra la actualización de su modelo de impresión. Se confeccionará el modelo sólo para aquellos comprobantes que se desee imprimir.
  9. [Tipos de comprobante](https://ayudas.axoft.com/24ar/tipocomprobante_st): se refiere exclusivamente a los comprobantes que actualizarán stock desde este módulo. No se relaciona con los comprobantes que afectan stock desde los módulos Ventas o Compras en forma automática.



###### Puesta en marcha para el proceso de armado (opcional)

Una vez definidos los artículos, es posible comenzar la implementación de fórmulas para el proceso de armado. Esta información no es necesaria para el funcionamiento básico del sistema.  
Los pasos para utilizar las funciones de armado son:

  1. [Componentes de costos](https://ayudas.axoft.com/24ar/componentecosto_st): estas componentes no son obligatorias.
  2. [Fórmulas](https://ayudas.axoft.com/24ar/formulas_st).
  3. [Tipo/s de comprobante](https://ayudas.axoft.com/24ar/tipocomprobante_st) especial para armado: se definirá un tipo de comprobante especial para registrar los movimientos de stock por armado.



###### Puesta en marcha para el cálculo de PPP (opcional)

Para implementar correctamente el cálculo de PPP es necesario:

  1. Indicar que utiliza precio promedio ponderado en el proceso [Parámetros de Stock](https://ayudas.axoft.com/24ar/parametrogeneral_st).
  2. Indicar qué tipos de comprobantes (que opcionalmente afectan PPP) actualizan PPP, a través del proceso Tipos de comprobante de los módulos Stock y Compras.
  3. Ingresar el valor inicial de PPP.



Para ingresar el valor inicial de PPP existen dos opciones:

  * Si no existen movimientos de stock, las opciones posibles son: 
    * Ingresar el valor de PPP inicial como precio del artículo, al realizar la carga inicial de stock mediante un [ingreso a stock](https://ayudas.axoft.com/24ar/ingresostock_st) o [ajuste de inventario](https://ayudas.axoft.com/24ar/ajusteinventario_st) valorizados (que afecte PPP).
    * Ingresar manualmente el PPP inicial para cada artículo en el proceso [Actualización individual de PPP](https://ayudas.axoft.com/24ar/pppactualizacionindividual_st).
  * Si existen movimientos de stock: 
    * En este caso se debe ingresar manualmente el PPP inicial para cada artículo en el proceso [Actualización individual de PPP](https://ayudas.axoft.com/24ar/pppactualizacionindividual_st).



###### Integración con otros módulos

Para comenzar a trabajar con los módulos Compras o Ventas solamente será necesario definir los parámetros de stock, depósitos y artículos. Los demás puntos son necesarios para las actualizaciones del módulo Stock propiamente dicho.

##### Consideraciones de implementación

Para implementar el sistema es importante la correcta definición de los parámetros de stock y archivos maestros. Es conveniente realizar un análisis global de todas las alternativas y adoptar la que sea más favorable para la modalidad de trabajo de su empresa.  
**Parámetros:** un parámetro es un dato que influye en el comportamiento del sistema.  
Por ejemplo: en la definición de un artículo, el parámetro Lleva Stock Asociado provocará en el sistema un funcionamiento diferente; en cambio, la Descripción de un artículo si bien es un dato importante, no cambia el funcionamiento del sistema cualquiera fuere su valor.

Parámetros de tipo general y particular:

Hay parámetros que son de tipo general, es decir únicos para todo el sistema, y otros que son a nivel particular. Por ejemplo, un parámetro general corresponderá si el sistema [axvar variable=intermod_st-manejapart-llevaescalas], mientras que un parámetro particular corresponderá si un artículo "X" maneja [axvar variable=intermod_st-partidas-escalas]. Este último parámetro afecta únicamente a ese artículo "X" mientras que el primero habilita el manejo de [axvar variable=intermod_st-partidas-escalas] en general.

Si se implementan varios módulos, y por ser Tango un sistema integrado, los parámetros influyen en algunos casos en el resto de los módulos.

Instalación:

Al instalar el módulo Ventas o Compras el módulo Stock estará automáticamente presente en la instalación. Por ello, para comenzar a trabajar en Ventas y Compras la puesta en marcha también involucra la puesta en marcha conjunta del módulo Stock.

Hay parámetros y datos que se definen en el módulo Stock y que afectan al resto del sistema.  
A continuación, se enumeran los procesos que contienen este tipo de información y una breve referencia general. Para conocer en profundidad el detalle de cada parámetro o dato, opciones y restricciones puede recurrir a la explicación particular del proceso que lo contiene.

##### Contenido dependiente

  * [Archivos](https://ayudas.axoft.com/24ar/ayudas/st/archivos_carp_st/)
  * [Movimientos](https://ayudas.axoft.com/24ar/ayudas/st/movimiento_carp_st/)
  * [Procesos periódicos](https://ayudas.axoft.com/24ar/ayudas/st/procesoperiodico_carp_st/)
  * [Informes](https://ayudas.axoft.com/24ar/ayudas/st/informes_carp_st/)
  * [Análisis Multidimensional](https://ayudas.axoft.com/24ar/ayudas/st/analmultidimensional_st/)
  * [Modelos de impresión de comprobantes en Stock](https://ayudas.axoft.com/24ar/ayudas/st/modeloimpresioncomprob_st/)
