import pytest
from rest_framework import status
from rest_framework.test import APIClient

from django.urls import reverse

from apps.common.models.model import Address, City


@pytest.fixture
def city():
    return City.objects.create(name="Toshkent")


@pytest.fixture
def address(city):
    return Address.objects.create(name="Main St", phone_number="+998997878876", city=city, detail_address="Uzbekistan")


@pytest.mark.django_db
def test_create_city():
    url = reverse("create-city")
    data = {"name": "Chilonzor"}

    client = APIClient()
    response = client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert "id" in response.data


@pytest.mark.django_db
def test_create_address(city):
    url = reverse("create-address")  # Ensure this matches the name in your urls.py
    data = {"name": "Main St", "phone_number": "+998997878876", "city": city.id, "detail_address": "Uzbekistan"}
    client = APIClient()
    response = client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert "id" in response.data


@pytest.mark.django_db
def test_create_district(city):
    url = reverse("create-district")
    data = {"name": "Toshkent", "city": city.id}

    client = APIClient()
    response = client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert "id" in response.data


@pytest.mark.django_db
def test_get_all_address(address):
    url = reverse("getAll-address")

    client = APIClient()
    response = client.get(url, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, list)
    assert len(response.data) >= 1
    assert response.data[0]["name"] == address.name


@pytest.mark.django_db
def test_city_update(city):
    url = reverse("update-city", kwargs={"id": city.id})
    update_date = {"name": "Yakkasaroy"}

    client = APIClient()
    response = client.put(url, update_date, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == "Yakkasaroy"


@pytest.mark.django_db
def test_delete_city(city):
    url = reverse("delete-city", kwargs={"id": city.id})

    client = APIClient()
    response = client.delete(url, format="json")

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not City.objects.filter(id=city.id).exists()
