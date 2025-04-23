import pytest
from rest_framework.test import APIClient

from apps.aboutus.models import CategoryRestourant, Restourant, Reviews
from apps.common.models.model import Address, City
from apps.users.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def city():
    return City.objects.create(name="Toshkent")


@pytest.fixture
def address(city):
    address = Address.objects.create(
        name="Yakkasaroy", phone_number="+998997786687", city=city, detail_address="Bunyodkor"
    )
    return address


@pytest.fixture
def reviews(user, restourant):
    reviews = Reviews.objects.create(rating=3, comment="hello", user=user, restourant=restourant)
    return reviews


@pytest.fixture
def category():
    return CategoryRestourant.objects.create(name="fast", order=1)


@pytest.fixture
def user(address):
    return User.objects.create(
        full_name="sulton malik",
        phone_number="+998998478877",
        email="sulton@gmail.com",
        address_id=address,
        gender="male",
    )


@pytest.fixture
def restourant(user, category, address):
    res = Restourant.objects.create(
        name="Food",
        description="food desc",
        category=category,
        address_id=address,
        location_url="https://yandex.uz/maps/org/244997649299/?ll=69.221894%2C41.293430&z=16",
        orders_count=1,
        working_hourse=" 09:00 - 20:00",
    )
    return res
