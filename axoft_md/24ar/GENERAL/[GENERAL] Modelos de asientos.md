# Modelos de asientos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_integrcont_gla/?p=9803/

## Contenido

# Modelos de asientos

Esta opción permite definir prototipos o modelos de asientos, que luego pueden ser utilizados en la carga manual de [asientos](?p=9755) o desde el proceso de [Generación masiva de asientos](?p=9784). En ambos casos, estos modelos agilizan y facilitan a usted el ingreso de asientos.

Contabilidad divide los datos de un modelo de asiento de contabilidad en las siguientes solapas: [Principal](?p=9803#principal), [Cuentas contables](?p=9803#cuentascontables), [Parametrización](?p=9803#parametrizacion), Observaciones y Datos Adicionales.

##### Principal

Esta solapa reúne los datos del encabezado del modelo de asiento.  
Al ingresar un modelo de asiento, usted debe asignarle un código y un tipo de asiento.

Código: cada modelo que usted defina se identificará por este código. Es posible ingresar hasta 10 caracteres. El sistema valida que sea único, es decir, que no se repita en dos modelos.

Descripción: es posible ingresar una descripción o referencia.

Tipo de asiento: los asientos modelo son de un tipo de asiento específico. Usted puede definir varios modelos de un mismo tipo de asiento. Para más información sobre tipos de asiento, consulte la ayuda en línea o el manual electrónico del módulo Procesos generales.

Leyenda: de manera opcional, ingrese un texto o leyenda para el encabezado del modelo en pantalla.  
Haga clic en el botón correspondiente para seleccionar una leyenda predeterminada para el encabezado del modelo. Cada leyenda está identificada por un código y una descripción.

Para más información sobre leyendas para encabezados de asientos, consulte la ayuda del módulo Procesos generales.

##### Cuentas contables

En esta solapa, usted define el cuerpo o renglones del asiento modelo.  
Acceda a las opciones asociadas a cada dato de la grilla, haciendo clic en el botón derecho del mouse.

**Detalle del modelo**

Nro.: es el número de renglón del modelo.

Cuenta: ingrese o seleccione la [cuenta contable](?p=9774) para el renglón.  
Si usted ingresa en su lugar, la Descripción de la cuenta, este dato se completa automáticamente.

Descripción de la cuenta: este dato se completa automáticamente al completar la columna "Cuenta". Sin embargo, también es posible seleccionar la cuenta mediante su descripción. En ese caso, la columna "Cuenta" se completará automáticamente.

D/H: es el tipo de imputación que habitualmente lleva la cuenta en el modelo. Por defecto, se propone 'D'.

Fórmula / Importe: ingrese la fórmula o el importe del renglón. Una fórmula se define ingresando directamente su gramática, o bien haciendo clic en el botón "..." para invocar al asistente de [Definición guiada de fórmulas para Contabilidad](?p=9791/#definicion-guiada-de-formulas-para-contabilidad). Esta columna se utilizará desde el proceso [Generación masiva de asientos](?p=9784).

Código de leyenda / Descripción de la leyenda: es posible asociar una leyenda por defecto a cada línea o renglón del asiento modelo.  
Usted puede elegir la leyenda según su código o su descripción. La columna restante se completará automáticamente.  
Para más información sobre leyendas para líneas de asientos, consulte la ayuda en línea del módulo Procesos generales.

**Detalle de apropiaciones**

El ingreso de esta grilla es opcional y se habilita sólo si la cuenta contable usa auxiliares contables.

Tipo de auxiliar: ingrese o seleccione el código o descripción del auxiliar contable a utilizar en el modelo. Sólo se pueden seleccionar o ingresar tipos de auxiliares manuales.

Regla de apropiación: ingrese o seleccione el código o descripción de la regla de apropiación a aplicar para el modelo.  
La regla de apropiación de un modelo de asiento tiene prioridad sobre la regla de apropiación por defecto asociada al tipo de auxiliar.  
Para más información, consulte en la ayuda en línea o en el manual electrónico del módulo Procesos generales, las opciones de la carpeta Auxiliares contables.

##### Parametrización

Habilitado para generación masiva de asientos: por defecto este parámetro estará desactivado. Si lo activa, podrá configurar el modelo de asiento para ser utilizado desde el proceso Generación masiva de asientos.

Generación: seleccione esta opción si desea generar Asientos o Contra - asientos.

Asientos: seleccione si desea generar asientos Contables o Extracontables.

Moneda del asiento: indique la moneda de ingreso del asiento a generar, podrá ser la moneda corriente o alguna moneda extranjera contable. Por defecto se propone la moneda corriente.

Clase de asiento: indique la clase de asiento del asiento a generar. Por defecto se propone la clase de asiento Básico.

Asientos generados: al presionar este botón se accede a la consulta de todos los asientos generados por este modelo de asiento. Haciendo doble clic sobre cada asiento, se accede a la pantalla de asientos.

##### Contenidos relacionados

  * [Videos sobre parametrización contable](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/paramcontab_gral_vid/)
