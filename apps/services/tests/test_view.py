import pytest
from rest_framework import status

from django.urls import reverse


@pytest.mark.django_db
def test_size_view(api_client, test_size):
    url = reverse("create-size")

    data = {"code": "S", "price_adjustment": 12}

    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert len(response.data) >= 1


@pytest.mark.django_db
def test_size_all_view(api_client, test_size):
    url = reverse("all-size")

    response = api_client.get(url, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, list)


@pytest.mark.django_db
def test_topping_view(api_client, test_topping):
    url = reverse("create-topping")

    data = {"name": "barg", "price": 12}

    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert len(response.data) >= 1


@pytest.mark.django_db
def test_topping_all_view(api_client, test_topping):
    url = reverse("all-topping")

    response = api_client.get(url, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, list)


@pytest.mark.django_db
def test_order_view(api_client, test_order, user, restourant):
    url = reverse("create-order")
    data = {
        "user": user.id,
        "restourant": restourant.id,
        "total_price": 123,
        "notes": "Hey Hello",
        "status": "pending",
        "payment_method": "cash",
    }

    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert len(response.data) >= 1


@pytest.mark.django_db
def test_order_all_view(api_client, test_topping):
    url = reverse("all-order")

    response = api_client.get(url, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, list)


@pytest.mark.django_db
def test_order_detail_view(api_client, test_order, test_size, test_topping, food_test):
    url = reverse("order-detail")
    data = {
        "order": test_order.id,
        "food": food_test.id,
        "size": test_size.id,
        "topping": test_topping.id,
        "quantity": 12,
        "price": 1234,
    }

    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert len(response.data) >= 1


@pytest.mark.django_db
def test_order_detail_all_view(api_client, test_order_detail):
    url = reverse("all-order-detail")

    response = api_client.get(url, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, list)
    assert len(response.data) >= 1
