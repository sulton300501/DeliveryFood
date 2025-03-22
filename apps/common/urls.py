from django.urls import path

from apps.common import views

urlpatterns = [
    path("common/CreateCity/", views.CityAPIView.as_view(), name="create-city"),
    path("common/CreateDistrict/", views.DistrictAPIView.as_view(), name="create-district"),
    path("common/CreateAddress/", views.AddressAPIView.as_view(), name="create-address"),
    path("common/GetAllAddress/", views.GetAllAddressAPIView.as_view(), name="getAll-address"),
    path("common/CityUpdate/<int:id>/", views.CityUpdateView.as_view(), name="update-city"),
    path("common/CityDelete/<int:id>/", views.CityDeleteView.as_view(), name="delete-city"),
]
