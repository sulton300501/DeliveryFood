import pytest
from rest_framework import status

from django.urls import reverse


@pytest.mark.django_db
def test_create_room(api_client, test_room):
    url = reverse("room-list-create")
    data = {"room_name": "python"}

    response = api_client.post(url, data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert len(response.data) >= 1


@pytest.mark.django_db
def test_create_message(api_client, test_message, test_room):
    url = reverse("message-list-create")
    data = {"room": test_room.id, "sender": "Sulton", "message": "Hello"}

    response = api_client.post(url, data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert len(response.data) >= 1
