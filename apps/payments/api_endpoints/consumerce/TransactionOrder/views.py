from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import OrderTransactionSerializer

from apps.aboutus.models import Restourant
from apps.payments.models import Transaction, UserCard
from apps.services.models import Order


class OrderTransactionAPIView(GenericAPIView):
    serializer_class = OrderTransactionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    # 👉 Swagger uchun "fake" queryset
    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Order.objects.none()
        return super().get_queryset()

    def post(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

        data = self.serializer_class(data=request.data)
        if not data.is_valid():
            return Response({"message": "Error"}, status=status.HTTP_400_BAD_REQUEST)

        user = request.user
        card_id = data.validated_data.get("card_id")
        logs = data.validated_data.get("logs")  # noqa
        price = order.total_price

        try:
            card = UserCard.objects.get(cardId=card_id, user=user, is_active=True)
        except UserCard.DoesNotExist:
            return Response({"error": "Card not found"}, status=status.HTTP_404_NOT_FOUND)

        transaction = Transaction.objects.create(
            user=user,
            payment_type=Transaction.PaymentTypeChoice.CARD,
            card=card,
            amount=price,
            order=order,
            status=Transaction.TransactionStatusChoices.PENDING,
            logs="{}",
        )

        if card.balance < price:
            transaction.status = Transaction.TransactionStatusChoices.FAILED
            transaction.save()
            return Response({"error": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)

        card.balance -= price
        card.save()

        try:
            restaurant = Restourant.objects.get(pk=order.restaurant_id)
            restaurant.orders_count += 1
            restaurant.save()
        except Restourant.DoesNotExist:
            return Response({"error": "Restaurant not found"}, status=status.HTTP_404_NOT_FOUND)

        transaction.status = Transaction.TransactionStatusChoices.PAID
        transaction.save()

        return Response({"message": "You have transaction successfully"}, status=status.HTTP_201_CREATED)


__all__ = ["OrderTransactionAPIView"]
