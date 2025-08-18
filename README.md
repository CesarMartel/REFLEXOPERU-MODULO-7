# Módulo 7 - UBIGEO

## Descripción

Este módulo proporciona un sistema completo para la gestión de datos geográficos (UBIGEO) de Perú y otros países. Implementa una API REST y vistas web para acceder y manipular información de países, regiones, provincias, distritos y direcciones.

## Características Principales

- **API REST completa**: Endpoints para operaciones CRUD en todas las entidades geográficas
- **Múltiples versiones de API**: Compatibilidad con diferentes niveles de integración
- **Interfaz web**: Vistas HTML para explorar los datos geográficos
- **Jerarquía geográfica**: Relaciones entre países, regiones, provincias y distritos
- **Códigos UBIGEO**: Soporte para el estándar oficial de códigos UBIGEO de Perú
- **Importación de datos**: Comandos para importar datos desde archivos CSV
- **Pruebas unitarias**: Cobertura completa de modelos, servicios y vistas

## Estructura del Proyecto

- **Config/**: Configuración principal del proyecto Django
- **Reflexo/**: Aplicación principal con la lógica de negocio
  - **models/**: Definición de modelos de datos
  - **views/**: Vistas y controladores para la API y páginas web
  - **serializers/**: Serializadores para la API REST
  - **services/**: Lógica de negocio y servicios
  - **management/**: Comandos personalizados de Django
  - **test/**: Pruebas unitarias y de integración
- **bd/**: Archivos CSV con datos geográficos

## Requisitos

- Python 3.8+
- Django 3.2+
- Django Rest Framework 3.12+
- Otras dependencias listadas en requirements.txt

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/REFLEXOPERU-MODULO-7.git
   cd REFLEXOPERU-MODULO-7
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Aplica las migraciones:
   ```bash
   python manage.py migrate
   ```

5. Importa los datos geográficos:
   ```bash
   python manage.py import_ubigeo_data --type=countries --file=bd/countries.csv
   python manage.py import_ubigeo_data --type=regions --file=bd/regions.csv
   python manage.py import_ubigeo_data --type=provinces --file=bd/provinces.csv
   python manage.py import_ubigeo_data --type=districts --file=bd/districts.csv
   ```

6. Inicia el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

## Uso de la API

Consulta la documentación detallada en `Config/README.md` para ver todos los endpoints disponibles.

Ejemplos básicos:

- Listar regiones: `GET /api/v3/regions/`
- Crear región: `POST /api/v3/regions/create/`
- Obtener provincias de una región: `GET /api/v3/regions/{region_id}/provinces/`
- Obtener distritos de una provincia: `GET /api/v3/provinces/{province_id}/districts/`

## Integración con Otros Módulos

Este módulo está diseñado para ser utilizado por otros módulos del sistema REFLEXOPERU. Para integrarlo:

1. Incluye este módulo como dependencia en tu proyecto
2. Utiliza los endpoints de la API para obtener y manipular datos geográficos
3. Importa los modelos y servicios necesarios para acceder directamente a la lógica de negocio

## Pruebas

Ejecuta las pruebas unitarias y de integración:

```bash
python manage.py test
```

O utilizando pytest:

```bash
pytest
```

## Documentación Adicional

Cada carpeta del proyecto contiene un archivo README.md con documentación específica:

- **Config/README.md**: Configuración y endpoints de la API
- **Reflexo/README.md**: Estructura general de la aplicación
- **Reflexo/models/README.md**: Modelos de datos
- **Reflexo/views/README.md**: Vistas y controladores
- **Reflexo/serializers/README.md**: Serializadores para la API
- **Reflexo/services/README.md**: Servicios y lógica de negocio
- **Reflexo/test/README.md**: Pruebas unitarias y de integración
- **Reflexo/management/commands/README.md**: Comandos personalizados
- **bd/README.md**: Datos geográficos en CSV

## Contribución

1. Haz un fork del repositorio
2. Crea una rama para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`)
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva funcionalidad'`)
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request
