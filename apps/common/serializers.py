# from sorl.thumbnail import get_thumbnail
# from rest_framework import serializers
# from django.core.files.images import get_image_dimensions




# class ThumbnailImageSerializer(serializers.Serializer):
#     def to_representation(self, image):
#         try:
#             width , height = get_image_dimensions(image)
#             request = self.context["request"]
#             return {
#             "large": request.build_absolute_uri(
#                 get_thumbnail(image , f"{int(width // 1.5)} x {int(height // 1.5)}",quality=99).url
#             ),
#             "medium": request.build_absolute_uri(
#                 get_thumbnail(image , f"{int(width // 2 )}x{int(height // 2)}", quality=99).url
#             ),
#             "small": request.build_absolute_uri(
#                 get_thumbnail(image , f"{int(width // 3 )}x{int(height // 3)}", quality=99).url
#             )
#              }
#         except Exception as ex:
#             print(ex)
