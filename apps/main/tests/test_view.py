import pytest
from rest_framework import status

from django.urls import reverse


@pytest.mark.django_db
def test_category_food(category_food, api_client):
    url = reverse("create-category-food")

    data = {"name": "burger", "order": 1, "slug": "food"}

    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_all_category_food(api_client, category_food):
    url = reverse("all-food-category")

    response = api_client.get(url, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, list)
    assert len(response.data) >= 1


@pytest.mark.django_db
def test_promo_food(api_client):
    url = reverse("create-promo")

    data = {"name": "hegdj334", "discount_percent": 13}

    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_all_promo_food(api_client, promo_test):
    url = reverse("all-promo")

    response = api_client.get(url, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, list)
    assert len(response.data) >= 1
