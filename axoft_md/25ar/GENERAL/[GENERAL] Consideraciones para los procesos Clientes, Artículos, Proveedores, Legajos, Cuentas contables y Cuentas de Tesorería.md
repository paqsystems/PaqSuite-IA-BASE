# Consideraciones para los procesos Clientes, Artículos, Proveedores, Legajos, Cuentas contables y Cuentas de Tesorería

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Operación
- URL: https://ayudas.axoft.com/25ar/documentos/operacion/apertura_oper/excel_oper/excel_consideracion_oper/

## Contenido

# Consideraciones para los procesos Clientes, Artículos, Proveedores, Legajos, Cuentas contables y Cuentas de Tesorería

A continuación, te detallamos las consideraciones particulares que tienen estos procesos:

  * **Plantilla para ingresar los datos indispensables:** debido a la gran cantidad de campos que poseen estos procesos, te proponemos una plantilla con los datos mínimos que pensamos que vas a completar en Excel; tené en cuenta que podés incorporar otras columnas de acuerdo con tus necesidades.
  * **Uso de plantillas durante la importación:** los procesos [Clientes](?p=19466), [Legajos](?p=11999) y [Artículos](?p=17285) ofrecen la posibilidad de definir valores por defecto para los principales campos de los respectivos procesos a través del uso de plantillas. Durante la importación del archivo Excel podrás seleccionar una para completar las celdas que no tengan valor para cada registro. Tené en cuenta que esto aplica también para aquellas columnas que son obligatorias (pintadas en amarillo). Por ejemplo, si tenés definida una plantilla en la que la unidad de medida de los artículos es el código "UNI" podrás no completar esa columna en el archivo Excel y asignaremos a el valor "UNI" a todos artículos que no tengan especificada una unidad de medida.
  * **Asignación de valores por defecto durante la importación:** si el proceso no contempla el uso de plantillas o simplemente no acostumbras a utilizarlas, tené en cuenta que completaremos cada celda vacía con el mismo valor que proponemos durante el uso habitual del sistema. Por ejemplo, durante la creación de artículos consideramos que los artículos "no usan escalas"; si no completas esa celda asumiremos que el registro a importar tampoco lo usa. Otros campos pueden tener un valor por defecto que surge de los parámetros generales de cada módulo; por ejemplo, para el caso de artículos podés definir las alícuotas de IVA que utilizás habitualmente para Compras y Ventas. Si en general aplicás la alícuota del 21% a todos tus artículos podés ignorar en el archivo Excel la columna "IVA Ventas" ya que el sistema completará las celdas vacías con lo definido en [Parámetros generales de Stock](?p=17198). Si algún artículo debe aplicar una alícuota específica, bastará con que completes esa celda para ese registro en particular.  
Para conocer los valores por defecto que asumirá el sistema te sugerimos que pruebes ingresar manualmente un registro; por ejemplo, ingresá al proceso [Artículos](https://ayudas.axoft.com/25ar/articulo_carp_st) y pulsá la opción "Nuevo". Todos los valores por defecto que veas en pantalla serán los mismos que asignemos a las celdas que no completes en el archivo Excel.
  * **Codificación automática de clientes / proveedores:** tené en cuenta que la importación de Excel de estos procesos no respeta la codificación automática definida en [Parámetros de Ventas](?p=19401) / [Parámetros de Compras](?p=14676). Si utilizás este tipo de codificación y querés importar nuevos registros deberás asignar los códigos siguiendo los lineamientos de esa codificación ya que Tango no verificará la secuencialidad ni el uso de prefijos.
  * **Codificación de artículos de tipo "combinación":** recordá que el código de los artículos de tipo combinación (escalas) se forma por CODIGO DE ARTICULO BASE + VALOR ESCALA 1 + VALOR ESCALA 2; por ejemplo, 010030001BLA siendo 010030 el código de artículo base, 001 el valor correspondiente a los ventiladores con palas de madera y BLA el correspondiente a los ventiladores de color blanco. Si tenés dudas sobre cómo se compone la codificación de tu artículo te recomendamos que pruebes creando un artículo de prueba en el proceso [Artículos](https://ayudas.axoft.com/25ar/articulo_carp_st).
