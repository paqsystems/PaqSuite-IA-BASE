# Guía de Punto de Venta sobre código de operación de traslado - Rentas Bs.As. (COT)

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_gv2/guia_codopertraslad_gv2/

## Contenido

# Guía de Punto de Venta sobre código de operación de traslado - Rentas Bs.As. (COT)

Según la reglamentación del Régimen de Traslado o Transporte en la Provincia de Buenos Aires establecida en las Resoluciones Normativas Nº 14/11; Nº 34/11 y Nº 45/11, se dictan las normas reglamentarias para dar cumplimiento con la obligación de los propietarios o poseedores de determinados bienes, de amparar el traslado en el territorio provincial mediante un código de operación.

Dicho traslado o transporte de bienes en el territorio de la provincia de Buenos Aires está amparado por el Código de Operación de Traslado (COT).

__Nota

Recuerde que la tecla rápida _< F3>_ permite realizar la búsqueda de un texto en el árbol de procesos de todos los módulos. Como resultado, se exhibirá el nombre de los procesos que incluyen el texto ingresado, con la indicación del módulo y carpeta en la que se encuentran.

El siguiente instructivo pretende mostrar los pasos a seguir para configurar correctamente el sistema para operar en base a esta normativa.

**Obtención del COT correspondiente al traslado o transporte de mercadería a realizar  
**Usted puede trabajar en base a dos modalidades:

  * **Obtención automática del COT:** (modalidad recomendada) para trabajar de esta forma utilice el proceso [Generación de Archivo de Transporte de Bienes - Rentas Bs. As.](?p=21480/#generacion-de-archivo-de-transporte-de-bienes-rentas-bsas)
  * **Obtención del COT de forma manual:** en este caso debe comunicarse telefónicamente con Rentas Bs. As. a fin de conseguir el COT. Posteriormente deberá ingresar al proceso [Modificación de Comprobantes](?p=20552) para registrar el COT correspondiente a cada comprobante. Para ello, busque el comprobante a modificar y pulse la tecla _< F6> \- Código Transporte Rentas_.



##### Puesta en marcha

Para generar el archivo solicitado por Rentas Bs. As., debe realizar el procedimiento detallado a continuación.  
Toda esta información se verá reflejada en el proceso [Generación Archivo Transporte de Bienes - Rentas Bs. As.](https://ayudas.axoft.com/24ar/genarchtranspbienrentbsas_gv2), disponible en Informes | Información impositiva.

**Parámetros de Ventas  
**Como primera medida, ingrese a [Empresa](https://ayudas.axoft.com/24ar/paramgrales_gv2/#parametros-para-empresa) dentro del proceso [Parámetros de Ventas](https://ayudas.axoft.com/24ar/paramgrales_gv2), para ingresar los datos relacionados a su domicilio. Desde la solapa Comprobantes, sub-solapa Transporte de bienes (COT), active el parámetro Genera Remitos Electrónicos y tilde las opciones Edita importe total sin impuestos y Edita cantidad total de kilos.  
Ingrese los datos relacionados a su domicilio y a continuación, los vinculados con la logística.

Genera remitos electrónicos: este parámetro general habilita la configuración de artículos y el envío de información de los comprobantes a Rentas Bs. As., para obtener el Código de Operación y Traslado (posibilita el uso de la función _< F6> \- Código Transporte Rentas_ en los procesos [Consulta de remitos](?p=19261), [Consulta de comprobantes](?p=21172) y [Modificación de comprobantes](?p=20552)).

Para más información consulte [Generación Archivo Transporte de Bienes - Rentas Bs. As.](?p=21480/#generacion-de-archivo-de-transporte-de-bienes-rentas-bsas)

Planta: indique el número de planta habitual desde donde parten sus envíos.

Puerta: indique el número de puerta habitual desde donde parten sus envíos.

Edita importe total sin impuestos: active este parámetro si usted cumple con la normativa vigente, para ingresar el importe desde la generación de comprobantes. A partir del 05 de agosto del 2019, el importe a informar será neto de componente tributario.  
Desde la emisión de remitos debe informar el importe sin impuestos.  
Desde facturas, notas de crédito y notas de débito, dentro de _Más Acciones_ se visualizará una opción de _Transporte de bienes_ que se completará con el importe total calculado (sin impuestos), pudiendo ser modificado.

Edita cantidad total de kilos: para ingresar el pasaje correspondiente en kilogramos desde la generación de comprobantes, necesario si usted cumple con la Normativa Nº 014/11, vigente desde el 15 de Mayo del 2011.  
Este valor debe ser un valor entero y sin decimales. En la emisión de remitos, facturas, notas de crédito y notas de débito, dentro de _Más Acciones_ se visualizará una opción de _Transporte de bienes_ para ingresar dicho valor.

Para que ambos parámetros estén habilitados, configure en 'Si' el parámetro Genera remitos electrónicos. Si usted no tilda alguno de los parámetros mencionados, y cumple con la Normativa Nº 014/11, podrá ingresar los valores correspondientes desde [Generación Archivo Transp. de Bienes-Rentas BS.AS.](?p=21480/#generacion-de-archivo-de-transporte-de-bienes-rentas-bsas) en las columnas "Importes sin impuestos" y "Total kilogramos", antes de realizar la exportación.  
Al tener tildadas esas opciones, cada vez que emita un remito o una factura que afecte stock tendrá la posibilidad de cargar los datos referidos al importe total sin impuestos y el total de kilos para que esa información sea enviada a ARBA.

Versión: la opción 'Original' se considera por defecto. A partir del día 05 de agosto 2019, deberá seleccionar la opción 'Agosto 2019' como versión de COT a utilizar.

Importe mínimo sin impuestos: es el importe que actúa de filtro en el campo Importe sin impuestos del seleccionador de comprobantes, del proceso Generación Archivo Transp. de Bienes-Rentas Bs.As.

Cantidad total mínima de kilos: es la cantidad en kilos que actúa de filtro en el campo Desde cantidad total de kilos del seleccionador de comprobantes, del proceso Generación Archivo Transp. de Bienes-Rentas Bs.As.

**Datos de los transportistas  
**Desde Archivos | Actualizaciones del proceso [Transportes](https://ayudas.axoft.com/24ar/transporte_gv2) del módulo Ventas ingrese la información correspondiente al domicilio, la categoría frente al IVA y el número de CUIT de los transportistas.

**Configuración de artículos  
**Desde el módulo Stock, en la solapa Datos Legales del el proceso [Artículos](https://ayudas.axoft.com/24ar/articulo_carp_st#datoslegales), complete los datos requeridos por Rentas Bs. As. para la generación de remitos electrónicos.  
Para ello, ingrese el código único de producto conforme a la codificación MERCOSUR para ser utilizada en los remitos electrónicos, de acuerdo al Nomenclador de Artículos de Rentas y se conforma con una combinación de seis dígitos; el código de las unidades de medida (de Stock y de Ventas) según la tabla de valorización de Rentas Bs. As. y sus equivalencias.  
En el caso de ingresar un código único de producto inválido, el sistema exhibirá la lista de códigos que comiencen con los valores ingresados.  
Para más información, consulte en la ayuda o en el manual del módulo Stock, la explicación correspondiente al proceso [Artículos](https://ayudas.axoft.com/24ar/articulo_carp_st), para el ítem Transporte de Bienes - Rentas Bs.As.  
Usted puede actualizar esta información, en forma masiva, mediante el proceso [Actualización Global de Códigos de Rentas Bs. As.](?p=17020) (del módulo Stock).

**Comando Configuración de Generación Archivo Transporte de Bienes - Rentas Bs. As.  
**Para el envío de información a Rentas Bs. As. es necesario establecer un canal seguro (HTTPS).  
De acuerdo a lo mencionado en la Disposición Normativa Serie "B" 63/06, debe registrarse como usuario en la aplicación Transporte de Bienes en el sitio web de [Rentas Bs. As.](http://www.arba.gov.ar)  
Una vez que reciba la dirección de URL, el código de usuario y la contraseña para conectarse con el sitio de Rentas Bs.As., ingrese al proceso [Generación Archivo Transporte de Bienes - Rentas Bs. As.](https://ayudas.axoft.com/24ar/genarchtranspbienrentbsas_gv2), disponible en Informes | Archivos DGI, haga clic en el comando Configuración y registre estos datos en la solapa Rentas.  
Además, en la solapa Conexión a Internet indique el tipo de conexión. Si utiliza una conexión específica (con Proxy), indique los datos necesarios para conectarse exitosamente. Puede definir que el sistema utilice la configuración definida en el Explorador de Internet para facilitar la parametrización de conexión a Internet.

##### Detalle del circuito

Como primer medida, usted genera los remitos desde el proceso [Remitos](?p=19774) o desde las facturas remitidas desde [Facturas](?p=19327).  
En el momento de emitir un remito o una factura que afecte stock, antes de la grabación del comprobante, el sistema mostrará la ventana Transporte de Bienes desde donde usted podrá modificar el importe total sin impuestos y el total de kilos que luego serán informados a ARBA.  
Desde la opción de configuración del proceso [Generación Archivo Transporte de Bienes-Rentas Bs. As.](?p=21480/#generacion-de-archivo-de-transporte-de-bienes-rentas-bsas) configure los siguientes campos correspondiente a origen, destino, datos del transporte y el recorrido a realizar.  
Desde la solapa Selección de comprobantes usted podrá seleccionar los comprobantes a informar. Una vez seleccionados podrá observar el importe con impuestos y el total de kilogramos, que corresponden a los valores que se cargaron en la ventana Transporte de Bienes al momento de la emisión del remito o factura.

Más información:

Tenga en cuenta que tanto el _Importe con impuestos_ y el _Total kilogramos_ que aparecen en esta ventana podrán ser modificados en caso de que el usuario necesite informar un dato diferente al que cargó al emitir el remito o la factura.

Al grabar con <F10> se enviará la información a ARBA, en caso de que el comprobante se aceptado se obtendrá un código de integridad. También cuenta con la posibilidad de visualizar el comprobante aceptado desde la opción Listar.

**Nuevas disposiciones ARBA (05-08-2019)  
**Para más información, consulte el siguiente link: [http://www.arba.gov.ar/Apartados/Agentes/AgenteCot.asp?apartado=IIBB&Lugar=E](http://www.arba.gov.ar/Apartados/Agentes/AgenteCot.asp?apartado=IIBB&Lugar=E)

  * A partir del 05/08/2019, los importes informados a A.R.B.A. corresponden a totales sin impuestos.
  * A partir del 05/08/2019, para cada documento emitido a Consumidor Final que supere o iguale los $ 5000 sin impuestos, se debe proporcionar los datos de documento / CUIT y Nombre / Razón Social.



**Consulta de los datos ingresados para Rentas Bs.As.  
**Usted puede consultar la información ingresada, desde los siguientes procesos:

  * [Consulta de Remitos](?p=19261), pulsando la tecla _< F6> \- Código Transporte Rentas_.
  * [Consulta de Comprobantes](?p=21172), pulsando la tecla _< F6> \- Código Transporte Rentas_.
  * Informe de Remitos electrónicos / COT desde Live.
