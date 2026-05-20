# Actualización de ajustes afectados al mejor sueldo

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_sua/guia_puestamarcha_sua/?p=13003/

## Contenido

# Actualización de ajustes afectados al mejor sueldo

Permite registrar una ocurrencia de ajuste de liquidación, para un legajo en una determinada fecha.

Modalidad de ingreso: seleccione una de las siguientes modalidades de ingreso: 'Por fecha', 'Por ajuste', 'Por legajo' o 'Por archivo externo'.  
De acuerdo a la modalidad seleccionada, se habilitarán diferentes parámetros a completar.

Obtener ajustes: al presionar este botón y de acuerdo a los parámetros definidos, el sistema mostrará los ajustes previamente cargados y habilitará el alta, baja y/o modificación de ajustes.

Detalle de ajustes: complete las siguientes columnas dependiendo de la modalidad de ingreso seleccionada.

  * Fecha: indique la fecha del ajuste.
  * Legajo: seleccione el legajo al que se le aplicara el ajuste.
  * Ajuste: seleccione el código de ajuste previamente definido.
  * Cantidad: indique la cantidad del ajuste.
  * Valor: indique valor del ajuste.
  * Período afectado: período al cual se imputará el importe liquidado para el cálculo del mejor sueldo.
  * Estado: si el ajuste se encuentra "Liquidado" y desea que sea tenido en cuenta en las liquidaciones nuevamente modifique el estado del mismo seleccionando con botón derecho del mouse la opción "Cambiar estado a liquidar". En cambio, si el ajuste no debe ser considerado en la liquidación de conceptos modifique el estado del mismo seleccionando "Cambiar estado a liquidado".



Aclaraciones:

El importe liquidado se obtiene de la liquidación del concepto al cual se encuentra asociado el ajuste y su parametrización. Para más información acerca de los códigos y la parametrización de ajustes, consulte el ítem [Ajustes afectados al mejor sueldo](?p=13011).  
Para más información sobre el cálculo del importe liquidado consulte el ítem [Cálculo de ajustes afectados al mejor sueldo](?p=13163/#ejemplo).

__Nota

Tenga en cuenta que en la liquidación se considerarán los ajustes cuyo período afectado no supere los 365 días (12 meses) hacia atrás desde el período de liquidación activo. Los ajustes anteriores a este límite no serán tenidos en cuenta.

##### Por archivo externo

Genera ajustes afectados al mejor sueldo, a partir de novedades generadas con Excel, sobre la base de un archivo de integración que cumpla con la definición de estructura e integración de registro.  
Para realizar la importación de datos, presione el botón "Seleccionar archivo" y proceda a seleccionar el archivo Excel. Una vez procesado el archivo, los datos se mostrarán en la grilla donde podrá dar de alta, modificar o dar de baja los ajustes. Para concluir el proceso debe presionar "Aceptar" o <F + 10>.  
Cuando realice importaciones de novedades desde Excel, tenga en cuenta que el archivo debe respetar el orden de las columnas y además incluir el título de cada una de ellas

Especificaciones de estructura:

En la siguiente tabla se detalla la estructura de registro y las longitudes de cada campo:

**Columna** | **Longitud** | **Tipo de dato**  
---|---|---  
Fecha | 10 | Fecha (máscara: dd/mm/aaaa)  
Legajo | 9 | Numérico  
Ajuste | 10 | Carácter  
Cantidad | 10 | Importe  
Valor | 10 | Importe  
Período Afectado | 10 | Fecha (máscara: dd/mm/aaaa)  
Estado | 10 | Carácter  
  
Especificaciones de integridad:

**Campo** | **Validación de dato**  
---|---  
Fecha | La fecha no puede estar vacía y debe estar dentro de los tramos laborales del legajo.  
Legajo | El número de legajo no puede estar vacío, debe existir y estar habilitado para sueldos.  
Ajuste | El código de ajuste no puede estar vacío y debe existir como Ajuste.  
Cantidad | La cantidad debe ser igual o mayor a "0".  
Valor | El valor debe ser igual o mayor a "0".  
Período afectado | La fecha no puede estar vacía.  
Estado | Los valores posibles son 'A liquidar' o 'Liquidado'.  
  
Separador decimal: parametrice el separador decimal a considerar como válido. Para ello, ingrese al proceso [Parámetros de Sueldos](?p=13208), en la solapa Novedades, e indique en el parámetro Símbolo para separador de decimales si utiliza "punto" o "coma" como separador decimal.

Desde esta planilla Excel usted accederá a un modelo para comenzar a trabajar.

[ PlantillaAjustesMejorSueldo.xlsx](https://ayudas.axoft.com/download/PlantillaAjustesMejorSueldo.xlsx)

__Nota

La importación desde archivo **Excel** esta disponible sólo para licencias _Plus_ o _Gold_.

##### Contenidos relacionados

  * [Video de novedades y licencias](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/novedlicencia_sua_vid/)

  * [Videos sobre conceptos y fórmulas de sueldos](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/conceptos_sua_vid/)

  * [Videos sobre libros de sueldos digital](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/librosueldig_sua_vid/)

  * [Videos sobre registración de novedades](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/novedades_sua_vid/)
