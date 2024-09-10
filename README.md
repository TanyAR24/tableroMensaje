# TableroMensajes
# Objetivo del trabajo práctico
Desarrollar un proyecto Django denominado TableroMensajes siguiendo el patrón de diseño Modelo-Vista-Plantilla (MVT). Este proyecto permitirá a las/los estudiantes aplicar conceptos fundamentales de Django, como la creación de vistas basadas en funciones y en clases, el uso del Django Template Language (DTL), modularización y reutilización de plantillas, y la implementación de funcionalidades clave como la creación, visualización y eliminación de mensajes.

## Descripción
TableroMensajes es un sistema de mensajería desarrollado con Django que permite a los usuarios autenticados enviar, recibir y eliminar mensajes. 

## Funcionalidades Implementadas

### 1. Creación de Mensajes
- Los usuarios autenticados pueden crear nuevos mensajes.
- Se implementa tanto con vistas basadas en funciones (FBV) como con vistas basadas en clases (CBV).

### 2. Visualización de Mensajes
- **Mensajes Recibidos:** Los usuarios pueden ver los mensajes recibidos de otros usuarios.
- **Mensajes Enviados:** Los usuarios pueden ver los mensajes que han enviado.

### 3. Eliminación de Mensajes
- Los usuarios pueden eliminar mensajes que han enviado o recibido.

### 4. Autenticación de Usuarios
- Los usuarios pueden registrarse, iniciar sesión y acceder al sistema utilizando el sistema de autenticación de Django.

## Estructura de Plantillas
- **Herencia de plantillas:** Se usa una plantilla base (`base.html`) que define el diseño general de la aplicación. Las plantillas específicas para cada vista heredan de esta plantilla base.
- Plantillas creadas para:
  - **Crear mensajes** (`crear_mensaje.html`)
  - **Ver mensajes enviados** (`mensajes_enviados.html`)
  - **Ver mensajes recibidos** (`mensajes_recibidos.html`)
  - **Eliminar mensajes** (`eliminar_mensaje.html`)

## Rutas (URLs)
- `/mensajes/crear/`: Permite crear un mensaje.
- `/mensajes/enviados/`: Muestra los mensajes enviados.
- `/mensajes/recibidos/`: Muestra los mensajes recibidos.
- `/mensajes/eliminar/<int:mensaje_id>/`: Elimina el mensaje con el ID especificado.


## Usuarios de Prueba
- **Usuario:** Brisa | **Correo:** brisa.pp@gmail.com | **Contraseña:** Palito99
- **Usuario:** Pedro | **Correo:** pedrito@gmail.com | **Contraseña:** 55Rosado
- **Usuario:** Lalisa | **Correo:** lol@gmail.com | **Contraseña:** Inca6678

## Instalación

1. Clone el repositorio:
   ```bash
   git clone https://github.com/TanyAR24/tableroMensaje.git