# Fórmulas del Liquidador de IVA

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_iv/definiciones_guia_iva/?p=8384/

## Contenido

# Fórmulas del Liquidador de IVA

Utilice este proceso para crear nuevas fórmulas en el sistema. Las fórmulas representan conceptos que se pueden utilizar durante el ingreso de comprobantes. Por ejemplo importe gravado, IVA, bonificación, etc.

Cada fórmula definida por el usuario (o preconfigurada por el sistema) tiene un significado, por ejemplo alícuota de IVA, total del comprobante, retención, etc., es decir cada importe que compone un comprobante debe estar definido como una fórmula.  
Para más información sobre el impacto de las fórmulas en el resto del sistema, consulte el ítem [Definiciones](?p=8370).  
Los campos que debe ingresar para definir una fórmula son:

Número: representa el código de la fórmula. Si bien este campo no es modificable y será propuesto por el sistema, es de vital importancia para el funcionamiento del sistema. Ya que es el número que se utiliza para hacer referencias entre fórmulas, en caso de que así lo desee.

Nombre: es el nombre conceptual asociado a la fórmula, por ejemplo neto gravado, total del comprobante, etc.

Tipo de fórmula: debido a que el Liquidador de IVA es totalmente parametrizable, debe informar el significado de cada fórmula para que el sistema pueda "interpretar" el concepto que está definiendo.

**Código** | **Significado**  
---|---  
BU | Bien de Uso  
BO | Bonificación  
EP | Exportación  
IM | Importación  
IL | IVA Liberado  
ID | IVA Tasa Dif.  
IG | IVA Tasa Gral.  
EX | Exento  
II | Impuesto Interno  
GR | Neto Gravado  
NG | Neto No Gravado  
PB | Percep. IB  
PI | Percep. IVA  
RI | Retención IVA  
RG | Reten. Ganancias  
RB | Retención IB.  
SD | Sin Definir  
TO | Tot. Comprobante  
  
Régimen: cuando la fórmula definida corresponda a una retención o percepción, debe indicar el régimen correspondiente. Esta información es tenida en cuenta en el proceso [Generación archivo ARCA - SICORE](?p=8346/#generacion-de-archivo-dgi-sicore) y en [Generación Archivo SIAp - SIFERE](?p=8346/#generacion-archivo-siap-sifere).

**Condición** : cuando la fórmula definida corresponda a una retención o percepción, es posible informar la condición correspondiente según el régimen previamente asociado. Esta información es tenida en cuenta en el proceso [Generación archivo ARCA - SICORE](?p=8346/#generacion-de-archivo-dgi-sicore).  
Por defecto el valor de la condición será 0 (cero).

Cód. provincia: si el Tipo de fórmula es 'Percepción IB' o 'Retención IB', se habilitará este campo para asignarle una provincia. Este no es un dato obligatorio.

Fórmulas: realice desde aquí o desde el panel ubicado en la parte inferior, formulaciones de cálculos mediante la utilización de variables.  
Una fórmula puede estar integrada por expresiones matemáticas como ser: operadores aritméticos, relacionales, lógicos, funciones, constantes numéricas y por variables. Para más información consulte la ayuda sobre [variables de reemplazo](?p=8450).

__Nota

Las fórmulas son una expresión matemática que puede contener operadores, constantes, funciones y variables. Los resultado de las fórmulas serán evaluados únicamente en el ingreso de comprobantes y el resultado será almacenado en el comprobante.

__Importante

Cualquier modificación a una fórmula afecta a la carga de comprobantes, por lo tanto, es conveniente que una vez ingresado uno o más comprobantes no se modifiquen las fórmulas. En realidad los cambios realizados a una fórmula afectan al ingreso de nuevos comprobantes. Los comprobantes existentes no serán afectados a menos que se los vuelva a editar.

##### Definición guiada de fórmulas...

Puede optar por ingresar la sintaxis válida de la fórmula (si es un usuario experto) o bien, utilizar el asistente para el armado guiado de la fórmula.  
Utilice el botón "Definición guiada" para invocar al asistente visual que lo ayudará en la definición de la fórmula.  
La fórmula se irá componiendo de la selección efectuada de variables y por medio del botón "Verificar" se podrá evaluar la gramática de la misma.

__Recuerde

Puede hacer referencia a fórmulas ya existentes utilizando la variable T# siendo '#' el número de fórmula.

##### Contenidos relacionados

  * [Videos sobre Liquidador de IVA](https://ayudas.axoft.com/25ar/videos/iva_carp_vid/)
