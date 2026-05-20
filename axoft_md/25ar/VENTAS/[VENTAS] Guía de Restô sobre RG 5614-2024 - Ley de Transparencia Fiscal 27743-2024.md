# Guía de Restô sobre RG 5614/2024 - Ley de Transparencia Fiscal 27743/2024

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv3/guia_rg5614_gv3/

## Contenido

# Guía de Restô sobre RG 5614/2024 - Ley de Transparencia Fiscal 27743/2024

Esta guía de implementación le indica los pasos a seguir para poner en marcha este circuito. La RG 5614/2024 especifica que los emisores Responsables Inscriptos deben discriminar el IVA e Impuestos Nacionales Indirectos (impuestos internos) que incidan en el precio, en la impresión de los comprobantes de ventas (Comprobantes tipo 'B') que emitan a Consumidores Finales y Exentos.

__Nota

Para más información referida a este tema, puede observar [este video](https://www.youtube.com/watch?v=8x0M5SiZDz8). También puede consultar la reglamentación y ley 27743 en <https://www.boletinoficial.gob.ar/detalleAviso/primera/318151/20241213> y <https://www.boletinoficial.gob.ar/detalleAviso/primera/310191/20240708> (Titulo VII, Régimen de Transparencia Fiscal al Consumidor) respectivamente.  


Para comenzar a utilizar el circuito debe seguir estos pasos.

##### Puesta en marcha

Ingrese a la configuración de la terminal, en la solapa Facturación, sección Resoluciones AFIP y tilde la opción RG 5614 - Ley de Transparencia Fiscal 27743/2024.

Si emite comprobantes electrónicos o pre-impresos, ingrese al proceso [Formularios](?p=11875) del módulo Procesos generales (Tablas generales | Formularios | Ventas) de aquellos formularios que utilice para comprobantes letra 'B' y agregue en el espacio inferior izquierdo (la normativa así lo indica) las leyendas y variables de impresión que se detallan a continuación según el tipo de comprobante.

**Variable de impresión** | **Significado**  
---|---  
@T8 | Muestra el total de IVA.  
@VI | Muestra el total de IVA sin percepciones.  
@VN | Muestra el total de impuestos internos.  
  
Luego, en formularios de facturas y notas de crédito la leyenda a agregar es: "Régimen de transparencia fiscal al consumidor (Ley 27743)".  
De esta manera, en el comprobante la leyenda aparecerá como se muestra en la siguiente imagen.

##### Configuración de leyendas y variables en controladores fiscales

Si el usuario emite comprobantes fiscales, debe configurar las leyendas y variables correspondientes desde:

Menú: Ventas Restô | Archivos | Carga Inicial | Parámetros Generales

En la vista Valores por defecto para controladores fiscales, ubique la sección Pie.

###### Controladores fiscales de generación anterior

En estos equipos solo están disponibles las líneas 12, 13 y 14 para definir leyendas y variables.

**Siga estos pasos:**

  1. En la línea 12, en el campo Código de variable (columna izquierda), ingrese "@T8".
  2. En el campo Texto para variable, ingrese "IVA".
  3. En la línea 13, en el campo Código de variable, ingrese "@VN".
  4. En el campo Texto para variable, ingrese "IMP INT".
  5. La línea 14 quedará libre para que, en caso de ser necesario, pueda agregar otra variable adicional.



__Nota

Las variables deben ubicarse en dos líneas consecutivas.  


**Descripción de variables:**

**@T8:** muestra el total de IVA.

**@VN:** muestra el total de impuestos internos.

__Importante

Ambas se imprimen en facturas y notas de crédito.  


###### Controladores fiscales de última generación

En estos equipos se encuentran habilitadas las líneas 12 a 21, con soporte para variables adicionales.  
Las variables disponibles son:

**Variable** | **Valor que representa**  
---|---  
@X1 | Ley de transparencia fiscal  
@X2 | IVA contenido  
@X3 | Otros impuestos nacionales indirectos  
  
**Ejemplo de configuración:**

Línea | Columna ixquierda | Columna derecha  
---|---|---  
19 | @X1 | (Sin variable)  
20 | @X2 | @T8  
21 | @X3 | @VN  
  
De esta forma, el ticket fiscal mostrará los conceptos y totales asociados a las variables configuradas.
