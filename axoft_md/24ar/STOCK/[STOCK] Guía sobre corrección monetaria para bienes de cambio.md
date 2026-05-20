# Guía sobre corrección monetaria para bienes de cambio

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Stock
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_st/guia_correccmonetbiencamb_st/

## Contenido

# Guía sobre corrección monetaria para bienes de cambio

Esta guía le indica cómo trabajar con corrección monetaria de bienes de cambio, según el artículo 41 de la ley de renta chilena. 

Al realizar un cierre por corrección monetaria, los costos de sus artículos se ajustarán según lo indicado en la ley, facilitando así la información requerida para su posterior registración contable.

##### Puesta en marcha

Para aplicar corrección monetaria, siga estos pasos:

  1. Defina en la sección valorización de [Parámetros de Inventario](https://ayudas.axoft.com/24ar/parametrogeneral_st) la configuración relacionada a corrección monetaria. Debe seleccionar un criterio de valorización de precio promedio ponderado P.P.P (cierre mensual o cierre mensual con valor diario) y los siguientes parámetros específicos de corrección monetaria: 
     1. Próximo período de cierre.
     2. Índices de precios al consumidor.
     3. Tipo de cotización.  
Para más información, consulte la ayuda de [Parámetros generales de Inventario](https://ayudas.axoft.com/24ar/parametrogeneral_st).
  2. Seleccione los artículos a los que se les debe aplicar la corrección monetaria: puede realizarlo desde [Artículos](https://ayudas.axoft.com/24ar/articulo_carp_st) o [Actualización masiva de artículos](https://ayudas.axoft.com/24ar/actualizmasivartic_st), habilitando la opción Aplica corrección monetaria e indicando el origen del artículo (nacional o importado).  
Es importante destacar que sólo los productos que lleven stock, y que no estén configurados como bienes de uso, pueden configurarse como artículos que apliquen corrección monetaria.



Tenga en cuenta:

El cálculo indicado en la ley para realizar el ajuste de bienes de cambio involucra la variación del índice de precios al consumidor (IPC) y la variación del tipo de cambio de la moneda extranjera contable habitual. Para obtener ambas variaciones automáticamente en el proceso [cierre por corrección monetaria](https://ayudas.axoft.com/24ar/correccmonetcierre_st), se recomienda ingresar previamente los valores correspondientes al ejercicio en [Índices](?p=11941) y [Cotizaciones](?p=11848).

__Importante

Tenga en cuenta que según el origen del artículo se aplican diferentes cálculos de corrección monetaria según la ley.

##### Detalle del circuito

La corrección monetaria debe efectuarse, según lo indica la ley, luego de la finalización del ejercicio comercial, y permite actualizar el precio promedio ponderado de los artículos que aplican esta corrección, según su origen.

  * Para artículos nacionales: se aplica un coeficiente de variación del índice de precios del consumidor.
  * Para artículos importados: se aplica un coeficiente de variación del tipo de cambio de la moneda extranjera.



Luego de aplicar la corrección monetaria, los diferentes procesos e informes en donde se utilice el precio promedio ponderado tomarán el nuevo costo ajustado. Antes de efectuar el cierre por corrección monetaria, es necesario realizar el cierre de precio promedio ponderado.

Cierre de artículos por corrección monetaria

A través de este proceso se podrán efectuar cierres 'transitorios' y 'definitivos' por corrección monetaria.

Cierre transitorio

El cierre transitorio se ejecuta con la finalidad de saber cuál sería la corrección monetaria de cada uno de los artículos configurados a tal efecto, a un período dado dentro del ejercicio comercial actual. El usuario podrá ejecutar tantos cierres transitorios como necesite dentro del único ejercicio 'abierto'. Una vez efectuado el cierre definitivo, el ejercicio pasa a estar en estado 'cerrado', abriéndose en forma automática el ejercicio siguiente.

__Importante

Sólo se podrá consultar el último cierre transitorio, ya que al tratarse de un cierre temporario, los mismos se van depurando a medida que se van efectuando nuevos cierres.

Cierre definitivo

El cierre definitivo se ejecuta con la finalidad de ajustar los costos PPP de los productos configurados a tal efecto, con los importes resultantes del proceso de corrección monetaria. Los datos correspondientes a la variación (anual y semestral) del índice de precios al consumidor, y de la tasa de cambio correspondiente al dólar observado, podrá ser calculado en forma automática, siempre y cuando haya ingresado los valores correspondientes en las tablas [Índices](?p=11941) y [Cotizaciones](?p=11848)., que se encuentran dentro del módulo Procesos generales.

En caso de no haber ingresado dichos valores, puede ingresarlos en forma manual. A diferencia del cierre transitorio, los cierres definitivos son almacenados en el sistema, y no se depuran con nuevos cierres.

Consulta del resultado de la corrección monetaria

Luego de efectuar un cierre por corrección monetaria, el proceso informa los resultados en pantalla, pudiendo ser exportados a un archivo Excel.

Para acceder a esa misma información puede utilizar también las consultas Live, dentro de Inventario/ Valorización / Corrección monetaria.

Además, es posible incluir la corrección monetaria dentro del informe [Tarjeta de inventario Kardex](?p=17038/#informe-kardex), pudiendo analizar la variación en la valorización de existencias en el tiempo, y los ajustes a realizar por dichos cambios de valorización en su inventario.

Si desea modificar los valores resultantes del cierre por corrección monetaria, puede realizar la [Anulación del cierre](?p=17069), para luego volver a generarlo.

¿Cómo ingreso un comprobante con fecha anterior al último cierre?

Una vez ejecutado el cierre definitivo por corrección monetaria, no se podrán eliminar cierres de PPP ni ingresar o eliminar comprobantes cuya fecha sea inferior al último cierre por corrección monetaria.

Si fuese necesario ingresar o eliminar algún comprobante que afectó al último cierre definitivo siga los pasos que se especifican a continuación:

  * [Anule el cierre por corrección monetaria](?p=17069).
  * [Anule el cierre de PPP.](?p=17232)
  * Ingrese o elimine los comprobantes que fuesen necesarios.
  * Ejecute nuevamente el [cierre periódico PPP.](?p=17233)
  * Por último, ejecute el [cierre por corrección monetaria](https://ayudas.axoft.com/24ar/correccmonetcierre_st).



##### Detalle del cálculo de corrección monetaria para bienes de cambio

Según el artículo 41 de la ley de renta chilena, los bienes de cambios se deberán revaluar anualmente (al cierre del año comercial de cada empresa) según el siguiente criterio:

  * Bienes adquiridos en el mercado local
    * Comprados en el segundo semestre del ejercicio comercial: se deben revaluar al precio más alto facturado en el segundo semestre, el cual no podrá ser inferior al precio más alto en el citado ejercicio.
    * Comprados en el primer semestre del ejercicio comercial: se deben revaluar al precio más alto facturado en el primer semestre, reajustado según el porcentaje de variación experimentada por el índice de precios al consumidor en el segundo semestre del ejercicio.
    * Bienes nacionales cuyas existencias se mantienen del ejercicio anterior: su costo de reposición se determina reajustando su valor de libros, por la variación experimentada por el índice de precios al consumidor durante todo el ejercicio.
  * Bienes adquiridos en el extranjero
    * Importados en el segundo semestre del ejercicio comercial: se deben revaluar al valor de su última importación, aunque este último no sea el más alto del ejercicio.
    * Importados en el primer semestre del ejercicio comercial: se deben revaluar al valor de su última importación, reajustado según el porcentaje de variación experimentado por el tipo de cambio de la moneda extranjera contable habitual, durante el segundo semestre del ejercicio.
    * Bienes importados cuyas existencias se mantienen del ejercicio anterior: su costo de reposición se determina reajustando su valor de libros, por la variación experimentada por el tipo de cambio de la moneda extranjera contable habitual, durante todo el ejercicio.



**Ejemplo...**

Saldos de artículos en stock al 31/12/2012

**Artículo** | **Origen** | **Fecha** | **Último Ingreso** | **Precio** | **El precio se obtiene del**  
---|---|---|---|---|---  
NAC1 | Nacional | 03/02/2012 | 1er semestre | $500 | Precio más alto facturado en el 1er semestre  
NAC2 | Nacional | 29/07/2012 | 2do semestre | $600 | Precio más alto facturado en el ejercicio  
IMPO1 | Importado | 05/02/2012 | 1er semestre | $650 | Última importación del ejercicio  
IMPO2 | Importado | 31/12/2011 | Año anterior | $700 | Valor de libros al cierre del ejercicio anterior  
  
Variación del índice de precios al consumidor en el ejercicio 2012.

**Índice** | **Valor en puntos** | **Variación porcentual**  
---|---|---  
11/2011 | 05/2012 | 11/2012 | Semestral | Anual  
Índice de precios al consumidor | 106,37 | 107,79 | 108,64 | 0,8% | 2,1%  
  
Variación del tipo de cambio en el ejercicio 2012

**Moneda** | **Cotizaciones al:** | **Variación porcentual**  
---|---|---  
31/12/2011 | 30/06/2012 | 31/12/2012 | Semestral | Anual  
Dólar EE.UU | 519,20 | 501,84 | 479,96 | -4,36% | -7,56%  
  
Resultado de la aplicación de la corrección monetaria

**Artículo** | **Origen** | **Fecha** | **Precio** | **% Variación** | **Costo PPP al 12/2012** | **Precio con C.M.** | **Corrección monetaria**  
---|---|---|---|---|---|---|---  
NAC1 | Nacional | 03/02/2012 | $500 | 0,80% | 450,00 | 504,00 | 54,00  
NAC2 | Nacional | 29/07/2012 | $600 | 0,00% | 560,00 | 600,00 | 40,00  
IMPO1 | Importado | 05/02/2012 | $650 | -4,36% | 610,00 | 621,66 | 11,66  
IMPO2 | Importado | 31/12/2011 | $700 | -7,56% | 670,00 | 647,08 | -22,92
