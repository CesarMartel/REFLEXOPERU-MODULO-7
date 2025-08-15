# Sistema ReflexoPeru - Módulo 7: UBIGEO
## Descripción del Proyecto
El Sistema ReflexoPeru es una plataforma médica especializada en terapias, diseñada para facilitar la gestión de pacientes, terapeutas y servicios médicos. El Módulo 7 se enfoca específicamente en la implementación del sistema de UBIGEO (Ubicación Geográfica), que permite la gestión jerárquica de ubicaciones geográficas (países, regiones, provincias y distritos) para el correcto registro de direcciones de pacientes, terapeutas y usuarios del sistema.

## Equipo de Desarrollo
- César Martel - Scrum Master
- Miguel Ruiz - Desarrollador Backend
- Sebastian Rosas - Desarrollador Backend
- Fernando Dionicio - Desarrollador Frontend
- Roxana Matamoros - Desarrolladora Frontend
## Tecnologías Utilizadas
- Backend : Django 5.2.4, Django REST Framework 3.15.2
- Testing : Pytest, Pytest-Django, Pytest-cov
- Frontend : HTML, CSS, JavaScript, React (consumo de APIs)
- Otros : Pillow para manejo de imágenes
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
```plaintext
Estructura del Proyecto
├── Config/                     # Configuración del proyecto Django
├── Reflexo/                     # Aplicación principal
│   ├── models/                  # Modelos de datos
│   │   ├── country.py           # Modelo de países
│   │   ├── region.py            # Modelo de regiones
│   │   ├── province.py          # Modelo de provincias
│   │   └── district.py          # Modelo de distritos
│   ├── views/                   # Controladores y APIs
│   │   ├── views_country.py     # API de países
│   │   ├── views_region.py      # API de regiones
│   │   ├── views_provincia.py   # API de provincias
│   │   ├── views_distrito.py    # API de distritos
│   │   ├── views_ubigeoController.py # API unificada
│   │   └── views_web.py         # Vistas web
│   ├── templates/               # Plantillas HTML
│   ├── test/                    # Pruebas unitarias
│   └── management/commands/     # Comandos personalizados
│       ├── load_sample_data.py  # Carga de datos de muestra
│       ├── load_ubigeo_data.py  # Carga de datos de ubigeo
│       └── validate_ubigeo.py   # Validación de códigos
├── bd/                          # Archivos CSV con datos iniciales
│   ├── countries.csv            # Datos de países
│   ├── regions.csv              # Datos de regiones
│   ├── provinces.csv            # Datos de provincias
│   └── districts.csv            # Datos de distritos
└── static/                      # Archivos estáticos
    ├── css/                     # Hojas de estilo
    ├── js/                      # Scripts JavaScript
    └── logo.png                 # Logo del sistema

<<<<<<< HEAD
Framework: Django

API: Django REST Framework (DRF)

Control de Versiones: Git / GitHub

Gestión de Proyectos: Trello

Integración Continua: GitHub Actions
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
4. Librerías Utilizadas
El proyecto utiliza las siguientes librerías:

| Librería                | Versión | Descripción                                           | Estado         |
| ----------------------- | ------- | ----------------------------------------------------- | -------------- |
| Django                  | 5.2.4   | Framework web principal                               | En uso         |
| Django REST Framework   | 3.15.2  | Para crear APIs RESTful                               | Parcialmente   |
| pytest                  | 8.4.1   | Framework de pruebas                                  | En uso         |
| pytest-django           | 4.11.1  | Integración de pytest con Django                      | En uso         |
| pytest-cov              | 5.0.0   | Para análisis de cobertura de código                  | En uso         |
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
5. Equipo de Desarrollo
El equipo encargado de la migración del módulo de Ubigeo está compuesto por los siguientes miembros:

| Rol                 | Nombre            |
| ------------------- | ------------------|
|     Scrum Master    | Cesar Martel      |
|      Developer      | Sebastian Rosas   |
|      Developer      | Yhefritd Huacho   |
|      Developer      | Fernando Dionicio |
|      Developer      | Miguel Ruiz       |
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
6. Instalación y Configuración
Para ejecutar el proyecto localmente, sigue los siguientes pasos:

Clona el repositorio:
git clone [https://github.com/CesarMartel/UBIGEO-DJANGO.git]
cd [UBIGEO-DJANGO]

Crea y activa un entorno virtual:
python -m venv venv
source venv/bin/activate  (en macOS/Linux)
venv\Scripts\activate    (en Windows)

Instala las dependencias:
pip install -r requirements.txt

Configura la base de datos:
Asegúrate de que la configuración en settings.py sea correcta.

Aplica las migraciones:
python manage.py makemigrations ubigeo
python manage.py migrate

7. Uso
Para levantar el servidor de desarrollo, ejecuta:

python manage.py runserver

El proyecto estará disponible en http://127.0.0.1:8000/. Los endpoints de la API se pueden encontrar en la configuración de urls.py.
=======
    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### Modelo Country (País)
- Campos : name, ubigeo_code, created_at, updated_at
- Relaciones : users, patients, therapists
### Modelo Region (Región)
- Campos : name, ubigeo_code, deleted_at, created_at, updated_at
- Relaciones : users, patients, therapists, provinces
### Modelo Province (Provincia)
- Campos : name, region (FK), ubigeo_code, created_at, updated_at
- Relaciones : users, patients, therapists, districts
### Modelo District (Distrito)
- Campos : name, province (FK), ubigeo_code, created_at, updated_at
- Relaciones : users, patients, therapists
## APIs Desarrolladas
### API de Países
- GET /api/countries - Listar países
- GET /api/countries/{id} - Obtener país específico
- POST /api/countries - Crear país
- PUT /api/countries/{id} - Actualizar país
- DELETE /api/countries/{id} - Eliminar país
### API de Regiones
- GET /api/regions - Listar regiones
- GET /api/regions/{id} - Obtener región específica
- POST /api/regions - Crear región
- PUT /api/regions/{id} - Actualizar región
- DELETE /api/regions/{id} - Eliminar región
### API de Provincias
- GET /api/provinces - Listar provincias
- GET /api/provinces/{id} - Obtener provincia específica
- GET /api/provinces/region/{region_id} - Provincias por región
- POST /api/provinces - Crear provincia
- PUT /api/provinces/{id} - Actualizar provincia
- DELETE /api/provinces/{id} - Eliminar provincia
### API de Distritos
- GET /api/districts - Listar distritos
- GET /api/districts/{id} - Obtener distrito específico
- GET /api/districts/province/{province_id} - Distritos por provincia
- POST /api/districts - Crear distrito
- PUT /api/districts/{id} - Actualizar distrito
- DELETE /api/districts/{id} - Eliminar distrito
## Datos Precargados
- 250 países con códigos ISO2 únicos
- 25 regiones de Perú
- 196 provincias organizadas por región
- 1,874 distritos organizados por provincia
## Características Implementadas
- CRUD Completo : Gestión completa de países, regiones, provincias y distritos
- API RESTful : Endpoints para consumo desde aplicaciones frontend
- Jerarquía de Ubicaciones : Relaciones jerárquicas entre entidades geográficas
- Validación de Códigos : Sistema de validación de códigos de ubigeo
- Importación de Datos : Comandos para importar datos desde archivos CSV
- Soft Delete : Eliminación lógica de registros para mantener integridad referencial
- Pruebas Unitarias : Cobertura de pruebas para modelos y APIs
## Instalación y Configuración
1. 1.
   Clonar el repositorio
2. 2.
   Instalar dependencias: pip install -r requirements.txt
3. 3.
   Aplicar migraciones: python manage.py migrate
4. 4.
   Cargar datos iniciales: python manage.py load_sample_data
5. 5.
   Iniciar servidor de desarrollo: python manage.py runserver
    
>>>>>>> 9f30893823309ee8ae29c1b3df933393372a3ab3
