# API

## Metadata

- Producto: Tango
- Version: 25AR
- Modulo: General
- Categoria: Operación
- URL: https://ayudas.axoft.com/25ar/documentos/operacion/apertura_oper/api_oper/

## Contenido

# API

Una de las características importantes que notarás en el sistema es que todo proceso ofrece el concepto de apertura, esto significa que vas a poder actualizar la información del sistema a través de una interfaz estándar que hemos definido.

Esta interfaz, conocida comúnmente por sus siglas en inglés API (Application Programming Interface), ofrece un conjunto de funciones en las que ofrecemos funcionalidad de cada uno de los procesos del sistema.  
Si leíste el párrafo anterior y no te entendés de qué estamos hablando, probablemente no tengas un perfil técnico, pero no te preocupes, en el siguiente párrafo te lo explicaremos de una forma más coloquial para que entiendas el uso que le podrías dar en tu empresa, comercio o estudio contable.  
Cada uno de los procesos de la nueva plataforma cuenta con una API. La API es una interface que permite que interactúen dos aplicaciones entre sí para lograr un intercambio de datos entre ellas. Si necesitás hacer un desarrollo externo a Tango informale a tu programador o asesor técnico que ahora contamos con APIs. No sólo será más fácil su trabajo, sino que a través de ellas podemos garantizar que se apliquen las mismas validaciones que utilizamos nosotros cuando vos trabajás con el sistema. De esta forma podemos asegurar que la información ingresada al sistema sea consistente.  
Todas las API de Tango están autodocumentadas y están detalladas en cada uno de los procesos.  
Para conocer más sobre API mirá este video.

##### Características principales del API REST

Las operaciones que podés hacer son:

  * **GET** para consultar y leer.
  * **POST** para crear.
  * **PUT** para editar.
  * **DELETE** para eliminar.



Lo más importante a tener en cuenta al crear nuestro servicio o API REST no es el lenguaje en el que lo programes, sino que las respuestas a las peticiones se hagan en JSON, ya que es el lenguaje de intercambio de información más usado en la actualidad.  
Si sos programador, podes interactuar con el API REST de Tango utilizando cualquier lenguaje de programación. Ejemplo: C#, JAVA, PHP, Swift, Kotlin, etc.

##### Obtener "Token de desarrollador"

Para utilizar el API del sistema, debes obtener primero una identificación de usuario, a la que llamamos TOKEN.  
Ese TOKEN lo debés enviar en el encabezado (header) de cada transacción para garantizar la seguridad de la operación.  
Para obtener el TOKEN, ingresá al Menú web del sistema > Menú de usuario y seleccioná la opción Desarrollador; luego de ingresar pulsá sobre el botón "Generar" y obtendrás el TOKEN que debé utilizar en el header para identificar tus transacciones.

##### Identificando la empresa

**Tango** es un sistema multiempresa, cuando utilizás el API REST, es necesario que identifiques la empresa sobre la que querés realizar la transacción. Esa identificación es un número que podés obtener en dos lugares:

  * **Obervando la URL del sistema:** ingresá al menú del sistema y buscá en la dirección de internet de tu navegador el número que figura a continuación del texto "company/". Por ejemplo, en la url "https://MiTango.axoft.com/company/117/menu/10023" la identificación de tu empresa corresponde al número 117.
  * **Consultando la base de datos "Diccionario":** realizá una consulta a tabla "Empresa" y tomá el valor del campo ID_Empresa para la empresa con la que querés operar.



##### Header

El "Header" es una propiedad del API REST y acompaña a cada método que expone el sistema como un conjunto de clave valor. En esta propiedad identificamos el tipo de transporte que es JSON, el token de acceso y la identificación de empresa.
    
    
    "Accept", "application/json";
    "ApiAuthorization", “8c45ec224ab849a3ac3519414d5f476f”
    "Company", 1

##### Métodos disponibles en API

Cada proceso cuenta con métodos para poder consumir del servicio API REST.  
Estos métodos se encuentran autodocumentados y podés acceder a ellos ingresando a la opción Apertura > API dentro de la barra de herramientas de cado proceso.  
Dentro de esa opción vas a encontrar información de cada método, información del modelo de transporte, un ejemplo en C# y otro en TypeScript a fin de que puedas copiar y pegar el código a tu programa.  
También, podés probar el API desde esta misma sección; por ejemplo, si te posicionás en "Consulta", completás los parámetros y presionás el botón "Ejecutar" vas a obtener los registros correspondientes al proceso en esa empresa en formato JSON.

__Nota

La respuesta del método "Consulta" (Get) o "Avanzada" (GetByFilter) no permite hacer una posterior modificación o alta de un registro. Para ello, puede usar el método "Registro" (GetById), modificar el JSON de respuesta y luego ejecutar el método "Modificación" o "Alta" correspondiente.  


Cuando ejecutes los métodos de ALTA, MODIFICACION o ELIMINACION es importante que siempre revises la respuesta que devuelve el proceso ya que puede ocurrir que la operación no se pueda realizar debido a alguna validación o falla en el armado del JSON.

__Nota

En el método 'Consulta', en un proceso de tipo ABM, obtenemos las columnas y filtros de la Vista por defecto con que fue desarrollado el proceso. Si queremos obtener otras columnas o aplicar un filtro nuevo, se debe crear una [Vista nueva](?p=39165) y el nombre de la vista se debe pasar en el parámetro VIEW.

##### Método Consulta de procesos Live

En los procesos de tipo Consulta Live, contamos con apertura en cada uno de los procesos. El método 'Consulta' devuelve la consulta Live ejecutándose con los parámetros por defecto.

Se pueden modificar los filtros de fecha en los parámetros fromDate y toDate.  
Toda la información de la consulta se devuelve paginada. El desarrollador puede modificar el tamaño de la página en el parámetro pageSize y obtener una página específica utilizando el parámetro pageIndex.  
En el Json que retorna con los datos especificados, siempre se devuelve información con respecto a la cantidad de registros y cantidad de páginas para que el desarrollador lo tenga en cuenta en su lógica de consulta.

**¿Cuáles son las condiciones comerciales para el uso de las API del sistema?**  
Tenga en cuenta que el uso de las API, en general, requiere que su sistema se encuentre dentro del período de actualizaciones (abono anual) y que esté utilizando alguna de las dos últimas versiones vigentes del sistema. Adicionalmente, es necesario que su sistema se encuentre dentro de las categorías Plus, XPlus o Gold y en particular las API correspondientes a transacciones, como es el caso de pedidos, facturas, etc., tienen un costo adicional en función del módulo al que pertenecen.  
Para conocer aquellas API que ya tiene disponibles consulte la solapa API (Apertura) en el proceso [Datos de licencia](?p=34562) del módulo Administrador general. Para adquirir API para su sistema consulte con su ejecutivo de cuenta o su distribuidor oficial.

##### PDFs via API

El sistema permite generar y descargar un documento en formato PDF con la información correspondiente al proceso ejecutado. Esta capacidad se aplica a procesos [Ficha Live y Consultas Live](?p=9196). Para tal fin, ambos procesos cuentan con la acción Descargar PDF.

A continuación, se detallan los nombres de los procesos para su adecuada configuración y puesta en marcha. También se especifican los respectivos indicadores (ID), estos indicadores son necesarios para la correcta parametrización e implementación dentro del sistema.

**Ficha Live:**

  * Ficha Live de órdenes de compra:  
ID_CPA35
  * Ficha Live de órdenes de pago:  
ID_CPA04
  * Ficha Live de cotizaciones:  
ID_GVA08
  * Ficha Live de remitos:  
ID_STA14
  * Ficha Live de recibos:  
ID_GVA12
  * Ficha Live de facturas, créditos y débitos:  
ID_GVA12



**Consultas Live:**

  * Resumen de cierres de caja:  
ID_SBA28
  * Reportes fiscales (Ventas):  
ID_REPORTE_FISCAL
  * Reportes fiscales (Central):  
ID_CTA_REPORTE_FISCAL
  * Cierre de caja:  
ID_CTA_RESUMEN_CIERRE_CAJA



##### Contenidos relacionados

  * [Apertura de comprobantes](https://ayudas.axoft.com/25ar/ayudas/gv/procesofacturacion_gv/pos_gv/masacciones_posgv/apertutcomprob_posgv/)

  * [Lista de tablas del sistema](https://ayudas.axoft.com/25ar/documentos/operacion/tablas_oper/)

  * [Video sobre administración de stock](https://ayudas.axoft.com/25ar/videos/gral_carp_vid/adminstock_gral_vid/)

  * [Videos sobre Tango Colectora](https://ayudas.axoft.com/25ar/videos/st_carp_vid/colectora_st_vid/)
