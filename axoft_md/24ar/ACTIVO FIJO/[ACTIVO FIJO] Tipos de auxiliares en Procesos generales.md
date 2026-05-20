# Tipos de auxiliares en Procesos generales

## Metadata

- Producto: Tango
- Version: 24AR
- Modulo: Activo Fijo
- Categoria: Guía
- URL: https://ayudas.axoft.com/24ar/documentos/guias/guias_carp_afa/guiaintegracion_afa/?p=11835/

## Contenido

# Tipos de auxiliares en Procesos generales

Utilice esta opción para definir los auxiliares y subauxiliares (o tipos de subcuentas) de cada tipo de auxiliar (centros de costo, proyecto, división, legajo, cliente, proveedor, etc.).

Para definir un tipo de auxiliar, asígnele un código y de manera opcional, una descripción. El sistema valida que el código sea único.

##### Principal

Origen: indique el origen del tipo de auxiliar que está dando de alta. El origen puede ser manual o automático. Si es automático, debe indicar el tipo de auxiliar automático, el cual puede ser: 'Proveedor', 'Artículo', 'Cliente' o 'Legajo'.

Apertura en subauxiliares: tilde este parámetro para habilitar la apertura de los auxiliares en subauxiliares.

Grilla de auxiliares: defina los auxiliares asociados al tipo de auxiliar.  
Para cada auxiliar indique su código y si está habilitado. Al inhabilitar un auxiliar, es posible indicar el período de inhabilitación.  
El sistema valida que ingrese al menos un auxiliar en esta grilla.

Grilla de subauxiliares: esta grilla está disponible sólo si usted habilitó la apertura en subauxiliares. En ese caso, defina cada uno de los subauxiliares correspondientes a los auxiliares ingresados.  
El sistema valida, por cada auxiliar cargado, que ingrese al menos un subauxiliar en esta grilla.  
La definición de subauxiliares tiene las mismas características que la de los auxiliares.

__Nota

Es posible activar la marca de Apertura en subauxiliares aunque el tipo de auxiliar tenga asientos asociados en los módulos. El proceso actualizará los movimientos generados en los módulos, apropiando los subauxiliares al subauxiliar 'Sin Asignar'. Es importante aclarar que no es posible realizar el camino inverso.

##### Contenidos relacionados

  * [Video sobre imputación contable Sueldos](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/imputcontsueldos_gral_vid/)

  * [Videos sobre asientos contables en Sueldos](https://ayudas.axoft.com/24ar/videos/sua_carp_vid/asientocontabl_sua_vid/)

  * [Videos sobre auxiliares contables y contabilidad por proyectos](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/conproyectos_cna_vid/)

  * [Videos sobre parametrización contable](https://ayudas.axoft.com/24ar/videos/gral_carp_vid/paramcontab_gral_vid/)
