# Reflexo/views/__init__.py

# Países
from .views_country import (
    countries, country_detail, country_create, country_update, country_delete
)

# Provincias
from .views_provincia import (
    provinces, province_detail, province_create, province_update, province_delete
)

# Regiones
from .views_region import (
    regions, region_detail, region_create, region_update, region_delete
)

# Distritos
from .views_distrito import (
    districts, district_detail, district_create, district_update, district_delete
)

# Direcciones
from .address import (
    addresses, address_detail, address_create, address_update, address_delete,
    addresses_by_country, addresses_by_region, addresses_by_province, addresses_by_district,
    search_addresses, addresses_by_ubigeo, address_restore
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
