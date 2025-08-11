# Reflexo/views/__init__.py

# Países
from .views_country import list_countries

# Provincias
from .views_provincia import ProvinceListView

# Regiones
from .views_region import RegionView

# Endpoints de ubigeo (CRUD completo)
from .views_ubigeoController import (
    regions, provinces, districts, countries,
    region_detail, region_create, region_update, region_delete,
    province_detail, province_create, province_update, province_delete,
    district_detail, district_create, district_update, district_delete,
    country_create,
    country_update,
    country_delete,
)

# Vistas web
from .views_web import (
    home_view,
    debug_view,
    countries_view,
    regions_view,
    provinces_view,
    districts_view,
    api_countries,
    api_regions,
    api_provinces,
    api_districts
)
