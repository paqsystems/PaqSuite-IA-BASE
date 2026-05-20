# Guía sobre emisión de comprobantes "A" a clientes monotributistas (RG 5003)

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_rg5003_gv/

## Contenido

# Guía sobre emisión de comprobantes "A" a clientes monotributistas (RG 5003)

Esta guía de implementación le indica los pasos a seguir para poner en marcha este circuito. La RG 5003 especifica que a partir del 01/07/2021 se debe emitir comprobantes del tipo 'A' con IVA discriminado a clientes monotributistas.

Si quiere ver más información referida a este tema, mire [este video](?p=46164).

Para comenzar a utilizar el circuito debe seguir estos pasos:

  * Ingrese a [Parámetros generales](https://ayudas.axoft.com/25ar/paramgrales_gv) y tilde la opción RG 5003- Emisión de comprobantes "A" a monotributistas dentro de la solapa Comprobantes | General.
  * Si emite **comprobantes electrónicos** , ingrese al proceso [Formularios](?p=11875) del módulo Procesos generales | Tablas generales | Formularios | Ventas y agregue la siguiente variable.  
**@YM:** esta variable permite imprimir la siguiente leyenda que exige la RG 5003: _"El crédito fiscal discriminado en el presente comprobante, sólo podrá ser computado a efectos del Régimen de Sostenimiento e Inclusión Fiscal para Pequeños Contribuyentes de la Ley Nº 27.618"_. Este texto solo se imprime cuando haya activado el parámetro general y esté emitiendo un comprobante a un monotributista.



__Importante

Como el texto ocupa 191 caracteres, implementamos una nueva variable de control denominada **@R5003CARACTERESPORLINEA** que permite definir la cantidad de caracteres a imprimir en el renglón, por ejemplo, si la configura así _@R5003CARACTERESPORLINEA=50_ imprimirá la leyenda en 4 renglones.  
Tenga en cuenta que para implementar este ejemplo deberá repetir la variable de reemplazo **@YM** en 4 renglones como detallamos a continuación:

@YM  
@YM  
@YM  
@YM

Aún cuando la norma no especifica en qué lugar del comprobante se debe mostrar la leyenda, sugerimos hacerlo en algún lugar del pie ya que está cerca de los importes de IVA a los que hace referencia el texto.

En los formularios sólo es necesario configurar la variable de control (**@R5003CARACTERESPORLINEA**) y la variable de impresión de la leyenda (**@YM**), en los typs de los talonario 'A' que se utilizan para generar los comprobantes a los monotributista.

  * Si emite comprobantes a través de **controladores o impresoras fiscales** , ingrese al proceso [Parámetros generales](https://ayudas.axoft.com/25ar/paramgrales_gv) del módulo Ventas y agregue la siguiente variable.  
**@YM:** esta variable permite imprimir la leyenda que exige la RG 5003 en este tipo de equipos:_"Receptor del comprobante - Responsable Monotributo"_. Tenga en cuenta que los controladores fiscales de "vieja tecnología" imprimirán esta leyenda en dos reglones por lo que le sugerimos que deje la línea siguiente a la variable **@YM** en blanco.



##### Otras consideraciones

**Emisión de comprobantes  
**Tenga en cuenta que una vez configurada esta RG, el sistema considerará que debe emitir comprobantes 'A' a todos los monotributistas y en líneas generales aplicará las mismas validaciones que se aplican para responsables inscriptos.

**Facturación masiva de pedidos  
**Para evitar que tenga que modificar el talonario de factura de los pedidos existentes de clientes monotributistas (que seguramente tienen asignado un talonario de comprobantes 'B') incorporamos el parámetro Facturar también pedidos de clientes monotributistas que tengan talonario 'B'.  
Tilde esta opción para que los incluya al facturar pedidos correspondientes a talonarios de factura 'A'.

**Alta de clientes  
**Cuando registre un nuevo cliente Monotributista con categoría de IVA 'RS' -sea éste un cliente habitual, ocasional o potencial, el sistema le asignará la nueva configuración impositiva (desde todas las opciones del sistema que habilitan el alta de clientes).

**Notas de débito y notas de crédito electrónicas a clientes Monotributistas  
**Para registrar ajustes, devoluciones, recargos, etc., originados por facturas (clase 'B') de clientes Monotributistas (con categoría de IVA 'RS'), ingrese un comprobante de débito o de crédito con clase 'A' - es posible indicar el comprobante de referencia (tipo y número de comprobante) y el período asociado.

El Período asociado (Desde Fecha - Hasta Fecha) se informará en el xml del comprobante a enviar a AFIP. Este dato es de ingreso obligatorio.  
Al informar un comprobante de referencia, quedará registrada en el sistema, la imputación del comprobante (de débito o de crédito).  
En los procesos de generación automática o masiva de comprobantes de débito o crédito, quedan registradas las imputaciones en el sistema y se informará automáticamente el período asociado en el xml del comprobante a enviar a AFIP. Por defecto, se informa la fecha de emisión del comprobante de ajuste, como rango fechas de este período.

De esta manera, evitará que su comprobante electrónico sea rechazado por AFIP (al ser de distinta clase o tener letra diferente a la del comprobante de origen).

**Facturación masiva de pedidos de tiendas  
**Tenga en cuenta que al facturar pedidos originados en Tango Tiendas con anterioridad a la activación del [parámetro relacionado con la RG 5003](https://ayudas.axoft.com/25ar/paramgrales_gv/#parametros-para-comprobantes), el sistema los facturará utilizando el talonario 'A' definido en este proceso de facturación masiva a pesar de que tengan asignado un talonario 'B'.

##### Contenidos relacionados

  * [Video sobre Ley 27618 de monotributo](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/leymonotributo_gral_vid/)

  * [Video sobre emisión de facturas "A" a monotributistas](https://ayudas.axoft.com/25ar/videos/gv_carp_vid/factamonotrib_gv_vid/)
