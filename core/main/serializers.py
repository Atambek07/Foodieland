from rest_framework import serializers
from .models import Category, Recipe, DetailRecipe, Instagram, HotRecipe


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class InstagramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instagram
        fields = '__all__'

class HotRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotRecipe
        fields = '__all__'

class DetailRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailRecipe
        fields = '__all__'
