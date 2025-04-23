import pytest

from apps.common.models.model import Address, City, District


@pytest.mark.django_db
def test_city():
    city = City.objects.create(name="Toshkent")

    assert city.name == "Toshkent"


@pytest.fixture
def city():
    return City.objects.create(name="Toshkent")


@pytest.mark.django_db
def test_district(city):

    district = District.objects.create(name="Chilonzor", city=city)

    assert district.name == "Chilonzor"
    assert district.city == city


@pytest.mark.django_db
def test_address(city):
    address = Address.objects.create(
        name="Yakkasaroy", phone_number="+998997786687", city=city, detail_address="Bunyodkor"
    )

    assert address.phone_number == "+998997786687"
    assert address.city == city
