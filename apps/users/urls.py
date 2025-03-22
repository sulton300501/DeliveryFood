from django.urls import path

from apps.users import api_endpoints

urlpatterns = [
    path("login/", api_endpoints.NewLoginAPIView.as_view(), name="login"),
    path("ConfirmLogin/", api_endpoints.NewLoginConfirmAPIView.as_view(), name="confirm-login"),
    path("profile/", api_endpoints.ProfileAPIView.as_view(), name="profile"),
]
