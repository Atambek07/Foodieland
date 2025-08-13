from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    img = models.ImageField(upload_to='category/', null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="recipes/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    prep_time = models.IntegerField(default=0)
    is_starred = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Instagram(models.Model):
    content = models.FileField(upload_to='instagram/')

    class Meta:
        ordering = ['id']


class HotRecipe(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="hot-recipes/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    prep_time = models.IntegerField(default=0)
    date = models.DateField()
    chef = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class DetailRecipe(models.Model):
    CATEGORY_CHOICES = [
        ('For main dishes', 'For main dishes'),
        ('For the sauce', 'For the sauce'),
    ]

    name = models.CharField(max_length=100)
    chef = models.CharField(max_length=100)
    date = models.DateField()
    prep_time = models.IntegerField(default=0)
    cook_time = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="details/")
    description = models.TextField()

    calories = models.FloatField(default=0)
    total_fat = models.FloatField(default=0)
    protein = models.FloatField(default=0)
    carbohydrate = models.FloatField(default=0)
    cholesterol = models.FloatField(default=0)

    ingredient = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    direction_title = models.CharField(max_length=100)
    direction_img = models.ImageField(upload_to='directions/', null=True, blank=True)
    direction_text = models.TextField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
