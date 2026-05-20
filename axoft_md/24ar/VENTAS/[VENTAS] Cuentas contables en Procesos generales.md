# Cuentas contables en Procesos generales

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv/guia_integrcont_gv/?p=11850/

## Contenido

# Cuentas contables en Procesos generales

Registre los datos y parámetros de las cuentas imputables para Contabilidad.

Las cuentas no imputables se definen en la opción [Jerarquías](?p=9794) del módulo Contabilidad.  
Se dividen los datos de una cuenta contable imputable en las siguientes solapas:

  * **Principal:** con los datos de identificación y habilitación de la cuenta imputable.
  * **Leyendas:** con la configuración de leyendas por defecto para la registración de la cuenta en el Debe o en el Haber del asiento contable.
  * **Módulos:** se indican los módulos para los que está habilitada la cuenta contable.
  * **Observaciones:** con el comentario o texto que haya ingresado, en forma opcional, para la cuenta.



Estas solapas contienen información de tipo general, es decir, pueden definirse desde este proceso o bien, desde la opción [Cuentas contables](?p=9774) del módulo Contabilidad.

##### Datos a ingresar en una nueva cuenta

Para dar de alta una cuenta contable imputable sólo necesita ingresar los siguientes datos:

Código de cuenta: es posible utilizar letras, números y caracteres especiales, hasta un máximo de 20 posiciones.

En la opción [Parámetros generales](?p=12044) puede definir una máscara para el ingreso del código de cuenta. En ese caso, el código a ingresar debe respetar la máscara parametrizada.  
En la definición de las estructuras de árbol o jerarquías podrá utilizar este código u otro, por lo que no es necesario que este código responda a las necesidades de definición del árbol de cuentas contables. Para más información, consulte la opción Jerarquías en la ayuda en línea o en el manual electrónico del módulo Contabilidad.

Clase de cuenta: indica la naturaleza de la cuenta contable. Asigne una de las siguientes clases a la cuenta en pantalla:

  * **A:** Activo
  * **P:** Pasivo
  * **PN:** Patrimonio Neto
  * **R+:** Resultado positivo
  * **R-:** Resultado negativo
  * **RA:** Resultados acumulados
  * **RE:** Resultado del ejercicio



Sólo es posible modificar este dato si la cuenta contable está sin clasificar. Este caso corresponde a las cuentas definidas en Tango Contabilidad y cuya información fue migrada a Contabilidad.

Tipo de cuenta: por defecto, se propone como tipo de cuenta no monetaria. La clasificación de las cuentas en monetaria o no monetaria no se considera en los procesos automáticos como ajuste por inflación o conversión a moneda extranjera contable. Estos procesos tienen su propia configuración.

Saldo habitual: se completa por defecto, según la clase de cuenta seleccionada. El sistema tiene en cuenta esta definición para los listados de control de saldos.

Usa auxiliares contables: si desea que a la cuenta contable se le puedan asociar auxiliares contables deberá, como primera medida, activar este parámetro.

##### Leyendas para cuentas

Es posible asociar a la cuenta contable, leyendas para los asientos.  
Para ello, complete la grilla de esta solapa, de la siguiente manera:

  1. Seleccione el Código o Descripción de una leyenda para líneas de asientos.
  2. Indique la columna en la que se aplicará la leyenda (Debe / Haber).
  3. De manera opcional, es posible elegir entre las leyendas incluidas en la grilla, una leyenda por defecto para el Debe y otra para el Haber (Si / No).



El sistema valida que el código de leyenda ingresado en la grilla sea único.  
Para más información, consulte la opción [Leyendas para líneas de asientos](?p=11952).

##### Módulos para cuentas

En esta solapa se indican los módulos en los que está habilitada la cuenta contable.  
Desafecte o destilde el o los módulos para los que no desea habilitar la cuenta.

##### Contenidos relacionados

  * [Video sobre cierre de ejercicio](https://ayudas.axoft.com/24ar/videos/cna_carp_vid/cierreejerc_cna_vid/)

  * [Video sobre imputación contable Sueldos](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/imputcontsueldos_gral_vid/)

  * [Video sobre planes de cuentas contables](https://ayudas.axoft.com/24ar/videos/cna_carp_vid/plancuentas_cna_vid/)

  * [Videos sobre asientos contables en Sueldos](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/asientocontabl_sua_vid/)

  * [Videos sobre auxiliares contables y contabilidad por proyectos](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/conproyectos_cna_vid/)

  * [Videos sobre imputaciones contables](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/impcont1_gral_vid/)

  * [Videos sobre parametrización contable](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/paramcontab_gral_vid/)
