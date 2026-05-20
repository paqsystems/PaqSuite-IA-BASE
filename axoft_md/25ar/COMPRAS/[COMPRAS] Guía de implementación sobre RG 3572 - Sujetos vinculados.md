# Guía de implementación sobre RG 3572 - Sujetos vinculados

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_cp2/guia_calcretotras_cp2/?p=11911/

## Contenido

# Guía de implementación sobre RG 3572 - Sujetos vinculados

Según la RG 3572/13, se deben informar las operaciones en el mercado interno de las empresas vinculadas entre sí a AFIP, tanto para personas físicas como para personas jurídicas comprendidas en la Tercera Categoría del Impuesto a las Ganancias.

Para ello, debe generar el formulario de Declaración Jurada Nº 968 e informar mensualmente las operaciones realizadas en el período, utilizando el programa aplicativo denominado "AFIP - DGI - REGIMEN INFORMATIVO DE OPERACIONES EN EL MERCADO INTERNO - SUJETOS VINCULADOS - Versión 1.0".  
Con Tango, usted cumple con las disposiciones de esta norma, generando el soporte magnético para la RG 3572, habiendo configurado previamente los proveedores y clientes vinculados a su empresa.

__Nota

Tenga en cuenta que la información utilizada para generar el soporte magnético se obtiene de los módulos **Ventas** , **Ventas Restô** , **Proveedores** , **Compras** y **Compras e Importaciones**.

##### Puesta en marcha

Si el origen de la información es Tango Gestión, para generar el archivo solicitado por la RG 3572, configure previamente:

  * [Parámetros de Ventas](?p=19401/#parametros-para-comprobantes) (en Comprobantes tilde la opción RG 3572 - Sujetos vinculados - Genera información de las operaciones de ventas).
  * [Parámetros de Compras](?p=14676/#principal) (tilde la opción Genera información RG 3572 - Sujetos vinculados).
  * [Clientes](?p=19444) (en la solapa Datos para facturación y cobranzas tilde la opción RG 3572 - Sujetos vinculados: Empresa vinculada e indique el Tipo de operación habitual para el cliente).
  * [Proveedores](?p=14686) (en el parámetro Empresa vinculada ingrese con el valor 'S' e indique el Tipo de operación habitual para el proveedor).



Si el origen de la información es el módulo Liquidador de IVA, para generar el archivo solicitado por la RG 3572, configure previamente:

  * [Clientes](?p=8349) (tilde la opción Sujeto vinculado y seleccione la opción correspondiente del campo Operación sujeto vinculado).
  * [Proveedores](?p=8430) (tilde la opción Sujeto vinculado y seleccione la opción correspondiente del campo Operación sujeto vinculado).
  * Tenga en cuenta, además, la relación entre las fórmulas y los tipos de importes.



**Tabla de relación entre los tipos de importes y fórmulas**

**Código** | **Descripción**  
---|---  
IVA21 | IVA 21%  
IVA27 | IVA 27%  
IVA10.5 | IVA 10.5%  
SUBTGR | Subtotal gravado  
EXENTO | Exento  
IMPNOGR | Importes no integran el Subtotal gravado  
TOTAL | Total  
  
##### Detalle del circuito

Mensualmente, mediante el aplicativo "SIAp - Sujetos vinculados", informe a AFIP de las operaciones con empresas vinculadas.  
Si el origen de la información es Gestión (módulo Ventas o Compras), los comprobantes que se informan son los siguientes:

Ventas:

  * Facturas
  * Notas de crédito
  * Notas de débito



Compras:

  * Factura
  * Factura - remito
  * Factura de importación
  * Nota de crédito
  * Nota de débito



Si el origen de la información es el módulo Liquidador de IVA los comprobantes que se informan son los [tipos de comprobantes](?p=8444) que están definidos como tipos de comprobantes interno: factura, nota de crédito y nota de débito.  
Las condiciones que deben cumplir los comprobantes son las siguientes:

  * Deben pertenecer al período seleccionado en el proceso de generación. En el caso de los comprobantes de Compras se toma en cuenta la fecha contable.
  * Deben estar configurados para intervenir en los libros IVA (Compras o Ventas).
  * El cliente o proveedor debe estar configurado como 'empresa vinculada'.



Al configurar un cliente o proveedor como empresa vinculada, debe informar el código de operación habitual para los comprobantes.

  * Los comprobantes ingresados con anterioridad (desde el 01 de Enero 2014 a la fecha de actualización de su sistema), tomarán automáticamente el valor asociado al cliente / proveedor.
  * Los nuevos comprobantes tomarán por defecto el valor configurado en el cliente / proveedor, pudiendo modificarlo en el momento del ingreso o desde el proceso [Modificación de comprobantes de Ventas](?p=20552) y [Compras](?p=15550). En caso de que el origen de la información sea el módulo Liquidador de IVA puede realizar esta operación desde el proceso de [Registración de comprobantes](?p=8433).



Los códigos de operación son los indicados en el ANEXO III de la RG 3572.  
Por último, para generar el archivo, ingrese al proceso de [Generación de RG 3572](?p=11988).
