import pytest

from django.contrib.auth import get_user_model
from django.core.cache import cache

from .serializers import NewLoginConfirmSerializers

User = get_user_model()


@pytest.mark.django_db
def test_cache_code_otp_token():
    phone = "+998997574688"
    code = "111111"

    cache.set(f"otp_{phone}", code)

    serializer = NewLoginConfirmSerializers(data={"phone_number": phone, "code": code})

    assert serializer.is_valid()
    data = serializer.save()

    assert data["message"] == "Login Successfully"
    assert "access" in data["token"]
    assert "refresh" in data["token"]

    user = User.objects.get(phone_number=phone)
    assert user.username == phone
