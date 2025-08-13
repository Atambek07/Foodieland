from django.contrib import admin
from . import models

admin.site.register(models.Recipe)
admin.site.register(models.Instagram)
admin.site.register(models.HotRecipe)
admin.site.register(models.Category)
admin.site.register(models.DetailRecipe)
