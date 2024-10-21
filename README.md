# biblioteca_digital
Sistema de Gestión de Biblioteca de la Universidad Tecnológica de Salamanca

## Pre-requisitos

- Instalar [Docker.](https://www.docker.com/get-started)
- Instalar [Docker Compose.](https://docs.docker.com/compose/install/)

## Instalación

- Clonar repositorio `git clone https://github.com/JoseRazo/biblioteca-uts.git`
- Entrar a la carpeta del proyecto `cd biblioteca-uts`
- Generar imagen docker**`docker-compose build`**
- Crear proyecto en caso de que no exista **`docker compose run biblioteca_uts django-admin startproject biblioteca .`**
- Generar contenedores **`docker-compose up -d`**
- Crear APP `docker compose run biblioteca_uts python manage.py startapp nombre_de_la_app`
- Crear migraciones `docker compose run biblioteca_uts python manage.py makemigrations`
- Ejecutar migraciones `docker compose run biblioteca_uts python manage.py migrate`
- Crear superusuario **`docker compose run biblioteca_uts python manage.py createsuperuser`**
- Configurar archivo **`.env`** si es necesario.

## Abrir proyecto

Abrir navegador y entrar a URL [127.0.0.1:8080](http://127.0.0.1:8080)


----------------------------------------------------------
# biblioteca_django
# De este modo no tendremos problemas al correr el entorno virtual que hayamos creado en nuestra maquina
# Este archivo .gitignore solo es visible en GitHub
#
# Entra en la carpeta que se clono
#
# Se tendrá que crear la carpeta venv
# Crear entorno virtual
# py -m venv venv
#
# Correr el entorno virtual
# .\venv\Scripts\active
#
# Ejecutar archivo requirements.txt
# pip install -r requirements.txt
#
# Entrar a carpeta del proyecto "biblioteca"
#
# Si aun no se ha realizado las migraciones, se debe correr el comando
# py manage.py makemigrations
# py manage.py migrate
#
# Crear superUsuario
# py manage.py createsuperuser
#
# pip install django-session-security
# Si no te lo permite realizar lo siguiente (en orden)
# Usar: pip uninstall django-session-security
# Usar: pip install django-session-security
#
#
# Ejecutar runserver
# py manage.py runserver
#
#
# Librerías adicionales
# pip install django-import-export
# pip install django-mysql
#
# pip install django-environ
#
