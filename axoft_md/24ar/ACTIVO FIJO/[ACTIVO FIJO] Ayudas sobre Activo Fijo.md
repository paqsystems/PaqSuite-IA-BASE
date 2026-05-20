# Ayudas sobre Activo Fijo

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Activo Fijo
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_afa/guia_administracionbienes/?p=5016/

## Contenido

# Ayudas sobre Activo Fijo

El módulo **Activo Fijo** permite llevar a cabo la administración, el control y la contabilización de los bienes que forman parte del activo de la empresa, incluyendo procesos tales como registración de movimientos, depreciación de bienes, ajuste por inflación, generación de asientos y exportación de los mismos a **Contabilidad**.

##### Características generales

A continuación, realizamos una breve descripción de las opciones que componen el menú del módulo **Activo Fijo**.

**Archivos  
**Incluye el mantenimiento de los archivos maestros del sistema (bienes, agrupaciones de bienes como rubro, tipos de bienes, etc.); y carga inicial (como modelos de asientos, tipos de movimientos, etc.)

**Movimientos  
**Comprende la actualización de aquellos eventos (activación, mejoras, revalúo, etc.) producidos durante un período y que afectan a la depreciación de bienes y a la situación del bien a lo largo de su vida útil.

**Procesos periódicos  
**Abarca procesos que corresponden a funciones de cierta periodicidad, como depreciación de bienes, corrección monetaria, generación de asientos contables, y su traspaso a **Contabilidad**.

**Informes  
**Incluye el reporte del subdiario de asientos, el mismo facilita el control de los asientos generados con el detalle de auxiliares/subauxiliares de acuerdo a los movimientos registrados para los bienes.

##### Puesta en marcha de Activo Fijo

Sin parametrización inicial alguna, a medida que acceda a los procesos de Activo Fijo, Tango Astor lo guiará en la definición de parámetros y registros maestros.  
Si ejecuta un proceso que requiere datos que aún no han sido ingresados, Tango Astor lo guía en su ingreso, sin necesidad de que usted deba abandonar el proceso en ejecución.  
Para ubicar rápidamente los procesos citados en la ayuda, recuerde que la función Buscar (ubicada en el Menú del sistema, se activa pulsando la tecla <F3>) permite realizar una búsqueda de un texto en el árbol de procesos de todos los módulos. Como resultado, se exhibirá el nombre de los procesos que incluyen el texto ingresado, con la indicación del módulo y carpeta en la que se encuentran.  
Detallamos a continuación la secuencia sugerida de ingreso de parámetros y registros maestros:

**Módulo** | **Proceso** | **Detalle**  
---|---|---  
Procesos generales | [Empresa](?p=11858) | Defina los datos de la empresa legales y comerciales, identifique a la empresa con una sucursal.  
Procesos generales | [Sucursales](?p=11989) | Es un valor requerido para la empresa. Esta información requerida para centralizar información contable de otras sucursales o empresas generadas por otros módulos.  
Activo Fijo |  [Ejercicios](?p=5927) | Es un valor requerido para la carga movimientos en el sistema.  
Procesos generales | [Monedas](?p=11955) | Es un valor requerido para la carga de bienes y de movimientos. El sistema proporciona una moneda corriente y una moneda extranjera contable. Usted puede modificar el código y la descripción de la misma. Estas monedas también sirven para la integración con el módulo Compras y con el módulo Contabilidad.  
Procesos generales | [Tipos de cotización](?p=11995) | Es un valor requerido para definir una moneda del tipo 'Extranjera contable' o una moneda del tipo 'Otra moneda'. El sistema propone un tipo de cotización por defecto  
Procesos generales | [Parámetros contables](?p=11964) | Defina la moneda extranjera contable habitual para la integración con los módulos Compras y Contabilidad.  
Procesos generales | [Cuentas](?p=11849) | Es un valor requerido para la contabilización de movimientos y para la configuración de modelos de asientos en Activo Fijo.  
Procesos generales | [Tipos de asientos](?p=11994) | Es un valor requerido para la configuración de modelos de asientos en Activo Fijo.  
Procesos generales |  [Tipos de auxiliares](?p=11835) | No es un valor requerido. Si usted desea informar sub-imputaciones en los asientos contables generados en Activo Fijo, puede definir distintos criterios como tipos de auxiliares.  
Procesos generales |  [Auxiliares por cuenta](?p=11827) | No es un valor requerido. Si usted desea informar sub-imputaciones en los asientos contables generados en Activo Fijo, debe relacionar las cuentas que usan auxiliares contables con los tipos de auxiliares .  
Activo Fijo |  [Tipo de valoración](?p=5956) | Es un valor requerido, el sistema permite definir hasta tres tipos de valoración.  
Activo Fijo | [Métodos de depreciación](?p=5945) | El sistema propone el método lineal y el método por capacidad de producción.  
Activo Fijo | [Rubros](?p=5951) | Es un valor requerido para dar de alta los bienes en el sistema.  
Activo Fijo | [Tipos de bienes](?p=5955) | Es un valor requerido para dar de alta los bienes en el sistema.  
Activo Fijo | [Parámetros de Activo Fijo](?p=5948) | Es necesario definir la fecha de carga inicial o puesta en marcha del sistema y en caso de generar asiento en los movimientos debe definir el tipo de valoración para contabilizar.  
Activo Fijo | [Talonarios](?p=5953) | Es un valor requerido para poder generar movimientos.  
Activo Fijo | [Conceptos](?p=5908) | Es un valor opcional en la carga de movimientos.  
Activo Fijo | [Modelos de asientos](?p=5933) | Es un valor requerido para poder contabilizar los movimientos de los bienes  
Stock | [Artículos](?p=17195) | Es un valor opcional. Si usted desea dar de alta bienes desde el módulo Compras es necesario definir los artículos que representan bienes.  
Compras | [Conceptos de compra](?p=14626) | Es un valor opcional. Si usted desea asociar gasto a los bienes para la puesta en marcha, es necesario definir conceptos que representan gastos para bienes.  
Procesos generales | [Departamentos](?p=11852) | Es un valor opcional en la carga de bienes.  
Activo Fijo | [Ubicaciones](?p=5957) | Es un valor opcional en la carga de bienes.  
Activo Fijo | [Responsables](?p=5950) | Es un valor opcional en la carga de bienes.  
Activo Fijo | [Estados](?p=5912) | Es un valor opcional en la carga de bienes.  
Activo Fijo | [Identificaciones adicionales](?p=5939) | Es un valor opcional en la carga de bienes.  
Activo Fijo | [Bienes](?p=5938/#puesta-en-marcha-de-la-integracion-de-activo-fijo) | Es un valor requerido.  
  
##### Contenido dependiente

  * [Archivos](https://ayudas.axoft.com/24ar/ayudas/afa/archivos_afa/)
  * [Movimientos](https://ayudas.axoft.com/24ar/ayudas/afa/movimientos/)
  * [Procesos periódicos](https://ayudas.axoft.com/24ar/ayudas/afa/procesosperiodicos_afa/)
  * [Informes](https://ayudas.axoft.com/24ar/ayudas/afa/informes_carp_afa/)



##### Contenidos relacionados

  * [Videos sobre bienes de uso](https://ayudas.axoft.com/24ar/videos/afa_carp_vid/bienes_afa_vid/)
