from rest_framework import serializers

from apps.aboutus.models import (
    CategoryRestourant,
    FavouriteRestaurant,
    Restourant,
    Reviews,
)
from apps.common.serializers import ThumbnailImageSerializer
from apps.users.api_endpoints.Profile.serializers import ProfileSerializer


class RestourantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restourant
        fields = (
            "id",
            "name",
            "category",
            "description",
            "avatar",
            "cover_image",
            "address_id",
            "location_url",
            "working_hourse",
            "active",
        )


class RestourantALLSerializer(serializers.ModelSerializer):
    thumbnail_avatar = ThumbnailImageSerializer(source="avatar", read_only=True)
    thumbnail_image = ThumbnailImageSerializer(source="cover_image", read_only=True)
    avatar = serializers.ImageField(write_only=True)
    cover_image = serializers.ImageField(write_only=True)

    class Meta:
        model = Restourant
        fields = (
            "id",
            "name",
            "description",
            "category",
            "thumbnail_avatar",
            "thumbnail_image",
            "avatar",
            "cover_image",
            "address_id",
            "latitude",
            "longitude",
            "working_hourse",
        )


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ("id", "rating", "comment", "user", "restourant")


class ReviewsAllSerializer(serializers.ModelSerializer):
    user = ProfileSerializer()
    restourant = RestourantALLSerializer()

    class Meta:
        model = Reviews
        fields = ("id", "rating", "comment", "user", "restourant")


class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouriteRestaurant
        fields = ("id", "user", "restourant")


class CategoryRestourantSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryRestourant
        fields = ("id", "name", "order")


class FavouriteAllSerializer(serializers.ModelSerializer):
    user = ProfileSerializer()
    restourant = RestourantALLSerializer()

    class Meta:
        model = FavouriteRestaurant
        fields = ("id", "user", "restourant")
