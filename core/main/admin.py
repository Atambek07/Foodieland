from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models
from django.utils.html import format_html

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    """Настройки админ-панели для Категорий."""
    list_display = ('name', 'image_preview')
    search_fields = ('name',)
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.img:
            # mark_safe используется, чтобы Django не экранировал HTML-тег
            return mark_safe(f'<img src="{obj.img.url}" style="max-height: 50px; max-width: 100px;" />')
        return "Нет изображения"
    image_preview.short_description = 'Превью изображения'


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Настройки админ-панели для Рецептов."""
    list_display = ('name', 'category', 'prep_time')
    list_filter = ('category',)
    search_fields = ('name',)
    list_per_page = 25 # Количество объектов на одной странице


@admin.register(models.HotRecipe)
class HotRecipeAdmin(admin.ModelAdmin):
    """Настройки админ-панели для Горячих Рецептов."""
    list_display = ('name', 'category', 'chef', 'date', 'prep_time')
    list_filter = ('category', 'chef', 'date')
    search_fields = ('name', 'chef')
    list_per_page = 25


@admin.register(models.DetailRecipe)
class DetailRecipeAdmin(admin.ModelAdmin):
    """Настройки админ-панели для Детальных Рецептов."""
    list_display = ('name', 'category', 'chef', 'date', 'cook_time')
    list_filter = ('category', 'chef', 'ingredient')
    search_fields = ('name', 'chef', 'description')
    list_per_page = 20

    # Эта настройка организует сложную страницу редактирования в логические группы
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'chef', 'date', 'category', 'img', 'description')
        }),
        ('Время и Ингредиенты', {
            'fields': (('prep_time', 'cook_time'), 'ingredient')
        }),
        ('Пищевая ценность (на порцию)', {
            'fields': (('calories', 'total_fat'), ('protein', 'carbohydrate'), 'cholesterol'),
            'classes': ('collapse',),  # Эту группу можно будет сворачивать
        }),
        ('Инструкции по приготовлению', {
            'fields': ('direction_title', 'direction_img', 'direction_text')
        }),
    )


@admin.register(models.Instagram)
class InstagramAdmin(admin.ModelAdmin):
    """Настройки админ-панели для контента Instagram."""
    list_display = ('id', 'content_link')

    def content_link(self, obj):
        if obj.content:
            return mark_safe(f'<a href="{obj.content.url}" target="_blank">Посмотреть файл</a>')
        return "Файл не загружен"
    content_link.short_description = 'Ссылка на файл'

class FAQInline(admin.TabularInline):
    model = models.BlogFAQ
    extra = 1
    min_num = 1
    verbose_name = "FAQ"
    verbose_name_plural = "FAQ"


@admin.register(models.BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date")
    search_fields = ("title", "author")
    list_filter = ("date",)
    inlines = [FAQInline]

class BlogListAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date", "image_preview", "author_image_preview")
    search_fields = ("title", "author")
    list_filter = ("date", "author")
    ordering = ("-date",)
    date_hierarchy = "date"
    readonly_fields = ("image_preview_form", "author_image_preview_form")  # Превью в форме

    def image_preview(self, obj):
        if obj.img:
            return format_html('<img src="{}" width="80" height="50" style="object-fit:cover;border-radius:5px;" />', obj.img.url)
        return "—"
    image_preview.short_description = "Image"

    def author_image_preview(self, obj):
        if obj.author_img:
            return format_html('<img src="{}" width="50" height="50" style="object-fit:cover;border-radius:50%;" />', obj.author_img.url)
        return "—"
    author_image_preview.short_description = "Author Image"

    def image_preview_form(self, obj):
        if obj.img:
            return format_html('<img src="{}" width="200" style="object-fit:cover;border-radius:5px;" />', obj.img.url)
        return "No image uploaded"
    image_preview_form.short_description = "Current Image"

    def author_image_preview_form(self, obj):
        if obj.author_img:
            return format_html('<img src="{}" width="100" style="object-fit:cover;border-radius:50%;" />', obj.author_img.url)
        return "No image uploaded"
    author_image_preview_form.short_description = "Current Author Image"

admin.site.register(models.BlogList, BlogListAdmin)
admin.site.register(models.TastyRecipe)