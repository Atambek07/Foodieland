from . import serializers, models
from rest_framework import generics

class CategoryList(generics.ListAPIView):
    """
    ### Список категорий 📚

    Этот эндпоинт позволяет получить полный список всех категорий.
    """
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def get(self, request, *args, **kwargs):
        """
        **Получить все категории**

        Возвращает список всех категорий, доступных в системе.
        """
        return super().get(request, *args, **kwargs)

class RecipeList(generics.ListAPIView):
    """
    ### Список рецептов 🍲

    Возвращает список всех рецептов.
    """
    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer

    def get(self, request, *args, **kwargs):
        """
        **Получить все рецепты**

        Получить список всех рецептов с краткими данными.
        """
        return super().get(request, *args, **kwargs)

class RecipeRetrieve(generics.RetrieveAPIView):
    """
    ### Просмотр одного рецепта

    Просмотр детальной информации по конкретному рецепту, используя его ID.
    """
    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer

class InstagramList(generics.ListAPIView):
    """
    ### Список постов из Instagram 📸

    Просмотр всех постов из Instagram.
    """
    queryset = models.Instagram.objects.all()
    serializer_class = serializers.InstagramSerializer

class InstagramRetrieve(generics.RetrieveAPIView):
    """
    ### Детальный просмотр поста из Instagram

    Получить детальную информацию по одному посту, используя его ID.
    """
    queryset = models.Instagram.objects.all()
    serializer_class = serializers.InstagramSerializer

class HotRecipeList(generics.ListAPIView):
    """
    ### Список популярных рецептов 🔥

    Эндпоинт для получения списка самых популярных рецептов.
    """
    queryset = models.HotRecipe.objects.all()
    serializer_class = serializers.HotRecipeSerializer

class HotRecipeRetrieve(generics.RetrieveAPIView):
    """
    ### Детальный просмотр популярного рецепта

    Позволяет получить подробные данные по одному популярному рецепту.
    """
    queryset = models.HotRecipe.objects.all()
    serializer_class = serializers.HotRecipeSerializer


class DetailRecipeList(generics.ListAPIView):
    """
    ### Список детальных рецептов

    Получение списка подробных рецептов.
    """
    queryset = models.DetailRecipe.objects.all()
    serializer_class = serializers.DetailRecipeSerializer

class DetailRecipeRetrieve(generics.RetrieveAPIView):
    """
    ### Детальный просмотр одного рецепта

    Эндпоинт для просмотра одного подробного рецепта по его ID.
    """
    queryset = models.DetailRecipe.objects.all()
    serializer_class = serializers.DetailRecipeSerializer

class BlogPostList(generics.ListAPIView):
    """
    ### Список детальных блогов

    Получение списка общих блогов.
    """
    queryset = models.BlogPost.objects.all()
    serializer_class = serializers.BlogPostSerializer

class BlogPostRetrieve(generics.RetrieveAPIView):
    """
    ### Детальный просмотр одного блога

    Эндпоинт для просмотра одного подробного блога по его ID.
    """
    queryset = models.BlogPost.objects.all()
    serializer_class = serializers.BlogPostSerializer

class BlogListAPIView(generics.ListAPIView):
    """
    ### Список блогов

    Получение списка общих блогов.
    """
    queryset = models.BlogList.objects.all()
    serializer_class = serializers.BlogListSerializer

class BlogRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.BlogList.objects.all()
    serializer_class = serializers.BlogListSerializer

class TastyRecipeList(generics.ListAPIView):
    queryset = models.TastyRecipe.objects.all()
    serializer_class = serializers.TastyRecipeSerializer

class CreateApplication(generics.CreateAPIView):
    """
    #Создать бланку для заявки

    Для созданий заявки
    """
    queryset = models.Application.objects.all()
    serializer_class = serializers.ApplicationSerializer