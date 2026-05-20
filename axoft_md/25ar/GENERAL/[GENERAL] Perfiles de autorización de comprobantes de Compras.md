# Perfiles de autorización de comprobantes de Compras

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_guiagenerarchpdf_gla/?p=14679/

## Contenido

# Perfiles de autorización de comprobantes de Compras

Utilice este proceso para definir los perfiles de autorización de comprobantes a pagar, para los distintos usuarios.

Usted tendrá acceso a este proceso sólo si está activo el [parámetro general](https://ayudas.axoft.com/25ar/paramgrales_cp2/#parametros-para-comprobantes) Requiere autorización para el pago.  
Los perfiles definidos mediante esta opción se utilizarán en el proceso [Autorización de comprobantes a pagar](https://ayudas.axoft.com/25ar/ccorrautcomprpagar_cp2).  
Los perfiles de autorización permiten adaptar la selección de los comprobantes en el proceso mencionado a los requerimientos de su empresa, como así también determinar restricciones para algunos usuarios en particular.  
La autorización de comprobantes para su pago puede estar a cargo de más de una persona. Por ello, es posible seleccionar para cada perfil, los valores a tener en cuenta en la autorización (o desautorización) de un comprobante a pagar.  
La definición de perfiles no es obligatoria.  
Cada perfil está identificado por un código de perfil y tiene asociada una descripción.  
Defina también los siguientes datos:

  * El importe máximo para facturas.
  * El importe máximo para notas de débito.
  * El importe máximo para notas de crédito.



Tenga en cuenta que los valores del importe mínimo para facturas, notas de débito y notas de crédito serán tomas desde la configuración realizada en [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2/#parametros-para-comprobantes).  
La moneda de expresión de estos valores es la definida en el proceso [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2).  
Es posible definir para cada tipo de comprobante (facturas, notas de crédito y notas de débito), un importe mínimo y un importe máximo a autorizar. El importe mínimo a autorizar se define en el proceso [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2). El importe máximo a autorizar por cada comprobante lo define en cada perfil de autorización de comprobantes a pagar.  
El sistema valida que el importe ingresado como importe máximo para cada uno de los comprobantes no sea inferior al importe mínimo a autorizar.  
En el momento de ingresar al proceso [Autorización de Comprobantes a Pagar](https://ayudas.axoft.com/25ar/ccorrautcomprpagar_cp2), el sistema realizará los siguientes controles:

  * Si no se definieron perfiles, se tendrá en cuenta la definición de [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2) de este módulo.
  * Si el usuario que ingresa tiene definido un sólo perfil, éste se utilizará en el proceso.
  * Si el usuario que ingresa tiene definido más de un perfil, podrá seleccionar el perfil a utilizar.
  * Si se definieron perfiles pero el usuario que ingresa no está asignado a ninguno, se tendrá en cuenta la definición de [Parámetros de Compras](https://ayudas.axoft.com/25ar/paramgrales_cp2) de este módulo.



Una vez generado un perfil, es necesario asociar los usuarios habilitados a utilizarlo.

##### Usuarios

A través de este comando se ingresan los usuarios habilitados para el perfil activo (el que se encuentra en pantalla).  
El sistema sugiere, por defecto, el usuario que está trabajando en ese momento en el sistema, siendo posible agregar otros.  
Luego de ingresar el último usuario, es necesario posicionarse en el renglón siguiente pulsando <Enter> y confirmar el proceso pulsando <F10> para que se almacenen los datos ingresados.

##### Contenidos relacionados

  * [Perfiles de solicitud de compra](https://ayudas.axoft.com/25ar/ayudas/cp2/archivos_carp_cp2/cargainicial_cp2/perfiles_carp_cp2/perfsolicitudcp_cp2/)

  * [Videos sobre autorizaciones](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/autorizaciones1_gral_vid/)

  * [Videos sobre órdenes de pago individual y masivo](https://ayudas.axoft.com/25ar/videos/cp2_carp_vid/ordenpago_cp2_vid/)
