from rest_framework import generics
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from django.core.exceptions import ObjectDoesNotExist
from django.http import FileResponse
from django.shortcuts import render  # noqa

from .filter import FoodFilter

from apps.main.models import CategoryFood, Food, FoodReviews, MediaFile, Promo, Tags
from apps.main.serializers import (
    CategoryFoodSerializer,
    FoodReviewsSerializer,
    FoodSerializer,
    FoodTagSerializer,
    MediaFileSerializer,
    PromoSerializer,
)


class SlugRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "slug"
    lookup_url_kwarg = "slug"


class CategoryFoodAPIView(generics.CreateAPIView):
    serializer_class = CategoryFoodSerializer
    queryset = CategoryFood.objects.all()


class CategoryFoodAllView(generics.ListAPIView):
    queryset = CategoryFood.objects.all()
    serializer_class = CategoryFoodSerializer


# class CategoryDetailView(SlugRetrieveAPIView):
#     queryset = CategoryFood.objects.all()
#     serializer_class = CategoryFoodSerializer


class MediaFileView(generics.CreateAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileSerializer
    parser_classes = (MultiPartParser, FormParser)


class MediaFileALLView(generics.ListAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileSerializer


class PromoView(generics.CreateAPIView):
    queryset = Promo.objects.all()
    serializer_class = PromoSerializer


class PromoAllView(generics.ListAPIView):
    queryset = Promo.objects.all()
    serializer_class = PromoSerializer


class FoodView(generics.CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodALLView(APIView):
    def get(self, request, slug):
        response = {}
        try:
            document = MediaFile.objects.filter(food__slug=slug)
            document_serializer = MediaFileSerializer(document, many=True, context={"request": request})
            response["document"] = document_serializer.data
        except ObjectDoesNotExist:
            pass

        return Response(response)


class MediaUploadFile(generics.RetrieveAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        file_path = instance.file.path
        file_name = instance.file.name
        response = FileResponse(open(file_path, "rb"))
        response["Content-Disposition"] = "attachment; filename=%s" % file_name
        return response


class FoodReviewsView(generics.CreateAPIView):
    queryset = FoodReviews.objects.all()
    serializer_class = FoodReviewsSerializer


class FoodAllReviewsView(generics.ListAPIView):
    queryset = FoodReviews.objects.all()
    serializer_class = FoodReviewsSerializer
    filterset_class = FoodFilter


class FoodTagView(generics.CreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = FoodTagSerializer
