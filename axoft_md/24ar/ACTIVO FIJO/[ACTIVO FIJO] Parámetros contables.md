# Parámetros contables

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Activo Fijo
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_afa/guia_administracionbienes/?p=11964/

## Contenido

# Parámetros contables

Algunos de los siguientes parámetros contables son de aplicación opcional y en caso de definirlos, serán propuestos por defecto en los distintos procesos.

El sistema divide los datos para el ingreso de parámetros generales en dos solapas más la solapa Observaciones.

##### Parametrización contable

Utiliza máscara para las cuentas contables: indique si utiliza una máscara en particular para el ingreso del código de cuentas contables. Por defecto, este parámetro no está activo.  
Si usted activa este parámetro y existen [cuentas contables](?p=11850), el sistema solicita su confirmación para recodificar los códigos según la nueva máscara y el separador elegidos.  
Si usted desactiva este parámetro, el sistema solicita su confirmación para eliminar los separadores de las cuentas. Si no confirma esta operación, el parámetro queda activado.

Separador: indica cuál es el separador en la máscara de las cuentas contables. Este campo está disponible sólo si utiliza máscara para las cuentas contables. Por defecto, se utiliza el punto (.).

Al presionar la tecla <F10>, el sistema solicita su confirmación para actualizar el separador en el código de cuentas. Si no confirma esta operación, se mantiene el separador anterior.

Máscara: si está activo el parámetro Utiliza máscara para las cuentas contables, indique el formato de la máscara. Para ello, utilice el carácter X y el separador elegido. El sistema valida que no existan códigos de cuenta con una longitud mayor a la longitud de la máscara. En ese caso, solicita que modifique el formato de la máscara.

Ejemplo: en este campo se exhibe una representación según la máscara ingresada.

Completar con ceros a: este campo se habilita sólo si se modifica la máscara y ya existen cuentas contables. Los valores posibles son 'Derecha' o 'Izquierda'. Por defecto, se considera la opción 'Derecha'.  
Siempre que utilice máscara para las cuentas contables, el código de la [cuenta contable](?p=11850) respeta la máscara elegida. Si agranda la máscara, se completan los códigos de cuentas contables existentes con ceros a derecha o izquierda (según lo indicado en el campo Completar con ceros a).

Código de moneda extranjera contable habitual: elija la [moneda](?p=11956) de tipo 'Extranjera contable' a utilizar por defecto. Este valor es obligatorio para la integración contable con el módulo Contabilidad y los módulos Compras, Ventas y Tesorería.

Código de jerarquía habitual: elija la jerarquía a utilizar por defecto. Este parámetro se habilita si usted posee el módulo Contabilidad en su sistema. Se puede utilizar si integra con Contabilidad desde el módulo CashFlow.

##### Integración contable

Número de lote: ingrese el número de lote contable a generar, en caso de exportar asientos contables.

Elimina los archivos de integración entre módulos al procesar importaciones: por defecto este parámetros está desactivado. Si usted lo activa cada vez que realice una importación de archivo, el mismo será eliminado del directorio de origen.

Comportamiento para el alta de nuevos registros: para definir el comportamiento que desea adoptar referido a la parametrización contable al momento del alta de nuevos registros (artículos, conceptos de compras, proveedores, cuentas de tesorería, clientes, clientes IVA, proveedores IVA). No aplica al alta de plantillas.

  * Confirma: al momento del alta del nuevo registro se va a visualizar la parametrización contable con la opción de modificarlo.
  * Muestra: al momento del alta del nuevo registro se va a visualizar la parametrización contable pero no podrá modificarla.
  * Oculta: no se va a visualizar la configuración contable del nuevo registro que se da de alta.



Al momento de dar de alta una factura de compras, se puede dar de alta un nuevo artículo, de acuerdo a la configuración que haya realizado en este proceso, podrá modificar, consultar o directamente ocultar la parametrización contable.

##### Contenidos relacionados

  * [Video sobre ajustes en Compras](https://ayudas.axoft.com/24ar/videos/cp2_carp_vid/ajustes_cp2_vid/)

  * [Video sobre diferencia de cambio en Compras](https://ayudas.axoft.com/24ar/videos/cp2_carp_vid/diferenciacambio_cp2_vid/)

  * [Video sobre diferencia de cambio en Ventas](https://ayudas.axoft.com/24ar/videos/gv_carp_vid/diferenciacambio_gv_vid/)
