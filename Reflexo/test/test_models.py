from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models.country import Country
from ..models.region import Region
from ..models.province import Province
from ..models.district import District
from ..models.address import Address


class CountryModelTest(TestCase):
    """Tests para el modelo Country"""
    
    def setUp(self):
        self.country = Country.objects.create(
            name="Perú",
            ubigeo_code="PE"
        )
    
    def test_country_creation(self):
        """Test de creación de país"""
        self.assertEqual(self.country.name, "Perú")
        self.assertEqual(self.country.ubigeo_code, "PE")
        self.assertIsNotNone(self.country.created_at)
        self.assertIsNotNone(self.country.updated_at)
    
    def test_country_str_representation(self):
        """Test de representación en string"""
        self.assertEqual(str(self.country), "Perú")
    
    def test_country_meta(self):
        """Test de configuración Meta"""
        self.assertEqual(Country._meta.verbose_name, "País")
        self.assertEqual(Country._meta.verbose_name_plural, "Países")


class RegionModelTest(TestCase):
    """Tests para el modelo Region"""
    
    def setUp(self):
        self.region = Region.objects.create(
            name="Lima",
            ubigeo_code="15"
        )
    
    def test_region_creation(self):
        """Test de creación de región"""
        self.assertEqual(self.region.name, "Lima")
        self.assertEqual(self.region.ubigeo_code, "15")
        self.assertIsNone(self.region.deleted_at)
    
    def test_region_str_representation(self):
        """Test de representación en string"""
        self.assertEqual(str(self.region), "15 - Lima")
    
    def test_region_soft_delete(self):
        """Test de soft delete"""
        self.region.delete()
        self.assertIsNotNone(self.region.deleted_at)
    
    def test_region_restore(self):
        """Test de restauración"""
        self.region.delete()
        self.region.restore()
        self.assertIsNone(self.region.deleted_at)


class ProvinceModelTest(TestCase):
    """Tests para el modelo Province"""
    
    def setUp(self):
        self.region = Region.objects.create(
            name="Lima",
            ubigeo_code="15"
        )
        self.province = Province.objects.create(
            name="Lima",
            region=self.region,
            ubigeo_code="1501"
        )
    
    def test_province_creation(self):
        """Test de creación de provincia"""
        self.assertEqual(self.province.name, "Lima")
        self.assertEqual(self.province.region, self.region)
        self.assertEqual(self.province.ubigeo_code, "1501")
    
    def test_province_str_representation(self):
        """Test de representación en string"""
        self.assertEqual(str(self.province), "1501 - Lima")
    
    def test_province_region_relationship(self):
        """Test de relación con región"""
        self.assertEqual(self.province.region.name, "Lima")
        self.assertIn(self.province, self.region.provinces.all())


class DistrictModelTest(TestCase):
    """Tests para el modelo District"""
    
    def setUp(self):
        self.region = Region.objects.create(
            name="Lima",
            ubigeo_code="15"
        )
        self.province = Province.objects.create(
            name="Lima",
            region=self.region,
            ubigeo_code="1501"
        )
        self.district = District.objects.create(
            name="Lima",
            province=self.province,
            ubigeo_code="150101"
        )
    
    def test_district_creation(self):
        """Test de creación de distrito"""
        self.assertEqual(self.district.name, "Lima")
        self.assertEqual(self.district.province, self.province)
        self.assertEqual(self.district.ubigeo_code, "150101")
    
    def test_district_str_representation(self):
        """Test de representación en string"""
        self.assertEqual(str(self.district), "150101 - Lima")
    
    def test_district_province_relationship(self):
        """Test de relación con provincia"""
        self.assertEqual(self.district.province.name, "Lima")
        self.assertIn(self.district, self.province.districts.all())


class AddressModelTest(TestCase):
    """Tests para el modelo Address"""
    
    def setUp(self):
        self.country = Country.objects.create(
            name="Perú",
            ubigeo_code="PE"
        )
        self.region = Region.objects.create(
            name="Lima",
            ubigeo_code="15"
        )
        self.province = Province.objects.create(
            name="Lima",
            region=self.region,
            ubigeo_code="1501"
        )
        self.district = District.objects.create(
            name="Lima",
            province=self.province,
            ubigeo_code="150101"
        )
        self.address = Address.objects.create(
            street="Av. Arequipa",
            number="123",
            apartment="A-101",
            reference="Frente al parque",
            country=self.country,
            region=self.region,
            province=self.province,
            district=self.district,
            postal_code="15001",
            latitude="-12.0464",
            longitude="-77.0428"
        )
    
    def test_address_creation(self):
        """Test de creación de dirección"""
        self.assertEqual(self.address.street, "Av. Arequipa")
        self.assertEqual(self.address.number, "123")
        self.assertEqual(self.address.apartment, "A-101")
        self.assertEqual(self.address.country, self.country)
        self.assertEqual(self.address.region, self.region)
        self.assertEqual(self.address.province, self.province)
        self.assertEqual(self.address.district, self.district)
        self.assertTrue(self.address.is_active)
    
    def test_address_str_representation(self):
        """Test de representación en string"""
        expected = "Av. Arequipa, N° 123, Dpto. A-101, 150101 - Lima, 1501 - Lima, 15 - Lima, Perú"
        self.assertEqual(str(self.address), expected)
    
    def test_address_get_full_address(self):
        """Test de método get_full_address"""
        full_address = self.address.get_full_address()
        self.assertIsInstance(full_address, str)
        self.assertIn("Av. Arequipa", full_address)
    
    def test_address_get_ubigeo_code(self):
        """Test de método get_ubigeo_code"""
        ubigeo = self.address.get_ubigeo_code()
        self.assertEqual(ubigeo, "150101")
    
    def test_address_get_coordinates(self):
        """Test de método get_coordinates"""
        coords = self.address.get_coordinates()
        self.assertIsInstance(coords, dict)
        self.assertEqual(coords['latitude'], -12.0464)
        self.assertEqual(coords['longitude'], -77.0428)
    
    def test_address_without_coordinates(self):
        """Test de dirección sin coordenadas"""
        address_no_coords = Address.objects.create(
            street="Av. Test",
            country=self.country,
            region=self.region,
            province=self.province,
            district=self.district
        )
        coords = address_no_coords.get_coordinates()
        self.assertIsNone(coords)
