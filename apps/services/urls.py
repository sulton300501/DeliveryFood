from django.urls import path

from . import views

urlpatterns = [
    path("services/PostSize/", views.SizeViews.as_view(), name="create-size"),
    path("services/GetAllSize/", views.SizeAllViews().as_view(), name="all-size"),
    path("services/PostTopping/", views.ToppingViews.as_view(), name="create-topping"),
    path("services/GetAllTopping/", views.ToppingAllViews().as_view(), name="all-topping"),
    path("services/PostOrderDetails/", views.OrderDetailViews.as_view(), name="order-detail"),
    path("services/GetAllOrderDetails/", views.OrderDetailAllViews().as_view(), name="all-order-detail"),
    path("services/PostOrder/", views.OrderViews.as_view(), name="create-order"),
    path("services/GetAllOrder/", views.OrderAllViews().as_view(), name="all-order"),
]
