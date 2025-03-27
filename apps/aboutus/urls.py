from django.urls import path

from apps.aboutus import views

urlpatterns = [
    path("about/PostRestourant/", views.RestourantAPIView.as_view()),
    path("about/GetSingleRestourant/<slug:slug>/", views.RestourantDetailView.as_view()),
    path("about/GetAllRestourant/", views.RestourantAllAPIView.as_view()),
    path("about/PostReviews/", views.ReviewsAPIView.as_view()),
    path("about/GetSingleReviews/", views.ReviewsSingleAPIView.as_view()),
    path("about/GetAllReviews/", views.ReviewsAllAPIView.as_view()),
    path("about/PostCategory/", views.CreateGategoryAPIView.as_view()),
    path("about/PostFavourite/Restourant/", views.FavouriteRestourantAPIView.as_view()),
    path("about/GetAllFavourite/Restourant/", views.FavouriteAllRestourantAPIView.as_view()),
    path("about/GetDetailFavourite/Restourant/", views.GetDetailRestourantFavourite.as_view()),
]
