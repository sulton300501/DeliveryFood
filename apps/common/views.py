from rest_framework import generics

from django.shortcuts import render  # noqa

from . import serializers

from apps.common.models import model

# Create your views here.


class SlugRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "slug"
    lookup_url_kwarg = "slug"


class CityAPIView(generics.CreateAPIView):
    serializer_class = serializers.CitySerializer
    queryset = model.City.objects.all()


class DistrictAPIView(generics.CreateAPIView):
    serializer_class = serializers.DistrictSerializer
    queryset = model.District.objects.all()


class AddressAPIView(generics.CreateAPIView):
    serializer_class = serializers.AddressSerializer
    queryset = model.Address.objects.all()


class GetAllAddressAPIView(generics.ListAPIView):
    serializer_class = serializers.AddressAllSerializer
    queryset = model.Address.objects.all()


class CityUpdateView(generics.UpdateAPIView):
    queryset = model.City.objects.all()
    serializer_class = serializers.CitySerializer
    lookup_field = "id"


class CityDeleteView(generics.DestroyAPIView):
    queryset = model.City.objects.all()
    serializer_class = serializers.CitySerializer
    lookup_field = "id"
