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

class BlogList(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='blogs/')
    description = models.TextField()
    date = models.DateField()
    author = models.CharField(max_length=100)
    author_img = models.ImageField(upload_to='blogs/authors/')

    class Meta:
        ordering = ['-date']  # От новых к старым
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title

class TastyRecipe(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='tasty-recipes/')
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    author_img = models.ImageField(upload_to='blog-post/authors/')
    img = models.ImageField(upload_to='blog-post/')
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title

class BlogFAQ(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='faqs')
    question = models.CharField(max_length=100)
    answer = models.TextField()
    image = models.ImageField(upload_to='blog-post/faqs/', null=True, blank=True)

    def __str__(self):
        return f"{self.question[:50]}..."

class Application(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    enquiry = models.CharField()
    message = models.TextField()

    def __str__(self):
        return self.name
