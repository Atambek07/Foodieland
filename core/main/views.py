from . import serializers, models
from rest_framework import generics

class CategoryList(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class RecipeList(generics.ListAPIView):
    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer

class RecipeRetrieve(generics.RetrieveAPIView):
    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer

class InstagramList(generics.ListAPIView):
    queryset = models.Instagram.objects.all()
    serializer_class = serializers.InstagramSerializer

class InstagramRetrieve(generics.RetrieveAPIView):
    queryset = models.Instagram.objects.all()
    serializer_class = serializers.InstagramSerializer

class HotRecipeList(generics.ListAPIView):
    queryset = models.HotRecipe.objects.all()
    serializer_class = serializers.HotRecipeSerializer

class HotRecipeRetrieve(generics.RetrieveAPIView):
    queryset = models.HotRecipe.objects.all()
    serializer_class = serializers.HotRecipeSerializer


class DetailRecipeList(generics.ListAPIView):
    queryset = models.DetailRecipe.objects.all()
    serializer_class = serializers.DetailRecipeSerializer

class DetailRecipeRetrieve(generics.RetrieveAPIView):
    queryset = models.DetailRecipe.objects.all()
    serializer_class = serializers.DetailRecipeSerializer