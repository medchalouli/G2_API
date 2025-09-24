from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'rating')
    search_fields = ('name', 'description')
    list_filter = ('price', 'rating')

admin.site.register(Product, ProductAdmin)
