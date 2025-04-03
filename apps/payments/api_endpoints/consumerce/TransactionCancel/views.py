from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.payments.models import PaymentRefund, Transaction


class TransactionCancelAPIView(APIView):
    def post(self, request, pk):
        try:
            transaction = Transaction.objects.get(pk=pk)
            user = request.user

            if transaction.status == "cancelled":
                return Response(
                    {"error": "You have cancelled transaction so we cannot refund"}, status=status.HTTP_400_BAD_REQUEST
                )

            if transaction.status == "failed":
                return Response(
                    {"error": "Your transaction failed so we cannot refund"}, status=status.HTTP_400_BAD_REQUEST
                )

            if transaction.withdrawed:
                return Response(
                    {"error": "We have already refund your transaction"}, status=status.HTTP_400_BAD_REQUEST
                )

            PaymentRefund.objects.create(
                transaction=transaction, user=user, status=PaymentRefund.PaymentRefundStatusChoices.PENDING
            )

            return Response({"message": "Transaction cancelled successfully"})
        except Transaction.DoesNotExist:
            return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)
