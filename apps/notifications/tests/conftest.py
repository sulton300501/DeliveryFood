import pytest
from rest_framework.test import APIClient

from apps.notifications.models import Message, Room


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def test_room():
    data = Room.objects.create(room_name="room")

    return data


@pytest.fixture
def test_message(test_room):
    data = Message.objects.create(room=test_room, sender="Sulton", message="xabar")

    return data
