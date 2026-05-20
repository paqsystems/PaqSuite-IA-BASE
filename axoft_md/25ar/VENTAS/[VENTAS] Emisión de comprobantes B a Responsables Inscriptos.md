# Emisión de comprobantes B a Responsables Inscriptos

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv2/guia_rg5616_gv2/?p=13061/

## Contenido

# Emisión de comprobantes B a Responsables Inscriptos

Si el CUIT del cliente presenta requerimientos pendientes de verificaciones, ARCA considerará automáticamente que el cliente o receptor del comprobante es un Consumidor Final.

En esta situación, si está activo el parámetro general RG 5616 - Emisión de comprobantes y es 'Responsable Inscripto', al emitir las facturas electrónicas de tipo 'B' para estos clientes desde el Facturador con la opción:

  * **Facturas:**  
El sistema exhibirá el mensaje: "El talonario 'B' seleccionado no corresponde con la categoría de IVA 'Responsable inscripto' del cliente ¿Desea cambiarlo? Si continúa se va a considerar a la condición ante el IVA del cliente como 'Consumidor Final'."  
Las opciones disponibles serán: 'Cambiar talonario' o 'Continuar'.  
Si elige 'Continuar', el sistema asignará al cliente la condición de IVA: 'Consumidor Final' para el comprobante en edición y deshabilitará la posibilidad de modificar el talonario.
  * ****Facturación masiva:  
****El sistema exhibirá la opción:  
"'Cambiar condición de IVA por RG 5616': si tilda este parámetro, ante pedidos de Responsables Inscriptos que tengan asignado un talonario electrónico 'B', el sistema los considerará Consumidores Finales al facturarlos."
