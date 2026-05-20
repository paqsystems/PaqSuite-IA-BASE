# Paqsuite + AWS + Tailscale + SQL Server

# Guía completa de implementación (MVP inicial)

Autor: ChatGPT  
Fecha: Mayo 2026

---

# OBJETIVO

Implementar:

```text
Frontend Web (AWS)
        ↓ HTTPS
Backend API (AWS)
        ↓ Tailscale privada
SQL Server Cliente
```

Sin:

abrir puertos públicos;
exponer SQL Server a Internet;
VPNs complejas;
cambios importantes en las APIs actuales.
CONCEPTO GENERAL

Tailscale crea una red privada segura entre:

el servidor AWS;
el servidor del cliente.

Ambos equipos quedan conectados mediante IPs privadas internas:

100.x.x.x

El backend en AWS podrá acceder al SQL Server del cliente como si estuvieran en la misma red privada.

```text
ARQUITECTURA FINAL
┌─────────────────────────┐
│ Usuario Web             │
└──────────┬──────────────┘
           │ HTTPS
           ▼
┌─────────────────────────┐
│ Frontend                │
│ AWS                     │
└──────────┬──────────────┘
           │ API
           ▼
┌─────────────────────────┐
│ Backend API             │
│ Laravel / .NET          │
│ AWS EC2                 │
└──────────┬──────────────┘
           │ Tailscale
           ▼
┌─────────────────────────┐
│ SQL Server Cliente      │
│ Tango Gestión           │
└─────────────────────────┘
```

# ETAPA 1 — CREAR CUENTA EN TAILSCALE

## 1.1 Crear cuenta

Ingresar a:

https://tailscale.com

Presionar:

Get Started

Podés usar:

Google
Microsoft
GitHub

Mi recomendación:

Usar Google Workspace empresarial

# ETAPA 2 — CREAR EL TAILNET

¿Qué es un Tailnet?

Es la red privada virtual de Tailscale.

Ejemplo:

paqsuite.tailnet

Todos los equipos conectados aparecerán allí.

# ETAPA 3 — INSTALAR TAILSCALE EN AWS

## 3.1 Crear servidor EC2

Recomendación inicial

Ubuntu Server 24 LTS

Tamaño:

t3.small

o:

t3.medium

## 3.2 Conectarse por SSH

Desde Windows usar:

PuTTY

o:

Windows Terminal

## 3.3 Instalar Tailscale

Ejecutar:

curl -fsSL https://tailscale.com/install.sh | sh

## 3.4 Iniciar Tailscale

Ejecutar:

sudo tailscale up

El sistema mostrará una URL.

Ejemplo:

https://login.tailscale.com/a/xxxxxxxx

Abrirla desde el navegador.

Autorizar el dispositivo.

## 3.5 Verificar IP privada

Ejecutar:

tailscale ip -4

Resultado:

100.101.102.103

IMPORTANTE:

Esa NO es una IP pública.

Es privada dentro de Tailscale.

Guardar esa IP.

# ETAPA 4 — INSTALAR TAILSCALE EN EL CLIENTE

## 4.1 Descargar Tailscale

Ir a:

https://tailscale.com/download/windows

Instalar normalmente.

## 4.2 Iniciar sesión

Abrir Tailscale.

Loguearse con la misma cuenta usada en AWS.

## 4.3 Verificar conexión

El equipo aparecerá en:

https://login.tailscale.com/admin/machines

## 4.4 Obtener IP privada del cliente

En PowerShell:

tailscale ip -4

Ejemplo:

100.88.77.66

Guardar esa IP.

# ETAPA 5 — CONFIGURAR SQL SERVER

## 5.1 Abrir SQL Server Configuration Manager

Ir a:

Inicio
→ SQL Server Configuration Manager

## 5.2 Habilitar TCP/IP

Ir a:

SQL Server Network Configuration
→ Protocols for MSSQLSERVER

Habilitar:

TCP/IP = Enabled

## 5.3 Configurar puerto fijo

Abrir:

TCP/IP
→ IP Addresses

Buscar:

IPAll

Configurar:

TCP Port = 1433

Vaciar:

TCP Dynamic Ports

## 5.4 Reiniciar SQL Server

Desde:

SQL Server Services

Reiniciar:

SQL Server (MSSQLSERVER)

# ETAPA 6 — CONFIGURAR FIREWALL WINDOWS

## 6.1 Abrir PowerShell administrador

Ejecutar:

New-NetFirewallRule `
  -DisplayName "Paqsuite SQL Tailscale" `
  -Direction Inbound `
  -Protocol TCP `
  -LocalPort 1433 `
  -Action Allow `
  -RemoteAddress 100.64.0.0/10
  
## 6.2 Opción más segura

Permitir SOLO AWS:

New-NetFirewallRule `
  -DisplayName "Paqsuite SQL SOLO AWS" `
  -Direction Inbound `
  -Protocol TCP `
  -LocalPort 1433 `
  -Action Allow `
  -RemoteAddress 100.101.102.103
  
# ETAPA 7 — PROBAR CONECTIVIDAD

## 7.1 Desde AWS

Probar ping:

ping 100.88.77.66

## 7.2 Probar SQL

Instalar netcat:

sudo apt install netcat

Probar:

nc -zv 100.88.77.66 1433

Resultado esperado:

succeeded

# ETAPA 8 — CONFIGURAR MAGICS DNS

¿Qué es MagicDNS?

Permite usar nombres en lugar de IPs.

Ejemplo:

cliente1.tailnet.ts.net

## 8.1 Activar MagicDNS

Ir a:

https://login.tailscale.com/admin/dns

Activar:

Enable MagicDNS

## 8.2 Ver hostname

En:

Machines

Aparecerá:

cliente1

El hostname completo será:

cliente1.tailnet.ts.net

# ETAPA 9 — CONFIGURAR EL BACKEND

## 9.1 Cambiar connection string

ANTES:

Server=192.168.0.10;

AHORA:

Server=cliente1.tailnet.ts.net,1433;

## 9.2 Ejemplo .NET

```
var connectionString =
$"Server=cliente1.tailnet.ts.net,1433;" +
$"Database=EMPRESA;" +
$"User Id=paqsuite_api;" +
$"Password=xxxx;" +
$"TrustServerCertificate=True;";
9.3 Ejemplo Laravel
DB_CONNECTION=sqlsrv
DB_HOST=cliente1.tailnet.ts.net
DB_PORT=1433
DB_DATABASE=EMPRESA
DB_USERNAME=paqsuite_api
DB_PASSWORD=xxxx
ETAPA 10 — MULTIEMPRESA
Objetivo

Un único backend AWS.

Múltiples clientes.
```

# 10.1 Crear base central AWS

Ejemplo:

PAQSUITE_CORE

## 10.2 Tabla EMPRESAS_CONEXION

CREATE TABLE EMPRESAS_CONEXION
(
    ID_EMPRESA INT PRIMARY KEY,
    NOMBRE VARCHAR(100),
    HOST_TAILSCALE VARCHAR(200),
    SQL_DATABASE VARCHAR(100),
    SQL_USER VARCHAR(100),
    SQL_PASSWORD VARBINARY(MAX),
    ACTIVO BIT
)

## 10.3 Ejemplo de registros

Empresa	Host
Cliente A	clienteA.tailnet.ts.net
Cliente B	clienteB.tailnet.ts.net
Cliente C	clienteC.tailnet.ts.net
10.4 Flujo
Usuario login
→ Empresa identificada
→ Buscar conexión
→ Conectar SQL correcto

# ETAPA 11 — SEGURIDAD

## 11.1 NO usar SA

Crear usuario:

CREATE LOGIN paqsuite_api
WITH PASSWORD = 'password_seguro'

## 11.2 Dar permisos mínimos

Solo:

SELECT
EXECUTE SPs
INSERT/UPDATE específicos si hace falta.

## 11.3 ACLs Tailscale

Ir a:

https://login.tailscale.com/admin/acls
ACL básica
{
  "acls": [
    {
      "action": "accept",
      "src": ["100.101.102.103"],
      "dst": ["100.88.77.66:1433"]
    }
  ]
}

Esto significa:

Solo AWS puede acceder al SQL del cliente.

# ETAPA 12 — MONITOREO FUTURO

Más adelante crear:

Paqsuite Connector Monitor

Funciones:

heartbeat;
diagnóstico;
logs;
verificar SQL;
verificar Tailscale.

Pero NO es necesario para comenzar.

# ETAPA 13 — RENDIMIENTO

IMPORTANTE

Tailscale NO suele ser el problema.

El problema suele ser:

consultas enormes;
SELECT *;
traer demasiados datos.
Recomendaciones

SIEMPRE:

TOP
WHERE
SPs
Indices
Evitar
SELECT *

# ETAPA 14 — PRIMER MVP RECOMENDADO

Objetivo

Demostrar:

AWS consulta SQL Server cliente
SIN abrir puertos
MVP mínimo
AWS
EC2 Ubuntu
Laravel/.NET
Tailscale
Cliente
SQL Server
Tailscale
API simple

Ejemplo:

/api/testclientes

La API:

conecta por Tailscale;
consulta una tabla;
devuelve JSON.

# RESULTADO FINAL

Obtendrás:

✅ Backend cloud moderno
✅ SQL Server privado
✅ Sin abrir puertos públicos
✅ APIs actuales reutilizadas
✅ Multiempresa
✅ Un solo deploy AWS
✅ Arquitectura profesional
✅ Escalable
✅ Bajo costo operativo

# EVOLUCIÓN FUTURA

Más adelante podrás agregar:

agente inteligente;
sincronización;
cache local;
monitoreo avanzado;
múltiples servidores AWS;
balanceo;
microservicios.

Pero para comenzar:

- Tailscale SOLO

es una excelente decisión.

# ADICIONALES

## Emular URL simil DNS

sudo tailscale serve https / http://127.0.0.1:3000

esto genera una url con el nombre de la máquina y puerto 3000

## Habilitar Firewall en AWS

1. EC2
2. Instance
3. Security
4. Click en el Security Group
5. Inbound Rules
6. Add Rule
Type: MySQL/Aurora
Protocol: TCP
Port: 3306
Source: 100.64.0.0/10