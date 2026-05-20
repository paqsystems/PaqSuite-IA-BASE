# Guía de Restô sobre trabajo en modalidad Shopping

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv3/guia_shopping_gv3/

## Contenido

# Guía de Restô sobre trabajo en modalidad Shopping

Si usted tiene un punto de venta operando en un centro comercial perteneciente a alguno de los siguientes grupos: Grupo Alto Palermo S.A., Grupo Nordelta, Solar de la Abadia, Nuevo Centro o Grupo IRSA - Interfaz Fiserv; puede generar desde el módulo Ventas Restô la información necesaria para estos centros comerciales.

En este caso, es necesario definir una serie de parámetros, que se tendrán en cuenta en el momento de generar comprobantes de facturación (facturas, notas de crédito y anulaciones).

##### Puesta en marcha

Para comenzar a trabajar con la modalidad Shopping será necesario configurar la base de datos, para ello siga los siguientes pasos:  
Acceda Archivos Carga inicial [Parámetros generales.](paramgrales_gv3) En la sección "Modalidad Shopping" deberá indicar:

Genera información para shoppings: mediante este parámetro, usted define el grupo de Shopping al que pertenece, siendo posible:

  * Grupo Alto Palermo S. A.
  * Grupo Nordelta
  * Solar de la Abadía
  * Nuevo Centro
  * Grupo IRSA - Interfaz Fiserv
  * No Utiliza.



###### Grupo Alto Palermo S.A.

Rubro del local: ingrese el número de rubro del local, el que es provisto y definido por el soporte técnico de cada Shopping.

Número de contrato: ingrese el número de contrato del local, el que es provisto y definido por el soporte técnico de cada Shopping.

Número de POS: ingrese el código que identifica al puesto o caja dentro del local. Por ejemplo para los locales con más de una caja; cada caja tiene asignado un número de pos comenzando desde 1.

Número de local: ingrese el código que identifica al local dentro del centro comercial, el que es provisto y definido por el soporte técnico de cada Shopping.

Ubicación de archivo local: indique la ruta en que se guarda localmente el archivo generado para Shopping.

Ubicación del archivo remoto: indique la ruta en que se guarda en la red el archivo generado para Shopping.

Una vez configurado parámetros generales acceda a [Archivos Caja Cuentas](cuentacaja_gv3).  
Para cada cuenta en la opción de menú Shopping, debe indicar el tipo de cuenta Shopping al que se asocia.

¿Cómo acceder al código equivalente de cuenta para Shopping?  
Los medios de pago a configurar para el Grupo Alto Palermo son:

**Código** | **Detalle**  
---|---  
E | Efectivo  
A | Altocheck (Cheque regalo)  
C | Cheques  
D | Dólares  
O | Otro medio de pago  
  
Tarjetas:

**Código** | **Detalle**  
---|---  
MC | MasterCard  
VI | Visa  
EL | Visa Electrón  
AM | American Express  
TS | Tarjeta Shopping  
DI | Diners  
SC | Tarjeta Shopping Cash  
TN | Tarjeta Naranja  
PC | Provencred  
LI | Líder  
MA | Maestro  
TV | Tarjeta Nevada  
AG | Argencard  
CA | Cabal  
CI | Credicred  
CR | Credencial  
IC | Italcred  
MI | Mira  
TF | Tarjeta CRM Falabella  
MS | Tarjeta Musimundo  
PL | C&A Private Label  
DT | Tarjeta Data 2000  
MP | Tarjeta Mendoza Plaza Shopping  
AZ | Tarjeta Azul  
CD | Cabal Débito (24 Horas)  
  
Será posible configurar en la cuent, otro código que no exista en esta lista, con sólo ingresarlo en el campo. En este caso, el sistema lo informará en el archivo como un nuevo código de tipo tarjeta.  
Para el caso de la cuenta Efectivo - Pesos en el tipo de cuenta Shopping se indicará con la letra 'E'.

###### Grupo Nordelta

Rubro del local: ingrese el número de rubro del local, el que consta de 4 dígitos y es provisto y definido por el soporte técnico de cada Shopping.

Número de contrato: ingrese el número de contrato del local, el que consta de 6 dígitos numéricos y es provisto y definido por el soporte técnico de cada Shopping

Número de POS: ingrese el código que identifica al puesto o caja dentro del local. Por ejemplo para los locales con más de una caja; cada caja tiene asignado un número de pos comenzando desde 1.

Número de local: ingrese el código que identifica al local dentro del centro comercial, el que es provisto y definido por el soporte técnico de cada Shopping.

Ubicación del archivo transfer.exe: indique la ruta en que se encuentra el archivo transfer.exe provisto por el Shopping.

Ubicación del archivo para retransmisión: indique la ruta en que se encuentra el archivo para la retransmisión al Shopping. La extensión del archivo debe ser 'eee'.

Una vez configurado parámetros generales acceda a [Archivos Caja Cuentas](cuentacaja_gv3).  
Para cada cuenta en la opción de menú Shopping, debe indicar el tipo de cuenta Shopping al que se asocia.

¿Cómo acceder al código equivalente de cuenta para Shopping?  
Los códigos numéricos de medios de pago a configurar para el Grupo Nordelta son:

**Código** | **Descripción**  
---|---  
1 | Efectivo  
2 | Tarjeta  
3 | Cheque  
4 | Efectivo Dólar  
6 | Otro medio de pago  
  
Para el medio de pago 'Tarjeta', defina el código de tarjeta con los siguientes códigos:

**Código** | **Descripción**  
---|---  
1 | Mastercard  
2 | Visa  
3 | Visa electrón  
4 | American Express  
5 | Diners  
6 | Naranja  
7 | Provencred  
8 | Líder  
9 | Maestro  
10 | Nevada  
11 | Argencard  
12 | Cabal  
13 | Carta Franca  
14 | Credencial  
15 | Italcred  
16 | Mira  
  
De todas maneras, será posible configurar en la cuenta, otro código que no exista en esta lista, con sólo ingresarlo en el campo. En este caso, el sistema lo informará en el archivo como un nuevo código de tipo tarjeta.  
Una vez configurada las cuentas acceda a [Archivos / Personal / mozo](personmozo_gv3) y a [Archivos / Personal / Repartidor](personrepartidor_gv3).  
Para cada mozo/repartidor, debe indicar el Código Shopping, ingrese en este campo un código numérico (el que se enviará como parte de la información de los comprobantes facturados).

###### Solar de la Abadía y Nuevo Centro

Rubro del local: ingrese el número de rubro del local, el que consta de 4 dígitos y es provisto y definido por el soporte técnico de cada Shopping.

Número de contrato: ingrese el número de contrato del local, el que consta de 6 dígitos numéricos y es provisto y definido por el soporte técnico de cada Shopping.

Número de POS: ingrese el código que identifica al puesto o caja dentro del local. Por ejemplo para los locales con más de una caja; cada caja tiene asignado un número de pos comenzando desde 1.

Número de cliente: ingrese el código que identifica al local dentro del centro comercial, el que es provisto y definido por el soporte técnico de cada Shopping.

Ubicación del archivo transfer.exe: indique la ruta en que se encuentra el archivo transfer.exe.

Ubicación del archivo para retransmisión: indique la ruta donde se encuentra el archivo para la retransmisión al Shopping. La extensión del archivo debe ser 'eee'.

Una vez configurado parámetros generales acceda a [Archivos Caja Cuentas](cuentacaja_gv3).  
Para cada cuenta en la opción de menú Shopping, debe indicar el tipo de cuenta Shopping al que se asocia.

¿Cómo acceder al código equivalente de cuenta para Shopping?  
Los códigos numéricos de medios de pago a configurar son:

**Código** | **Descripción**  
---|---  
1 | Efectivo  
2 | Tarjeta  
3 | Cheque  
4 | Efectivo Dólar  
6 | Otro medio de pago  
  
Para el medio de pago 'Tarjeta', defina el código de tarjeta con los siguientes códigos:

**Código** | **Descripción**  
---|---  
1 | Mastercard  
2 | Visa  
3 | Visa electrón  
4 | American Express  
5 | Diners  
6 | Naranja  
7 | Provencred  
8 | Líder  
9 | Maestro  
10 | Nevada  
11 | Argencard  
12 | Cabal  
13 | Carta Franca  
14 | Credencial  
15 | Italcred  
16 | Mira  
18 | Cordobesa  
19 | CMR  
20 | Kadicard  
  
Es posible configurar en la cuenta otro código que no exista en esta lista, con sólo ingresarlo en el campo. En este caso, el sistema lo informará en el archivo como un nuevo código de tipo tarjeta.  
Una vez configurada las cuentas acceda a [Archivos / Personal / Mozo](personmozo_gv3) y a [Archivos / Personal / Repartidor](personrepartidor_gv3)  
Para cada mozo/repartidor, debe indicar el siguiente dato:

Datos Shoppings: configurar en forma obligatoria, para cada mozo el tipo y número de documento, a fin de identificarlos en la información generada en el archivo ASCII.  
Los tipos de documentos válidos son:

  * DNI: Documento único de identidad
  * CI: Cedula de identidad
  * LC: Libreta cívica
  * LE: Libreta de enrolamiento
  * PAS: Pasaporte
  * CUIT: Código único de identificación tributaria
  * CUIL: Código único de identificación laboral
  * LEG: Legajo



Tenga en cuenta que será posible configurar otro tipo de documento que no exista en la lista, con sólo ingresarlo en el campo. En este caso, el sistema lo informará en el archivo como un nuevo tipo.  
El número ingresado como documento no debe tener puntos ni guiones.

¿Cómo acceder al código equivalente de cuenta para Shopping?  
Como la imagen lo indica, para el caso de la cuenta Efectivo - Pesos, en el tipo de cuenta Shopping se indicará con la letra 'E'.

###### Grupo IRSA - Interfaz Fiserv

Para poder configurar en los parámetros generales la modalidad 'Genera información para Shopping Grupo IRSA - Interfaz Fiserv', deberá tener configurado previamente los tipos de cuenta para Shopping, sin excepción, para todas cuentas de caja que tenga dadas de alta en su sistema.  
Para ello acceda a Ventas Restô _| Archivos | Caja |[Cuentas](?p=24601)_. Para cada cuenta en la opción de menú Shopping, debe indicar el tipo de cuenta Shopping al que se asocia. Este dato será de carácter obligatorio.

__Nota

Todas las cuentas de caja del tipo 'Tarjeta', deberán permitir registrar los datos del cupón al momento de generar la factura y la misma debe ser abonada con alguna cuenta de caja del tipo 'Tarjeta'. Es decir, las cuentas de caja del tipo 'Tarjeta' deberán tener el valor del parámetro _Ingresa datos del cheque / cupón_ con valor 'S'. Si posee alguna cuenta de caja del tipo 'Tarjeta' y, la cual podría ser usada al momento de generar una factura, el sistema no le permitirá generar el ticket, por lo que tendrá que dar de alta a una nueva cuenta de caja igual a la que desea utilizar para abonar la factura, pero, cuyo parámetro _Ingresa datos del cheque / cupón_ tenga el valor 'S' en el ABM de cuentas.

Además. será necesario configurar el tipo (débito o crédito) para cada tarjeta (en Ventas Restô _| Archivos | Caja |[Tarjetas](?p=24977)_). Este dato es de carácter obligatorio para trabajar con la modalidad _Shopping Grupo IRSA - Interfaz Fiserv_.  
Una vez configuradas las cuentas de caja y el tipo de tarjeta, se deberá acceder al módulo de parámetros generales y configurar los siguiente en la vista 'modalidad shopping'.

CUIT: ingrese solo el número de CUIT de su empresa adherida al Grupo IRSA. No Introduzca guiones o caracteres especiales.

Número de POS: ingrese el código que identifica al puesto o caja dentro del local. Por ejemplo, para los locales con más de una caja; cada caja debe tener asignado un número de POS diferente comenzando desde 1.

Código de comercio: este dato es provisto y definido por el soporte técnico de cada Shopping.

¿Cómo acceder al código equivalente de cuenta para Shopping?  
Los códigos numéricos de medios de pago a configurar para el Grupo IRSA - Interfaz Fiserv son:

**Código** | **Detalle**  
---|---  
E | Efectivo  
C | Cheques  
D | Dólares  
Q | Medio Electrónico/Billetera Digital  
R | Gift Card  
O | Otro medio de pago  
  
En el caso de que la cuenta sea del tipo 'Tarjeta', para cada tipo de tarjeta se debe indicar la abreviatura correspondiente, la cual representa el código para Shopping.

**Tarjetas:**

**Descripción** | **Código**  
---|---  
American Express | AM  
Argencard | AG  
Argenta | TA  
C&A Private Label | PL  
Cabal | CA  
Cabal Débito (24 Horas) | CD  
Carta Auto | CT  
Carta Franca | FR  
Castillo | CS  
Cencosud | CE  
Clipper | CL  
Credencial | CR  
Credial | CI  
Credicash | CC  
Credicred | CI  
Credimas | CM  
CRM Falabella | TF  
Data 2000 | DT  
Diners | DI  
Elebar | EB  
Empresur | EM  
Favacard | FV  
Fedil | FE  
Italcred | IC  
Kadicard | KD  
Líder | LI  
Tarjeta Confiable | CO  
Maestro | MA  
MAS | SM  
Mastercard | MC  
Mira | MI  
Nativa | NT  
Nevada | TV  
Nexo | NE  
Novacash | NC  
Okey Group | OG  
Primicia | PR  
Provencred | PC  
Saltcard | SA  
Salto 96 | SL  
Shopping Cash | SC  
Sol | SO  
Sucredito | SR  
Tarjeta Azul | AZ  
Tarjeta Mendoza Plaza Shopping | MP  
Tarjeta Musimundo | MS  
Tarjeta Naranja | TN  
Tarjeta Naranja Plan Zeta | TN  
Tarjeta Platino | NO  
Tarjeta Shopping | TS  
Visa | VI  
Visa Débito | EL  
Giftcard APSA | GC  
Giftcard Otros | GO  
  
Recuerde que al dar de alta una cuenta tipo 'Tarjeta' en la modalidad shopping 'Grupo IRSA - Interfaz Fiserv', es necesario indicar que se ingresarán los datos del cupón (_Ingresa dato cheque/cupón_ = 'SI') así como definir en el proceso [Tarjetas](?p=24977) si son del tipo débito o crédito.

##### Detalle del circuito

Luego de parametrizar la base de datos, está en condiciones de generar automáticamente los datos a transferir, a través de los procesos Facturación, Nota de crédito y Anulación.

###### Retransmisión de comprobantes

Además podrá generar los datos a transferir de forma manual a través de un proceso batch, seleccionando un rango de fechas o un rango de comprobantes.  
Esta opción es de utilidad ante eventuales problemas que impidan la generación normal de este archivo en el momento de emitir un comprobante de facturación.  
Para ello acceda a factura mesa y haga clic en el botón correspondiente para abrir la ventana de parámetros de la generación del archivo para Shopping.

__Nota

Esta funcionalidad no estará disponible cuando el sistema esté configurado para el envío de información a shopping 'Grupo IRSA – Interfaz Fiserv'.

###### Análisis de información

Si desea analizar los datos que se envían por medio de informes puede acceder a:

  * **Informe Facturación IVA ventas**. Para más información acceda: [IVA ventas](ivaventa_gv3).
  * **Informe Caja Detalle de Comprobantes**. Para más información acceda a [Detalle de comprobantes de caja](detcomprobcaja_gv3).
