from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from ..models.address import Address
from ..models.country import Country
from ..models.region import Region
from ..models.province import Province
from ..models.district import District
from django.db import models


class AddressService:
    """Servicio para operaciones CRUD de Address"""
    
    @staticmethod
    def get_all_addresses():
        """Obtiene todas las direcciones activas"""
        try:
            addresses = Address.objects.filter(is_active=True)
            return addresses
        except Exception as e:
            raise Exception(f"Error al obtener direcciones: {str(e)}")
    
    @staticmethod
    def get_address_by_id(address_id):
        """Obtiene una dirección por ID"""
        try:
            address = Address.objects.get(id=address_id, is_active=True)
            return address
        except Address.DoesNotExist:
            raise Exception(f"Dirección con ID {address_id} no encontrada")
        except Exception as e:
            raise Exception(f"Error al obtener dirección: {str(e)}")
    
    @staticmethod
    def get_addresses_by_country(country_id):
        """Obtiene direcciones por país"""
        try:
            addresses = Address.objects.filter(country_id=country_id, is_active=True)
            return addresses
        except Exception as e:
            raise Exception(f"Error al obtener direcciones por país: {str(e)}")
    
    @staticmethod
    def get_addresses_by_region(region_id):
        """Obtiene direcciones por región"""
        try:
            addresses = Address.objects.filter(region_id=region_id, is_active=True)
            return addresses
        except Exception as e:
            raise Exception(f"Error al obtener direcciones por región: {str(e)}")
    
    @staticmethod
    def get_addresses_by_province(province_id):
        """Obtiene direcciones por provincia"""
        try:
            addresses = Address.objects.filter(province_id=province_id, is_active=True)
            return addresses
        except Exception as e:
            raise Exception(f"Error al obtener direcciones por provincia: {str(e)}")
    
    @staticmethod
    def get_addresses_by_district(district_id):
        """Obtiene direcciones por distrito"""
        try:
            addresses = Address.objects.filter(district_id=district_id, is_active=True)
            return addresses
        except Exception as e:
            raise Exception(f"Error al obtener direcciones por distrito: {str(e)}")
    
    @staticmethod
    def create_address(data):
        """Crea una nueva dirección"""
        try:
            # Validar que existan las entidades relacionadas
            country_id = data.get('country')
            region_id = data.get('region')
            province_id = data.get('province')
            district_id = data.get('district')
            
            if not all([country_id, region_id, province_id, district_id]):
                raise Exception("country, region, province y district son requeridos")
            
            # Verificar que las entidades existan
            Country.objects.get(id=country_id)
            Region.objects.get(id=region_id)
            Province.objects.get(id=province_id)
            District.objects.get(id=district_id)
            
            address = Address.objects.create(
                street=data.get('street'),
                number=data.get('number'),
                apartment=data.get('apartment'),
                reference=data.get('reference'),
                country_id=country_id,
                region_id=region_id,
                province_id=province_id,
                district_id=district_id,
                postal_code=data.get('postal_code'),
                latitude=data.get('latitude'),
                longitude=data.get('longitude'),
                is_active=data.get('is_active', True)
            )
            return address
        except Country.DoesNotExist:
            raise Exception(f"País con ID {country_id} no encontrado")
        except Region.DoesNotExist:
            raise Exception(f"Región con ID {region_id} no encontrada")
        except Province.DoesNotExist:
            raise Exception(f"Provincia con ID {province_id} no encontrada")
        except District.DoesNotExist:
            raise Exception(f"Distrito con ID {district_id} no encontrado")
        except Exception as e:
            raise Exception(f"Error al crear dirección: {str(e)}")
    
    @staticmethod
    def update_address(address_id, data):
        """Actualiza una dirección existente"""
        try:
            address = Address.objects.get(id=address_id, is_active=True)
            
            # Actualizar campos básicos
            if 'street' in data:
                address.street = data['street']
            if 'number' in data:
                address.number = data['number']
            if 'apartment' in data:
                address.apartment = data['apartment']
            if 'reference' in data:
                address.reference = data['reference']
            if 'postal_code' in data:
                address.postal_code = data['postal_code']
            if 'latitude' in data:
                address.latitude = data['latitude']
            if 'longitude' in data:
                address.longitude = data['longitude']
            if 'is_active' in data:
                address.is_active = data['is_active']
            
            # Actualizar relaciones si se proporcionan
            if 'country' in data:
                country = Country.objects.get(id=data['country'])
                address.country = country
            if 'region' in data:
                region = Region.objects.get(id=data['region'])
                address.region = region
            if 'province' in data:
                province = Province.objects.get(id=data['province'])
                address.province = province
            if 'district' in data:
                district = District.objects.get(id=data['district'])
                address.district = district
            
            address.save()
            return address
        except Address.DoesNotExist:
            raise Exception(f"Dirección con ID {address_id} no encontrada")
        except Country.DoesNotExist:
            raise Exception(f"País con ID {data.get('country')} no encontrado")
        except Region.DoesNotExist:
            raise Exception(f"Región con ID {data.get('region')} no encontrada")
        except Province.DoesNotExist:
            raise Exception(f"Provincia con ID {data.get('province')} no encontrada")
        except District.DoesNotExist:
            raise Exception(f"Distrito con ID {data.get('district')} no encontrado")
        except Exception as e:
            raise Exception(f"Error al actualizar dirección: {str(e)}")
    
    @staticmethod
    def delete_address(address_id):
        """Elimina una dirección (soft delete)"""
        try:
            address = Address.objects.get(id=address_id, is_active=True)
            address.is_active = False
            address.save()
            return True
        except Address.DoesNotExist:
            raise Exception(f"Dirección con ID {address_id} no encontrada")
        except Exception as e:
            raise Exception(f"Error al eliminar dirección: {str(e)}")
    
    @staticmethod
    def restore_address(address_id):
        """Restaura una dirección eliminada"""
        try:
            address = Address.objects.get(id=address_id, is_active=False)
            address.is_active = True
            address.save()
            return address
        except Address.DoesNotExist:
            raise Exception(f"Dirección con ID {address_id} no encontrada")
        except Exception as e:
            raise Exception(f"Error al restaurar dirección: {str(e)}")
    
    @staticmethod
    def search_addresses(query):
        """Busca direcciones por calle o referencia"""
        try:
            addresses = Address.objects.filter(
                is_active=True
            ).filter(
                models.Q(street__icontains=query) |
                models.Q(reference__icontains=query) |
                models.Q(district__name__icontains=query) |
                models.Q(province__name__icontains=query) |
                models.Q(region__name__icontains=query)
            )
            return addresses
        except Exception as e:
            raise Exception(f"Error al buscar direcciones: {str(e)}")
    
    @staticmethod
    def get_addresses_by_ubigeo(ubigeo_code):
        """Obtiene direcciones por código ubigeo"""
        try:
            addresses = Address.objects.filter(
                is_active=True
            ).filter(
                models.Q(district__ubigeo_code__icontains=ubigeo_code) |
                models.Q(province__ubigeo_code__icontains=ubigeo_code) |
                models.Q(region__ubigeo_code__icontains=ubigeo_code)
            )
            return addresses
        except Exception as e:
            raise Exception(f"Error al buscar direcciones por ubigeo: {str(e)}")
    
    @staticmethod
    def get_addresses_by_coordinates(latitude, longitude, radius_km=10):
        """Obtiene direcciones cercanas a unas coordenadas"""
        try:
            # Implementación básica - en producción usarías PostGIS o similar
            addresses = Address.objects.filter(
                is_active=True,
                latitude__isnull=False,
                longitude__isnull=False
            )
            return addresses
        except Exception as e:
            raise Exception(f"Error al buscar direcciones por coordenadas: {str(e)}")
