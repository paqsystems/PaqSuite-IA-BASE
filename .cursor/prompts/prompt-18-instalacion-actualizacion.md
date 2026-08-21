te comento cómo tengo pensada la instalación de un cliente nuevo.

recordemos primero que vamos a tener deploys de plataforma por producto:
- frontend producción: https://{proyecto}paqsystems.vercel.app/
- frontend desarrollo: https://{proyecto}paqsystems-dev.vercel.app/
- backend producción: https://backend{proyecto}paqsystems.on-forge.com/
- backend desarrollo: https://backenddev{proyecto}paqsystems.on-forge.com/
(SoT: docs/_base/00-urls-deploy-proyecto.md; persistir en docs/06-operacion/urls-deploy.md al scaffoldear)

un cliente va invocar una url de la forma {cliente}.{proyecto}.paqsystems.com (sin cambio)
este redirige al frontend Vercel de producción indicando el {cliente}
se hace login al backend Forge llevando el {cliente} como parámetro de alguna forma.
con {cliente} y {proyecto} se accede a paqsystems.empresas_conexion para obtener:
a) base sql y credenciales.
b) base de datos del diccionario y base de datos de la empresa inicial (en caso de sistemas mono, ambas bases coinciden)
c) Si el acceso es a través de gateway-agente (ver proyecto Paqsuite-IA-AgentesClientes)

entonces, en una instalacion nueva : 
a) en la base diccionario genera todas las tablas PQ (pq_menus, de seguridad, de excel, pivots, grillas, informes, grupos empresarios, tareas programadas, etc)
b) un rol "Supervisor" de acceso total.
c) Un usuario "admin" con contraseña "Paqsystems"
d) un usuario "PQ" con contraseña "PaqSystems26*"
e) una empresa en pq_empresa, con el mismo nombre de la empresa que figura en Empresas_Conexion (que ya debe existir previamente)
f) dos registros en pq_permisos, para asignar a esos dos usuarios el rol Supervisor en la empresa definida.
g) De todos los proyectos contratados por el cliente :
    1) todos los Stored Procedures en la tabla empresa definida y diccionario
	2) los registros de PQ_MENU 
	3) los registros de PQ_PARAMETROS_GRAL 
	4) los registros de las tablas de trabajo (excels, pivots, grillas, informes, etc)
	5) todas las tablas PQ necesarias en la tabla empresa definida.

en una actualización, ya sea por nuevos módulos, upgrade del proyecto, etc:
a) En la base diccionario
	1) Actualizaciones de tablas PQ
	2) Actualizaaciones de store Procedures
	3) Actualización del menú
	4) actualizaciones de tablas de componentes : excels, pivots, grillas, informes, etc. etc.
b) en cada una de las bases que se encuentren en pq_empresa (1 sola en mono) :
	1) Actualizaciones de tablas PQ
	2) Actualizaciones de stored Procedures
	3) Actualizaciones de pq_parametros_gral (insert o update de caption y tooltip, NO de valor_*)

con respecto a agentes-gateways.
la idea es que existan proyectos (en principio el de Tango), cuyas bases se encontraran en los propios servidores de los clientes. por ende, vamos a implementar la solución agentes-gateway arriba mencionado.
como buena práctica me sugeriste trabajar con SP para que no circulen comandos sql por la red. 
por lo tanto, haría como regla general para la resolución de todas las API, que siempre se trabaje con SP, aunque no se opere esta tecnología.
sólo habrá que contemplar (acá en el framework y en todos los proyectos) para determinar que cuando en EMPRESAS_CONEXION figure que trabaja con agente-gateway, debe utilizar esta herramienta y no al SQL directamente.

creo que no me olvido de ningún otro objeto, consultarme cualquier cosa.

las definiciones de módulos por cliente no sé si lo trasladaría a producción. creo que debería conservarse en las bases de desarrollo, y de allí generar todos los scripts y seeders necesarios.
ya que sino estarían expuestas a que terceros agreguen gratuitamente módulos a un cliente.

Diseño actual de la tabla EMPRESAS_CONEXION : 

CREATE TABLE [dbo].[empresas_conexion](
	[id] [bigint] IDENTITY(1,1) NOT NULL,
	[proyecto] [nvarchar](100) NOT NULL,
	[cliente] [nvarchar](100) NOT NULL,
	[nombre] [nvarchar](200) NOT NULL,
	[host] [nvarchar](255) NOT NULL,
	[port] [int] NOT NULL,
	[database_name] [nvarchar](100) NOT NULL,
	[username] [nvarchar](100) NOT NULL,
	[password] [nvarchar](max) NOT NULL,
	[activo] [bit] NOT NULL,
	[created_at] [datetime2](3) NULL,
	[updated_at] [datetime2](3) NULL,
	[dictionary_database] [nvarchar](100) NULL,
	[agent_id] [nvarchar](100) NULL,
	[client_id] [nvarchar](100) NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

ALTER TABLE [dbo].[empresas_conexion] ADD  DEFAULT ('1433') FOR [port]
GO

ALTER TABLE [dbo].[empresas_conexion] ADD  DEFAULT ('1') FOR [activo]
GO
