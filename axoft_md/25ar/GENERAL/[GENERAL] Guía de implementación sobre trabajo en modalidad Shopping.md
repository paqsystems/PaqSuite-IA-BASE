# Guía de implementación sobre trabajo en modalidad Shopping

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_guiagenerarchpdf_gla/?p=6179/

## Contenido

# Guía de implementación sobre trabajo en modalidad Shopping

Si tiene un punto de venta operando en un centro comercial perteneciente a alguno de los siguientes grupos: Grupo Alto Palermo S.A., Caballito Shopping Center, Solar de la Abadía, Nuevo Centro o Grupo IRSA - Interfaz Fiserv, Grupo Fortin Maure - Interfaz Solutions Malls; puede generar desde el módulo Ventas la información requerida por estos centros comerciales.

En este caso, es necesario definir una serie de parámetros que se tendrán en cuenta en el momento de generar comprobantes de facturación (facturas, notas de crédito, notas de débito y anulaciones).

##### Puesta en marcha

Para comenzar a trabajar con la modalidad 'Shopping' debe verificar la parametrización de su sistema.  
Acceda a [Parámetros de Ventas | Comprobantes](?p=19401/#parametros-para-comprobantes), en la sección Integración con shoppings debe indicar:

Genera información para shoppings: mediante este parámetro, define el grupo de Shopping al que pertenece, siendo posible:

  * No utiliza.
  * Grupo Alto Palermo S. A.
  * Caballito Shopping Center.
  * Solar de la Abadía.
  * Nuevo Centro.
  * Grupo IRSA - Interfaz Fiserv.
  * Grupo Fortin Maure - Interfaz Solutions Malls.



###### Grupo Alto Palermo S.A.

Rubro del local: ingrese el número de rubro del local, el que es provisto y definido por el soporte técnico de cada Shopping.

Número de contrato: ingrese el número de contrato del local, el que es provisto y definido por el soporte técnico de cada Shopping.

Número de local: ingrese el código que identifica al local dentro del centro comercial, el que es provisto y definido por el soporte técnico de cada Shopping.

Ubicación del archivo local: indique la ruta en que se guarda localmente el archivo generado para Shopping.

Ubicación del archivo remoto: indique la ruta en que se guarda en la red el archivo generado para Shopping.

Punto de venta por terminal: ingrese el código que identifica a la terminal, puesto o caja dentro del local.

Una vez configurados los parámetros de Ventas, acceda a [Cuentas de Tesorería](?p=10235). Para cada cuenta de tesorería se deben configurar los Datos para archivo shopping.

Clase de cuenta: debe indicar la forma de pago asociada a la cuenta. Los medios de pago a configurar para el Grupo Alto Palermo son:

**E** | Efectivo  
---|---  
**T** | Tarjeta  
**A** | Alto Check  
**C** | Cheques  
**D** | Dólares  
**K** | Cuenta corriente  
**O** | Otro medio de pago  
  
Código para tarjeta: debe definir el código de tarjeta a informar cuenta la cuenta es de tipo 'Tarjeta'. Los códigos de tarjeta a configurar para el Grupo Alto Palermo son:

**MC** | MasterCard  
---|---  
**VI** | Visa  
**EL** | Visa Electrón  
**AM** | American Express  
**TS** | Tarjeta Shopping  
**DI** | Diners  
**SC** | Tarjeta Shopping Cash  
**TN** | Tarjeta Naranja  
**PC** | Provencred  
**LI** | Líder  
**MA** | Maestro  
**TV** | Tarjeta Nevada  
**AG** | Argencard  
**CA** | Cabal  
**CI** | Credicred  
**CR** | Credencial  
**IC** | Italcred  
**MI** | Mira  
**TF** | Tarjeta CRM Falabella  
**MS** | Tarjeta Musimundo  
**PL** | C&A Private Label  
**DT** | Tarjeta Data 2000  
**MP** | Tarjeta Mendoza Plaza Shopping  
**AZ** | Tarjeta Azul  
**CD  
** | Cabal Débito (24 Horas)  
  
Será posible configurar en la cuenta otro código que no exista en esta lista, con sólo ingresarlo en el campo. En este caso, el sistema lo informará en el archivo como un nuevo código de tipo 'Tarjeta'.

###### Caballito Shopping Center

Rubro del local: ingrese el número de rubro del local, el que es provisto y definido por el soporte técnico de cada Shopping.

Número de contrato: ingrese el número de contrato del local, el que es provisto y definido por el soporte técnico de cada Shopping.

Número de local: ingrese el código que identifica al local dentro del centro comercial, el que es provisto y definido por el soporte técnico de cada Shopping.

Ubicación del archivo local: indique la ruta en que se guarda localmente el archivo generado para Shopping (.sdf).

Ubicación del archivo remoto: indique la ruta en que se guarda en la red el archivo generado para Shopping (.sdf).

Punto de venta por terminal: ingrese el código que identifica a la terminal, puesto o caja dentro del local.

Una vez configurados los parámetros de Ventas, acceda a [Cuentas de Tesorería](?p=10235). Para cada cuenta de tesorería se deben configurar los Datos para archivo shopping.

Clase de cuenta: debe indicar la forma de pago asociada a la cuenta. Los medios de pago a configurar para Caballito Shopping Center son:

**1** | Efectivo  
---|---  
**2** | Tarjeta  
**3** | Cheque  
**4** | Efectivo dólar  
**6** | Otro medio de pago  
  
Código para tarjeta: debe definir el código de tarjeta a informar cuenta la cuenta es de tipo 'Tarjeta'. Los códigos de tarjeta a configurar para Caballito Shopping Center son:

**1** | Mastercard  
---|---  
**2** | Visa  
**3** | Visa electrón  
**4** | American Express  
**5** | Diners  
**6  
** | Naranja  
**7  
** | Provencred  
**8  
** | Líder  
**9  
** | Maestro  
**10  
** | Nevada  
**11  
** | Argencard  
**12  
** | Cabal  
**13  
** | Carta Franca  
**14  
** | Credencial  
**15  
** | Italcred  
**16  
** | Mira  
  
De todas maneras, será posible configurar en la cuenta, otro código que no exista en esta lista, con sólo ingresarlo en el campo. En este caso, el sistema lo informará en el archivo como un nuevo código de tipo 'Tarjeta'.

###### Solar de la Abadía y Nuevo Centro

Rubro del local: ingrese el número de rubro del local, el que es provisto y definido por el soporte técnico de cada Shopping.

Número de contrato: ingrese el número de contrato del local, el que es provisto y definido por el soporte técnico de cada Shopping.

Número de cliente: ingrese el código que identifica al cliente dentro del centro comercial, el que es provisto y definido por el soporte técnico de cada Shopping.

Ubicación del archivo local: indique la ruta en que se guarda localmente el archivo generado para Shopping.

Ubicación del archivo remoto: indique la ruta donde se encuentra el archivo para la retransmisión al Shopping (Batch.exe).

Punto de venta por terminal: ingrese el código que identifica a la terminal, puesto o caja dentro del local.

Una vez configurados los parámetros de Ventas, acceda a [Cuentas de Tesorería](?p=10235). Para cada cuenta de tesorería se deben configurar los Datos para archivo shopping.

Clase de cuenta: debe indicar la forma de pago asociada a la cuenta. Los medios de pago a configurar para Solar de la Abadía o Nuevo Centro son:

**1** | Efectivo  
---|---  
**2** | Tarjeta  
**3** | Cheque  
**4** | Efectivo dólar  
**6** | Otro medio de pago  
  
Código para tarjeta: debe definir el código de tarjeta a informar cuenta la cuenta es de tipo ‘Tarjeta’. Los códigos de tarjeta a configurar para Solar de la Abadía o Nuevo Centro son:

**AG  
** | Argencard  
---|---  
**MC** | MasterCard  
**VI** | Visa  
**DI** | Diners  
**AM** | American Express  
**TS** | Tarjeta Shopping  
**SC** | Tarjeta Shopping Cash  
**TN** | Tarjeta Naranja  
**CA** | Cabal  
**CD** | Cabal 24  
**FR** | Carta Franca  
**CR** | Credencial  
**EL** | Electrón  
**MA** | Maestro  
**LI** | Líder  
**PC** | Provencred  
**IC** | Italcred  
**MI** | Mira  
**TV** | Tarjeta Nevada  
  
Es posible configurar en la cuenta otro código que no exista en esta lista, con sólo ingresarlo en el campo. En este caso, el sistema lo informará en el archivo como un nuevo código de tipo 'Tarjeta'.

###### Grupo IRSA - Interfaz Fiserv

Código de comercio: este dato es provisto y definido por el soporte técnico de cada Shopping.

Punto de venta por terminal: ingrese el código que identifica a la terminal, puesto o caja dentro del local.

__Nota

Además, debe completar el número de identificación tributaria (CUIT) en la solapa _Principal_ del proceso [Parámetros de Ventas](?p=19401).

Una vez configurados los parámetros de Ventas, acceda a [Cuentas de Tesorería](?p=10235). Para cada cuenta de tesorería se deben configurar los Datos para archivo shopping.

Clase de cuenta: debe indicar la forma de pago asociada a la cuenta. Los medios de pago a configurar para el Grupo IRSA - Interfaz Fiserv son:

**E** | Dinero (local)  
---|---  
**T** | Tarjeta  
**C** | Cheque  
**D** | Dólares  
**K** | Cuenta  
**Q** | Medio Electrónico/Billetera Digital  
**R  
** | Gift Card  
**O** | Otro medio de pago  
  
Código para tarjeta: debe definir el código de tarjeta a informar cuenta la cuenta es de tipo 'Tarjeta'. Los códigos de tarjeta a configurar para el Grupo IRSA - Interfaz Fiserv son:

**AM** | American Express  
---|---  
**AG** | Argencard  
**TA** | Argenta  
**PL** | C&A Private Label  
**CA** | Cabal  
**CD** | Cabal Débito (24 Horas)  
**CT** | Carta Auto  
**FR** | Carta Franca  
**CS** | Castillo  
**CE** | Cencosud  
**CL** | Clipper  
**CR** | Credencial  
**CI** | Credial  
**CC** | Credicash  
**CI** | Credicred  
**CM** | Credimas  
**TF** | CRM Falabella  
**DT** | Data 2000  
**DI** | Diners  
**EB  
** | Elebar  
**EM** | Empresur  
**FV** | Favacard  
**FE** | Fedil  
**IC  
** | Italcred  
**KD  
** | Kadicard  
**LI  
** | Líder  
**CO  
** | Tarjeta Confiable  
**MA  
** | Maestro  
**SM** | MAS  
**MC** | Mastercard  
**MI  
** | Mira  
**NT  
** | Nativa  
**TV** | Nevada  
**NE** | Nexo  
**NC** | Novacash  
**OG** | Okey Group  
**PR** | Primicia  
**PC** | Provencred  
**SA** | Saltcard  
**SL** | Salto 96  
**SC  
** | Shopping Cash  
**SO** | Sol  
**SR** | Sucredito  
**AZ  
** | Tarjeta Azul  
**TN** | Tarjeta Naranja  
**TN** | Tarjeta Naranja Plan Zeta  
**NO** | Tarjeta Platino  
**TS  
** | Tarjeta Shopping  
**VI  
** | Visa  
**EL** | Visa Débito  
**GC  
** | Giftcard APSA  
**GO  
** | Giftcard Otros  
  
###### Grupo Fortin Maure - Interfaz Solutions Malls

Usuario: ingrese el usuario que será utilizada para autenticarse. Este dato es provisto y definido por Fortin Maure.

Clave: ingrese la contraseña que será utilizada para autenticarse. Este dato es provisto y definido por Fortin Maure.

Nro. de cliente: ingrese el código que identifica al cliente. Este dato es provisto y definido por Fortin Maure.

Una vez configurados los parámetros de venta, acceda a [Cuentas de Tesorería](?p=10235). Para cada cuenta de tesorería se deben configurar los Datos para archivo shopping.

Clase de cuenta: debe indicar la forma de pago asociada a la cuenta. Los medios de pago a configurar para el Grupo Fortin Maure - Interfaz Solutions Malls son:

**EF** | Pago en efectivo  
---|---  
**DB** | Pago con tarjeta de débito  
**CD** | Pago con tarjeta de crédito  
**TR** | Pago con transferencia bancaria  
**CC** | Venta en cuenta corriente  
**OT** | Otros medios de pago  
  
##### Detalle del circuito

Luego de parametrizar el sistema, está en condiciones de generar automáticamente los datos a transferir, a través de los procesos Facturación, Nota de crédito y Anulación.

**Retransmisión de comprobantes  
**Además, podrá generar los datos a transferir de forma manual a través de un proceso batch, seleccionando un rango de fechas.  
Esta opción es de utilidad ante eventuales problemas que impidan la generación normal de este archivo en el momento de emitir un comprobante de facturación.  
Para ello ingrese al menú principal del Facturador, haga clic en Más acciones y luego seleccione la opción Archivo shopping.

__Nota

Esta funcionalidad no estará disponible cuando el sistema esté configurado para que genere información para shoppings mediante Grupo IRSA - Interfaz Fiserv o Grupo Fortin Maure - Interfaz Solutions Malls.
