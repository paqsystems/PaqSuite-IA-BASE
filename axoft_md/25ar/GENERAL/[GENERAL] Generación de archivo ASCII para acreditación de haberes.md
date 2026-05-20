# Generación de archivo ASCII para acreditación de haberes

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Guía
- URL: https://ayudas.axoft.com/25ar/documentos/guias/guias_carp_gla/guia_integrcont_gla/?p=13021/

## Contenido

# Generación de archivo ASCII para acreditación de haberes

Utilice el asistente para generar el archivo ASCII con la información de los totales a acreditar para cada empleado por el pago de sus haberes. Para determinar el formato del archivo asociado al banco en el que se presentará, utilice el proceso [Definición de formato archivo ASCII.](?p=13060)

Tenga en cuenta que sólo intervienen en este proceso los legajos cuya forma de pago sea 'Depósito bancario'. Revise este parámetro en la solapa [Pago](?p=13153/#pago) del proceso [Legajos de Sueldos](?p=13153).  
Dado que se trata de una operación de transferencia bancaria, el asistente requerirá los siguientes datos: Banco, Formato de acreditación o transferencia, Cuenta de origen (la cuenta de la empresa configurada en el proceso Bancos del módulo Procesos Generales), Fecha, Número de acreditación y Período.

Legajos a considerar: indique si desea emitir el archivo para los legajos con cuentas del mismo banco seleccionado, o para cuentas de otros bancos. Por defecto tomara los valores asignados en el alta de la definición del ASCII.

Número de acreditación: es opcional. Utilícelo si informa este dato en el archivo ASCII, de acuerdo al formato requerido por el banco.

Referencia: campo de texto donde es posible informar el tipo de liquidación a presentar según conceptos especificados por el banco.

**Ejemplo:** para algunos bancos predeterminados es requerido informar tipo de liquidación mediante un código.

  * Acreditamiento de haberes.
  * Sueldo anual complementario.
  * Vacaciones.



Selección de liquidaciones: la opción disponible para la selección de liquidaciones se realiza por Período. Ingresando el mes y año a considerar.  
Una vez seleccionado el período, la grilla se completará automáticamente con todas las liquidaciones correspondientes. Luego, podrá actualizar la selección, eliminando de la grilla aquellas liquidaciones que no desee generar.

Todos los [datos fijos de liquidaciones](?p=13052) elegidos para pagar deben tener estado 'Cerrada' o 'Transferida' y activo el parámetro Habilitado para pago.  
Si en el proceso [Parámetros de Sueldos](?p=13208) está activo el parámetro Autoriza acreditación de haberes de la solapa Novedades, se considerarán en la generación los importes verificados mediante el proceso [Autorización acreditación de haberes](?p=13022) cuyo estado de la acreditación sea 'A acreditar'. Una vez generado el archivo ASCII, el estado cambiará a 'Acreditado'.  
Es posible modificar los importes a acreditar que surgen de los totales netos de recibo.  
Si en [Parámetros de Sueldos](?p=13208) está habilitado el parámetro Edita acreditación de haberes, en el proceso [Generación de archivo ASCII para acreditación de haberes](?p=13021) podrá modificar el importe de la acreditación bancaria a generar.

Legajos

Utilice el [Seleccionador de legajos](?p=11882/#definiciones-previas) para conformar el conjunto de empleados cuyas liquidaciones desea procesar.

**Detalle de la acreditación bancaria a generar**  
En esta pestaña podrá visualizar, en una grilla, los legajos incluidos en la acreditación bancaria. Además, podrá consultar si un empleado tiene asociados múltiples CBU.  
Para obtener más información, diríjase a la solapa Pagos del proceso Legajos de sueldos.

Más información:

Esta opción genera una vista detallada de la acreditación correspondiente a los legajos previamente seleccionados.  
En caso de que algún legajo no tenga completos los datos bancarios obligatorios (como número de cuenta o CBU), el sistema mostrará un mensaje de alerta para su corrección si correspondiera antes de continuar con la generación.

##### Contenidos relacionados

  * [Video sobre pago automático de haberes](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/pagoautomhaber_sua_vid/)

  * [Video sobre pago de haberes e integración con Interbanking](https://ayudas.axoft.com/25ar/videos/sua_carp_vid/pagohaber_sua_vid/)
