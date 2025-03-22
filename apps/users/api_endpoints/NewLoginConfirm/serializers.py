from django.contrib.auth import get_user_model
from django.core.cache import cache
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .utils import get_tokens_for_user

User = get_user_model()


class NewLoginConfirmSerializers(serializers.Serializer):
    phone_number = serializers.CharField()
    code = serializers.CharField()

    def create(self, validated_data):
        phone_number = validated_data["phone_number"]
        code = validated_data["code"]

        otp_get_key = f"otp_{phone_number}"
        otp_cache_code = cache.get(otp_get_key)

        if not otp_cache_code:
            raise ValidationError({"error": "Error", "message": "Message error"})

        if str(otp_cache_code) != code:
            raise ValidationError({"error": "Invalid code", "message": "The OTP code is invalid"})

        user, created = User.objects.get_or_create(phone_number=phone_number, username=phone_number)

        token = get_tokens_for_user(user)

        return {"message": "Login Successfully", "token": token}
