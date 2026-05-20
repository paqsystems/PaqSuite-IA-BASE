# Imputación contable

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Ventas
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gv/guia_integrcont_gv/?p=19790/

## Contenido

# Imputación contable

Los datos del asiento se exhiben en formato grilla, podrán existir más o menos líneas de acuerdo a la definición del modelo de asiento y de los artículos o conceptos ingresados en el comprobante.

Al pie de la grilla, se exhibe la suma de los importes en la columna "Debe", la suma de los importes en la columna "Haber" y la diferencia entre ambas.  
Cada renglón se compone de los siguientes datos:

Número: es el número de renglón del asiento. Este dato no es editable.

Código de cuenta: ingrese o seleccione el código de [cuenta contable](?p=11850). Este dato es de ingreso obligatorio. En caso de poder editar la cuenta o de agregar más renglones, puede seleccionar una cuenta contable habilitada para el módulo en el que se encuentra.

Descripción de cuenta: este dato se completa automáticamente al completar la columna "Código de cuenta".

Debe / Haber: por defecto el importe se completará automáticamente de acuerdo al comprobante. Usted puede editar el importe. El sistema realiza los siguientes controles: el asiento debe tener dos líneas como mínimo, el asiento debe balancear, no se permite ingresar importes negativos, ni dejar renglones con importe en cero, los importes del asiento deben coincidir con los valores ingresados en el comprobante.  
El ingreso de este dato es obligatorio.  
Si ingresa el importe en la columna "Debe", se deshabilita la edición de la columna "Haber" y viceversa.  
Haga clic en el botón "..." para abrir la calculadora.

Auxiliares: el valor de este campo depende de la definición del parámetro Usa auxiliares contables en la [cuenta contable](?p=11850) y de los tipos de auxiliares asociados a la cuenta contable desde el proceso [Actualización individual de auxiliares contables](?p=11827).  
Para ingresar o consultar las imputaciones a auxiliares y subauxiliares contables de la [cuenta contable](?p=11850) en la que está posicionado, ubique el cursor sobre esta columna y haga clic o presione la tecla <Enter>. Las imputaciones pueden ser manuales o bien, basadas en reglas de apropiación automáticas asociadas a la cuenta - tipo de auxiliar.  
Es posible ingresar el porcentaje y que se calcule en forma automática el importe, o viceversa. Si la imputación a auxiliares contables queda pendiente por el total del importe de la línea o renglón del asiento, el porcentaje será igual a 100% para el auxiliar 'Sin Asignar'.  
Usted puede seleccionar una regla de apropiación, puede elegir una regla que esté habilitada para el módulo en el cual se encuentra.  
Usted puede definir una regla por defecto y si el tipo de auxiliar es del tipo 'Manual' y no usa apertura en Subauxiliares, puede asociar un grupo de auxiliares para relación cuenta - tipo auxiliar. Esto permite habilitar sólo algunos auxiliares de todos los auxiliares creados para el tipo de auxiliar y actúa como un filtro.  
Es prioritario aplicar la regla de apropiación por defecto (ya sea del módulo o definida en Procesos generales sobre un grupo de auxiliares asociado) en el asiento. Una vez aplicada la regla, presione el botón "Ver todos los auxiliares" para reemplazar los auxiliares de la regla defecto, por los auxiliares del grupo asociado. Esto significa que el asiento:

  * O es excluyente.
  * O aplica la regla.
  * O apropia uno o más de los auxiliares del grupo de auxiliares asociados.



Si no posee un grupo de auxiliares asociados, cuando presione el botón "Ver todos los auxiliares" se agregarán todos los auxiliares sin aplicar ningún filtro o grupo.  
Para más información consulte el ítem [Actualización individual de auxiliares contables](?p=11827).

Leyenda: el sistema exhibe la leyenda definida en el modelo de asiento, será posible modificarla.

Diferencia: corresponde al total del debe menos el total del haber. No es posible grabar un asiento con diferencia distinta a cero.

Asignar diferencia <F9>: permite asignar al renglón actual la diferencia entre el total del debe y del haber.
