# Tipos de bienes

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_integrcont_gla/?p=5955/

## Contenido

# Tipos de bienes

Mediante este proceso, usted puede crear una clasificación de segundo nivel para poder tipificar a los bienes según el comportamiento. Cada tipo de bien pertenece a un rubro.

Los datos definidos para el tipo de bien serán utilizados como defectos en el ingreso de bienes.

**Ejemplo...**

Dentro de "Bienes de uso" tenemos como tipos de bienes: Maquinarias, Rodados, Muebles y útiles, etc.

Dentro de los "Bienes intangibles" tenemos como tipos de bienes: Marcas y patentes, Llaves, etc.

Dentro de las "Inversiones permanentes" tenemos como tipos de bienes: Acciones en otras empresas, etc.

##### Principal

Código: cada tipo de bien que usted defina se identificará por este código. Es posible ingresar hasta 10 caracteres. El sistema valida que sea único, es decir, que no se repita en dos tipos de bienes.  
Si utiliza la codificación automática de bienes y se incluye prefijo el código de tipo de bien, no puede modificar el código del tipo de bien.

Descripción: es posible ingresar una descripción o referencia.

Rubro: seleccione el rubro al cual pertenece el tipo de bien.

Deprecia: indique si el tipo de bien estará habilitado para el cálculo de depreciación o no.

Método de depreciación: seleccione el método que desea utilizar para el cálculo de depreciación.

Unidad vida útil: si el método de depreciación interno elegido es del tipo 'Lineal' seleccione en qué unidad se va a expresar la vida útil, el sistema propone dos unidades: 'Años' y 'Meses'.

Unidad de medida: si el método de depreciación interno elegido es del tipo 'Capacidad de producción' seleccione en qué unidad de medida se va a expresar la cantidad producida esperada para el bien. Usted puede seleccionar una unidad de medida habilitada para el módulo de Activo Fijo.

Vida útil: si el método de depreciación interno elegido es del tipo 'Lineal', ingrese la duración de utilización del bien.

Cantidad: si el método de depreciación interno elegido es del tipo 'Capacidad de producción', ingrese la cantidad total esperada de producción del bien.

Porcentaje depreciable: informe el porcentaje del valor del bien para depreciar si el bien se deprecia por el total del valor del bien o por un porcentaje menor al 100%.

Frecuencia: seleccione la frecuencia de depreciación que desea utilizar para el cálculo de depreciación.

Valor fin vida útil: ingrese el valor que tiene el bien finalizada su vida útil

##### Cuentas contables

En esta ficha usted define las cuentas contables según el tipo de bien.

Sólo puede seleccionar cuentas contables que estén habilitadas para el módulo Activo Fijo y que no afecten ajuste por inflación del módulo de Tango Astor Contabilidad.

Usted podrá definir en forma opcional las siguientes cuentas: cuenta del bien, cuenta de compra, cuenta depreciación, cuenta depreciación extraordinaria, cuenta depreciación acumulada, cuenta para mejoras, cuenta revalúo, cuenta de baja, cuenta resultado ajuste, cuenta resultado por tenencia.

Estas cuentas se utilizarán en la generación del asiento contable según los distintos movimientos ingresados en [Registración de movimientos](?p=6749).

##### Identificaciones adicionales

Usted puede definir características comunes por tipo de bien para eso cree [Identificaciones adicionales](?p=5939) y luego asócielas desde esta solapa.

**Ejemplo...**

Podrá informar para los bienes que tengan asociados el tipo de bien Rodados todos los datos cómo modelo, patente, número de motor, etc.

##### Contenidos relacionados

  * [Videos sobre bienes de uso](https://ayudas.axoft.com/24ar/videos/afa_carp_vid/bienes_afa_vid/)
