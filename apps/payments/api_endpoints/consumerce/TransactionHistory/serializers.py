from rest_framework import serializers

from apps.payments.models import Transaction


class TransactionHistorySerializer(serializers.ModelSerializer):
    order = serializers.CharField(source="order.id")

    class Meta:
        model = Transaction
        fields = ("user", "card", "amount", "order", "status")
