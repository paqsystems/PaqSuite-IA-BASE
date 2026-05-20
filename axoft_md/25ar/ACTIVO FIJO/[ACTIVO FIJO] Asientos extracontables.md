# Asientos extracontables

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: Activo Fijo
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_afa/guiaintegracion_afa/?p=9756/

## Contenido

# Asientos extracontables

Invoque esta opción para ingresar, modificar, eliminar e imprimir asientos extracontables.

Este tipo de asientos pueden incluirse en los distintos informes del sistema. Son válidas las consideraciones detalladas anteriormente para los [asientos contables](?p=9755).

Moneda extracontable

La [moneda](?p=9806) de ajuste extracontable puede ser la moneda corriente o una moneda extranjera contable, pero nunca una moneda del tipo 'otra moneda'.  
Los importes de los asientos extracontables se guardan sólo en esta moneda.

Para este tipo de asientos, el botón "Monedas del asiento" de la barra de herramientas incluye la opción 'Todas'. Esta opción, que está activa si es que existe un asiento, muestra todos los asientos sin filtrarlos por una moneda en especial.  
En los siguientes ítems, detallamos las funcionalidades propias de estos asientos.

Unidades adicionales en asientos extracontables

Haga clic en el botón para activar o desactivar la exhibición, al pie de la ventana, del panel de [unidades adicionales](?p=9824). Por defecto, este panel está oculto.  
Para las [cuentas contables](?p=9774) que usan unidad adicional, es posible ingresar el importe en el renglón del asiento o bien, indicar la cantidad o importe en el panel de unidades adicionales para que el sistema calcule el importe del renglón.  
Si usted ingresa el importe en el renglón del asiento y está activo el panel de unidades adicionales, pueden presentarse las siguientes situaciones:

  1. La cuenta contable no tiene activo el parámetro Usa unidad adicional. En este caso, el panel de unidades adicionales se muestra deshabilitado.
  2. La cuenta contable usa unidad adicional de tipo 'Monetaria'. En el panel se exhibe el código. En una primera solapa, el sistema exhibe la descripción, el tipo de cotización y la cotización para la fecha del asiento de la [moneda](?p=9806) de la [unidad adicional](?p=9824) y calcula el importe del renglón expresado en esa moneda. Es posible cambiar el importe reexpresado. En tanto que el tipo de cotización y/o la cotización sólo son factibles de modificación si en la opción [Monedas](?p=9806) está activo el parámetro Edita tipo de cotización y/o Edita cotización. Tenga en cuenta que, si la moneda de la unidad adicional es distinta a la moneda extracontable (y no es la moneda corriente), se exhibe en una segunda solapa, la información de la conversión de la moneda extracontable a la moneda corriente. En el caso de igualdad de monedas, se considera una cotización igual a l y no se exhiben las solapas.
  3. La cuenta contable usa unidad adicional de tipo 'No monetaria'. En este caso, el panel de unidades adicionales exhibe en su sector izquierdo, el código, la descripción, el tipo de valorización, la valorización correspondiente a la fecha del asiento y la moneda del [tipo de valorización](?p=9821) de la [unidad adicional](?p=9824) y se calcula la cantidad de unidades. El tipo de valorización y/o la valorización sólo son factibles de cambio si en la opción [Unidades adicionales](?p=9824) está activo el parámetro Edita tipo de valorización y/o Edita valorización. En el sector derecho del panel, se exhibe el tipo de cotización y la cotización de la [moneda](?p=9806) asociada al [tipo de valorización](?p=9821) de la [unidad adicional](?p=9824) y el importe del renglón expresado en esa moneda. Usted puede modificar el importe calculado en este sector. El tipo de cotización y/o la cotización no se exhiben si la moneda es de tipo 'Corriente'; caso contrario, estos datos son editables sólo si en la opción [Monedas](?p=9806) está activo el parámetro Edita tipo de cotización y/o Edita cotización. Tenga en cuenta que si la [moneda](?p=9806) asociada al [tipo de valorización](?p=9821) de la unidad adicional es la moneda corriente, se exhibe una única solapa con la información de la conversión de la moneda extracontable a la moneda corriente. En cambio, si la [moneda](?p=9806) asociada al [tipo de valorización](?p=9821) de la unidad adicional es distinta a la moneda extracontable, se exhibe en una segunda solapa, la información de la conversión de la moneda extracontable a la moneda corriente.



Para más información acerca de tipos de cotización y cotizaciones, consulte la ayuda del módulo Procesos generales.
