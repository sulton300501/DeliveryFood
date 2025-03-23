from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(required=True)
    avatar = serializers.ImageField(required=False)
    address_id = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    gender = serializers.CharField()

    class Meta:
        model = User
        fields = (
            "full_name",
            "avatar",
            "address_id",
            "phone_number",
            "email",
            "gender",
        )
