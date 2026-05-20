# Percepciones

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_guiagenerarchpdf_gla/?p=19407/

## Contenido

# Percepciones

Usted puede definir distintos tipos de percepciones, obteniendo una mayor flexibilidad y la posibilidad de asociarles un modelo de formato adecuado para la generación de soportes magnéticos.

Este proceso permite agregar, modificar y eliminar tipos de percepción con distintas bases de cálculo y alícuotas. Para definir adecuadamente las percepciones, es recomendable que revise la [Guía de implementación sobre percepciones definibles](?p=27041).

Para cada código de percepción definible se ingresarán los siguientes datos:

##### Principal

Código y Descripción de la percepción: permite identificar los distintos tipos, bases y alícuotas de percepciones posibles.

Tipo de impuesto: en este campo se parametriza el tipo de impuesto de la percepción definible.  
Los valores posibles son:

  * IVA
  * Ingresos Brutos
  * Impuestos Internos
  * Otros impuestos



Código de régimen: ingrese el código asignado por la AFIP u otro organismo para la Percepción indicada.

Jurisdicción: ingrese en este campo a qué Jurisdicción pertenece la percepción.  
Los valores posibles son:

  * Nacional
  * Provincial
  * Municipal
  * Otra



Si se selecciona una Jurisdicción Provincial se habilitará el campo Código de Provincia para poder seleccionarla.

__Nota

En la generación del archivo Libro IVA Digital, los importes correspondientes a percepciones se ubican en distintos campos según la combinación entre el tipo de impuesto y la jurisdicción.

**Tipo de impuesto** | **Jurisdicción** | **Campo del archivo**  
---|---|---  
IVA u Otros impuestos | Nacional | Importe de percepciones o pagos a cuenta de impuestos nacionales  
IVA u Otros impuestos | Municipal | Importe de percepciones impuestos municipales  
Ingresos Brutos | Cualquiera | Importe de percepciones de Ingresos Brutos  
IVA u Otros impuestos | Provincial u Otra | Otros tributos
