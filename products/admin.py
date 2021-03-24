from django.contrib import admin
from .models import Category, Product, Variant, ImageAlbum, Image

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
        'album',
    )


class VariantAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'product',
        'sku',
    )


class ImageAlbumAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'album',
        'image'
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Variant, VariantAdmin)
admin.site.register(ImageAlbum, ImageAlbumAdmin)
admin.site.register(Image, ImageAdmin)
