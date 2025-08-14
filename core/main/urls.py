from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from . import views

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('api/categories/', views.CategoryList.as_view(), name='category-list'),
    path('api/recipes/', views.RecipeList.as_view(), name='recipe-list'),
    path('api/recipes/<int:pk>/', views.RecipeRetrieve.as_view(), name='recipe-detail'),
    path('api/instagram/', views.InstagramList.as_view(), name='instagram-list'),
    path('api/instagram/<int:pk>/', views.InstagramRetrieve.as_view(), name='instagram-detail'),
    path('api/hot-recipes/', views.HotRecipeList.as_view(), name='hot-recipe-list'),
    path('api/hot-recipes/<int:pk>/', views.HotRecipeRetrieve.as_view(), name='hot-recipe-detail'),
    path('api/detail-recipes/', views.DetailRecipeList.as_view(), name='detail-recipe-list'),
    path('api/detail-recipes/<int:pk>/', views.DetailRecipeRetrieve.as_view(), name='detail-recipe-detail'),
    path('api/blog-list/', views.BlogListAPIView.as_view(), name='blog-list'),
    path('api/blog-list/<int:pk>/', views.BlogRetrieveAPIView.as_view(), name='blog-list-detail'),
    path('api/blog-posts/', views.BlogPostList.as_view(), name='blog-post-list'),
    path('api/blog-post/<int:pk>/', views.BlogPostRetrieve.as_view(), name='blog-post-detail'),
    path('api/tasty-recipes/', views.TastyRecipeList.as_view(), name='tasty-recipe-list'),
    path('api/create-application/', views.CreateApplication.as_view(), name='create-application'),
]