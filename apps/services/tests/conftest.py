import pytest
from rest_framework.test import APIClient

from apps.services.models import Order, OrderDetails, Size, Topping


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def test_size():
    data = Size.objects.create(code="S", price_adjustment=12)

    return data


@pytest.fixture
def test_topping():
    data = Topping.objects.create(name="topping name", price=123)
    return data


@pytest.fixture
def test_order(user, restourant):
    data = Order.objects.create(
        user=user, restourant=restourant, total_price=123, notes="hello world", status="pending", payment_method="cash"
    )

    return data


@pytest.fixture
def test_order_detail(test_order, food_test, test_size, test_topping):
    data = OrderDetails.objects.create(
        order=test_order, food=food_test, size=test_size, topping=test_topping, quantity=12, price=123
    )

    return data
