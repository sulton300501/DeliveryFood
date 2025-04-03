from rest_framework import serializers

from apps.payments.models import UserCard  # noqa


class OrderTransactionSerializer(serializers.Serializer):
    card_id = serializers.UUIDField()
    logs = serializers.CharField()
