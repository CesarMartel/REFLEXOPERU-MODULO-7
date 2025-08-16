# Importar todos los modelos
from .country import Country, CountryUser, CountryPatient, CountryTherapist
from .region import Region, RegionUser, RegionPatient, RegionTherapist
from .province import Province, ProvinceUser, ProvincePatient, ProvinceTherapist, ProvinceDistrict
from .district import District, DistrictUser, DistrictPatient, DistrictTherapist
from .address import Address

__all__ = [
    'Country', 'CountryUser', 'CountryPatient', 'CountryTherapist',
    'Region', 'RegionUser', 'RegionPatient', 'RegionTherapist',
    'Province', 'ProvinceUser', 'ProvincePatient', 'ProvinceTherapist', 'ProvinceDistrict',
    'District', 'DistrictUser', 'DistrictPatient', 'DistrictTherapist',
    'Address',
]
