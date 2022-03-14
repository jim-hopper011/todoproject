from django.contrib import admin
from .models import Category,Product
# Register your models here.
class adminc(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category, adminc)

class adminp(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'avai']
    list_editable = ['price', 'stock', 'avai']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(Product, adminp)