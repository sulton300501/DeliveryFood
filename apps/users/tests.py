import pytest

from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_contact_create():
    user = User.objects.create(full_name="Sulton", phone_number="+998998789876", email="sulton@gmail.com")

    assert user.phone_number == "+998998789876"
    assert user.email == "sulton@gmail.com"
