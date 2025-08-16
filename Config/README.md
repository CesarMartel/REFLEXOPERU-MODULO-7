# Configuración del Proyecto UBIGEO

Este directorio contiene los archivos de configuración principal del proyecto Django para el Módulo 7 de UBIGEO.

## Archivos Principales

- **settings.py**: Configuración general del proyecto Django
- **urls.py**: Definición de todas las rutas y endpoints de la API
- **wsgi.py**: Configuración para despliegue WSGI
- **asgi.py**: Configuración para despliegue ASGI

## Configuración (settings.py)

El archivo `settings.py` contiene la configuración principal del proyecto, incluyendo:

- Base de datos: SQLite (db.sqlite3)
- Idioma: Español (es)
- Zona horaria: America/Lima
- Aplicaciones instaladas: Django Admin, Rest Framework, Reflexo
- Configuración de plantillas: Ubicadas en Reflexo/templates
- Archivos estáticos: Configurados en la carpeta static
- Configuración CSRF para desarrollo local

## Endpoints de la API (urls.py)

El proyecto ofrece múltiples versiones de API para acceder a los datos de UBIGEO:

### API v1 - Endpoints Básicos

- `/api/countries/` - Lista de países
- `/api/regions/` - Lista de regiones
- `/api/provinces/` - Lista de provincias
- `/api/districts/` - Lista de distritos

### API v2 - Endpoints Alternativos

- `/api/v2/countries/` - Lista alternativa de países
- `/api/v2/regions/` - Lista alternativa de regiones
- `/api/v2/provinces/` - Lista alternativa de provincias
- `/api/v2/districts/` - Lista alternativa de distritos

### API v3 - CRUD Completo

#### Regiones
- `/api/v3/regions/` - Listar regiones
- `/api/v3/regions/create/` - Crear región
- `/api/v3/regions/<id>/` - Detalle de región
- `/api/v3/regions/<id>/update/` - Actualizar región
- `/api/v3/regions/<id>/delete/` - Eliminar región

#### Provincias
- `/api/v3/provinces/` - Listar provincias
- `/api/v3/provinces/create/` - Crear provincia
- `/api/v3/provinces/<id>/` - Detalle de provincia
- `/api/v3/provinces/<id>/update/` - Actualizar provincia
- `/api/v3/provinces/<id>/delete/` - Eliminar provincia
- `/api/v3/regions/<region_id>/provinces/` - Provincias por región

#### Distritos
- `/api/v3/districts/` - Listar distritos
- `/api/v3/districts/create/` - Crear distrito
- `/api/v3/districts/<id>/` - Detalle de distrito
- `/api/v3/districts/<id>/update/` - Actualizar distrito
- `/api/v3/districts/<id>/delete/` - Eliminar distrito
- `/api/v3/provinces/<province_id>/districts/` - Distritos por provincia

#### Países
- `/api/v3/countries/` - Listar países
- `/api/v3/countries/create/` - Crear país
- `/api/v3/countries/<id>/update/` - Actualizar país
- `/api/v3/countries/<id>/delete/` - Eliminar país

### Vistas Web

- `/` - Página de inicio
- `/debug/` - Vista de depuración
- `/countries/` - Vista de países
- `/regions/` - Vista de regiones
- `/provinces/` - Vista de provincias
- `/districts/` - Vista de distritos

## Despliegue

El proyecto está configurado para ser desplegado usando WSGI (wsgi.py) o ASGI (asgi.py) dependiendo del entorno de producción elegido.