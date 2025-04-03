from rest_framework import permissions  # noqa
from rest_framework.generics import DestroyAPIView

from apps.payments.models import UserCard


class CardDeleteAPIView(DestroyAPIView):
    queryset = UserCard.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        # Agar Swagger tomonidan chaqirilgan bo'lsa
        if getattr(self, "swagger_fake_view", False):
            return UserCard.objects.none()  # Swagger uchun bo'sh queryset

        if self.request.user.is_anonymous:
            return UserCard.objects.none()  # Tizimga kirmagan foydalanuvchi uchun bo'sh queryset

        return self.request.user.usercards.filter(is_deleted=False)
