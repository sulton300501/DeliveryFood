from rest_framework import generics

from django.shortcuts import render  # noqa

from apps.services.models import Order, OrderDetails, Size, Topping
from apps.services.serializers import (
    OrderDetailSerializer,
    OrderSerializer,
    SizeSerializers,
    ToppingSerializer,
)


class SizeViews(generics.CreateAPIView):
    serializer_class = SizeSerializers
    queryset = Size.objects.all()


class SizeAllViews(generics.ListAPIView):
    serializer_class = SizeSerializers
    queryset = Size.objects.all()


class ToppingViews(generics.CreateAPIView):
    serializer_class = ToppingSerializer
    queryset = Topping.objects.all()


class ToppingAllViews(generics.ListAPIView):
    serializer_class = ToppingSerializer
    queryset = Topping.objects.all()


class OrderDetailViews(generics.CreateAPIView):
    serializer_class = OrderDetailSerializer
    queryset = OrderDetails.objects.all()


class OrderDetailAllViews(generics.ListAPIView):
    serializer_class = OrderDetailSerializer
    queryset = OrderDetails.objects.all()


class OrderViews(generics.CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderAllViews(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
