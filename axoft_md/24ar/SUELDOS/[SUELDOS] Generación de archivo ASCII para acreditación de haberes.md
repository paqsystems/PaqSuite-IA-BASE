# Generación de archivo ASCII para acreditación de haberes

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Sueldos
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_sua/guia_puestamarcha_sua/?p=13021/

## Contenido

# Generación de archivo ASCII para acreditación de haberes

Utilice el asistente para generar el archivo ASCII con la información de los totales a acreditar para cada empleado por el pago de sus haberes. Para determinar el formato del archivo asociado al banco en el que se presentará, utilice el proceso [Definición de formato archivo ASCII.](?p=13060)

Tenga en cuenta que sólo intervienen en este proceso los legajos cuya forma de pago sea 'Depósito bancario' o 'Cheque'. Revise este parámetro en la solapa [Pago](?p=13153/#pago) del proceso [Legajos de Sueldos](?p=13153).  
El pago automático se implementa sobre una operación de transferencia bancaria, por lo que el asistente solicita los datos de Banco / Cuenta origen (cuenta de la empresa definida en el proceso [Bancos](?p=11836) del módulo Procesos generales), Fecha y Nro. de acreditación y Período.

Legajos a considerar: indique si desea emitir el archivo para los legajos con cuentas del mismo banco seleccionado, o para cuentas de otros bancos. Por defecto tomara los valores asignados en el alta de la definición del ASCII.

Número de acreditación: es opcional. Utilicélo si informa este dato en el archivo ASCII, de acuerdo al formato requerido por el banco.

Referencia: campo de texto donde es posible informar el tipo de liquidación a presentar según conceptos especificados por el banco.

**Ejemplo:** para algunos bancos predeterminados es requerido informar tipo de liquidación mediante un código.

  * Acreditamiento de haberes.
  * Sueldo anual complementario.
  * Vacaciones.



Selección de liquidaciones: las opciones disponibles son por 'Liquidación' o por 'Período'. En este último caso, ingrese el mes y año a considerar.

Liquidaciones que intervienen en la generación de la acreditación: seleccione las liquidaciones cuyos haberes desea acreditar.  
Si la selección de liquidaciones es por 'Liquidación', usted elige en la grilla los datos fijos de liquidación en forma manual.  
Si la selección de liquidaciones es por 'Período', la grilla será completada con todas las liquidaciones del período elegido. Una vez obtenidos los datos fijos en la grilla, actualice la selección, borrando aquellos que no desee generar.

Todos los [datos fijos de liquidaciones](?p=13052) elegidos para pagar deben tener estado 'Cerrada' o 'Transferida' y activo el parámetro Habilitado para pago.  
Si en el proceso [Parámetros de Sueldos](?p=13208) está activo el parámetro Autoriza acreditación de haberes de la solapa Novedades, se considerarán en la generación los importes verificados mediante el proceso [Autorización acreditación de haberes](?p=13022) cuyo estado de la acreditación sea 'A acreditar'. Una vez generado el archivo ASCII, el estado cambiará a 'Acreditado'.  
Es posible modificar los importes a acreditar que surgen de los totales netos de recibo.  
Si en [Parámetros de Sueldos](?p=13208) está habilitado el parámetro Edita acreditación de haberes, en el proceso [Generación de archivo ASCII para acreditación de haberes](?p=13021) podrá modificar el importe de la acreditación bancaria a generar.

Legajos

Utilice el [Seleccionador de legajos](?p=11882/#definiciones-previas) para conformar el conjunto de empleados cuyas liquidaciones desea procesar.

Botón Imprimir

Utilice este botón para listar los pagos que se generan en el archivo ASCII.

##### Contenidos relacionados

  * [Video sobre pago automático de haberes](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/pagoautomhaber_sua_vid/)

  * [Video sobre pago de haberes e integración con Interbanking](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/pagohaber_sua_vid/)
