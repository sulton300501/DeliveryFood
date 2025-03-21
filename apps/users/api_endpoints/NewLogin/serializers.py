# from rest_framework import serializers
# import random
# from django.core.cache import cache
# from django.core.exceptions import ValidationError
# from django.contrib.auth import get_user_model


# User = get_user_model()



# class NewLoginSerializer(serializers.Serializer):
#     phone_number = serializers.CharField()

#     def create(self, validated_data):
#         phone_number = validated_data['phone_number']
#         otp_first_code = random.randint(100000 , 999999)
#         print(otp_first_code)
#         otp_first_key = f"otp_{phone_number}"

#         otp_get_key = cache.get(otp_first_key)

#         if otp_first_key:
#             raise ValidationError(
#                {
#                 "error":"already send code",
#                 "message":"We have already send"
#                }
#             )

#         User.objects.get_or_create(phone_number=phone_number , username=phone_number)
#         cache.set(otp_first_key , otp_first_code , 60)

#         return {"message":"OTP key send successfully"}
