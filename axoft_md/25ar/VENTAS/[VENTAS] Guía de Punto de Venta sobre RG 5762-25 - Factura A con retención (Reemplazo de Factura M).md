# Guía de Punto de Venta sobre RG 5762/25 - Factura A con retención (Reemplazo de Factura M)

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv2/guia_rg5762_gv2/

## Contenido

# Guía de Punto de Venta sobre RG 5762/25 - Factura A con retención (Reemplazo de Factura M)

Esta guía está dirigida a los usuarios de empresas que emiten comprobantes con letra 'M' o que requieran implementar comprobantes 'A' con retención. El objetivo es acompañar la transición establecida por la Resolución General 5762/2025 de ARCA, que elimina comprobantes 'M' a partir del 1 de diciembre de 2025, reemplazándolos por nuevas modalidades de comprobantes 'A'.

La RG 5762/2025 establece dos modalidades de comprobantes 'A':

  * Factura A "OPERACIÓN SUJETA A RETENCIÓN", que reemplaza funcionalmente a la factura 'M', y mantiene el régimen de retenciones fiscales: 100% del IVA y 6% de Ganancias. Se aplica a contribuyentes que no superen los controles fiscales o no acrediten solvencia patrimonial.
  * Factura A "PAGO EN CBU INFORMADA", que permite emitir comprobantes sin retenciones si el contribuyente cumple los controles de la RG 4132 y canaliza todos los cobros en el CBU declarado ante ARCA.



**Novedades y modificaciones  
**La implementación se enfoca en:

  * La incorporación del campo Aplica RG 5762/25 en la definición de talonarios.
  * La necesidad de que los nuevos talonarios 'A con retención' continúen la numeración del talonario 'M' preexistente.



##### Puesta en marcha

**Creación de nuevo talonario 'A' con retención**

  1. Ingrese a Ventas | Archivos | Carga Inicial | Talonarios | Definición.
  2. Cree un talonario 'A' y tilde el parámetro Aplica RG 5762/25, si el contribuyente presenta inconsistencias fiscales o no acredita solvencia patrimonial. 
     1. Si desea continuar con la numeración del talonario 'M', ingrese en el campo Primer número habilitado el valor del próximo número a emitir que tenía en su talonario 'M'. Si corresponde a un punto de venta nuevo, ingrese como Primer número habilitado el valor '1'.
     2. Ingrese a la solapa Impresión: 
        1. Cree un nuevo formulario registrando la parametrización correspondiente y configurando el dibujo (TYP).
        2. Incorpore la leyenda "OPERACIÓN SUJETA A RETENCIÓN" en la cabecera o parte superior.



__Nota

Para más información sobre definición de talonarios, consulte la ayuda de [Definición de talonarios](https://ayudas.axoft.com/25ar/talonario_gv2).  
Para más información sobre configuración de formularios de comprobantes de ventas, consulta la ayuda de [Formularios de ventas](?p=22758).  


Sugerencia:

Usted puede duplicar los TYPs actuales de comprobantes 'M' e incorporar solo la leyenda, manteniendo el diseño original.  


##### Preguntas frecuentes

**¿Qué sucede con los clientes que actualmente emiten comprobantes 'M'?  
**Pueden emitir:

  * Factura A "OPERACIÓN SUJETA A RETENCIÓN".
  * Factura A "PAGO EN CBU INFORMADA".



El contribuyente puede conservar el mismo punto de venta para mantener la correlatividad fiscal o definir uno nuevo si desea diferenciar los comprobantes emitidos bajo el nuevo régimen.

**¿Qué pasa con los talonarios 'M' manuales vigentes?**  
Pueden seguir utilizándose hasta su fecha de vencimiento impresa, conforme lo dispone ARCA. Una vez vencidos, deberán reemplazarse por los nuevos talonarios 'A'.

**¿Qué debo hacer con los talonarios 'M' del sistema?  
**Debe modificar la numeración del "Último número habilitado", con el último generado con ese talonario.

**¿Qué sucede si intento crear un talonario electrónico con letra 'M?  
**A partir del 01/12/2025, la Factura 'M' deja de estar vigente según la RG 5762/2025.  
Por lo tanto, al intentar seleccionar la letra 'M' en la definición de talonarios, el sistema muestra la siguiente advertencia: "El comprobante M se encuentra fuera de vigencia a partir del 01/12/2025 (RG 5762/2025). Utilice comprobante A."  
Esta advertencia tiene carácter informativo y busca guiar al usuario para que, en lugar de crear talonarios 'M', defina los nuevos talonarios 'A' conforme al régimen vigente.

**¿Puedo emitir comprobantes A "OPERACIÓN SUJETA A RETENCIÓN" desde un Controlador Fiscal?**  
No. Los comprobantes clase A "OPERACIÓN SUJETA A RETENCIÓN" no pueden ser emitidos mediante controladores fiscales, según lo dispuesto por la RG 5762/2025. Estas operaciones deberán realizarse exclusivamente por medios electrónicos a través del Régimen de Emisión de Comprobantes Electrónicos Originales (RECE).
