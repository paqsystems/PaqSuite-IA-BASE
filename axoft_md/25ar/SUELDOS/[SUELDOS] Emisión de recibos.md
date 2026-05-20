# Emisión de recibos

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_sua/guia_puestamarcha_sua/?p=13078/

## Contenido

# Emisión de recibos

Emita los recibos definitivos de las liquidaciones y empleados seleccionados, utilizando formato RPT o TYP, según lo configurado en [Tipos de liquidación](?p=13241).

Si en [Parámetros de Sueldos](?p=13208) posee configurado como modelo de impresión TYP, desde [Formularios](?p=11874) defina el formato del dibujo correspondiente a recibos.  
Si en [Parámetros de Sueldos](?p=13208), posee configurado como modelo de impresión RPT, defina el formato del recibo de sueldos mediante el administrador de reportes (esta opción está dentro del administrador general del sistema).

__Nota

Luego de realizar la impresión de recibos, las liquidaciones de empleados intervinientes cambiarán su estado a 'Recibo emitido'.

Generar PDF individual: obtenga el detalle de los recibos de sueldo en formato PDF de manera individual. El archivo generado se encontrará en la ruta configurada en Parámetros de Sueldos para tal fin.

__Nota

Tenga en cuenta que dicha funcionalidad es exclusiva para recibos generados con **Crystal Reports**.

**Ejemplo...**

_Tipo_comprobante_periodo_tipo_liquidacion_Nro_Legajo_CUIL.pdf_

**Descripción** | **Referencia** | **Ejemplo**  
---|---|---  
Tipo de comprobante | Asigna con una sigla de dos dígitos el tipo de comprobante "recibo de sueldos". | RS  
Período | Período seleccionado en formato año/mes. | 202102  
Tipo de liquidación (*) | Tipo de liquidación (Ver cuadro) | MEN  
Número de dato fijo | Número interno de la liquidación. | 360  
Número de legajo | Número de legajo. | 1231  
CUIL | Numero de CUIL del legajo. | 20-11111111-8  
  
__(*) Tipos de liquidación

**Número de tipo de liquidación** | **Descripción de tipo de liquidación** | **Código de identificación para recibos de sueldo**  
---|---|---  
1 | 1° Quincena | 1QA  
2 | 2° Quincena | 2QA  
3 | Mensual | MEN  
4 | Extraordinaria remunerativa | EXR  
5 | Vacaciones | VAC  
6 | Aguinaldo | SAC  
7 | Extraordinaria no remunerativa | ENR  
8 | Baja | EGR  
  
Enviar a Tango Empleados: disponga del detalle de recibos de sueldo en archivo PDF individual, para ser publicado al sitio de [Tango Empleados](?p=12448).  
Para más información, vea la [guía de implementación de Tango Empleados](?p=12504).

__Nota

Para conocer los requisitos a cumplir para utilizar sobre Tango empleados consulte su [web comercial.](https://www.tangonexo.com/empleados/)

##### Parámetros

Seleccione el período liquidado (mes y año).

Liquidaciones a procesar: seleccione las liquidaciones a considerar en la impresión de recibos. Por defecto, se incluyen las liquidaciones pendientes de emitir recibo, con estado 'Generada' (si No Autoriza liquidaciones) o con estado 'Revisada' (si Autoriza liquidaciones).  
Para reimprimir recibos, tilde la opción Liquidaciones con estado 'Recibo emitido'.  
Para más información, consulte el ítem [Estados posibles de una liquidación](?p=13037/#estados-posibles-de-una-liquidacion).

Emitir recibos agrupados por legajo: tilde esta opción si desea que los recibos se emitan agrupando los legajos de las liquidaciones seleccionadas; es de utilidad por ejemplo para imprimir la liquidación mensual y la de aguinaldo y que ambos recibos del mismo legajo queden en orden consecutivo.  
Esta funcionalidad solo está disponible si en [Formularios](?p=13208/#formularios) está seleccionada la opción RPT(*).  
Además, para poder utilizar tanto esta función como el ordenamiento por los campos del recibo, es necesario que todas las liquidaciones seleccionadas posean asociado el mismo formato de recibo, para más información consulte [Tipos de liquidación](?p=13241).

**(*)** En caso que se utilicen formatos personalizados por el usuario podrían no obtenerse los resultados esperados para dicha funcionalidad.

Incluye leyenda: es posible incluir una leyenda, para imprimir al pie del recibo de haberes. Si bien el texto se visualiza desde esta ventana, el ingreso se hace desde el proceso [Parámetros de Sueldos](?p=13208).

Obtener liquidaciones

Utilice el botón "Obtener liquidaciones" para marcar los datos fijos de liquidaciones que intervienen en la impresión. Por defecto, el sistema incluye todos los datos fijos del período seleccionado.

##### Legajos

Utilice el [Seleccionador de legajos](?p=11882/#definiciones-previas) para determinar el conjunto de empleados cuyos recibos desea emitir.

##### Contenidos relacionados

  * [Video sobre Capital Humano](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/caphumano_gral_vid/)

  * [Video sobre impuesto a las ganancias sobre horas extras](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/iigghoraextra_sua_vid/)

  * [Video sobre informes y salidas de Sueldos](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/informes_sua_vid/)

  * [Videos sobre Tango Empleados](https://ayudas.axoft.com/25ar/videos/nexo_carp_vid/empleados_nexo_vid/)

  * [Videos sobre modernización laboral - Cambios en Sueldos](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/modernlaboral_sua_vid/)
