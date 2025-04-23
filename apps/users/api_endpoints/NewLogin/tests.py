import pytest

from django.core.cache import cache

from .serializers import NewLoginSerializer

from apps.users.models import User


@pytest.fixture
def phone_number():
    return "998997876767"


@pytest.mark.django_db
def test_send_cache_code_first(phone_number):
    cache.delete(f"otp_{phone_number}")

    serializer = NewLoginSerializer(data={"phone_number": phone_number})
    assert serializer.is_valid()

    result = serializer.save()

    assert result["message"] == "OTP key send successfully"
    assert cache.get(f"otp_{phone_number}") is not None
    assert User.objects.filter(phone_number=phone_number).exists()


@pytest.mark.django_db
def test_send_cache_code_twice(phone_number):
    otp_code = 123456
    cache.set(f"otp_{phone_number}", otp_code, 60)

    serializer = NewLoginSerializer(data={"phone_number": phone_number})
    assert serializer.is_valid()

    with pytest.raises(Exception) as exc_info:
        serializer.save()

    assert "already send code" in str(exc_info)
