PROYECTO REFLEXOPERU - MODULO DE UBIGEO
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1. Descripción General del Proyecto Principal
El proyecto ReflexoPeru-V2-Front es una plataforma web integral diseñada para la gestión administrativa y operativa de un centro de reflexoterapia. El sistema permite administrar pacientes, programar citas, generar reportes detallados, gestionar personal y registrar pagos. Su objetivo es optimizar la operación diaria y facilitar la toma de decisiones estratégicas mediante el análisis de reportes y métricas visuales. El sistema está orientado a personal administrativo y terapeutas, ofreciendo una experiencia de usuario ágil y eficiente.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
2. Objetivo del Módulo - Grupo 7
El Grupo 7 tiene la responsabilidad de migrar el módulo de UBIGEO (ubicaciones geográficas) a un nuevo stack tecnológico. La tarea principal consiste en adaptar y reescribir la funcionalidad existente del módulo, que gestiona países, regiones, provincias y distritos, del lenguaje de programación original a Python utilizando el framework Django.

El objetivo de esta migración es modernizar el módulo, mejorar su escalabilidad y facilitar su integración con el resto de los componentes del nuevo sistema.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
3. Tecnologías y Herramientas
Lenguaje de Programación: Python

Framework: Django

API: Django REST Framework (DRF)

Control de Versiones: Git / GitHub

Gestión de Proyectos: Trello

Integración Continua: GitHub Actions
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
4. Equipo de Desarrollo
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
