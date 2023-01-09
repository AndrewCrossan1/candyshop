from django.contrib import admin

# Shop Administration
from .models import Product, Category, Brand


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Price', 'Stock', 'Available', 'Updated', 'category_name', 'brand_name')
    list_filter = ('Available', 'Created', 'Updated')
    list_editable = ('Price', 'Stock', 'Available')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Name', 'product_count', 'average_rating')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('Name', 'product_count')
    list_filter = ('Name',)
