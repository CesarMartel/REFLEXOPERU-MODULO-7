# Módulo 07 - Ubigeo y Ubicaciones 📍

## **Responsabilidades**
Modelos de ubicación (Country, Region, Province, District), APIs de ubigeo, gestión de ubicaciones y controllers de ubicación para el sistema de direcciones.

## **Meta: Lograr MVT con APIs para React**

### **Model (Modelo)**
- [x] **Country Model**: Modelo de países
- [x] **Region Model**: Modelo de regiones
- [x] **Province Model**: Modelo de provincias
- [x] **District Model**: Modelo de distritos
- [x] **Location Relationships**: Relaciones jerárquicas de ubicaciones

### **View (Vista/API)**
- [x] **Country Controllers**: Gestión de países
- [x] **Region Controllers**: Gestión de regiones
- [x] **Province Controllers**: Gestión de provincias
- [x] **District Controllers**: Gestión de distritos
- [x] **Ubigeo Controllers**: API unificada de ubigeo
- [x] **API Resources**: Transformación de datos para React

### **Template (Vistas Web)**
- [x] **Dashboard Views**: Vistas principales del sistema
- [x] **CRUD Views**: Vistas de gestión de entidades
- [x] **API Views**: Vistas para consumo de APIs
- [x] **Debug Views**: Vistas de depuración

## **Archivos Incluidos**
```
REFLEXO-MODULO-07/
├── Reflexo/
│   ├── models/
│   │   ├── country.py (Model)
│   │   ├── region.py (Model)
│   │   ├── province.py (Model)
│   │   └── district.py (Model)
│   ├── views/
│   │   ├── views_country.py (Controller)
│   │   ├── views_region.py (Controller)
│   │   ├── views_provincia.py (Controller)
│   │   ├── views_distrito.py (Controller)
│   │   ├── views_ubigeoController.py (API unificada)
│   │   └── views_web.py (Vistas web)
│   ├── templates/
│   │   ├── home.html
│   │   ├── countries.html
│   │   ├── regions.html
│   │   ├── provinces.html
│   │   └── districts.html
│   ├── test/
│   │   ├── test_views_country.py
│   │   ├── test_views_region.py
│   │   ├── test_views_provincia.py
│   │   └── test_views_distrito.py
│   └── management/commands/
│       ├── load_sample_data.py
│       ├── load_ubigeo_data.py
│       └── validate_ubigeo.py
├── bd/
│   ├── countries.csv
│   ├── regions.csv
│   ├── provinces.csv
│   └── districts.csv
└── static/
    ├── css/
    └── js/
```

## **APIs Desarrolladas para React**
- [x] `GET /api/countries` - Listar países
- [x] `GET /api/countries/{id}` - Obtener país específico
- [x] `POST /api/countries` - Crear país
- [x] `PUT /api/countries/{id}` - Actualizar país
- [x] `DELETE /api/countries/{id}` - Eliminar país
- [x] `GET /api/regions` - Listar regiones
- [x] `GET /api/regions/{id}` - Obtener región específica
- [x] `POST /api/regions` - Crear región
- [x] `PUT /api/regions/{id}` - Actualizar región
- [x] `DELETE /api/regions/{id}` - Eliminar región
- [x] `GET /api/provinces` - Listar provincias
- [x] `GET /api/provinces/{id}` - Obtener provincia específica
- [x] `GET /api/provinces/region/{region_id}` - Provincias por región
- [x] `POST /api/provinces` - Crear provincia
- [x] `PUT /api/provinces/{id}` - Actualizar provincia
- [x] `DELETE /api/provinces/{id}` - Eliminar provincia
- [x] `GET /api/districts` - Listar distritos
- [x] `GET /api/districts/{id}` - Obtener distrito específico
- [x] `GET /api/districts/province/{province_id}` - Distritos por provincia
- [x] `POST /api/districts` - Crear distrito
- [x] `PUT /api/districts/{id}` - Actualizar distrito
- [x] `DELETE /api/districts/{id}` - Eliminar distrito

## **Tareas Específicas**
- [x] **CRUD de Ubicaciones**: Gestión completa de países, regiones, provincias y distritos
- [x] **API de Ubigeo**: API unificada para consultas de ubicación
- [x] **Jerarquía**: Relaciones jerárquicas de ubicaciones
- [x] **Validación**: Validación de códigos de ubigeo
- [x] **Importación**: Importar datos de ubigeo desde CSV

## **Campos del Modelo Country**
- [x] Código de país (ubigeo_code)
- [x] Nombre del país (name)
- [x] Es activo (deleted_at para soft delete)
- [x] Timestamps (created_at, updated_at)

## **Campos del Modelo Region**
- [x] Código de región (ubigeo_code)
- [x] Nombre de región (name)
- [x] Es activo (deleted_at para soft delete)
- [x] Timestamps (created_at, updated_at)

## **Campos del Modelo Province**
- [x] Código de provincia (ubigeo_code)
- [x] Nombre de provincia (name)
- [x] Región (relación ForeignKey)
- [x] Es activo (deleted_at para soft delete)
- [x] Timestamps (created_at, updated_at)

## **Campos del Modelo District**
- [x] Código de distrito (ubigeo_code)
- [x] Nombre de distrito (name)
- [x] Provincia (relación ForeignKey)
- [x] Es activo (deleted_at para soft delete)
- [x] Timestamps (created_at, updated_at)

## **Estructura Jerárquica**
```
País (Perú)
├── Región (Lima)
│   ├── Provincia (Lima)
│   │   ├── Distrito (Miraflores)
│   │   ├── Distrito (San Isidro)
│   │   └── Distrito (Barranco)
│   └── Provincia (Callao)
│       ├── Distrito (Callao)
│       └── Distrito (Bellavista)
└── Región (Arequipa)
    └── Provincia (Arequipa)
        └── Distrito (Arequipa)
```

## **Datos Cargados**
- [x] **250 países** con códigos ISO2 únicos
- [x] **25 regiones** de Perú
- [x] **196 provincias** organizadas por región
- [x] **1874 distritos** organizados por provincia

## **Estado del Proyecto**
- [x] **CRUD completo** de ubicaciones implementado
- [x] **Jerarquía de ubicaciones** establecida
- [x] **Validación de ubigeo** robusta
- [x] **Integración con React** lista
- [x] **Datos de muestra** cargados
- [x] **Código reorganizado** por entidades

## **Instalación y Uso**

### Prerrequisitos
- Python 3.8+
- pip
- Git

### Pasos de Instalación
```bash
# 1. Clonar el repositorio
git clone <repository-url>
cd REFLEXO-MODULO-07

# 2. Crear entorno virtual
python -m venv env
env\Scripts\activate  # Windows
source env/bin/activate  # Linux/Mac

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar base de datos
python manage.py migrate

# 5. Cargar datos de muestra
python manage.py load_sample_data

# 6. Ejecutar servidor
python manage.py runserver
```

### Comandos Útiles
```bash
# Ejecutar tests
python -m pytest

# Tests con cobertura
python -m pytest --cov=Reflexo

# Cargar datos de ubigeo
python manage.py load_ubigeo_data

# Validar datos
python manage.py validate_ubigeo
```

## **Entregables Completados**
- [x] CRUD completo de ubicaciones
- [x] API de ubigeo funcional
- [x] Jerarquía de ubicaciones establecida
- [x] Validación de ubigeo robusta
- [x] Integración con React lista
- [x] Tests unitarios y de integración en verde
- [x] Código organizado y documentado
- [x] Datos de muestra cargados

## **Entregables Pendientes**
- [ ] Búsqueda y autocompletado implementado
- [ ] Caché de ubicaciones configurado
- [ ] APIs adicionales documentadas y testeadas
- [ ] Optimización de rendimiento
- [ ] Documentación completa de APIs

---