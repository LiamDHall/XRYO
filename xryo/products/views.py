from django.shortcuts import render
from .models import Product, Variant, ImageAlbum, Image

# Create your views here.


def all_products(request):
    """ View to return and render all_products as well allow search,
    sorting and filtering
    """

    products = Product.objects.all()
    variants = Variant.objects.all()
    album = ImageAlbum.objects.all()
    images = Image.objects.all()

    context = {
        'products': products,
        'variants': variants,
        'album': album,
        'images': images,
    }

    return render(request, 'products/products.html', context)
