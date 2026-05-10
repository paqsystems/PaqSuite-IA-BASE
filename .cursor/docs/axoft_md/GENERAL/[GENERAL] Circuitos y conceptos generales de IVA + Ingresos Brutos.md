# Circuitos y conceptos generales de IVA + Ingresos Brutos

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_iv/definiciones_guia_iva/

## Contenido

# Circuitos y conceptos generales de IVA + Ingresos Brutos

Existen 4 conceptos importantes que debe tener en cuenta cuando trabaja con Tango Liquidador de IVA.

  * Fórmulas
  * Modelos de ingreso de comprobantes
  * Reportes
  * Formularios



Cada fórmula definida por el usuario (o preconfigurada por el sistema) tiene un significado, por ejemplo alícuota de IVA, total del comprobante, retención, etc., es decir cada importe que compone un comprobante debe estar definido como una fórmula.

__Nota

Las fórmulas representan conceptos que se pueden utilizar durante el ingreso de comprobantes. Por ejemplo importe gravado, IVA, etc.  


Una vez definidas las [fórmulas](?p=8384) se generan los [modelos de ingreso](?p=8418) de comprobantes, que son una plantilla utilizada durante la registración de comprobantes donde debe indicar qué importes (fórmula) y en qué orden se van a ingresar.  
Finalizada la carga de modelos de ingreso de comprobantes, puede ingresar los comprobantes de ventas / compras.  
Una vez ingresados los comprobantes, puede listar la información a través de los reportes y formularios.  
Tenga en cuenta que cualquier cambio que realice sobre las fórmulas impactará sobre los próximos comprobantes que ingrese o modifique. Es decir durante el ingreso o actualización de comprobantes se trabaja con las fórmulas activas. Es probable que el sistema genere nuevos importes cuando modifique un comprobante afectado por un cambio de fórmula.

__Nota

El sistema no modifica los importes de los comprobantes afectados por cambios en las fórmulas a menos que los vuelva a editar.

##### Contenidos relacionados

  * [Videos sobre Liquidador de IVA](https://ayudas.axoft.com/24ar/videos/iva_carp_vid/)
