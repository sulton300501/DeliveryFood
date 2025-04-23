import io

import pytest
from PIL import Image
from rest_framework import status
from rest_framework.test import APIClient

from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from apps.aboutus.models import Restourant
from apps.common.models.model import Address, City
from apps.users.models import User


@pytest.fixture
def fake_image():
    image = Image.new("RGB", (100, 100), color="red")
    buffer = io.BytesIO()
    image.save(buffer, format="JPEG")
    buffer.seek(0)

    return SimpleUploadedFile(name="test.jpg", content=buffer.getvalue(), content_type="image/jpeg")


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
def restourant_test(category, address):
    rest = Restourant.objects.create(
        name="Food",
        description="food desc",
        category=category,
        address_id=address,
        location_url="https://yandex.uz/maps/org/244997649299/?ll=69.221894%2C41.293430&z=16",
        orders_count=1,
        working_hourse="09:00 - 20:00",
        active=True,
        slug="food",
    )

    return rest


@pytest.mark.django_db
def test_restourant(category, address, fake_image):
    url = reverse("create-restourant")
    client = APIClient()

    data = {
        "name": "Food",
        "description": "food desc",
        "category": category.id,
        "address_id": address.id,
        "location_url": "https://yandex.uz/maps/org/244997649299/?ll=69.221894%2C41.293430&z=16",
        "orders_count": 1,
        "working_hourse": "09:00 - 20:00",
        "active": True,
    }

    # Fayllar va ma'lumotlar birga multipart formatda jo'natiladi
    response = client.post(url, data=data, format="json")

    print(response.data)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_get_all_restourant(restourant_test):
    url = reverse("all-restourant")

    client = APIClient()
    response = client.get(url, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, list)
    assert len(response.data) >= 1
    assert response.data[0]["name"] == restourant_test.name


@pytest.mark.django_db
def test_restourant_detail(restourant_test):
    url = reverse("get-single-restourant", kwargs={"slug": restourant_test.slug})

    client = APIClient()
    response = client.get(url, format="json")
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_reviews(user, restourant):
    url = reverse("create-review")
    data = {"rating": 3, "comment": "reviews test", "user": user.id, "restourant": restourant.id}

    client = APIClient()
    response = client.post(url, data, format="json")

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_get_single_review(api_client, reviews):
    url = reverse("single-review")

    response = api_client.get(url, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["comment"] == reviews.comment


@pytest.mark.django_db
def test_get_all_reviews(api_client, reviews):
    url = reverse("reviews-all")

    response = api_client.get(url, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, list)
    assert response.data[0]["comment"] == reviews.comment
    assert len(response.data) >= 1


@pytest.mark.django_db
def test_create_category():
    url = reverse("create-category")
    data = {"name": "food", "order": 1}

    client = APIClient()
    response = client.post(url, data, format="json")

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_favourite_restourant(user, restourant, api_client):
    url = reverse("create-favourite")
    data = {"user": user.id, "restourant": restourant.id}

    response = api_client.post(url, data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
