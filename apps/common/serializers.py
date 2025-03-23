from rest_framework import serializers
from sorl.thumbnail import get_thumbnail

from django.core.files.images import get_image_dimensions

from apps.common.models.model import Address, City, District


class ThumbnailImageSerializer(serializers.Serializer):
    def to_representation(self, image):
        try:
            width, height = get_image_dimensions(image)
            request = self.context["request"]
            return {
                "large": request.build_absolute_uri(
                    get_thumbnail(image, f"{int(width // 1.5)} x {int(height // 1.5)}", quality=99).url
                ),
                "medium": request.build_absolute_uri(
                    get_thumbnail(image, f"{int(width // 2)}x{int(height //2)}", quality=99).url
                ),
                "small": request.build_absolute_uri(
                    get_thumbnail(image, f"{int(width // 3)}x{int(height // 3)}", quality=99).url
                ),
            }
        except Exception as ex:
            print(ex)


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("id", "name")


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ("id", "name", "city")


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ("id", "name", "phone_number", "city", "detail_address")


class CityAllSerializer(serializers.ModelSerializer):
    district = serializers.SerializerMethodField()

    class Meta:
        model = City
        fields = ("id", "name", "district")

    def get_district(self, obj):
        get_district_option = District.objects.filter(city_id=obj.id)
        get_district = DistrictSerializer(get_district_option, many=True).data
        return get_district


class AddressAllSerializer(serializers.ModelSerializer):
    city = CityAllSerializer()

    class Meta:
        model = Address
        fields = ("id", "name", "phone_number", "city", "detail_address")
