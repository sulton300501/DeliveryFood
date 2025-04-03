from rest_framework import serializers

from apps.services.models import Order, OrderDetails, Size, Topping


class SizeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ("id", "code", "price_adjustment")


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ("id", "name", "price")


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = ("id", "order", "food", "size", "topping", "quantity", "price")


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "user", "restourant", "total_price", "notes", "status", "payment_method")
