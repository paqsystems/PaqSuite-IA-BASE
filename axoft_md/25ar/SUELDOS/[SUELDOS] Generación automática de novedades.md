# Generación automática de novedades

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_sua/guia_puestamarcha_sua/?p=13098/

## Contenido

# Generación automática de novedades

A través de esta opción se incorporan en forma automática al módulo Sueldos, novedades a liquidar, generadas por medios externos, por el módulo Control de personal o bien, por registraciones propias del módulo Sueldos.

Un asistente lo guía en el proceso de generación.

Origen: seleccione el origen de los datos que generará la importación de novedades a Sueldos.

A continuación, detallamos las características para cada uno de los casos.

##### Partes diarios

Transporte de las novedades generadas en el módulo Control de personal.  
Esta opción está habilitada cuando en el proceso [Parámetros de Sueldos](?p=13208) se configuró la Registración de novedades de otros módulos en forma 'Diferida', y está deshabilitada, si se definió 'En línea'.  
Indique el grupo de legajos y las fechas a considerar en la generación.

##### Detalle de licencias

Generación de novedades a liquidar a partir del registro de los días por licencias (vea [Detalle de licencias](?p=13067)), realizado en el módulo Sueldos.  
Indique el grupo de legajos y las fechas a considerar en la generación.  
El proceso tiene en cuenta aquellas licencias con estado 'A generar'.  
Finalizada la generación de novedades, éstas quedan con estado 'Transferido'.

##### Vacaciones

Generación de novedades a liquidar a partir del registro de los días por licencia vacacional, realizado mediante el proceso de [Vacaciones](?p=13215) en el módulo Sueldos.  
Indique el grupo de legajos a considerar en la generación.  
A continuación, parametrice las novedades por vacaciones. Para ello, indique el año de cierre vacacional a considerar, el período a generar y los distintos códigos de novedad por vacaciones a liquidar por Convenio y Adicionales.  
El proceso tiene en cuenta aquellos tramos planificados con estado 'Definitivo'.  
Finalizada la generación de novedades, éstos quedan con estado 'Transferido'.

##### Vacaciones no gozadas

Generación de novedades a liquidar a partir del registro de los días por licencia vacacional no gozados, realizado mediante el proceso de [Vacaciones](?p=13215) en el módulo Sueldos.  
Parametrice las novedades por vacaciones. Para ello, indique el año de cierre vacacional a considerar, el período a generar y los distintos códigos de novedad por vacaciones a liquidar por Convenio y Adicionales, indicando sus respectivas fechas.  
A continuación, indique el grupo de legajos a considerar en la generación.  
El proceso tiene en cuenta aquellos tramos planificados con estado 'Definitivo'.  
Finalizada la generación de novedades, éstos quedan con estado 'Transferido'.

##### Tipos de archivo

Genera [novedades](?p=13190) a liquidar a partir de novedades generadas con cualquier otra aplicación, sobre la base de un archivo de integración que cumpla con la definición de estructura de registro.  
Seleccione el tipo de archivo externo: archivo de texto ASCII o archivo XML.  
A continuación, indique el directorio donde está grabado el archivo de integración que contiene las novedades a importar. Utilice el botón "Examinar".

__Nota

Tenga presente que el archivo a importar debe cumplir con las especificaciones de estructura e integridad de datos.

__Nota

La importación desde archivo **Excel** , a partir de la versión **Delta 2** , se encuentra disponible desde [Novedades registradas](?p=12996).

**Especificaciones de estructura**

En la siguiente tabla se detalla la estructura de registro y las longitudes de cada campo:

**Campo** | **Longitud** | **Tipo de dato**  
---|---|---  
LEGAJO | 9 | Numérico  
NOVEDAD | 10 | Carácter  
FECHA | 10 | Fecha(máscara: dd/mm/aaaa)  
CANTIDAD | 16 | Importe (máscara: sin separador de miles, con separador decimal informado en Parámetros de Sueldos | Novedades)  
VALOR | 16 | Importe (máscara: sin separador de miles, con separador decimal informado en Parámetros de Sueldos | Novedades)  
  
**Especificaciones de integridad:**

**Campo** | **Validación de dato**  
---|---  
LEGAJO | El Nro. de legajo no puede estar vacío, debe existir y estar habilitado para sueldos.  
NOVEDAD | El código de novedad no puede estar vacío y debe existir como novedad.  
FECHA | La fecha no puede estar vacía y debe estar dentro de los tramos laborales del legajo.  
CANTIDAD | La cantidad no puede estar vacía y debe ser igual o mayor a 0  
VALOR | El valor no puede estar vacío y debe ser igual o mayor a 0  
  
**Sin separación de campos**

Carácter: alineado a izquierda

Numérico / Importe: alineado a derecha

Separador decimal: parametrice el separador decimal a considerar como válido en la importación del archivo ASCII. Para ello, ingrese al proceso [Parámetros de Sueldos](?p=13208), en la solapa Novedades e indique en el parámetro Símbolo para separador de decimales, si utiliza "punto" o "coma" como separador decimal.

Para mayor información, consulte el ítem Archivo externo.

##### Contenidos relacionados

  * [Video de novedades y licencias](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/novedlicencia_sua_vid/)

  * [Video sobre Capital Humano](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/caphumano_gral_vid/)

  * [Video sobre Control de personal](https://ayudas.axoft.com/25ar/videos/cpa_carp_vid/)

  * [Video sobre trabajadores de jornada parcial](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/jornparcial_sua_vid/)

  * [Video sobre vacaciones](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/vacaciones_sua_vid/)

  * [Videos sobre Tango Empleados](https://ayudas.axoft.com/25ar/videos/nexo_carp_vid/empleados_nexo_vid/)

  * [Videos sobre registración de novedades](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/novedades_sua_vid/)
