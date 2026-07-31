# Dudas que siguen / nuevas (para cerrar)

## A — DDL / conexión

1. ¿Agregamos fecha_vencimiento (norma producto A6) o queda solo activo por ahora?
2. ¿Constraint UNIQUE (proyecto,cliente)? El DDL actual no lo tiene y el lookup lo necesita.
3. ¿Nombre canónico Framework EMPRESAS_CONEXION (docs) = tabla SQL empresas_conexion (case-insensitive en SQL Server)? Solo confirmar.

## B — Empresa inicial (detalle)

4. Si nombre en EMPRESAS_CONEXION viene NULL/vacío, ¿bloqueo de instalación o fallback (ej. = cliente)?
5. En multi, ¿el seed crea una empresa (la de nombre) y el resto se dan de alta después, o hay otra regla?

## C — Módulos / “proyectos contratados”

6. Si la matriz no vive en prod: ¿la fuente de verdad en dev es un manifiesto (JSON/SQL/repo) por {cliente}+{proyecto} que genera el seeder? ¿Quién lo edita (ops interno)?
7. “Todos los proyectos contratados” en una instalación: ¿significa módulos del mismo {proyecto} o también otros productos del cliente?

## D — Seguridad seed

8. Users admin / PQ con claves fijas: ¿obligatorio cambio en primer login (firstLogin / SPEC auth)? Recomendación: sí.
9. password en EMPRESAS_CONEXION en claro: ¿aceptable v1 o ya apuntamos a secreto cifrado/vault? (no bloquea A1, sí riesgo).

## E — Gateway + SP

10. ¿Modo gateway = agent_id no nulo (y/o client_id)?
11. “Siempre SP”: ¿norma obligatoria Framework (rechazar SQL ad-hoc en capas GEN) o SHOULD con excepción documentada? Impacta mucho el código existente.

## F — A1 restantes

12. API módulo no asignado: ¿fijamos Framework 403 + auth.forbidden (3003), o 404 + resource.notFound?
13. Ayuda: ¿confirmás v1 docs completos OK (filtrado módulo = mejora)?

# Respuestas

A1 ; agreguemos fecha_vencimiento. 
A2. Unique proyecto,cliente. 
A3. en mayuscula, aunque sea case-insensitive en SQl. 
b4. corregido, es NOT NULL ese campo. 
b5. el reseto se dan de alta después en el proceso ABM Empresas (Definiremos en detalle en su momento). 
C6. mi idea es tener tablas para el asunto en la base PAQSYSTEMS de desarrollo. 
c7 . ambas cosas. dentro del proyecto Tango habrá módulos (que algunos clientes contratarán alguno/s y otros otro/s, y a su vez un cliente puede contratar diferentes proyectos. (tango, pedidosweb, partes atención). 
D8. NO. PQ es un usuario que usaremos nosotros solos. ADMIN es un ingreso genérico, que se encargue el responsable del sistema en el cliente para cambiarlo cuando lo considere necesario. 
d9. aceptable en v1. 
E10. modo gateway = agent_id AND client_id NO NULOS. 
E11. SHOULD con excepción documentada. Así vamos migrando de a poco a SP y pueden coexistir ambos esquemas. Pero la idea es que a partir de ahora vamos a definir reglas en BASE para trabajar con SP, al menos que explicitamente se mencione no hacerlo . 
F12. lo debatimos en el proximo prompt 
F13. propongo que cada proyecto tenga una carpeta 99-manual-usuario con un unico archivo por módulo (podemos establecer con el mismo nombre del módulo, o que cuando generemos las tablas de módulos definamos un atributo para cargar allí el nombre). esto incluye una carpeta 99-manual-usuario para este framework. Estos documentos se incluirán siempre en ayuda. en los proyectos, según el módulo contratado.
	