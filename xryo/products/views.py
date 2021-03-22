from django.shortcuts import render, get_object_or_404
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


def product_detail(request, product_id):
    """ A view to details of a single product
    """

    product = get_object_or_404(Product, pk=product_id)

    print(f'PRODUCT === {product}')

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def product_variant(request, product_id, variant_id):
    """ A view to details of a single variant
    """

    product = get_object_or_404(Product, pk=product_id)
    variant = get_object_or_404(Variant, pk=variant_id)

    print(f'VARIANT === {variant}')
    print(f'PRODUCT === {product}')

    context = {
        'variant': variant,
        'product': product,
    }

    return render(request, 'products/product_variant.html', context)
