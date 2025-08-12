import pytest
from django.urls import reverse
from Reflexo.models import Country

@pytest.mark.django_db
def test_list_countries(client):
    # Crear datos de prueba
    Country.objects.create(name="Peru", ubigeo_code="PE")
    Country.objects.create(name="Mexico", ubigeo_code="MX")

    # Ejecutar petición
    url = reverse("list_countries")
    response = client.get(url)

    # Validar respuesta
    assert response.status_code == 200
    data = response.json()

    # Solo deben aparecer países activos
    names = [country["name"] for country in data]
    assert "Peru" in names
    assert "Mexico" in names
    assert "Argentina" not in names
