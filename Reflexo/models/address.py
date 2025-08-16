from django.db import models
from .country import Country
from .region import Region
from .province import Province
from .district import District


class Address(models.Model):
    """Modelo para manejar direcciones completas"""
    
    # Información básica de la dirección
    street = models.CharField(max_length=255, verbose_name="Calle")
    number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Número")
    apartment = models.CharField(max_length=50, blank=True, null=True, verbose_name="Departamento/Oficina")
    reference = models.TextField(blank=True, null=True, verbose_name="Referencia")
    
    # Ubicación geográfica
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="País")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Región/Departamento")
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name="Provincia")
    district = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name="Distrito")
    
    # Información adicional
    postal_code = models.CharField(max_length=10, blank=True, null=True, verbose_name="Código Postal")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name="Latitud")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name="Longitud")
    
    # Campos de auditoría
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    
    class Meta:
        verbose_name = "Dirección"
        verbose_name_plural = "Direcciones"
        ordering = ['country', 'region', 'province', 'district', 'street']
    
    def __str__(self):
        """Representación en string de la dirección"""
        address_parts = []
        
        if self.street:
            address_parts.append(self.street)
        if self.number:
            address_parts.append(f"N° {self.number}")
        if self.apartment:
            address_parts.append(f"Dpto. {self.apartment}")
        
        address_parts.append(str(self.district))
        address_parts.append(str(self.province))
        address_parts.append(str(self.region))
        address_parts.append(str(self.country))
        
        return ", ".join(address_parts)
    
    def get_full_address(self):
        """Obtiene la dirección completa formateada"""
        return str(self)
    
    def get_ubigeo_code(self):
        """Obtiene el código ubigeo completo de la dirección"""
        if self.district and self.district.ubigeo_code:
            return self.district.ubigeo_code
        elif self.province and self.province.ubigeo_code:
            return self.province.ubigeo_code
        elif self.region and self.region.ubigeo_code:
            return self.region.ubigeo_code
        return None
    
    def get_coordinates(self):
        """Obtiene las coordenadas de la dirección"""
        if self.latitude and self.longitude:
            return {
                'latitude': float(self.latitude),
                'longitude': float(self.longitude)
            }
        return None
