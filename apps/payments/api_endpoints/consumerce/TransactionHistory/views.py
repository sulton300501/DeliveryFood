from rest_framework import permissions
from rest_framework.generics import ListAPIView

from .serializers import TransactionHistorySerializer

from apps.payments.models import Transaction


class TransactionHistoryAPIView(ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionHistorySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
