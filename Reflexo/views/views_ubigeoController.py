from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from Reflexo.models import Region, Province, District, Country
import json

# ============================================================================
# ENDPOINTS PARA REGIONES
# ============================================================================

@require_http_methods(["GET"])
def regions(request):
    """Listar todas las regiones"""
    try:
        regions = Region.objects.filter(deleted_at__isnull=True).values(
            'id', 'name', 'ubigeo_code', 'created_at', 'updated_at'
        )
        return JsonResponse({
            'success': True,
            'data': list(regions),
            'count': len(regions)
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@require_http_methods(["GET"])
def region_detail(request, region_id):
    """Obtener una región específica"""
    try:
        region = Region.objects.filter(id=region_id, deleted_at__isnull=True).values(
            'id', 'name', 'ubigeo_code', 'created_at', 'updated_at'
        ).first()
        
        if not region:
            return JsonResponse({
                'success': False,
                'error': 'Región no encontrada'
            }, status=404)
        
        return JsonResponse({
            'success': True,
            'data': region
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def region_create(request):
    """Crear una nueva región"""
    try:
        data = json.loads(request.body)
        name = data.get('name')
        ubigeo_code = data.get('ubigeo_code')
        
        if not name:
            return JsonResponse({
                'success': False,
                'error': 'El nombre es obligatorio'
            }, status=400)
        
        # Validar que el código de ubigeo sea único
        if ubigeo_code and Region.objects.filter(ubigeo_code=ubigeo_code).exists():
            return JsonResponse({
                'success': False,
                'error': 'El código de ubigeo ya existe'
            }, status=400)
        
        region = Region.objects.create(
            name=name,
            ubigeo_code=ubigeo_code
        )
        
        return JsonResponse({
            'success': True,
            'data': {
                'id': region.id,
                'name': region.name,
                'ubigeo_code': region.ubigeo_code,
                'created_at': region.created_at,
                'updated_at': region.updated_at
            },
            'message': 'Región creada exitosamente'
        }, status=201)
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'JSON inválido'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@csrf_exempt
@require_http_methods(["PUT"])
def region_update(request, region_id):
    """Actualizar una región"""
    try:
        data = json.loads(request.body)
        region = Region.objects.filter(id=region_id, deleted_at__isnull=True).first()
        
        if not region:
            return JsonResponse({
                'success': False,
                'error': 'Región no encontrada'
            }, status=404)
        
        # Actualizar campos
        if 'name' in data:
            region.name = data['name']
        if 'ubigeo_code' in data:
            # Validar que el código sea único
            if Region.objects.filter(ubigeo_code=data['ubigeo_code']).exclude(id=region_id).exists():
                return JsonResponse({
                    'success': False,
                    'error': 'El código de ubigeo ya existe'
                }, status=400)
            region.ubigeo_code = data['ubigeo_code']
        
        region.save()
        
        return JsonResponse({
            'success': True,
            'data': {
                'id': region.id,
                'name': region.name,
                'ubigeo_code': region.ubigeo_code,
                'created_at': region.created_at,
                'updated_at': region.updated_at
            },
            'message': 'Región actualizada exitosamente'
        })
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'JSON inválido'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@csrf_exempt
@require_http_methods(["DELETE"])
def region_delete(request, region_id):
    """Eliminar una región (soft delete)"""
    try:
        region = Region.objects.filter(id=region_id, deleted_at__isnull=True).first()
        
        if not region:
            return JsonResponse({
                'success': False,
                'error': 'Región no encontrada'
            }, status=404)
        
        # Verificar que no tenga provincias asociadas
        if region.provinces.exists():
            return JsonResponse({
                'success': False,
                'error': 'No se puede eliminar una región que tiene provincias asociadas'
            }, status=400)
        
        region.delete()  # Soft delete
        
        return JsonResponse({
            'success': True,
            'message': 'Región eliminada exitosamente'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

# ============================================================================
# ENDPOINTS PARA PROVINCIAS
# ============================================================================

@require_http_methods(["GET"])
def provinces(request, region_id=None):
    """Listar provincias (opcionalmente filtradas por región)"""
    try:
        if region_id:
            provinces = Province.objects.filter(
                region_id=region_id
            ).values(
                'id', 'name', 'ubigeo_code', 'region__name', 'created_at', 'updated_at'
            )
        else:
            provinces = Province.objects.all().values(
                'id', 'name', 'ubigeo_code', 'region__name', 'created_at', 'updated_at'
            )
        
        return JsonResponse({
            'success': True,
            'data': list(provinces),
            'count': len(provinces)
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@require_http_methods(["GET"])
def province_detail(request, province_id):
    """Obtener una provincia específica"""
    try:
        province = Province.objects.filter(id=province_id).values(
            'id', 'name', 'ubigeo_code', 'region__name', 'region__id', 'created_at', 'updated_at'
        ).first()
        
        if not province:
            return JsonResponse({
                'success': False,
                'error': 'Provincia no encontrada'
            }, status=404)
        
        return JsonResponse({
            'success': True,
            'data': province
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def province_create(request):
    """Crear una nueva provincia"""
    try:
        data = json.loads(request.body)
        name = data.get('name')
        region_id = data.get('region_id')
        ubigeo_code = data.get('ubigeo_code')
        
        if not name or not region_id:
            return JsonResponse({
                'success': False,
                'error': 'El nombre y la región son obligatorios'
            }, status=400)
        
        # Verificar que la región existe
        try:
            region = Region.objects.get(id=region_id, deleted_at__isnull=True)
        except Region.DoesNotExist:
            return JsonResponse({
                'success': False,
                'error': 'La región especificada no existe'
            }, status=400)
        
        # Validar que el código de ubigeo sea único
        if ubigeo_code and Province.objects.filter(ubigeo_code=ubigeo_code).exists():
            return JsonResponse({
                'success': False,
                'error': 'El código de ubigeo ya existe'
            }, status=400)
        
        province = Province.objects.create(
            name=name,
            region=region,
            ubigeo_code=ubigeo_code
        )
        
        return JsonResponse({
            'success': True,
            'data': {
                'id': province.id,
                'name': province.name,
                'ubigeo_code': province.ubigeo_code,
                'region__name': province.region.name,
                'created_at': province.created_at,
                'updated_at': province.updated_at
            },
            'message': 'Provincia creada exitosamente'
        }, status=201)
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'JSON inválido'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@csrf_exempt
@require_http_methods(["PUT"])
def province_update(request, province_id):
    """Actualizar una provincia"""
    try:
        data = json.loads(request.body)
        province = Province.objects.filter(id=province_id).first()
        
        if not province:
            return JsonResponse({
                'success': False,
                'error': 'Provincia no encontrada'
            }, status=404)
        
        # Actualizar campos
        if 'name' in data:
            province.name = data['name']
        if 'region_id' in data:
            try:
                region = Region.objects.get(id=data['region_id'], deleted_at__isnull=True)
                province.region = region
            except Region.DoesNotExist:
                return JsonResponse({
                    'success': False,
                    'error': 'La región especificada no existe'
                }, status=400)
        if 'ubigeo_code' in data:
            # Validar que el código sea único
            if Province.objects.filter(ubigeo_code=data['ubigeo_code']).exclude(id=province_id).exists():
                return JsonResponse({
                    'success': False,
                    'error': 'El código de ubigeo ya existe'
                }, status=400)
            province.ubigeo_code = data['ubigeo_code']
        
        province.save()
        
        return JsonResponse({
            'success': True,
            'data': {
                'id': province.id,
                'name': province.name,
                'ubigeo_code': province.ubigeo_code,
                'region__name': province.region.name,
                'created_at': province.created_at,
                'updated_at': province.updated_at
            },
            'message': 'Provincia actualizada exitosamente'
        })
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'JSON inválido'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@csrf_exempt
@require_http_methods(["DELETE"])
def province_delete(request, province_id):
    """Eliminar una provincia"""
    try:
        province = Province.objects.filter(id=province_id).first()
        
        if not province:
            return JsonResponse({
                'success': False,
                'error': 'Provincia no encontrada'
            }, status=404)
        
        # Verificar que no tenga distritos asociados
        if province.districts.exists():
            return JsonResponse({
                'success': False,
                'error': 'No se puede eliminar una provincia que tiene distritos asociados'
            }, status=400)
        
        province.delete()
        
        return JsonResponse({
            'success': True,
            'message': 'Provincia eliminada exitosamente'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

# ============================================================================
# ENDPOINTS PARA DISTRITOS
# ============================================================================

@require_http_methods(["GET"])
def districts(request, province_id=None):
    """Listar distritos (opcionalmente filtrados por provincia)"""
    try:
        if province_id:
            districts = District.objects.filter(
                province_id=province_id
            ).values(
                'id', 'name', 'ubigeo_code', 'province__name', 'created_at', 'updated_at'
            )
        else:
            districts = District.objects.all().values(
                'id', 'name', 'ubigeo_code', 'province__name', 'created_at', 'updated_at'
            )
        
        return JsonResponse({
            'success': True,
            'data': list(districts),
            'count': len(districts)
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@require_http_methods(["GET"])
def district_detail(request, district_id):
    """Obtener un distrito específico"""
    try:
        district = District.objects.filter(id=district_id).values(
            'id', 'name', 'ubigeo_code', 'province__name', 'province__id', 'created_at', 'updated_at'
        ).first()
        
        if not district:
            return JsonResponse({
                'success': False,
                'error': 'Distrito no encontrado'
            }, status=404)
        
        return JsonResponse({
            'success': True,
            'data': district
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def district_create(request):
    """Crear un nuevo distrito"""
    try:
        data = json.loads(request.body)
        name = data.get('name')
        province_id = data.get('province_id')
        ubigeo_code = data.get('ubigeo_code')
        
        if not name or not province_id:
            return JsonResponse({
                'success': False,
                'error': 'El nombre y la provincia son obligatorios'
            }, status=400)
        
        # Verificar que la provincia existe
        try:
            province = Province.objects.get(id=province_id)
        except Province.DoesNotExist:
            return JsonResponse({
                'success': False,
                'error': 'La provincia especificada no existe'
            }, status=400)
        
        # Validar que el código de ubigeo sea único
        if ubigeo_code and District.objects.filter(ubigeo_code=ubigeo_code).exists():
            return JsonResponse({
                'success': False,
                'error': 'El código de ubigeo ya existe'
            }, status=400)
        
        district = District.objects.create(
            name=name,
            province=province,
            ubigeo_code=ubigeo_code
        )
        
        return JsonResponse({
            'success': True,
            'data': {
                'id': district.id,
                'name': district.name,
                'ubigeo_code': district.ubigeo_code,
                'province__name': district.province.name,
                'created_at': district.created_at,
                'updated_at': district.updated_at
            },
            'message': 'Distrito creado exitosamente'
        }, status=201)
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'JSON inválido'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@csrf_exempt
@require_http_methods(["PUT"])
def district_update(request, district_id):
    """Actualizar un distrito"""
    try:
        data = json.loads(request.body)
        district = District.objects.filter(id=district_id).first()
        
        if not district:
            return JsonResponse({
                'success': False,
                'error': 'Distrito no encontrado'
            }, status=404)
        
        # Actualizar campos
        if 'name' in data:
            district.name = data['name']
        if 'province_id' in data:
            try:
                province = Province.objects.get(id=data['province_id'])
                district.province = province
            except Province.DoesNotExist:
                return JsonResponse({
                    'success': False,
                    'error': 'La provincia especificada no existe'
                }, status=400)
        if 'ubigeo_code' in data:
            # Validar que el código sea único
            if District.objects.filter(ubigeo_code=data['ubigeo_code']).exclude(id=district_id).exists():
                return JsonResponse({
                    'success': False,
                    'error': 'El código de ubigeo ya existe'
                }, status=400)
            district.ubigeo_code = data['ubigeo_code']
        
        district.save()
        
        return JsonResponse({
            'success': True,
            'data': {
                'id': district.id,
                'name': district.name,
                'ubigeo_code': district.ubigeo_code,
                'province__name': district.province.name,
                'created_at': district.created_at,
                'updated_at': district.updated_at
            },
            'message': 'Distrito actualizado exitosamente'
        })
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'JSON inválido'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@csrf_exempt
@require_http_methods(["DELETE"])
def district_delete(request, district_id):
    """Eliminar un distrito"""
    try:
        district = District.objects.filter(id=district_id).first()
        
        if not district:
            return JsonResponse({
                'success': False,
                'error': 'Distrito no encontrado'
            }, status=404)
        
        district.delete()
        
        return JsonResponse({
            'success': True,
            'message': 'Distrito eliminado exitosamente'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

# ============================================================================
# ENDPOINTS PARA PAÍSES (mantener compatibilidad)
# ============================================================================

@require_http_methods(["GET"])
def countries(request):
    """Listar todos los países"""
    try:
        countries = Country.objects.all().values('id', 'name', 'phone_code', 'ISO2')
        return JsonResponse(list(countries), safe=False)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def country_create(request):
    """Crear un nuevo país"""
    try:
        data = json.loads(request.body)
        name = data.get('name')
        ubigeo_code = data.get('ubigeo_code')
        
        if not name:
            return JsonResponse({
                'success': False,
                'error': 'El nombre es obligatorio'
            }, status=400)
        
        # Validar que el código de ubigeo sea único
        if ubigeo_code and Country.objects.filter(ubigeo_code=ubigeo_code).exists():
            return JsonResponse({
                'success': False,
                'error': 'El código de ubigeo ya existe'
            }, status=400)
        
        country = Country.objects.create(
            name=name,
            ubigeo_code=ubigeo_code
        )
        
        return JsonResponse({
            'success': True,
            'data': {
                'id': country.id,
                'name': country.name,
                'ubigeo_code': country.ubigeo_code,
                'created_at': country.created_at,
                'updated_at': country.updated_at
            },
            'message': 'País creado exitosamente'
        }, status=201)
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'JSON inválido'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@csrf_exempt
@require_http_methods(["PUT"])
def country_update(request, country_id):
    """Actualizar un país"""
    try:
        data = json.loads(request.body)
        country = Country.objects.get(id=country_id)
        
        # Actualizar campos
        if 'name' in data:
            country.name = data['name']
        if 'ubigeo_code' in data:
            # Validar que el código sea único si se proporciona
            if data['ubigeo_code'] and Country.objects.filter(ubigeo_code=data['ubigeo_code']).exclude(id=country_id).exists():
                return JsonResponse({
                    'success': False,
                    'error': 'El código de ubigeo ya existe'
                }, status=400)
            country.ubigeo_code = data['ubigeo_code']
        
        country.save()
        
        return JsonResponse({
            'success': True,
            'data': {
                'id': country.id,
                'name': country.name,
                'ubigeo_code': country.ubigeo_code,
                'created_at': country.created_at,
                'updated_at': country.updated_at
            },
            'message': 'País actualizado exitosamente'
        })
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'JSON inválido'
        }, status=400)
    except Country.DoesNotExist:
        return JsonResponse({
            'success': False,
            'error': 'País no encontrado'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

@csrf_exempt
@require_http_methods(["DELETE"])
def country_delete(request, country_id):
    """Eliminar un país"""
    try:
        country = Country.objects.get(id=country_id)
        country.delete()
        
        return JsonResponse({
            'success': True,
            'message': 'País eliminado exitosamente'
        })
    except Country.DoesNotExist:
        return JsonResponse({
            'success': False,
            'error': 'País no encontrado'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)