# Familiares

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sua/guia_puestamarcha_sua/?p=13088/

## Contenido

# Familiares

Registre los familiares de un empleado y configure la intervención del familiar en distintos procesos del sistema: Asignaciones, Impuesto a las Ganancias e Impresión en el Libroley 20744.

A continuación se presentan los pasos necesarios para dar de alta un nuevo registro.

##### Principal

Número de legajo: seleccione el legajo al cual le asignará un familiar.

Parentesco: indique el grado de parentesco entre las siguientes opciones propuestas: Cónyuge, Hijo, Prenatal, Padre, Madre u Otro.

Fecha alta y Fecha baja: estas fechas se utilizan para los procesos donde interviene la nómina de familiares: [Liquidación de ganancias individual](?p=13158) y [Liquidación de ganancias global](?p=13162) (para considerar al familiar en forma completa o proporcional en el cálculo de las deducciones familiares) y la [Actualización automática de cantidades de familiares](?p=12988) (para generar la cantidad de cada asignación, de acuerdo al período de generación).

Apellido y Nombre: son datos obligatorios a completar.

_Datos personales_

Los campos Código de tipo de documento, Número de documento y CUIL son datos informativos del familiar no siendo obligatoria su carga.

Fecha de nacimiento: ingrese la fecha de nacimiento del familiar. Tenga en cuenta que este dato se utiliza para:

  * calcular la cantidad de hijos por los que se debe abonar asignaciones familiares, ejecutando el proceso [Actualización automática de cantidades de familiares](?p=12988). Recuerde que sólo se considerarán los hijos cuya edad sea menor o igual a la indicada en el proceso [Parámetros de Sueldos](?p=13208).
  * calcular la cantidad de hijos que se pueden deducir del impuesto a las ganancias durante los procesos [Liquidación de ganancias individual](?p=13158) y [Liquidación de ganancias global](?p=13162). Recuerde que sólo se considerarán aquellos hijos cuya edad sea menor o igual a la indicada en el proceso [Parámetros de Sueldos](?p=13208).



Edad: a partir de la fecha nacimiento se calcula la edad del familiar.

Ingrese información personal como lo son la nacionalidad, sexo y estado civil.

El campo Salud indica si el familiar presenta algún tipo de incapacidad.

_Datos del hijo_

Para los familiares con parentesco igual a 'Hijo', ingrese los siguientes datos:

Hijo: seleccione uno de los valores posibles: 'Propio' o 'Del cónyuge'.

Escolaridad y Grado: ingrese en forma opcional, el nivel de estudio actual y si corresponde, el grado o año.

Vigencia del certificado: ingrese en forma opcional, el mes y año hasta el que será válido el certificado de escolaridad. Se generan automáticamente las cantidades de familiares por escolaridad, teniendo en cuenta si están en vigencia para la liquidación, en caso de activar el valor 'Automático c/vto' para la opción Cantidad de familiares en el proceso [Parámetros de Sueldos](?p=13208).

_Parámetros legales_

Afecta ganancias: si activa este parámetro, el familiar se evaluará en el cálculo de las deducciones familiares en la liquidación del impuesto a las ganancias. La liquidación de ganancias, además, considera las fechas de vigencia de alta y baja del familiar, y la edad máxima para los familiares con parentesco Hijo, indicada en el proceso [Parámetros de Sueldos](?p=13208).

Porcentaje de deducción hijo: permite asignar el porcentaje de deducción para aquellos casos donde el parentesco del familiar sea "hijo" y el mismo este afectado por ganancias.  
El porcentaje aplicado determinará el importe a deducir por hijo en el cálculo del impuesto a las ganancias, este campo deberá evaluarse por cada uno, de forma independiente.

Afecta Libro ley 20744 (Art 52): por cada familiar puede establecer si se incluyen sus datos personales en la generación del Libroley de Sueldos.

Afecta asignaciones: si activa este parámetro, el familiar se considera en el cálculo de cantidades para la liquidación de asignaciones familiares, que se genera desde el proceso [Actualización automática de cantidades de familiares](?p=12988). El cálculo de las cantidades además, considera las fechas de vigencia de alta y baja del familiar, y la edad máxima para los familiares con parentesco 'Hijo', indicada en el proceso [Parámetros de Sueldos](?p=13208).  
Al generar el alta de un nuevo familiar, por defecto el campo estará inactivo.

Adherido obra social: active este parámetro para considerar al familiar como adherente a la obra social del empleado (titular de la obra social), generando la cantidad Adherentes desde el proceso [Actualización automática de cantidades de familiares.](?p=12988)

Trabaja: este campo se activa sólo si el parentesco del familiar es Cónyuge.

Detalle de familiar para ganancias: al realizar la importación de SiRADIG y tener familiares informados, se actualizará la información del detalle con los siguientes datos:

  * **Período desde:** mes/año desde que el familiar está vigente.
  * **Porcentaje de deducción hijo:** porcentaje de deducción informado en SiRADIG para el hijo desde el período informado.
  * **Salud:** normal o incapacitado para el trabajo informado en SiRADIG.
  * **Código SiRADIG:** código de la deducción informado en SiRADIG.
  * **Descripción:** descripción del parentesco para el período desde.
  * **Importado SiRADIG:** S/N según haya sido informado por SiRADIG o cargado manualmente.



##### Contacto

Puede obtener los datos del domicilio a través de la opción Asignar dirección y teléfono del empleado, o bien completar cada campo en forma manual.

##### Simplificación registral

Complete los datos requeridos para generar la información de vínculos familiares del aplicativo Simplificación registral.

##### Contenidos relacionados

  * [Video sobre liquidación de guardería](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/guarderia_sua_vid/)

  * [Videos sobre SiRADIG - Trabajador / Empleador](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/siradigtrabajador_sua_vid/)
