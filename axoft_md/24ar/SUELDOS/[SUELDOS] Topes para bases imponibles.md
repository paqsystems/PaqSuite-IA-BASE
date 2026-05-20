# Topes para bases imponibles

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sua/guia_librodigital_sua/?p=13071/

## Contenido

# Topes para bases imponibles

Configure en esta solapa los topes de aportes y contribuciones, de utilidad para el armado de fórmulas de liquidación; para la generación de remuneraciones imponibles para el Sicoss, Libro de Sueldos Digital y la certificación de servicios y remuneraciones.

Al cargar un nuevo registro de topes para bases imponibles y marcarlo como "Activo", está definiendo los valores a tomar en las variables de liquidación ya que este proceso reemplaza a los campos que se encontraban en la solapa Legales de Parámetros de sueldos.  
Al grabar un nuevo registro, se actualizan las bases imponibles para ganancias, dato necesario para calcular los topes de las retenciones de los conceptos que podían tener una parte exenta en el impuesto a las ganancias, por ejemplo, el SAC.

Defina con una nueva fecha de vigencia el importe de topes publicado por AFIP para Remuneraciones Imponibles 1, 4 y 5.  
El sistema, automáticamente toma dichos importes / 30 (días del mes) para hacer el cálculo en los topes días de SAC y vacaciones. Asimismo, los campos autocompletados pueden ser editados por usted.  
Recuerde marcar como "Activo" el que desea utilizar para la liquidación.  
Variables disponibles para fórmulas de conceptos de liquidación: MOMAX1, MOMAX2, MOMAX3 y MOMAX4.

__Nota

Al definir un registro como activo, el sistema establece automáticamente en "No" al resto.  
Siempre debe existir al menos un registro cargado. Si hay más de uno y desea eliminar el que actualmente esté marcado como activo, el sistema marca automáticamente como activo a la fecha de vigencia anterior. Si no hubiera una anterior, marca el siguiente.

__Importante

Tenga en cuenta que, para trabajar con apertura en Excel, el campo "Activo" debe contener las opciones "Sí" o "No". Si se importa un archivo de Excel que contiene más de un registro marcado como "Activo", la última vigencia importada quedará marcada como activa y el resto no.  


Vigencia desde: período en el que se publican los nuevos topes de bases imponibles.

Activo: marque este check para determinar que valores se tomaran en las liquidaciones de Libro de Sueldos Digital y SICOSS.

Topes de Seguridad Social

(SS)Mínimo liquidaciones normales: indique el tope mínimo para los importes de ‘Tipo 1 – Haber’ y/o ‘4 – No remunerativo’, incluidos en liquidaciones remunerativas normales. Debe ingresar el importe total informado por AFIP.

(SS)Mínimo liquidaciones de aguinaldo: este campo se completa en forma automática al informar el importe mínimo de liquidaciones normales de seguridad social.  
El importe asignado corresponde por defecto a la mitad de dicho importe mínimo el cual puede ser editado por otro valor requerido.

Máximo Importe a detraer: ingrese el importe máximo posible de detraer para liquidaciones normales.  
Será tomado en cuenta solo cuando el campo máximo importe a detraer asignado en el convenio asociado a los legajos sea igual a cero.

Topes de obra social

(OS)Mínimo liquidaciones normales: indique el tope mínimo para los importes de ‘Tipo 1 – Haber’ y/o ‘4 – No remunerativo’, incluidos en liquidaciones remunerativas normales.

(OS)Mínimo liquidaciones de aguinaldo: este campo se calcula en forma automática a partir del importe mínimo de liquidaciones normales de obra social.  
El importe asignado corresponde por defecto a la mitad de dicho importe mínimo el cual puede ser editado por otro valor requerido.

Tope diario

SAC proporcional: el sistema autocompleta este campo tomando la mitad del valor mínimo de liquidaciones normales de seguridad social dividiendo por 30 , obteniendo así el tope diario para SAC (de utilidad para el armado de fórmulas de liquidación). Es posible ingresar el valor de manera manual de acuerdo al criterio del usuario. Variable disponible para fórmulas de conceptos de liquidación: MINDA.

Adelanto vacaciones y remanente: tomando el importe mínimo de liquidaciones normales de seguridad social el sistema autocompleta este campo tomando el importe ingresado en dicho campo y aplicando el divisor 30, obteniendo así el tope diario de vacaciones (de utilidad para el armado de fórmulas de liquidación). Es posible ingresar el valor de manera manual de acuerdo al criterio del usuario.  
Variable disponible para fórmulas de conceptos de liquidación: MINDV.

Tope máximo

Multiplicador: puede utilizarlo en el armado de fórmulas de liquidación, para calcular los topes máximos a partir de los topes mínimos especificados.
