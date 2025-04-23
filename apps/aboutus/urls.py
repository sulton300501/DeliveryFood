from django.urls import path

from apps.aboutus import views

urlpatterns = [
    path("about/PostRestourant/", views.RestourantAPIView.as_view(), name="create-restourant"),
    path("about/GetSingleRestourant/<slug:slug>/", views.RestourantDetailView.as_view(), name="get-single-restourant"),
    path("about/GetAllRestourant/", views.RestourantAllAPIView.as_view(), name="all-restourant"),
    path("about/PostReviews/", views.ReviewsAPIView.as_view(), name="create-review"),
    path("about/GetSingleReviews/", views.ReviewsSingleAPIView.as_view(), name="single-review"),
    path("about/GetAllReviews/", views.ReviewsAllAPIView.as_view(), name="reviews-all"),
    path("about/PostCategory/", views.CreateGategoryAPIView.as_view(), name="create-category"),
    path("about/PostFavourite/Restourant/", views.FavouriteRestourantAPIView.as_view(), name="create-favourite"),
    path("about/GetAllFavourite/Restourant/", views.FavouriteAllRestourantAPIView.as_view()),
    path("about/GetDetailFavourite/Restourant/", views.GetDetailRestourantFavourite.as_view()),
]
