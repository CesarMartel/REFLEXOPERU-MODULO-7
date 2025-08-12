from django.http import JsonResponse
from Reflexo.models import Country

def list_countries(request):
    countries = Country.objects.values('id', 'name', 'ubigeo_code')
    return JsonResponse(list(countries), safe=False)
