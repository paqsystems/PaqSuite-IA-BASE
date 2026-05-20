# Políticas de redondeo

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_kit_gv/?p=10161/

## Contenido

# Políticas de redondeo

Este proceso le permite definir políticas de redondeo; de esta forma puede establecer los criterios utilizados por su empresa para ajustar sus precios, no solo la parte decimal sino también su parte entera.

Puede establecer una política para todos los precios o para un rango de precios en particular; por ejemplo, es probable que para montos bajos ajuste solo la parte decimal, para luego ir ajustando la unidad o decena en precios intermedios, y posteriormente ajustar la centena o unidades de mil en precios más altos.  
Si bien, en los párrafos siguientes encontrará varios ejemplos de aplicación, le recomendamos que utilice el simulador de redondeo incluida en este proceso para comprender cómo redondearíamos cada precio que desee evaluar, según los distintos criterios que ofrecemos.  
Tenga en cuenta que estas políticas se aplican en los siguientes procesos: [Criterios de actualización de precios](?p=10171), [Actualización global de precios](?p=19180) y [Administración de precios](?p=19189). La edición manual de precios, así como la importación de Excel, respeta el precio según lo indicado por el usuario.

##### Principal

Para crear una nueva política de redondeo, deberá indicar un código y su descripción, esto le permitirá identificar de manera unívoca a la regla generada. Además, debe indicar la cantidad de decimales con las que trabajará.

Decimales: indique la cantidad de decimales que utilizará para armar las reglas de redondeo. La cantidad de decimales que haya definido se usará para formatear los valores decimales de los rangos de precios y la máscara de redondeo.  
Si usted decide editar la cantidad de decimales de una política de redondeo que cuenta con otra configuración, se modificará la cantidad de decimales de los rangos de precios y máscara de redondeo existentes agregando un dígito con valor 0 al final, en caso de que la nueva configuración sea mayor a la anterior, o en caso de ser inferior se truncará.

**Ejemplo de modificación del campo “Cantidad de decimales”**

Tomando las siguientes pautas:

  * Caso con la cantidad de decimales en 2:  
Desde: 0,00  
Hasta (inclusive): 25.000,00  
Máscara: 9,99  
Modificamos la cantidad de decimales a 4:  
Desde: 0,0000  
Hasta (inclusive): 25.000,0000  
Máscara: 9,9900
  * Caso con la cantidad de decimales en 2:  
Desde: 0,00  
Hasta (inclusive): 25.000,00  
Máscara: 9,99  
Modificamos la cantidad de decimales a 1:  
Desde: 0,0  
Hasta (inclusive): 25.000,0  
Máscara: 9,9



Estas reglas o políticas de redondeo están conformadas por rangos de precios, métodos, direcciones y por la máscara que aplicará al precio base.

Desde y Hasta (inclusive): el valor del campo Desde no está incluido en el rango y se encontrará inhabilitado para edición. Para el primer rango, el valor del campo Desde comenzará con el valor en cero, para el resto, tomará el valor del campo Hasta (inclusive) correspondiente al rango anterior.  
El campo Hasta (inclusive) será el límite superior del rango de precios, siempre deberá ser mayor al valor Desde y nunca podrá superar al valor Hasta (inclusive) del siguiente registro (en caso de existir).  
Los precios comprendidos en estos rangos aplicarán la configuración realizada.

Método: indique que método de redondeo utilizará.  
Existen dos tipos posibles de elección:

  * **Fijo (ajusta el precio a la máscara):** seleccionando esta opción el precio se redondeará al valor de la máscara de redondeo. En cierto modo funciona como un reemplazo del precio base con la máscara utilizada, pudiendo en ocasiones incrementar a la unidad próxima entera o reducirla (**1**).  
Por ejemplo, si redondea con la máscara 0.90 hacia arriba, todos los precios terminarán en el siguiente valor más alto que termina en 0.90, inclusive al entero superior.  
Las siguientes máscaras son las utilizadas comúnmente para redondear:  
\- 0.99.  
\- 0.90.  
\- 9.99.  
\- 9.90.  
\- 99.99.  
\- 99.90.  
\- 90.99.  
\- 90.90.  
\- 999.99.  
\- 999.90.  
etc.
  * **Múltiplo (ajusta el precio a un múltiplo de la máscara):** seleccionando esta opción, el precio se redondeará al múltiplo del valor la máscara de redondeo (**2**).  
Por ejemplo, si redondea con la máscara 0.25 hacia arriba, todos los precios terminarán en el siguiente valor más alto que finalice en 0.25, 0.50, 0.75 o 0.00.  
Las siguientes máscaras son las utilizadas comúnmente para redondear:  
\- 0,01: redondee al centavo más cercano.  
\- 0,02: redondee al centavo par más cercano.  
\- 0,05: redondee a la moneda de cinco centavos más cercana.  
\- 0,10: redondee a la decena de centavos más cercana.  
\- 0,25: redondee al cuarto más cercano.  
\- 0,50: redondee a los cincuenta centavos más cercanos.  
\- 1,00: redondee al entero más cercano.  
\- 2,00: redondee al entero par más cercano.  
\- 5,00: redondee a los cinco enteros más cercanos.  
\- 10,00: redondee a la decena de entero más cercana.  
\- 100,00: redondee a la centena de entero más cercana.  
etc.



Puede utilizar otros intervalos de redondeo, pero producirán valores impares que probablemente no serán útiles para el redondeo de precios.

**Ejemplo (1)  
**Se utilizará la dirección de redondeo Hacia arriba a modo de ejemplo, más adelante se explicará su funcionamiento.

**Precio** | **Dirección** | **Máscara** | **Precio (redondeado)**  
---|---|---|---  
123,38 | Hacia arriba | 0,99 | 123,99  
3456,78 | Hacia arriba | 9,99 | 3459,99  
10350,25 | Hacia arriba | 99,99 | 10399,99  
  
**Ejemplo (2)  
**Se utilizará la dirección de redondeo Hacia arriba a modo de ejemplo, más adelante se explicará su funcionamiento.

**Precio** | **Dirección** | **Máscara** | **Precio (redondeado)**  
---|---|---|---  
123,38 | Hacia arriba | 0,05 | 123,40  
3456,78 | Hacia arriba | 10,00 | 3460,00  
10350,25 | Hacia arriba | 0,25 | 10350,50  
  
Dirección: indique que dirección de redondeo utilizará.  
Existen tres tipos posibles de elección:

  * **Hacia arriba:** seleccionando esta opción el precio se redondeará hacia el siguiente valor superior. Podrá utilizarse para el siguiente valor decimal o inclusive para el siguiente valor entero.
  * **Más cercano:** seleccionando esta opción el precio se redondeará hacia arriba o hacia debajo de acuerdo con que valor se encuentre más cerca del precio original (menor diferencia de redondeo).
  * **Hacia abajo:** seleccionando esta opción el precio se redondeará hacia el valor inferior de acuerdo con la máscara utilizada. Podrá utilizarse para el siguiente valor decimal o inclusive para el siguiente valor entero.



Máscara de redondeo: indique que máscara utilizará para redondear los precios. Para el método Fijo se utilizará como valor de reemplazo del precio a las unidades enteras y decimales abarcadas, en cambio para el método de Múltiplo, este valor se utilizará para encontrar los múltiplos superiores, más cercanos o inferiores del precio resultante.  
Puede utilizar los valores comentados en el apartado de **Método**.

**Ejemplo...  
**Listado de ejemplos utilizando las combinaciones posibles:

**Método** | **Dirección** | **Precio** | **Máscara** | **Diferencia** | **Precio final (redondeado)**  
---|---|---|---|---|---  
Fijo | Hacia arriba | 123,38 | 0,99 | 0,61 | 123,99  
Fijo | Más cercano | 123,38 | 0,99 | -0,39 | 122,99  
Fijo | Hacia abajo | 123,38 | 0,99 | -0,39 | 122,99  
Múltiplo | Hacia arriba | 123,38 | 0,05 | 0,02 | 123,40  
Múltiplo | Más cercano | 123,38 | 0,05 | 0,02 | 123,40  
Múltiplo | Hacia abajo | 123,38 | 0,05 | -0,03 | 123,35  
Fijo | Hacia arriba | 3456,78 | 9,90 | 3,12 | 3459,90  
Fijo | Más cercano | 3456,78 | 9,90 | 3,12 | 3459,90  
Fijo | Hacia abajo | 3456,78 | 9,90 | -6,88 | 3449,90  
Múltiplo | Hacia arriba | 3456,78 | 10,00 | 3,22 | 3460,00  
Múltiplo | Más cercano | 3456,78 | 10,00 | 3,22 | 3460,00  
Múltiplo | Hacia abajo | 3456,78 | 10,00 | -6,78 | 3450,00  
Fijo | Hacia arriba | 100,00 | 0,99 | 0,99 | 100,99  
Fijo | Más cercano | 100,00 | 0,99 | -0,01 | 99,99  
Fijo | Hacia abajo | 100,00 | 0,99 | -0,01 | 99,99  
Múltiplo | Hacia arriba | 15690,00 | 0,75 | 0,00 | 15690,00  
Múltiplo | Más cercano | 15690,00 | 0,75 | 0,00 | 15690,00  
Múltiplo | Hacia abajo | 15690,00 | 0,75 | 0,00 | 15690,00  
  
__Nota

Consideraciones a tener en cuenta para cuando el método elegido es **Fijo (ajusta el precio a la máscara)** :

  * Si la dirección de redondeo es _Hacia abajo_ : el valor de la máscara deberá ser mayor al valor _Desde_ y menor al valor _Hasta (inclusive)_.  
Esto no será aplicable para el primer rango de precios dado que el valor del campo _Desde_ comienza en cero.
  * Si la dirección de redondeo es _Hacia arriba_ : el valor de la máscara deberá ser menor o igual al precio _Hasta (inclusive)_.



**Ejemplos…**

**Desde** | **Hasta (inclusive)** | **Dirección** | **Máscara** | **Resultado**  
---|---|---|---|---  
0,00 | 2000,00 | Hacia abajo | 9,99 | OK  
10,00 | 1200,00 | Hacia abajo | 99,99 | ERROR  
0,00 | 550,00 | Hacia abajo | 999,99 | ERROR  
0,00 | 1000,00 | Hacia arriba | 0,99 | OK  
10,00 | 1200,00 | Hacia arriba | 99,99 | OK  
0,00 | 550,00 | Hacia arriba | 999,99 | ERROR  
  
Para ambos métodos, los precios que no puedan ser redondeados se mantendrán si modificaciones, por ejemplo:

**Precio** | **Dirección** | **Máscara** | **Precio (redondeado)**  
---|---|---|---  
1,85 | Hacia abajo | 9,99 | 1,85  
20,85 | Hacia abajo | 99,00 | 20,85  
  
Asimismo, debe tener presente que para cuando la máscara de redondeo sea superior al precio y el método elegido sea _Hacia arriba_ , el redondeo se aplicará igual pudiendo generar una diferencia significativa entre el precio base y el precio redondeado.  
Por ejemplo:

**Precio** | **Dirección** | **Máscara** | **Precio (redondeado)**  
---|---|---|---  
1,85 | Hacia arriba | 9,99 | 9,99  
30,85 | Hacia abajo | 999,99 | 999,99  
  
Simulador de redondeo: puede verificar el precio resultante a partir de las combinaciones de redondeos elegidas o bien, verificar como quedaría el precio redondeado con un numero generado al azar y que se irá modificando a medida que modifique las configuraciones de redondeo.

Si aún no comprende como quedaría su precio redondeado o prefiere verificar como sería con otros métodos o dirección de redondeo, usted cuenta con la posibilidad de visualizar más ejemplos desde el botón "Simulador de redondeo".  
En esta sección usted podrá simular y conocer cómo quedará su precio redondeado para todas las configuraciones disponibles a partir de un precio de ejemplo. Esto le ayudará a comprender y elegir la configuración que mejor su ajusta a su negocio.  
Deberá escribir el precio a redondear y presionar en el botón “Calcular”. Aplicará las máscaras definidas por defecto, en caso de querer utilizar otras, deberá modificarlas y volver a presionar el botón “Calcular”.

##### Contenidos relacionados

  * [Video sobre precios de ventas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/precioventa_gv_vid/)
