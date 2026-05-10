# Parametrización contable en Ventas - Modelos de asientos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_integrcont_gla/?p=19368/

## Contenido

# Parametrización contable en Ventas - Modelos de asientos

Esta opción permite definir prototipos o modelos de asientos, que luego pueden ser asociados a los [Tipos de comprobantes](https://ayudas.axoft.com/24ar/tipocomprobparamcont_gv) o pueden ser asociados a los comprobantes desde el ingreso de los mismos.

Estos modelos permiten agilizar y facilitar la generación de asientos contables del comprobante.  
Ventas divide los datos de un modelo de asiento en dos solapas.

##### Principal de un modelo de asiento

Esta solapa contiene los datos del encabezado del modelo de asiento.  
Al ingresar un modelo de asiento, asígnele un código, un tipo de asiento y habilite el modelo para uno o varios tipos de comprobantes (facturas, notas de débito y/o notas de crédito)

Código: cada modelo que usted defina se identificará por este código. Será posible ingresar hasta 10 caracteres.  
El sistema valida que sea único, es decir, que no se repita en dos modelos.

Descripción: en este campo podrá ingresar una descripción o referencia.

Tipo de asiento: desde aquí podrá seleccionar un tipo de asiento habilitado para el módulo, este es un dato obligatorio.  
Los tipos de asiento responden a una clasificación arbitraria, definida por usted. Puede definir varios modelos de asientos para un mismo tipo de asiento.  
Esta información será utilizada desde el módulo Contabilidad para emitir listados filtrando o agrupando por tipo de asiento.

Leyenda: se propone la leyenda defecto para el tipo de asiento seleccionado.  
Puede modificarla eligiendo otra leyenda asociada al tipo de asiento seleccionado. Es un valor opcional.  
Para más información sobre leyendas para encabezados de asientos consulte la ayuda en línea o el manual del módulo Procesos generales.

Por último, habilite el modelo de asiento para uno o más tipos de comprobantes (facturas, notas de débito y/o notas de crédito) para asignarle al asiento modelo que se está ingresando. Esta habilitación se utilizará como filtro en el momento de seleccionar el modelo de asiento defecto en el tipo de comprobante, o al seleccionar el modelo de asiento desde el ingreso de comprobantes.

##### Cuentas contables de un modelo de asiento

En esta solapa, usted define el cuerpo o renglones del asiento modelo.  
El sistema habilita los tipos contables según el tipo de comprobante seleccionado y propone el modelo de asiento para el comprobante:

  * [Detalle](https://ayudas.axoft.com/24ar/modeloasientoparamcont_gv#detalle_modelo) del modelo
  * Detalle de apropiaciones



**Detalle del modelo**

Nro: es el número de renglón del modelo. Este valor no puede modificarse.

Código de cuenta: ingrese o seleccione la cuenta contable habilitada para Ventas para el renglón.

Descripción de la cuenta: este dato se completa automáticamente al completar la columna "Cuenta".

D/H: es el tipo de imputación que habitualmente lleva la cuenta en el modelo.  
Por defecto, se propone el valor 'D' si el saldo habitual definido para la cuenta es deudor, o 'H' si el saldo habitual definido para la cuenta es acreedor.

Tipo contable: esta columna se propone según el tipo de comprobante asociado al modelo.

Leyenda: en este campo aparece automáticamente la descripción del tipo contable. Si lo desea, podrá modificar este valor. No es un valor obligatorio.

Reemplaza: este parámetro se activa sólo para los tipos contables que permiten el reemplazo de cuentas contables.  
En el caso del módulo Ventas se habilita para los tipos 'TO', 'SB' y 'EX'. Si se activa este parámetro en el momento de generar el asiento para el comprobante tomará la cuenta configurada para el cliente, o para los artículos que participan en el comprobante.

Edita cuenta: de manera predeterminada, este parámetro se encuentra desactivado. En el momento de generar el asiento en el ingreso del comprobante, permitirá cambiar la cuenta contable.

**Detalle de apropiaciones  
**El ingreso de esta grilla es opcional y se habilita sólo si la cuenta contable usa auxiliares contables.

Tipo de auxiliar: ingrese o seleccione el código o descripción del auxiliar contable a utilizar en el modelo. Sólo se podrán asociar tipos de auxiliares manuales.

Regla de apropiación: ingrese o seleccione el código o descripción de la regla de apropiación habilitada para el módulo Ventas.  
La regla de apropiación de un modelo de asiento tiene prioridad sobre la regla de apropiación por defecto asociada al tipo de auxiliar.

Para más información, consulte en la ayuda del módulo Procesos Generales, las opciones de la carpeta Auxiliares contables.

##### Contenidos relacionados

  * [Video de contabilización automática en cadenas](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/contabilcadenas_gral_vid/)

  * [Video sobre automatización contable](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/automcontable_gral_vid/)

  * [Video sobre integración contable](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/integrcontable_gral_vid/)

  * [Video sobre parametrización contable centralizada](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/centralizaparamcontab_gral_vid/)

  * [Videos sobre imputaciones contables](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/impcont1_gral_vid/)
