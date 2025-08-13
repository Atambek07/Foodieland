from django.urls import path

from . import views

urlpatterns = [
    path('category-list/', views.CategoryList.as_view()),
    path('recipe-list/', views.RecipeList.as_view()),
    path('recipe-retrieve/<int:pk>/', views.RecipeRetrieve.as_view()),
    path('instagram-list/', views.InstagramList.as_view()),
    path('instagram-retrieve/<int:pk>/', views.InstagramRetrieve.as_view()),
    path('hot-recipe-list/', views.HotRecipeList.as_view()),
    path('hot-recipe-retrieve/<int:pk>/', views.HotRecipeRetrieve.as_view()),
    path('detail-recipe-list/', views.DetailRecipeList.as_view()),
    path('detail-recipe-retrieve/<int:pk>/', views.DetailRecipeRetrieve.as_view()),
]