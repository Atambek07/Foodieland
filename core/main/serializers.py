from rest_framework import serializers
from .models import Category, Recipe, DetailRecipe, Instagram, HotRecipe, BlogFAQ, BlogPost, TastyRecipe, Application


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

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogFAQ
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'

class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'

class TastyRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TastyRecipe
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'