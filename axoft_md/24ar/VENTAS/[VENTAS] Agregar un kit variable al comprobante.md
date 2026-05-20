# Agregar un kit variable al comprobante

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_kit_gv/?p=18338/

## Contenido

# Agregar un kit variable al comprobante

Luego de realizar la búsqueda y selección del artículo de tipo kit variable, debe seleccionar en pantalla los artículos que formarán parte del mismo.  


La pantalla de selección de componentes para el kit variable está dividida en dos secciones.  
La sección izquierda mostrará un buscador de artículos (permitirá buscar por distintos criterios) y debajo las categorías en las que se agrupan los artículos que podrán ser seleccionados.  
Cada categoría, de acuerdo a la configuración elegida en 'control por categoría', mostrará una leyenda con la cantidad de artículos que podrán ser seleccionados.

Más información:

Los artículos que componen las categorías (el orden en que se presentarán) y la configuración de 'control por categoría' se realiza desde el proceso Fórmulas del módulo Stock.

En cada categoría, se mostrarán los artículos que las componen.  
Las unidades disponibles a seleccionar de cada artículo se irán actualizando a medida que se agreguen a la sección de artículos ya seleccionados para el kit.  
En la sección derecha de la pantalla se mostrarán estos componentes ya seleccionados, con sus cantidades y el precio adicional (en caso de tenerlo).

Más información:

El precio adicional será editable solamente para la categoría que tiene el parámetro 'Valoriza'. Caso contrario no podrá editarse. Por defecto, se carga automáticamente el precio adicional unitario configurado en la fórmula para ese artículo, categoría y la lista de precios seleccionada en el comprobante. Al modificar el precio, cambiará el precio total del kit.

Además de las cantidades para los componentes del kit, en pantalla se mostrarán los importes, precios adicionales (si los hubiera) y el precio final.  
Una vez seleccionados todos los artículos que conformarán el kit variable, al presionar Agregar kit <F10> se cargarán automáticamente en el comprobante.  
Estos componentes seleccionados para conformar el kit variable, corresponden a una unidad de kit. Vale decir que si desde el comprobante se solicitan dos kits, lo que se seleccione se multiplicará por dos.

__Nota

Al agregar artículos al kit variable, si alguno de ellos tiene errores (por ejemplo, falta de stock) se marcará ese renglón en color rojo, y al posicionarse sobre él se mostrará la información del error correspondiente.

Para más información sobre kits consulte la [Guía de implementación de kits](?p=27264).
