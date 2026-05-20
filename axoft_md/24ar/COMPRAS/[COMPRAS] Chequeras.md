# Chequeras

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Compras
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_cp/guia_cuentacorriente_cp/?p=10144/

## Contenido

# Chequeras

Este proceso permite definir las chequeras utilizadas para cada cuenta corriente bancaria y la numeración de cheques habilitados de cada una de ellas.

Usted puede ingresar nuevas chequeras, actualizar numeraciones o eliminar chequeras.

Tenga en cuenta:

  * Cada cuenta puede tener asociadas varias chequeras.
  * El número de cheque es de 11 dígitos, no obstante, no es obligatorio el ingreso de números completos. Utilice la cantidad de dígitos que considere necesario, tenga en cuenta que un número de cheque de una misma chequera no puede repetirse.
  * El uso de varias chequeras para una cuenta bancaria se justifica cuando usted se maneja físicamente con más de una chequera en forma simultánea; o bien, cuando se corre el riesgo de duplicar números de cheque (la identificación de un cheque se basa en el número de chequera más el número de cheque). En general, puede darse una duplicación por no utilizar números completos, ya que las terminaciones de los números de cheque se repiten con frecuencia.



Desde el campo Cuentas acceda al buscador pulsando la tecla <F7> o haciendo click en el botón "...".  
Utilice esta modalidad de búsqueda cuando necesite aplicar un criterio de selección determinado, por ejemplo: por código de banco, por cuenta asociada, etc.

__Nota

Tenga en cuenta que se selecciona un cheque a la vez.

Es posible cambiar el criterio de búsqueda por cada cheque.  
Los campos a definir son:

Cuenta: ingrese el código de cuenta correspondiente a la cuenta corriente bancaria o bien a una cuenta de cheques diferidos. Acceda al buscador de cuentas pulsando la tecla <F7> o haciendo clic en el botón "...".  
Ingresado el código, si ya existen chequeras definidas para la cuenta, se las visualizarán en pantalla.  
Los datos asociados a una chequera son:

  * **Número de Chequera:** es el número que identifica la chequera. Para una misma cuenta, este número no puede repetirse.  
Si desea eliminar una chequera, pulse la tecla <Supr> (o <Del>). El sistema valida que no esté utilizada por los cheques que se encuentran emitidos, salvo que esos cheques hayan sido pasados a archivo histórico.
  * **Primer número habilitado y Último número habilitado:** indique el primer y último número habilitado para la chequera.
  * **Próximo número habilitado:** este número es el que se tomará por defecto al emitir un nuevo cheque.
  * **Permite modificar número de cheque:** admite la modificación del número de cheque en Modificación de cheques propios, siempre que el cheque esté en estado 'Emitido' o 'Diferido' y no haya sido conciliado.



Número de CUIT: indica el número de CUIT del firmante asociado a la chequera.

Formulario asociado: asigne el formulario asociado a la chequera con la tecla <F7> \- Búsqueda rápida. Este formulario es el que se propondrá en el proceso [Impresión de cheques](?p=10330).

Aclaración sobre cheques comunes y cheques diferidos  
Los cheques comunes se emiten invocando directamente una cuenta corriente bancaria. Los cheques diferidos, invocando una cuenta bancaria de cheques diferidos.  
Los cheques emitidos por una cuenta de tipo 'Cheques Diferidos' son valores que se asocian en forma automática a una cuenta corriente bancaria (cuenta asociada).  
Por ello, es conveniente que las chequeras de una cuenta corriente y las de su cuenta asociada para cheques diferidos no superpongan sus números, ya que el sistema no permitirá generar dos cheques (cualquiera sea su tipo) con igual número de chequera y cheque. Si al emitir un cheque se diera esta situación, el sistema dará aviso de la duplicidad y requerirá el cambio de número.  
Si por algún motivo, los números de cheque de una misma cuenta fueran iguales, recomendamos utilizar distintos números de chequeras para cheques diferidos y cheques comunes.
