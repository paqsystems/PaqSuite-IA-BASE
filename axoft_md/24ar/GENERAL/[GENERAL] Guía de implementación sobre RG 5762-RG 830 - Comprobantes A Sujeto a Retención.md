# Guía de implementación sobre RG 5762/RG 830 - Comprobantes A Sujeto a Retención

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_guiagenerarchpdf_gla/?p=26834/

## Contenido

# Guía de implementación sobre RG 5762/RG 830 - Comprobantes A Sujeto a Retención

Esta guía detalla la configuración y el circuito operativo necesario para aplicar la retención prevista por la RG 5762 en comprobantes 051 - factura 'A' con leyenda "Operación sujeta a retención" (ex facturas 'M') - Comprobante para RG 3685/4597.

La RG 5762 funciona como retención relacionada a la retención de Ganancias RG 830. En las operaciones que cumplen las condiciones, el sistema calcula ambas retenciones, compara los importes y aplica la de mayor importe, dejando la otra visible en importe cero.  
Cada régimen mantiene sus propias bases, reglas y acumulaciones, y sus reportes impositivos correspondientes.

##### Puesta en marcha

A continuación, se detallan los pasos a seguir para la configuración de la retención relacionada RG 5762.

**Configuración de retenciones**

  * La retención principal RG 830 puede estar definida como 'Ganancias' o de tipo 'Otras'.
  * La retención RG 5762 debe configurarse como tipo 'Otras' y asociarse como retención relacionada.



_1) Crear la retención relacionada (RG 5762):_

  * Configurar la retención RG 5762 como tipo: 'Otras'.
  * Alícuota: según la normativa vigente.
  * Base de cálculo: importe del pago.



_2) Configurar la retención principal:_

  * En la retención de Ganancias, o en la retención principal tipo 'Otras', completar el campo Código de retención asociada RG 5762.



_3) Configuración en proveedores:_

  * El proveedor solo debe tener configurada la retención de ganancias base (RG 830). El sistema no requiere asignar la RG 5762 directamente en el proveedor.  
La aplicación depende de las condiciones definidas en el punto siguiente.



**Condición para aplicar la RG 5762**

  * En órdenes de pago:  
Si se incluye al menos un comprobante con leyenda “Operación sujeta a retención”.
  * En comprobantes al contado:  
El comprobante ingresado corresponde al tipo 051 – Factura A con leyenda “Operación sujeta a retención” en el campo comprobante para RG 3685/4597.
  * En pagos a cuenta:  
Siempre que el proveedor cumpla con al menos una de las siguientes condiciones: 
    * Condición A  
Tiene configurada una retención de Ganancias.  
En la solapa “Resoluciones”, tiene definido en Comprobante para RG 3685/4597 el código “051” - Factura A con leyenda “Operación sujeta a retención”.
    * Condición B  
El último comprobante registrado para ese proveedor corresponde a una operación sujeta a retención.  
Además, en su ficha tiene configurada una retención de Ganancias, y una retención relacionada asociada a esa retención de Ganancias.
  * Si se cumple alguna condición del punto anterior, el sistema muestra: 
    * “El proveedor tiene una retención asociada a la RG 5762. ¿Desea aplicar su cálculo en este pago?”
    * “Sí”: Se comparan la retención de la RG 5762 y la de la RG 830, y se aplica la que sea más alta.
    * “No”: solo se utiliza la retención de Ganancias (RG830) (si corresponde).



##### Preguntas frecuentes

**¿La RG 5762 aplica siempre?  
**No. Solo cuando el comprobante o la condición del proveedor corresponde a una operación sujeta a retención.

**¿Acumula con ganancias?  
**No. Cada régimen mantiene sus propios criterios y acumulados.

**¿Debe configurarse en todos los proveedores?  
**No. Basta con tener la retención que tiene la relación para que el sistema aplique la que corresponde.

**¿Puede presentarse un solo reporte?  
**Sí, pero ambas retenciones deben ser de tipo 'Otras'.

**Ejemplos:**

_Ejemplo 1_

  * Factura: $100.000
  * Ret. Ganancias: $8.000
  * Ret. RG 5762: $6.000
  * Aplica: Ret. Ganancias.



_Ejemplo 2_

  * Factura: $30.000
  * Ret. Ganancias: $500
  * Ret. RG 5762: $1.800
  * Aplica: Ret. RG 5762.



Aclaraciones adicionales:

La retención no aplicada queda visible con importe en 0.  
El sistema recalcula automáticamente si se agregan más comprobantes.  
Un comprobante sin leyenda “Sujeta a retención” no habilita la RG 5762.  
En pagos mixtos, basta con que uno tenga la leyenda para que el sistema habilite la retención relacionada.
