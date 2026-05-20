# Modelos de asientos de Activo Fijo

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_cp/guia_integrcontabl_cp/?p=5933/

## Contenido

# Modelos de asientos de Activo Fijo

Esta opción permite definir prototipos o modelos de asientos, que luego pueden ser asociados a los [Tipos de movimientos](?p=5954) o pueden ser asociados a movimientos desde [Registración de movimientos](?p=6749).

Estos modelos permiten en forma agilizar y facilitar la generación del mini - asiento del movimiento para el bien o los bienes incluidos.  
Activo Fijo divide los datos de un modelo de asiento en tres fichas: Principal, Cuentas contables y Observaciones.

##### Principal del modelo de asiento

Esta ficha reúne los datos del encabezado del modelo de asiento.  
Al ingresar un modelo de asiento, usted debe asignarle un código, un tipo de asiento y un tipo de movimiento interno.

Código: cada modelo que usted defina se identificará por este código. Es posible ingresar hasta 10 caracteres. El sistema valida que sea único, es decir, que no se repita en dos modelos.

Descripción: es posible ingresar una descripción o referencia.

Tipo de asiento: los modelos de asientos son de un tipo de asiento específico. Usted puede definir varios modelos de un mismo tipo de asiento. Puede elegir u tipo de asiento habilitado para el módulo de Activo Fijo. Es un valor obligatorio.

Leyenda: por defecto se propone la leyendapor defecto para el tipo de asiento seleccionado. Puede modificarla eligiendo otra leyenda asociada al tipo de asiento seleccionado. Es un valor opcional.  
Para más información sobre leyendas para encabezados de asientos, consulte la ayuda del módulo Procesos generales.

Tipo de movimiento interno: este es un valor obligatorio para el modelo de asiento.

##### Cuentas contables

En esta ficha, usted define el cuerpo o renglones del asiento modelo.  
El sistema habilita los tipos contables según según el tipo de movimiento interno seleccionado y propone el modelo de asiento para el movimiento.

Detalle del modelo

Al agregar un nuevo modelo de asiento y pasar a esta solapa, el sistema propone el modelo de asiento de acuerdo al tipo de movimiento interno seleccionado en la solapa principal, usted tiene que asociarle las cuentas contables en el modelo.

_**Número:** _es el número de renglón del modelo. Este valor no puede modificarse.

_**Código de cuenta:**_ ingrese o seleccione la cuenta contable habilitada para Activo Fijo para el renglón.

_**Descripción de la cuenta:** _este dato se completa automáticamente al completar la columna "Cuenta".

_**D/H:**_ es el tipo de imputación que habitualmente lleva la cuenta en el modelo. Por defecto, se propone según el tipo de movimiento interno asociado al modelo.

**_Tipo contable:_** esta columna se propone según el tipo de movimiento interno asociado al modelo.

**_Stock:_** por defecto se propone la descripción del tipo contable pero es posible modificarla.

_**Reemplaza:**_ por defecto este parámetro está activado y al momento de generar el mini-asiento para el movimiento tomará la cuenta configurada para el bien según el tipo contable del modelo de asiento.

_**Edita cuenta:**_ por defecto se propone este parámetro activado y al momento de generar el mini-asiento si genera asiento en el ingreso del movimiento, permite cambiar la cuenta contable.

Detalle de apropiaciones

El ingreso de esta grilla es opcional y se habilita sólo si la cuenta contable usa auxiliares contables.

_**Tipo de auxiliar:** _ingrese o seleccione el código o descripción del auxiliar contable a utilizar en el modelo.

_**Regla de apropiación:**_ ingrese o seleccione el código o descripción de la regla de apropiación habilitadas para Activo Fijo a aplicar para el modelo.  
La regla de apropiación de un modelo de asiento tiene prioridad sobre la regla de apropiación por defecto asociada al tipo de auxiliar.  
Para más información, consulte en la ayuda en línea o en el manual del módulo **Procesos generales** , las opciones de la carpeta Auxiliares contables.

[/axoft_note] 

##### Modelo de asiento por tipo de comprobante interno

En esta solapa se detallan los asientos propuestos por el sistema según el tipo de movimiento interno seleccionado.

**Modelo de asiento propuesto para el tipo de movimiento interno de Activación**

**Cuenta** | **D/H** | **Tipo contable** | **Leyenda** | **Reemplaza** | **Edita cuenta**  
---|---|---|---|---|---  
Cuenta del bien (A) | D | BIEN | Valor del bien | Si | Si  
Cuenta puente compra (A) | H | COMP | Valor de compra | Si | Si  
  
**Modelo de asiento propuesto para el tipo de movimiento interno de Ajuste por inflación**

**Cuenta** | **D/H** | **Tipo contable** | **Leyenda** | **Reemplaza** | **Edita cuenta**  
---|---|---|---|---|---  
Cuenta del bien (A) | D | BIEN | Valor del bien | Si | Si  
Depreciación (R-) | D | DEP | Valor depreciación | Si | Si  
Depreciación acumulada (A) | H | DEPAC | Valor depreciación acumulada | Si | Si  
Resultado del ajuste (R-, R+) | H | AXI | Valor del ajuste por inflación | Si | Si  
  
**Modelo de asiento propuesto para el tipo de movimiento interno de Baja**

**Cuenta** | **D/H** | **Tipo contable** | **Leyenda** | **Reemplaza** | **Edita cuenta**  
---|---|---|---|---|---  
Seguros a cobrar (A) | D | SEG | Seguro a cobrar | No | Si  
Depreciación acumulada (A) | D | DEPAC | Valor depreciación acumulada | Si | Si  
Resultado por baja (R-, R+) | D | RDO | Resultado de la baja | Si | Si  
Cuenta del bien (A) | H | BIEN | Valor del bien | Si | Si  
  
**Modelo de asiento propuesto para el tipo de movimiento interno de Baja por Venta**

**Cuenta** | **D/H** | **Tipo contable** | **Leyenda** | **Reemplaza** | **Edita cuenta**  
---|---|---|---|---|---  
Depreciación acumulada (A) | D | DEPAC | Valor depreciación acumulada | Si | Si  
Resultado por baja (R-, R+) | D | RDO | Resultado de la baja | Si | Si  
Cuenta del bien (A) | H | BIEN | Valor del bien | Si | Si  
  
**Modelo de asiento propuesto para el tipo de movimiento interno de Depreciación**

**Cuenta** | **D/H** | **Tipo contable** | **Leyenda** | **Reemplaza** | **Edita cuenta**  
---|---|---|---|---|---  
Depreciación (R-) | D | DEP | Valor depreciación | Si | Si  
Depreciación acumulada (A) | H | DEPAC | Valor depreciación acumulada | Si | Si  
  
**Modelo de asiento propuesto para el tipo de movimiento interno de Depreciación extraordinaria**

**Cuenta** | **D/H** | **Tipo contable** | **Leyenda** | **Reemplaza** | **Edita cuenta**  
---|---|---|---|---|---  
Depreciación extraordinaria (R-) | D | DEPEX | Valor depreciación extraordinaria | Si | Si  
Depreciación acumulada (A) | H | DEPAC | Valor depreciación acumulada | Si | Si  
  
**Modelo de asiento propuesto para el tipo de movimiento interno de Mejora**

**Cuenta** | **D/H** | **Tipo contable** | **Leyenda** | **Reemplaza** | **Edita cuenta**  
---|---|---|---|---|---  
Cuenta mejora (A) | D | MEJ | Valor de la mejora | Si | Si  
Cuenta puente compra (A) | H | COMP | Valor de compra | Si | Si  
  
**Modelo de asiento propuesto para el tipo de movimiento interno de Revalúo**

**Cuenta** | **D/H** | **Tipo contable** | **Leyenda** | **Reemplaza** | **Edita cuenta**  
---|---|---|---|---|---  
Cuenta del bien (A) | D | BIEN | Valor del bien | Si | Si  
Cuenta revalúo (R+) | H | REV | Valor del revalúo | Si | Si  
  
**Modelo de asiento propuesto para el tipo de movimiento interno de Revalúo para generar asiento de Resultado por tenencia**

**Cuenta** | **D/H** | **Tipo contable** | **Leyenda** | **Reemplaza** | **Edita cuenta**  
---|---|---|---|---|---  
Cuenta del bien (A) | D | BIEN | Valor del bien | Si | Si  
Resultado por tenencia (R+,R-) | H | TCIA | Valor del resultado por tenencia | Si | Si  
  
**Valores posibles que podrá tomar el debe o el haber del renglón en el modelo de asiento según el tipo contable**

  * BIEN: este tipo contable toma el valor afectado al bien y si está activo en el modelo de asiento el parámetro Reemplaza toma la Cuenta del bien elegida en el bien.
  * COMP: este tipo contable toma el valor afectado al bien y si está activo en el modelo de asiento el parámetro Reemplaza toma la Cuenta de compra elegida en el bien.
  * DEP: este tipo contable toma el valor afectado a la depreciación del bien y si está activo en el modelo de asiento el parámetro Reemplaza toma la Cuenta depreciación elegida en el bien.
  * DEPEX: este tipo contable toma el valor afectado a la depreciación extraordinaria del bien y si está activo en el modelo de asiento el parámetro Reemplaza toma la Cuenta depreciación extraordinaria elegida en el bien.
  * DEPAC: este tipo contable toma el valor afectado a la depreciación del bien y si está activo en el modelo de asiento el parámetro Reemplaza toma la Cuenta depreciación acumulada elegida en el bien.
  * MEJ: este tipo contable toma el valor de la mejora afectado al bien y si está activo en el modelo de asiento el parámetro Reemplaza toma la Cuenta para mejoras elegida en el bien.
  * REV: este tipo contable toma el valor del revalúo afectado al bien y si está activo en el modelo de asiento el parámetro Reemplaza toma la Cuenta revalúo elegida en el bien.
  * RDO: este tipo contable toma el resultado calculado de la diferencia en el asiento entre las cuentas del debe y del haber. Si está activo en el modelo de asiento el parámetro Reemplaza toma la Cuenta de baja elegida en el bien.
  * AXI: este tipo contable toma el resultado calculado de la diferencia en el asiento entre las cuentas del debe y del haber. Si está activo en el modelo de asiento el parámetro Reemplaza toma la Cuenta resultado ajuste elegida en el bien.
  * TCIA: este tipo contable toma el valor informado del revalúo para el bien. Si el tipo de movimiento de revalúo tiene activado el parámetro Genera asiento de Resultado por tenencia" y además está activo en el modelo de asiento el parámetro Reemplaza toma la Cuenta resultado tenencia elegida en el bien.
  * SEG: este tipo contable toma el valor informado del seguro a cobrar en el movimiento de baja y no es posible activar el parámetro Reemplaza, siempre toma la cuenta contable informada en el modelo de asiento.
