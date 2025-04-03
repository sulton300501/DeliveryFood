from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from .serializers import AddCardSerializer

from apps.payments.models import UserCard


class AddCardAPIView(CreateAPIView):

    queryset = UserCard.objects.all()
    serializer_class = AddCardSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @swagger_auto_schema(operation_summary="transaction")
    def get_queryset(self):
        return self.request.user.usercards.filter(is_deleted=False)
