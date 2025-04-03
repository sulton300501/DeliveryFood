from django.urls import path

from . import views

urlpatterns = [
    path("services/PostSize/", views.SizeViews.as_view()),
    path("services/GetAllSize/", views.SizeAllViews().as_view()),
    path("services/PostTopping/", views.ToppingViews.as_view()),
    path("services/GetAllTopping/", views.ToppingAllViews().as_view()),
    path("services/PostOrderDetails/", views.OrderDetailViews.as_view()),
    path("services/GetAllOrderDetails/", views.OrderDetailAllViews().as_view()),
    path("services/PostOrder/", views.OrderViews.as_view()),
    path("services/GetAllOrder/", views.OrderAllViews().as_view()),
]
