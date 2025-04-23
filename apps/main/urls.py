from django.urls import path

from . import views

urlpatterns = [
    path("main/PostCategory/Food/", views.CategoryFoodAPIView.as_view(), name="create-category-food"),
    path("main/GetAllCategory/Food", views.CategoryFoodAllView.as_view(), name="all-food-category"),
    path("main/PostMediaFile/Food/", views.MediaFileView.as_view()),
    path("main/GetAllMediaFile/Food", views.MediaFileALLView.as_view()),
    path("main/PostPromo/Food", views.PromoView.as_view(), name="create-promo"),
    path("main/GetAllPromo/Food", views.PromoAllView.as_view(), name="all-promo"),
    path("main/PostFood/", views.FoodView.as_view()),
    path("main/GetAllFood/<slug:slug>/", views.FoodALLView.as_view()),
    path("main/PostFoodReviews/", views.FoodReviewsView.as_view()),
    path("main/GetAllFoodReviews/", views.FoodAllReviewsView.as_view()),
    path("main/PostTag/", views.FoodTagView.as_view()),
    path("main/GetAllFoodTags/", views.FoodTagView.as_view()),
    path("main/GetDownloadMediaFile/<int:id>/", views.MediaUploadFile.as_view()),
]
