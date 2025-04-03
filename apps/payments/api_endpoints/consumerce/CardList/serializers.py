from rest_framework import serializers

from apps.payments.models import UserCard


class CardListModelSerializer(serializers.ModelSerializer):
    card_number = serializers.SerializerMethodField()

    class Meta:
        model = UserCard
        fields = ("cardId", "user", "card_number", "expire_date", "provider", "is_active")

    def get_card_number(self, obj):
        return f"{obj.card_number[:4]} **** **** {obj.card_number[-4:]}" if obj.card_number else None
