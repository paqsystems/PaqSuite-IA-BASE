# Cuentas de caja

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv3/guia_controlart_gv3/?p=24601/

## Contenido

# Cuentas de caja

Una cuenta de caja representa un medio de pago utilizado por sus clientes. Este proceso le permite definir distintos tipos de cuentas para registrar sus operaciones de caja.

En el sistema ya está definida una cuenta de tipo efectivo.

Código de cuenta: puede incluir hasta 11 dígitos. Este código de identificación es definido por usted y determina el ordenamiento de las cuentas en los informes del sistema.

Descripción: es el nombre de la cuenta, su ingreso es obligatorio.

Inhabilitado: al tildar este parámetro, la cuenta de caja dejará de ser visible en los circuitos donde usted tenga que elegir una cuenta de caja para continuar con el proceso (facturación, nota de crédito, cobranza y configuración entre otros). Es importante tener en cuenta que, para poder inhabilitar una cuenta de caja, la misma no debe formar parte de la configuración o parametrización del sistema.

Tipo de cuenta: el sistema contempla el manejo de los siguientes tipos de cuentas:

  * **E:** Efectivo
  * **C:** Cheques
  * **K:** Ticket
  * **T:** Tarjeta
  * **O:** Otras



Si usted acepta distintas formas de pago, puede definir una cuenta por cada una de las modalidades.

Ingresa datos del cheque / cupón: este dato se solicita si la cuenta es de tipo cheque o tarjeta.  
Si no necesita registrar los datos de los cheques o cupones que recibe en sus movimientos de cobranza, ingrese 'N'.  


Moneda Corriente / Moneda: indique si la cuenta está expresada en moneda corriente.  
Si se trata de una cuenta en moneda corriente, se propone automáticamente como moneda, el código 001 - PESOS.  
Si la cuenta está expresada en otra moneda, ingrese el código de [moneda](moneda_gv3) correspondiente.

Cuenta Habitual / Orden de Aparición / Descripción / Imagen: si se trata de una cuenta que usted utilizará con frecuencia en sus movimientos de cobranza, defínala como cuenta habitual e ingrese 'SI' en este campo.  
Además, asígnele un orden de aparición y una descripción. De manera opcional, es posible asociar una imagen a una cuenta habitual.  
Estos datos se tendrán en cuenta en el proceso de cobranza, para configurar el sector de cuentas habituales.

Código de imputación contable: si su sistema se integra con el módulo Contabilidad a través del Pasaje a Contabilidad, asocie la cuenta de caja con un código de cuenta contable.

Código de cuenta asociada de Tesorería: si usted utiliza el Pasaje a Tesorería para integrar su sistema con el módulo Tesorería, relacione la cuenta de caja con un código de cuenta existente en ese módulo.

Url (Apertura Pago): si su sistema Tango Restô integra con una aplicación externa para incorporar nuevos medios de pago electrónico en los circuitos de facturación y cobranza, en este campo deberá indicar la ruta donde está ejecutándose el servicio de apertura pago y el método de la aplicación externa en cuestión. Para más información visite el sitio web: <https://github.com/TangoSoftware/RestoAperturaPagos>.

##### Planes de tarjetas

Si la cuenta es de tipo tarjeta y si está activo el parámetro Ingresa datos del cheque / cupón, el sistema solicitará el ingreso de los datos correspondientes a planes de tarjetas de crédito.

Código de tarjeta: es el código de tarjeta a asociar a la cuenta.

Descripción del plan: ingrese la descripción del plan que representa la cuenta.

Cantidad de cuotas: es la cantidad de cuotas del plan. Este valor será propuesto por el sistema al confeccionar un cupón, pero puede modificarse.

Cuota de redondeo: indique a qué cuota (primera o última) se asignará el redondeo, si la división no es exacta.

Código de plan: indique el código del plan de tarjeta al que podría estar asociada esta tarjeta. Este valor es requerido solamente si usted esta haciendo uso del proceso de rendición a tesorería en central, en cuyo caso, este valor deberá coincidir con el código del plan registrado en el proceso de planes de tarjetas, en el módulo Tesorería en central.

__Nota

Para mas información relacionada con planes para tarjeta visitar la ayuda relacionada en el módulo [Tesorería](?p=10265).  


##### Montos predefinidos

Si desea podrá indicar montos predefinidos para la cuenta que esté cargando.  
Este proceso le permite definir distintos montos para registrar sus operaciones de caja.  
Un monto representa un medio de pago con un respectivo valor, que le permitirá agilizar el proceso de cobranza.  
De esta forma en vez de seleccionar una cuenta y luego tipear el monto recibido, con sólo seleccionar el monto, el proceso queda concluido y únicamente resta su confirmación.

**Ejemplo...  
**Si se quiere cobrar un comprobante por un valor de 45 pesos es posible que el cliente nos pague con 50 o 100 pesos con lo cual en vez de seleccionar la cuenta pesos y luego tipear el valor de 50 o 100, se puede predeterminar dichos montos, de forma tal que con un simple clic realice la cobranza.

Esta funcionalidad puede ser de mayor utilidad en modalidades Touch Screen.

Monto: indique el monto que desea representar. Por ejemplo el monto que representa cada billete, cupón o ticket.

Orden: indique el orden de aparición de dicho monto dentro del panel. El panel mostrará los montos por cada cuenta que se seleccione.

Habitual: indique si el monto es habitual para la cuenta asociada. Si un monto es configurado como habitual:

  * Podrá disponer de dicho monto dentro del panel de montos habituales, en el cual es posible visualizar montos de distintas cuentas.  
Dicha función es de utilidad cuando utiliza más de una cuenta de forma habitual, con lo cual el uso del panel de montos habituales le permitirá acceder más rápido a los montos de las distintas cuentas, sin tener que seleccionar primero una cuenta para luego visualizar los montos respectivos, como en el caso del panel de montos.  
El panel de montos habituales mostrará los montos ordenados por cuenta y por el orden indicado.
  * Podrá filtrar en los paneles por montos habituales. Ello es de utilidad cuando dispone de varios montos, en donde existen algunos que son de uso habitual y otros de uso ocasional.



Imagen: por cada una de las cuentas podrá asociar una imagen (la cual represente dicho monto) indicando la ruta de acceso a la misma. Por ejemplo; si quiere lograr una mejor representación del monto 1000, podrá asociar una imagen de un billete de 1000 pesos.  
Si no asocia ninguna imagen, por defecto se visualizará un botón con dicho monto. Sólo se admiten imágenes con formato .jpg o .bmp.

##### Integración con Tesorería

En este proceso podrá definir cual o cuales serán las cuentas de Tesorería vinculadas a la cuenta de Restô que se encuentra modificando. La información a completar depende del estado del parámetro general Utiliza múltiples cuentas.

Código de cuenta asociada de Tesorería: este campo deberá completarse cuando el parámetro general Utiliza múltiples cuentas sea 'N'.  
Si usted utiliza el Pasaje a Tesorería, Rendición a Tesorería o bien Transferencia de valores para integrar su sistema con el módulo Tesorería, relacione la cuenta de caja con un código de cuenta existente en ese módulo.

Saldo a dejar en la caja: este campo es visible solo en las cuentas de tipo 'Efectivo'.  
Si utiliza el proceso Rendición a Tesorería, se le sugerirá como importe a rendir el total del saldo de esa cuenta menos el saldo configurado en este campo.

Múltiples cuentas de Tesorería: si trabaja con el parámetro general Utiliza múltiples cuentas en 'S' deberá completar la tabla indicando por cada puesto de caja cual será la cuenta equivalente en tesorería.

##### Opción Shopping

Si en el proceso [Parámetros generales](paramgrales_gv3) está activo el parámetro Genera información para shoppings, ingrese en el campo Tipo de cuenta Shopping, la forma de pago asociada a la cuenta.

**Grupo Alto Palermo  
**Los medios de pago a configurar para el **Grupo Alto Palermo** son:

  * E: Efectivo
  * A: Alto Check
  * C: Cheques
  * D: Dólares
  * O: Otro medio
  * AG: Argencard
  * MC: Mastercard
  * VI: Visa
  * DI: Diners
  * AM: American Express
  * TS: Tarjeta Shopping
  * SC: Tarjeta Shopping Cash
  * TN: Tarjeta Naranja
  * CA: Cabal
  * CI: Credicred
  * CD: Cabal Débito (24 horas)
  * FR: Carta Franca
  * CR: Credencial
  * EL: Electrón
  * MA: Maestro
  * LI: Líder
  * PC: Provencred
  * IC: Italcred
  * MI: Mira
  * TF: Tarjeta CRM Falabella
  * MS: Tarjeta Musimundo
  * DT: Tarjeta data 2000
  * MP: Tarjeta Mendoza Plaza Shopping
  * AZ: Tarjeta Azul
  * TV: Tarjetas Nevadas



De todas maneras es posible configurar en la cuenta, otro código que no exista en esta lista, con sólo ingresarlo en el campo. En este caso, el sistema lo informará en el archivo como un nuevo código de tipo tarjeta.

**Grupo Nordelta  
**Los códigos numéricos de medios de pago a configurar para el Grupo Nordelta son:

  * 1: Efectivo
  * 2: Tarjeta
  * 3: Cheque
  * 4: Efectivo Dólar
  * 6: Otro medio de pago



Para el medio de pago 'Tarjeta', defina el código de tarjeta con los siguientes códigos:

  * 1: Mastercard
  * 2: Visa
  * 3: Visa electrón
  * 4: American Express
  * 5: Diners
  * 6: Naranja
  * 7: Provencred
  * 8: Líder
  * 9: Maestro
  * 10: Nevada
  * 11: Argencard
  * 12: Cabal
  * 13: Carta Franca
  * 14: Credencial
  * 15: Italcred
  * 16: Mira



De todas maneras es posible configurar en la cuenta, otro código que no exista en esta lista, con sólo ingresarlo en el campo. En este caso, el sistema lo informará en el archivo como un nuevo código de tipo tarjeta.

**Solar de la Abadía y Nuevo Centro  
**Los códigos numéricos de medios de pago a configurar son:

  * 1: Efectivo
  * 2: Tarjeta
  * 3: Cheque
  * 4: Efectivo Dólar
  * 6: Otro medio de pago



Para el medio de pago 'Tarjeta', defina el código de tarjeta con los siguientes códigos:

  * 1: Mastercard
  * 2: Visa
  * 3: Visa electrón
  * 4: American Express
  * 5: Diners
  * 6: Naranja
  * 7: Provencred
  * 8: Líder
  * 9: Maestro
  * 10: Nevada
  * 11: Argencard
  * 12: Cabal
  * 13: Carta Franca
  * 14: Credencial
  * 15: Italcred
  * 16: Mira
  * 18: Cordobesa
  * 19: CMR
  * 20: Kadicard



De todas maneras es posible configurar en la cuenta, otro código que no exista en esta lista, con sólo ingresarlo en el campo. En este caso, el sistema lo informará en el archivo como un nuevo código de tipo tarjeta.

**Grupo IRSA - Interfaz Fiserv**  
Los códigos de las cuentas de caja y los códigos para las diferentes tipos de tarjeta, los podrá encontrar en la sección _Grupo IRSA - Interfaz Fiserv_ de la [Guía de Restô sobre trabajo en modalidad Shopping](?p=28869/#grupo-irsa-interfaz-fiserv).

Más información:

No es posible eliminar una cuenta de caja si tiene movimientos; si en el proceso Parámetros generales está definida como cuenta habitual de cobranza.

##### Contenidos relacionados

  * [Videos de integración Tango Restô](https://ayudas.axoft.com/24ar/videos/gv3_carp_vid/mercpagodelivery_gv3_vid/)
