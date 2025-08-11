from django.shortcuts import render
from django.http import JsonResponse
from Reflexo.models import Country, Region, Province, District

def home_view(request):
    """Vista para la página principal"""
    return render(request, 'home.html')

def debug_view(request):
    """Vista de depuración para verificar el estado de la base de datos"""
    context = {
        'regions_count': Region.objects.count(),
        'provinces_count': Province.objects.count(),
        'districts_count': District.objects.count(),
        'countries_count': Country.objects.count(),
        'regions_with_ubigeo': Region.objects.filter(ubigeo_code__isnull=False).count(),
        'provinces_with_ubigeo': Province.objects.filter(ubigeo_code__isnull=False).count(),
        'districts_with_ubigeo': District.objects.filter(ubigeo_code__isnull=False).count(),
        'sample_regions': list(Region.objects.all()[:5].values('id', 'name', 'ubigeo_code')),
        'sample_provinces': list(Province.objects.all()[:5].values('id', 'name', 'ubigeo_code', 'region__name')),
        'sample_districts': list(District.objects.all()[:5].values('id', 'name', 'ubigeo_code', 'province__name')),
    }
    return render(request, 'debug.html', context)

def countries_view(request):
    """Vista para mostrar países"""
    countries = Country.objects.all()
    return render(request, 'countries.html', {'countries': countries})

def regions_view(request):
    """Vista para mostrar regiones"""
    regions = Region.objects.filter(deleted_at__isnull=True)
    # Agregar información de depuración
    print(f"Regiones encontradas: {regions.count()}")
    for region in regions:
        print(f"Región: {region.id} - {region.name}")
    return render(request, 'regions.html', {'regions': regions})

def provinces_view(request):
    """Vista para mostrar provincias"""
    provinces = Province.objects.all()
    regions = Region.objects.filter(deleted_at__isnull=True)
    # Agregar información de depuración
    print(f"Provincias encontradas: {provinces.count()}")
    for province in provinces:
        print(f"Provincia: {province.id} - {province.name}")
    return render(request, 'provinces.html', {
        'provinces': provinces,
        'regions': regions
    })

def districts_view(request):
    """Vista para mostrar distritos"""
    districts = District.objects.all()
    provinces = Province.objects.all()
    # Agregar información de depuración
    print(f"Distritos encontrados: {districts.count()}")
    for district in districts:
        print(f"Distrito: {district.id} - {district.name}")
    return render(request, 'districts.html', {
        'districts': districts,
        'provinces': provinces
    })

# API endpoints para AJAX
def api_countries(request):
    """API endpoint para países"""
    countries = Country.objects.values('id', 'name', 'phone_code', 'ISO2')
    return JsonResponse(list(countries), safe=False)

def api_regions(request):
    """API endpoint para regiones"""
    regions = Region.objects.filter(deleted_at__isnull=True).values('id', 'name')
    return JsonResponse(list(regions), safe=False)

def api_provinces(request):
    """API endpoint para provincias"""
    provinces = Province.objects.values('id', 'name', 'region__name')
    return JsonResponse(list(provinces), safe=False)

def api_districts(request):
    """API endpoint para distritos"""
    districts = District.objects.values('id', 'name', 'province__name')
    return JsonResponse(list(districts), safe=False)




