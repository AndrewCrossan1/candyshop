from django.contrib import admin

# Shop Administration
from .models import Product, Category, Brand, ProductRating


@admin.action(description='Generate new product')
def copy(modeladmin, request, queryset):
    temp = None
    if queryset.count() != 1:
        modeladmin.message_user(request, 'A new product can only be generated using one product')
        return
    for product in queryset:
        temp = product
    NewProduct = Product.objects.create(
        Name=temp.Name,
        Description=temp.Description,
        Price=temp.Price,
        Category=temp.Category,
        Tags=temp.Tags,
        Brand=temp.Brand,
        Stock=0
    )
    NewProduct.save()
    modeladmin.message_user(request, 'Product copied!')
    return


class RatingInlineAdmin(admin.TabularInline):
    model = ProductRating


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Price', 'Availability', 'Updated', 'category_name', 'brand_name', 'Rating')
    list_filter = ('Created', 'Updated', 'Category')
    readonly_fields = ('Available', 'Rating')
    list_editable = ('Price',)
    actions = [copy]
    inlines = [RatingInlineAdmin]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Name', 'product_count', 'average_rating')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('Name', 'product_count')
    list_filter = ('Name',)
