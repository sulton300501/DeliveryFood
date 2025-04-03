from rest_framework import permissions
from rest_framework.generics import ListAPIView

from .serializers import CardListModelSerializer

from apps.payments.models import UserCard


class CardListAPIView(ListAPIView):
    queryset = UserCard.objects.all()
    serializer_class = CardListModelSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.usercards.filter(is_deleted=False)
