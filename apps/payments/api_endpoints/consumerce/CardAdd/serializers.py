from datetime import datetime

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.payments.models import UserCard


class AddCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCard
        fields = ("card_number", "expire_date", "cvv")

    def validate_card_number(self, number):
        if len(number) != 16 or not number.isdigit():
            raise ValidationError({"error": "Card numbers must be 16 digit"})
        return number

    def validate_expire_date(self, date):
        if len(date) != 4 or not date.isdigit():
            raise ValidationError({"error": "Expire date must be XXYY"})

        month = int(date[:2])
        year = int(f"20{date[2:]}")
        now = datetime.now()
        if month < 1 or month > 12 or (year < now.year or (year == now.year and month < now.year)):
            raise ValidationError({"error": "Card is expired"})
        return date

    def validate_cvv(self, value):
        if not value:
            return value
        if len(value) < 3 or not value.isdigit():
            raise ValidationError({"error": "CVV must be 3 digits"})
        return value

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
