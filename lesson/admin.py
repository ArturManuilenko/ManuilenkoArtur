from django.contrib import admin
from . import models
# Register your models here.

# admin.site.register(models.Material) # ниже тоже самое но через декоратор и class
@admin.register(models.Material)
class Material(admin.ModelAdmin):
    list_display = ('title', 'slug', 'material_type', 'publish')
    list_filter = ('material_type', 'created')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title', )}
    ordering = ('material_type', 'publish')



