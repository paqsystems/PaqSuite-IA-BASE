# Guía de Punto de Venta sobre Unidad de Medida

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_st2/guia_unidadmedida_st2/

## Contenido

# Guía de Punto de Venta sobre Unidad de Medida

Usted puede administrar unidades de medida, identificando las cantidades expresadas para cada artículo, en los procesos de Stock, Ventas, Compras, Central, Contabilidad y Activo Fijo. De esa manera, el sistema podrá cuantificar con mayor exactitud los artículos en stock, así como su ingreso o egreso.

Para cada artículo puede definir (asociar) dos unidades de Stock, una presentación de Ventas y varias presentaciones de Compras:

  * Unidad de stock 1: es la unidad en la que se van a expresar los saldos, precios y costos del artículo. Una vez definida puede aplicar modificaciones, pero deberá ajustar los saldos, costos y actualizar el precio a la nueva unidad. Ej. Kilos, Barras, Cajas, etc.
  * Unidad de stock 2: es otra unidad de stock en la que se van a expresar los saldos y las series del artículo. Ej. Hormas, Rollos, etc.
  * Presentación de ventas: es una unidad alternativa para utilizar en el módulo Ventas. Puede aplicarse a modo descriptivo, o incluso tener una equivalencia fija a la unidad de stock. Ej. Caja x 1000, Lata x 2litros, etc.
  * Presentación de compras: es una unidad alternativa para utilizar desde el módulo Compras. Puede definir varias presentaciones de compras por artículo, y además de asignar una equivalencia con la unidad de stock, puede asignar precios para cada presentación.



##### Puesta en marcha

Como primera medida, configure las [unidades de medida de los artículos.](?p=17035/#unidades-de-medida) Defina las unidades de medida a utilizar, teniendo en cuenta las diferentes presentaciones en las que va a administrar sus artículos.  
Es posible configurar las unidades para nuevos artículos en [Parámetros de Stock](https://ayudas.axoft.com/24ar/parametrogeneral_st2) definiendo las unidades habituales para los módulos de Stock, Ventas y Compras, en el [Alta por defecto de artículos](https://ayudas.axoft.com/24ar/valordefectoartic_st2) o a través de la [Actualización masiva de artículos](https://ayudas.axoft.com/24ar/actualizmasivartic_st2).

**Ejemplo de Implementación:**

**Código de medida** | **Descripción de medida** | **Decimales** | **Sigla** | **Tipo de unidad**  
---|---|---|---|---  
AÑOS | Años | 0 | AS | Tiempo  
C/U | Cajas | 0 | C/U | Unidad  
HORH | Horas hombre | 2 | HH | Tiempo  
KGR | Kilogramos | 3 | Kg | Masa  
LIT | Litros | 2 | LT | Volumen  
MESES | Meses | 0 | MS | Tiempo  
  
**Carga inicial**

Para utilizar los circuitos de Sueldos, Compras y Ventas es necesario definir las unidades de medidas en los artículos.

Carga de Unidades de Medida

Defina las unidades de medidas a utilizar por el sistema desde [Unidades de medida](?p=11998).

Datos de Unidad de Medida

Cada unidad de medida tiene código, descripción, sigla, decimales (únicamente para Contabilidad y Activo Fijo), Tipo de Unidad (longitud / masa / tiempo / superficie / volumen), módulo donde pueden utilizarse (Contabilidad, Activo Fijo, Stock, Ventas y Compras), datos legales (valores por defecto para comprobantes electrónicos) y observaciones.

__Tenga en cuenta

Para los módulos **Stock** , **Compras** y **Ventas** , los valores de decimales para cantidades de artículos de stock son los parametrizados desde [Configuración de decimales](?p=9150/#decimales-de-tango) (solapa _"Decimales"_) del **Administrador del sistema**.  


La sigla de unidad de medida puede ser impresa en los movimientos de los distintos módulos del sistema.

##### Detalle del circuito

Una vez configuradas las unidades de medida para cada artículo, podrán ser utilizadas en los movimientos de los distintos circuitos administrativos del sistema. Las mismas se encuentran en los renglones de los movimientos, pudiendo seleccionarlas y/o visualizarlas de acuerdo al tipo de movimiento.

Unidades de Medida en Stock En cualquiera de los movimientos de stock, la unidad será obtenida desde el artículo seleccionado, únicamente podrá visualizarla (no es posible su modificación).

Unidades de Medida en Ventas  
En los movimientos de ventas podrá seleccionar entre dos unidades de medida (Stock y Ventas), configuradas desde el renglón del artículo seleccionado.  
La selección de unidad puede configurarse utilizando [Perfiles de Ventas](?p=19415).

Unidades de Medida en Compras  
En los movimientos de compras puede seleccionar más de 2 unidades de medida (Stock y Compras), configuradas desde el renglón del artículo seleccionado.  
La selección de unidad puede configurarse utilizando [Perfiles de Compras](?p=14679).

##### Contenidos relacionados

No se ha encontrado ninguno
