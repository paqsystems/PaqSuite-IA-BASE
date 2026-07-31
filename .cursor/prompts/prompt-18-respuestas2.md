con respecto a los modulos, pienso que se necesita (complementando lo que ya definiste).

tabla clientes . codigo cliente (idem al que se usará en la url de acceso y clave en EMPRESAS-CONEXION)
tabla proyectos. (tango, pedidosweb, partesatencion, novedadesweb, etc). igual nombre al que se usara en EMPRESAS-CONEXION
tabla modulos : proyecto - modulos : qué modulos existen por proyectos
	ejemplos
	tango - emfaco
	tango - robinet
	tango - comisiones
	tango - cashflow
	pedidosweb - basico
	pedidosweb - full
	duda : en esta tabla iria del nombre del documento de ayuda?
	duda : de acá se limita los registros de pq_parametros_gral?
tabla clientes - proyectos- modulos : acá se define qué contrata cada cliente en cuanto a proyectos y modulos	
tabla modulos - menus : qué opciones de todo el menú se incluyen en cada módulo
	campos : proyecto-modulo (¿id tabla proyecto-modulo?) - id menu de tabla pq_menu
	duda 1 : a partir de aquí se limita la instalación o acceso a las APIs asociadas a las opciones de menú? 
	duda 2 : y los SP asociados a las APIs? 
	duda 3 : de acá se limita la publicación de las APIs en el OPENAPI?
			no tendría inconvenientes que las APIs se instalen , siempre y cuando no se publiquen en el OPENAPI

REGLA : todas las tablas de este tema deben comenzar con un mismo prefijo (ej : PQ_INSTALACION_*)			