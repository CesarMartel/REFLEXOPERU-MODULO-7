from rest_framework import serializers
from ..models.address import Address
from .country_serializer import CountryListSerializer
from .region_serializer import RegionListSerializer
from .province_serializer import ProvinceListSerializer
from .district_serializer import DistrictListSerializer


class AddressSerializer(serializers.ModelSerializer):
    """Serializer para el modelo Address que acepta todos los campos"""
    
    class Meta:
        model = Address
        fields = '__all__'  # Incluye todos los campos del modelo
        read_only_fields = ('id', 'created_at', 'updated_at')  # Campos de solo lectura


class AddressListSerializer(serializers.ModelSerializer):
    """Serializer para listar direcciones con información básica"""
    
    class Meta:
        model = Address
        fields = ('id', 'street', 'number', 'apartment', 'district', 'province', 'region', 'country', 'is_active', 'created_at')


class AddressCreateSerializer(serializers.ModelSerializer):
    """Serializer para crear direcciones"""
    
    class Meta:
        model = Address
        fields = ('street', 'number', 'apartment', 'reference', 'country', 'region', 'province', 'district', 'postal_code', 'latitude', 'longitude', 'is_active')


class AddressUpdateSerializer(serializers.ModelSerializer):
    """Serializer para actualizar direcciones"""
    
    class Meta:
        model = Address
        fields = ('street', 'number', 'apartment', 'reference', 'country', 'region', 'province', 'district', 'postal_code', 'latitude', 'longitude', 'is_active')
        extra_kwargs = {
            'street': {'required': False},
            'number': {'required': False},
            'apartment': {'required': False},
            'reference': {'required': False},
            'country': {'required': False},
            'region': {'required': False},
            'province': {'required': False},
            'district': {'required': False},
            'postal_code': {'required': False},
            'latitude': {'required': False},
            'longitude': {'required': False},
            'is_active': {'required': False}
        }


class AddressDetailSerializer(serializers.ModelSerializer):
    """Serializer para mostrar detalles de dirección con información completa"""
    
    country = CountryListSerializer(read_only=True)
    region = RegionListSerializer(read_only=True)
    province = ProvinceListSerializer(read_only=True)
    district = DistrictListSerializer(read_only=True)
    
    class Meta:
        model = Address
        fields = ('id', 'street', 'number', 'apartment', 'reference', 'country', 'region', 'province', 'district', 'postal_code', 'latitude', 'longitude', 'is_active', 'created_at', 'updated_at')


class AddressWithUbigeoSerializer(serializers.ModelSerializer):
    """Serializer para direcciones con información de ubigeo"""
    
    country_name = serializers.CharField(source='country.name', read_only=True)
    region_name = serializers.CharField(source='region.name', read_only=True)
    region_ubigeo = serializers.CharField(source='region.ubigeo_code', read_only=True)
    province_name = serializers.CharField(source='province.name', read_only=True)
    province_ubigeo = serializers.CharField(source='province.ubigeo_code', read_only=True)
    district_name = serializers.CharField(source='district.name', read_only=True)
    district_ubigeo = serializers.CharField(source='district.ubigeo_code', read_only=True)
    full_ubigeo = serializers.SerializerMethodField()
    
    class Meta:
        model = Address
        fields = (
            'id', 'street', 'number', 'apartment', 'reference',
            'country', 'country_name',
            'region', 'region_name', 'region_ubigeo',
            'province', 'province_name', 'province_ubigeo',
            'district', 'district_name', 'district_ubigeo',
            'postal_code', 'latitude', 'longitude', 'is_active',
            'full_ubigeo', 'created_at', 'updated_at'
        )
    
    def get_full_ubigeo(self, obj):
        """Obtiene el código ubigeo completo"""
        return obj.get_ubigeo_code()


class AddressCompactSerializer(serializers.ModelSerializer):
    """Serializer compacto para direcciones"""
    
    full_address = serializers.SerializerMethodField()
    ubigeo_code = serializers.SerializerMethodField()
    
    class Meta:
        model = Address
        fields = ('id', 'full_address', 'ubigeo_code', 'is_active')
    
    def get_full_address(self, obj):
        """Obtiene la dirección completa formateada"""
        return obj.get_full_address()
    
    def get_ubigeo_code(self, obj):
        """Obtiene el código ubigeo"""
        return obj.get_ubigeo_code()
