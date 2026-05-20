# Guía de Restô sobre implementación de Tango Cobranzas

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv3/guia_nexocobr_gv3/

## Contenido

# Guía de Restô sobre implementación de Tango Cobranzas

Esta guía está orientada a todo aquel que desee implementar un circuito de cobranzas electrónicas a través de sistemas de pago en línea.

##### Puesta en marcha

Para comenzar a trabajar con [Tango Cobranzas](?p=12425) debe verificar la parametrización de su sistema.

**Vincule su empresa Tango con Tango Cobranzas  
**Es necesario vincular su empresa Tango con [Tango Cobranzas](?p=12425). Para ello siga los pasos indicados en la [puesta en marcha de Tango Cobranzas](?p=12440/#puesta-en-marcha).

**Tango Cobranzas**

  1. Ingrese a la aplicación a través del portal de nexo o directamente a la dirección <https://cobranzas.axoft.com>.
  2. Defina los parámetros generales y guarde la configuración.
  3. Asocie los sistemas de pago en línea que desee ofrecer a sus clientes como opciones de pago electrónico.



Para más información, haga clic [aquí](?p=12440/#puesta-en-marcha).

##### Puesta en marcha de Mercado Pago®

En esta pantalla puede asociar Tango Cobranzas con una cuenta de Mercado Pago® Chile.  
La vinculación se inicia haciendo clic en el botón "Asociar", lo que redireccionará a Mercado Pago® para que introduzca sus credenciales y posteriormente permita la conexión entre ambas aplicaciones.  
Si ya existe una sesión abierta de Mercado Pago® en el navegador, no le serán solicitados sus datos y la asociación se hará con dicho usuario. En caso de querer asociar Tango Cobranzas con otra cuenta, por favor cierre previamente esa sesión.  
Puede eliminar esta asociación posteriormente, si así lo desea.

###### Integración medios de pago de Mercado Pago®

Una vez asociada la cuenta de Mercado Pago®, tendrá disponible la acción "Integrar medios de pago". Este proceso le permitirá realizar la puesta en marcha para aceptar pagos de sus clientes a través de Mercado Pago®.  
Al ingresar a este proceso, en primer lugar, debe configurar la sucursal y luego crear las cajas QR asociadas a la sucursal. Para comenzar pulse en el mosaico "Sucursal". En esa pantalla se configuran los datos de la sucursal.  
Seleccione la opción que se ajuste a su configuración:

**Asociar a una nueva sucursal  
**Le permite crear una sucursal para operar con tu empresa asociándola a Mercado Pago®.  
Para ello, es necesario completar los siguientes datos:

  * **Nombre de sucursal:** es el nombre identificativo de la sucursal.
  * **Calle:** es la calle en la que se encuentra ubicada la sucursal.
  * **Número:** es la numeración de la calle que corresponde a la sucursal.
  * **Ciudad:** es la ciudad a la que pertenece la sucursal.
  * **Provincia:** es la provincia a la que pertenece la sucursal.



Al terminar de configurar la sucursal, pulse "Aceptar" para confirmar los cambios.

**Asociar a una sucursal ya creada en Mercado Pago®  
**Desde esta opción puede asociar tu sucursal de Tango Cobranzas con una que ya hayas creado previamente en Mercado Pago®. Recuerde que para hacer esto no debe estar siendo utilizada en otra empresa de Tango Cobranzas.  
Para ello, elija la sucursal ya creada en Mercado Pago® en "Seleccione la sucursal".  
Al terminar de configurar la sucursal, pulse "Aceptar" para confirmar los cambios.

**Cajas  
**Una vez configurada la sucursal, en la pantalla Integrar medios de pago, tendrá disponible el mosaico "Cajas". Púlselo para ingresar.  
En este proceso se administran las cajas que se van a utilizar, que por defecto se crearán asociadas a un código QR. Desde aquí podrá crear, editar o eliminar cajas.  
Para realizar la puesta en marcha de una caja, pulse en "Nueva" y complete los siguientes datos:

  * **Código de caja:** es un código alfanumérico que va a utilizar posteriormente para configurar la terminal.
  * **Descripción:** es una leyenda informativa a modo de descripción de esa caja.



Al terminar de crear la caja, pulse "Aceptar" para confirmar los cambios.  
Una vez creada la caja, aparecerá listada en la grilla de cajas.  
Para ver el código de QR generado para la caja recién creada, pulse dentro de la columna "Código QR", en el enlace "Ver". Este código QR es el que debe imprimir para operar con su caja de Mercado Pago® QR.

##### Preguntas frecuentes

**¿Cómo elimino una caja?  
**Para eliminar una caja, luego de ingresar en el proceso Integrar medios de pago, pulse en el mosaico "Cajas".  
Una vez dentro, elija la caja que desea eliminar y pulse la acción "Eliminar".

**Generé cajas en la web de Mercado Pago®, pero no las veo listadas en Tango Cobranzas. ¿Por qué?  
**Porque no serán consideradas para la integración con Tango Cobranzas aquellas cajas creadas a través del sitio de **Mercado Pago®**. Para operar con la aplicación deberá crear sus cajas desde el proceso Cajas exclusivamente.

**¿Cómo obtengo el código QR?  
**Para descargar o imprimir el código QR, luego de ingresar en el proceso Integrar medios de pago, pulse en el mosaico "Cajas".  
Una vez dentro, elija la caja de la cual desea obtener el QR y pulse el enlace "Ver" dentro de la columna "Código QR".

**¿Puedo regenerar el código QR asociado a una caja?  
**No, el código QR es fijo y sirve para identificar una caja de manera permanente. Para utilizar otro código QR, debe eliminar la caja y crear una nueva.

**¿En qué orden realizo la puesta en marcha de Mercado Pago® QR?  
**Asocie su cuenta de Mercado Pago® con la acción "Asociar".  
Configure la sucursal con la que deseas operar.

  1. Cree una caja QR.
  2. Descargue el código QR y déjelo a la vista de sus clientes para que lo puedan escanear con la aplicación de **Mercado Pago®**.



##### Contenidos relacionados

No se ha encontrado ninguno
