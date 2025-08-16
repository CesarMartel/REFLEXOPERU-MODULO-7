from django.contrib import admin
from .models.country import Country
from .models.region import Region
from .models.province import Province
from .models.district import District
from .models.address import Address


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'ubigeo_code', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'ubigeo_code')
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'ubigeo_code', 'deleted_at', 'created_at', 'updated_at')
    list_filter = ('deleted_at', 'created_at', 'updated_at')
    search_fields = ('name', 'ubigeo_code')
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    
    def get_queryset(self, request):
        """Mostrar solo regiones no eliminadas por defecto"""
        return super().get_queryset(request).filter(deleted_at__isnull=True)


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'ubigeo_code', 'created_at', 'updated_at')
    list_filter = ('region', 'created_at', 'updated_at')
    search_fields = ('name', 'ubigeo_code', 'region__name')
    ordering = ('region__name', 'name')
    readonly_fields = ('created_at', 'updated_at')
    autocomplete_fields = ('region',)


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'province', 'ubigeo_code', 'created_at', 'updated_at')
    list_filter = ('province__region', 'province', 'created_at', 'updated_at')
    search_fields = ('name', 'ubigeo_code', 'province__name', 'province__region__name')
    ordering = ('province__region__name', 'province__name', 'name')
    readonly_fields = ('created_at', 'updated_at')
    autocomplete_fields = ('province',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'number', 'district', 'province', 'region', 'country', 'is_active', 'created_at')
    list_filter = ('country', 'region', 'province', 'district', 'is_active', 'created_at', 'updated_at')
    search_fields = ('street', 'number', 'apartment', 'reference', 'district__name', 'province__name', 'region__name')
    ordering = ('country__name', 'region__name', 'province__name', 'district__name', 'street')
    readonly_fields = ('created_at', 'updated_at')
    autocomplete_fields = ('country', 'region', 'province', 'district')
    list_editable = ('is_active',)
    
    fieldsets = (
        ('Información de la Dirección', {
            'fields': ('street', 'number', 'apartment', 'reference', 'postal_code')
        }),
        ('Ubicación Geográfica', {
            'fields': ('country', 'region', 'province', 'district')
        }),
        ('Coordenadas', {
            'fields': ('latitude', 'longitude'),
            'classes': ('collapse',)
        }),
        ('Información del Sistema', {
            'fields': ('is_active', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
