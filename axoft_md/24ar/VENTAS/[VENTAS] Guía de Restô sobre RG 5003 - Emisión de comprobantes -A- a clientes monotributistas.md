# Guía de Restô sobre RG 5003 - Emisión de comprobantes "A" a clientes monotributistas

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv3/guia_rg5003_gv3/

## Contenido

# Guía de Restô sobre RG 5003 - Emisión de comprobantes "A" a clientes monotributistas

Esta guía de implementación le indica los pasos a seguir para poner en marcha este circuito. La RG 5003 especifica que a partir del 01/07/2021 se debe emitir comprobantes del tipo 'A' con IVA discriminado a clientes monotributistas.

Para comenzar a utilizar el circuito debe seguir estos pasos:

  * Ingrese a la configuración de la terminal, en la solapa Facturación sección Resoluciones AFIP, y tilde la opción RG 5003 - Emisión de comprobantes "A" a monotributistas.
  * Si emite comprobantes electrónicos, ingrese al proceso Formularios del módulo Procesos generales | Tablas generales | Formularios | Ventas y agregue la siguiente variable.  
**@YM:** esta variable permite imprimir la siguiente leyenda que exige la RG 5003: "El crédito fiscal discriminado en el presente comprobante, sólo podrá ser computado a efectos del Régimen de Sostenimiento e Inclusión Fiscal para Pequeños Contribuyentes de la Ley Nº 27.618". Este texto solo se imprime cuando haya activado el parámetro general y esté emitiendo un comprobante a un monotributista.



__Importante

Como el texto ocupa 191 caracteres, implementamos una nueva variable de control denominada**@R5003CARACTERESPORLINEA** que permite definir la cantidad de caracteres a imprimir en el renglón, por ejemplo, si la configura así _@R5003CARACTERESPORLINEA=50_ imprimirá la leyenda en 4 renglones. Tenga en cuenta que para implementar este ejemplo deberá repetir la variable de reemplazo **@YM** en 4 renglones como detallamos a continuación:

@YM  
@YM  
@YM  
@YM

Aún cuando la norma no especifica en qué lugar del comprobante se debe mostrar la leyenda, sugerimos hacerlo en algún lugar del pie ya que está cerca de los importes de IVA a los que hace referencia el texto.

Si emite comprobantes a través de controladores o impresoras fiscales, ingrese al proceso [Parámetros generales](?p=19401) del módulo Ventas y agregue la siguiente variable.

**@YM:** esta variable permite imprimir la leyenda que exige la RG 5003 en este tipo de equipos: "Receptor del comprobante - Responsable Monotributo". Tenga en cuenta que los controladores fiscales de "vieja tecnología" imprimirán esta leyenda en dos reglones por lo que le sugerimos que deje la línea siguiente a la variable **@YM** en blanco.

##### Otras consideraciones

**Emisión de comprobantes  
**Tenga en cuenta que una vez configurada esta RG, el sistema considerará que debe emitir comprobantes 'A' a todos los monotributistas y en líneas generales aplicará las mismas validaciones que se aplican para responsables inscriptos.

**Alta de clientes  
**Cuando registre un nuevo cliente Monotributista con categoría de IVA 'RS' -sea éste un cliente habitual, ocasional o potencial, el sistema le asignará la nueva configuración impositiva (desde todas las opciones del sistema que habilitan el alta de clientes).
