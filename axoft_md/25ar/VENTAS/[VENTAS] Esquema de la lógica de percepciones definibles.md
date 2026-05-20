# Esquema de la lógica de percepciones definibles

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_percepdefin_gv/guia_percdef_introduccion_gv/

## Contenido

# Esquema de la lógica de percepciones definibles

A continuación puede consultar la _lógica resumida_ que aplica el sistema para el cálculo de percepciones definibles, respondiendo las preguntas que se efectúa cada ítem, de modo de comprender los pasos que sigue el sistema cuando se presenta la situación planteada.  
Si desea consultar la _lógica detallada_ (observando un diagrama) pulse [aquí](?p=27041/#diagrama-de-la-logica-del-circuito-de-percepciones-definibles).

Definición de la percepción

En nuestro ejemplo, analizaremos la percepción definible denominada "Ejemplo de percepciones de ingresos brutos". Esta percepción debe calcularse sobre el neto gravado (base de cálculo) cuando se liquida a clientes "Mayoristas" mientras que para el resto de los casos se debe calcular sobre el **total del comprobante**.

En la parte inferior de la pantalla puede consultar las distintas alícuotas vigentes para la percepción.  
Para consultar esta información ingrese a [Percepciones definibles](?p=19407).

Siguiente >

Ingreso del artículo en una factura (análisis de impuestos)

Al ingresar un artículo en el comprobante el sistema verifica los impuestos que se le deben liquidar al cliente.

Al ingresar un artículo en el comprobante, el sistema verifica los impuestos que se le deben liquidar al cliente.

Siguiente >

Análisis del cliente

El sistema analiza cada una de las percepciones definibles que tiene asociadas el cliente.

Para consultar esta información ingrese a la pantalla [Características de facturación](?p=19444) en la actualización de Clientes.  
En este ejemplo el cliente tiene asociada la percepción "Ejemplo de percepciones de ingresos brutos".  
A continuación se analiza si tiene asignada una alícuota particular para este impuesto.

_¿El cliente tiene asociada una alícuota específica para la percepción definible?_

No |  Si  
---|---  
  
Análisis del artículo (cliente sin alícuota específica)

En este caso, tomamos el ejemplo de que el cliente no tiene asignada una alícuota específica. A continuación se verifica si el artículo tiene asociada la misma percepción que el cliente.

Tenga en cuenta que es condición que el impuesto esté asignado a nivel de cliente y de artículo para que se liquide el impuesto.

_¿El artículo tiene asignada la misma percepción?_

No |  Si  
---|---  
  
Análisis del artículo (cliente con alícuota específica)

En el caso que el cliente tenga asignada una alícuota de percepción específica, se verifica si el artículo tiene asociado el mismo código de percepción. Recuerde que el cliente tiene asignada la percepción denominada 'IB'.

Para consultar esta información ingrese a la pantalla Impuestos en la actualización de [Artículos](https://ayudas.axoft.com/25ar/articulo_carp_st).  
Tenga en cuenta que es condición que el impuesto esté asignado a nivel de cliente y de artículo para que se liquide.

_¿El artículo tiene asignada la misma percepción?_

No |  Si  
---|---  
  
Análisis de la alícuota a aplicar (la del cliente)

Como el cliente y el artículo tienen asignado el mismo código de percepción, se debe liquidar el impuesto.

Debido a que el cliente tiene asignada una alícuota específica, se utiliza dicha alícuota para el cálculo de la percepción.  
Si el cliente tiene asignada una clasificación para percepciones definibles, dicha clasificación debe estar asignada también a nivel artículo. De lo contrario, se lo considerará exento.

En la imagen superior se detalla la pantalla de Clientes mientras que en la inferior se muestra la de Artículos.

_Como último paso para liquidar el impuesto se debe establecer la base de cálculo._

Establecer la base de cálculo

Análisis de la base de cálculo a aplicar (Mayoristas)

Al tratarse de un cliente clasificado como "Mayorista" se busca la base de cálculo que corresponda a dicha clasificación.

En este caso particular se liquida el impuesto sobre el neto gravado aplicando la alícuota del cliente. En caso que no se encuentre una base de cálculo específica para esta clasificación no se liquidará el impuesto.

Pantalla de Clientes:

Pantalla de de Percepciones Definibles:

[ Analizar nuevamente la lógica](?p=27045)

No liquidación del impuesto (artículo exento según percepción)

Debido a que el artículo no tiene asignado el mismo código de percepción que el cliente, no se liquida el impuesto (el artículo se encuentra exento para esa percepción).

En la imagen superior se detalla la pantalla de Clientes mientras que en la inferior se muestra la de Artículos.

[ Analizar nuevamente la lógica](?p=27045)

Análisis de la clasificación del cliente

Cómo el artículo tiene asignada la misma percepción que el cliente, se le debe liquidar el impuesto. Como paso previo a la liquidación se verifica si el cliente tiene asignado alguna clasificación específica.

Para consultar esta información ingrese a la pantalla [Características de Facturación](?p=19444) en la actualización de Clientes.

_¿El cliente tiene asignada una clasificación específica para percepciones definibles?_

No |  Si  
---|---  
  
No liquidación del impuesto (artículo con diferente percepción que el cliente)

Al no tener asignado el artículo la misma percepción que el cliente no se liquida el impuesto.

Recuerde que es condición que el impuesto esté asignado a nivel de cliente y de artículo para que se liquide el impuesto.

En la imagen superior se detalla la pantalla de Clientes mientras que en la inferior se muestra la de Artículos.

[ Analizar nuevamente la lógica](?p=27045)

Determinación de la alícuota en base a la clasificación del cliente

Como el cliente tiene asignada una clasificación específica (en nuestro caso se trata de un "Mayorista") se verifica si se debe liquidar el impuesto (aplicar una alícuota) cuando se vende este artículo (Resma de hojas) a este tipo de clientes (Mayoristas).

_¿El artículo tiene definida una alícuota para la clasificación indicada en el cliente?_

No |  Si  
---|---  
  
Determinación de la alícuota general (con alícuota general)

Como el cliente no tiene asignada una clasificación para percepciones definibles, se verifica si el artículo tiene definida una alícuota general (para clientes sin clasificación).

Para consultar esta información ingrese a la pantalla Impuestos en la actualización de [Artículos](https://ayudas.axoft.com/25ar/articulo_carp_st).

_¿El artículo tiene definida una alícuota general (sin especificar una clasificación)?_

No |  Si  
---|---  
  
Aplicación de la alícuota para Mayoristas

En este caso se debe liquidar el impuesto aplicando la alícuota 2 (5%) por tratarse de un cliente "Mayorista".

En el caso que el cliente no tuviese una clasificación asociada se le debería aplicar la alícuota "general" (aplicable a clientes sin clasificación).

En la imagen superior se detalla la pantalla de Percepciones Definibles mientras que en la inferior se muestra la de Artículos.  
Como último paso para liquidar el impuesto se debe establecer la base de cálculo.

Establecer la base de cálculo

No liquidación del impuesto (sin alícuota a aplicar)

Al no encontrarse en el artículo una alícuota a aplicar para la clasificación del cliente, no se liquida el impuesto (el artículo se encuentra exento cuando se comercializa a ese tipo de clientes).

  
En la imagen superior se detalla la pantalla de Clientes mientras que en la inferior se muestra la de Artículos.

[ Analizar nuevamente la lógica](?p=27045)

Análisis de la base de cálculo a aplicar (Mayoristas)

Al tratarse de un cliente clasificado como "Mayorista" se busca la base de cálculo que corresponda a dicha clasificación.

En este caso particular se liquida el impuesto sobre el neto gravado aplicando la alícuota asignada al artículo para esa clasificación.  
En caso que no se encuentre una base de cálculo específica para esta clasificación no se liquidará el impuesto.  
Detalle de la pantalla de Clientes:

Pantalla de Percepciones Definibles:

[ Analizar nuevamente la lógica](?p=27045)

Aplicación de la alícuota general

Al existir una alícuota general para el artículo (sin especificar clasificación) corresponde liquidar el impuesto con dicha alícuota.

En este ejemplo se aplicaría una alícuota del 3%.

En la imagen se detalla la pantalla de Percepciones definibles mientras que en la inferior se muestra la de Artículos.  
Como último paso para liquidar el impuesto se debe establecer la base de cálculo.

Establecer la base de cálculo

No liquidación del impuesto (artículo exento por tipo de cliente)

En este caso no se liquida el impuesto ya que el artículo se encuentra exento cuando se comercializa a ese tipo de clientes.

Recuerde que es condición que el impuesto esté asignado a nivel de cliente y de artículo para que se liquide el impuesto. Cuando el cliente no tiene asignado una clasificación, debe existir en el artículo una alícuota no asociada a una clasificación específica. De lo contrario no se liquidará el impuesto

En la imagen superior se detalla la pantalla de Clientes mientras que en la inferior se muestra la de Artículos.

[ Analizar nuevamente la lógica](?p=27045)

Análisis de la base de cálculo a aplicar (base de cálculo general)

Al tratarse de un cliente sin clasificación asignada, se busca la base de cálculo general de la percepción (aquella que no tenga valor en la columna "Clasificación para percepciones").

En este caso particular se liquida el impuesto sobre el total del comprobante aplicando la alícuota general indicada en el artículo.

Características de facturación:

Actualización de Percepciones Definibles:

En la imagen superior se detalla la pantalla de Clientes mientras que en la inferior se muestra la de Percepciones definibles.

[ Analizar nuevamente la lógica](?p=27045)
