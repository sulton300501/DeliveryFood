from django.urls import path

from apps.payments.api_endpoints import consumerce

urlpatterns = [
    path("transaction/cards/list/", consumerce.CardListAPIView.as_view(), name="cards-list"),
    path("transaction/cards/detail/<uuid:pk>/", consumerce.CardDetailAPIView.as_view(), name="card-detail"),
    path("transaction/cards/delete/<uuid:pk>/", consumerce.CardDeleteAPIView.as_view(), name="card-delete"),
    path("transaction/cards/add-card/", consumerce.AddCardAPIView.as_view(), name="add-card"),
    path("transaction/history/", consumerce.TransactionHistoryAPIView.as_view(), name="transaction-hostory"),
    path("transaction/cancel/<int:pk>/", consumerce.TransactionCancelAPIView.as_view(), name="transaction-cancel"),
    path("transaction/food/pay/<int:pk>/", consumerce.OrderTransactionAPIView.as_view(), name="food-pay"),
]
