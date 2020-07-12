from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Company)
admin.site.register(models.Nationality)
admin.site.register(models.Meal)
admin.site.register(models.Food)
