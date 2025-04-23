from rest_framework import filters, generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import render  # noqa

from apps.aboutus.models import (
    CategoryRestourant,
    FavouriteRestaurant,
    Restourant,
    Reviews,
)
from apps.aboutus.serializers import (
    CategoryRestourantSerializer,
    FavouriteAllSerializer,
    FavouriteSerializer,
    RestourantALLSerializer,
    RestourantSerializer,
    ReviewsAllSerializer,
    ReviewsSerializer,
)


class SlugRetriewsAPIView(generics.RetrieveAPIView):
    lookup_field = "slug"
    lookup_url_kwarg = "slug"


class RestourantAPIView(generics.CreateAPIView):
    queryset = Restourant.objects.all()
    serializer_class = RestourantSerializer
    parser_classes = (JSONParser, FormParser, MultiPartParser)

    def get_queryset(self):
        return self.queryset.filter()


class RestourantAllAPIView(generics.ListAPIView):
    queryset = Restourant.objects.all()
    serializer_class = RestourantALLSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["name_uz", "name_ru"]

    def get_queryset(self):
        return self.queryset.filter(active=True)


class RestourantDetailView(SlugRetriewsAPIView):
    queryset = Restourant.objects.all()
    serializer_class = RestourantALLSerializer


class ReviewsAPIView(generics.CreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer


class ReviewsSingleAPIView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Reviews.objects.first()
        serializer = ReviewsSerializer(queryset, context={"request": request})
        return Response(serializer.data)


class ReviewsAllAPIView(generics.ListAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsAllSerializer


class CreateGategoryAPIView(generics.CreateAPIView):
    queryset = CategoryRestourant.objects.all()
    serializer_class = CategoryRestourantSerializer


class FavouriteRestourantAPIView(generics.CreateAPIView):
    queryset = FavouriteRestaurant.objects.all()
    serializer_class = FavouriteSerializer


class FavouriteAllRestourantAPIView(generics.ListAPIView):
    queryset = FavouriteRestaurant.objects.all()
    serializer_class = FavouriteAllSerializer


class GetDetailRestourantFavourite(generics.ListAPIView):
    queryset = FavouriteRestaurant.objects.all()
    serializer_class = FavouriteSerializer
