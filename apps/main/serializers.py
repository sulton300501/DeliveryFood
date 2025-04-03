from rest_framework import serializers

from apps.main.models import CategoryFood, Food, FoodReviews, MediaFile, Promo, Tags


class CategoryFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryFood
        fields = ("id", "name", "get_image", "order", "slug")


class MediaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ("id", "food", "title", "file")


class PromoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promo
        fields = ("id", "name", "discount_percent", "start_date", "end_date")


class FoodTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ("id", "name")


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = (
            "id",
            "name",
            "description",
            "category",
            "restourant",
            "base_price",
            "promo",
            "is_promo_active",
            "tags",
            "is_available",
            "slug",
        )


class FoodReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodReviews
        fields = (
            "id",
            "rating",
            "comment",
            "user",
            "food",
        )
