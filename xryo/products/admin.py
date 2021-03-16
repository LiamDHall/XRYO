from django.contrib import admin
from .models import Category, Product, Variant

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'rating',
        'images',
    )


class VariantAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'product',
        'sku',
        'price',
        'images',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Variant, VariantAdmin)
