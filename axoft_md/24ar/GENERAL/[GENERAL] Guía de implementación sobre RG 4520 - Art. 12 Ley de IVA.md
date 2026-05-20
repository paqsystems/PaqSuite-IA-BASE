# Guía de implementación sobre RG 4520 - Art. 12 Ley de IVA

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gla/guia_rg4520_gla/

## Contenido

# Guía de implementación sobre RG 4520 - Art. 12 Ley de IVA

Mediante la Resolución General 4520 (del 10/07/2019), AFIP establece un régimen especial para la emisión y almacenamiento electrónico de comprobantes originales. 

Con Tango, usted cumple con las disposiciones de esta norma para la emisión electrónica de comprobantes clase 'A' (facturas, notas de débito y notas de crédito).

##### Información general

Sujetos comprendidos  
Los responsables inscriptos en el Impuesto al Valor Agregado.  
El alcance del régimen se hace extensivo a los sujetos que actúen en carácter de intermediarios de las operaciones citadas en los párrafos siguientes.

Objetivo  
Respaldar las operaciones indicadas en los puntos 3 y 4 del inciso a) del Artículo 12 de la Ley del Impuesto al Valor Agregado, que no se encuentran alcanzadas por la restricción para el cómputo del crédito fiscal de conformidad a lo dispuesto en el Artículo 52 del Decreto Nº 692/98 y sus modificaciones, y a las previsiones de la Resolución General Nº 74.  
Detalle de operaciones contempladas:

  * Locaciones y prestaciones de servicios (a que se refieren los puntos 1, 2, 3, 12, 13, 15 y 16 del inciso e) del artículo 3º). 
    * Bares, restaurantes, cantinas, salones de té, confiterías y en general por quienes presten servicios de refrigerios, comidas o bebidas en locales —propios o ajenos—, o fuera de ellos.
    * Hoteles, hosterías, pensiones, hospedajes, moteles, campamentos, apart-hoteles y similares.
    * Posadas, hoteles o alojamientos por hora.
    * Casas de baños, masajes y similares.
    * Piscinas de natación y gimnasios.
    * Peluquerías, salones de belleza y similares.
    * Playas de estacionamiento o garajes y similares.
  * Compras e importaciones definitivas de indumentaria que no sea ropa de trabajo y cualquier otro elemento vinculado a la indumentaria y al equipamiento del trabajador para uso exclusivo en el lugar de trabajo.



Derogaciones  
Se deroga la Resolución General 3668 y sus modificatorias.  
Se deja sin efecto el formulario de declaración jurada 8001.

Emisión de comprobantes electrónicos originales  
Los sujetos mencionados deberán observar las disposiciones de la presente resolución general, a efectos de confeccionar las facturas, notas de crédito y notas de débito electrónicas originales clase 'A'.  
En los mencionados comprobantes electrónicos se deberá indicar expresamente el motivo de la excepción que permite la emisión de comprobantes clase 'A', según se trate de: Locador o prestador del mismo servicio; Conferencia, congreso, convención o evento similar; Ropa con destino a bien de cambio; Indumentaria y accesorios de uso exclusivo en los lugares de trabajo; Alojamiento o alimentación de la tripulación; Intermediario.

##### Puesta en marcha

  * [Parámetros de Ventas](?p=19401)
    * En la subsolapa Generales de la solapa [Comprobantes](?p=19401/#parametros-para-comprobantes) tilde el parámetro RG 4520 - IVA para registrar en el sistema que cumple con esta resolución.


  * Realice la puesta en marcha para comprobantes electrónicos. 
    * Para más información, consulte la [Guía de implementación y operación sobre comprobantes electrónicos](?p=26548) (del módulo Ventas).



##### Detalle del circuito

Para la emisión electrónica de comprobantes clase 'A' bajo la Resolución General 4520:

  * Opere con el Facturador para generar los comprobantes electrónicos.
  * Cuando ingrese comprobantes clase 'A', pulse las teclas <Alt + G> para seleccionar el motivo de excepción requerido por AFIP.
  * También puede generar sus comprobantes clase 'A' desde el proceso Facturación de pedidos, indicando el motivo de excepción para las facturas a generar.
  * Desde el [Administrador de Comprobantes Electrónicos](?p=19186), solicite a la AFIP la autorización de emisión de los comprobantes electrónicos pendientes o rechazados.  
Desde este proceso también podrá visualizar, imprimir o enviar por correo electrónico a sus clientes, los comprobantes ya autorizados por la AFIP.
  * Utilice los procesos [Modificación de comprobantes](?p=20552) y [Consulta de comprobantes](?p=21172) para cambiar o verificar la información de sus comprobantes ingresados.
  * Desde las consultas Live de facturación y de cuentas corrientes, en la solapa Información adicional para AFIP es posible consultar el código de excepción y su descripción asignado al comprobante.
