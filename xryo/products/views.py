from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Variant, ImageAlbum, Image
# Create your views here.


def all_products(request):
    """ View to return and render all_products as well allow search,
    sorting and filtering
    """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'search-text' in request.GET:
            query = request.GET['search-text']
            print(query)
            if not query:
                messages.error(request, "Empty Search")
                return redirect(reverse('home'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    variants = Variant.objects.all()
    album = ImageAlbum.objects.all()
    images = Image.objects.all()

    context = {
        'products': products,
        'search_term': query,
        'variants': variants,
        'album': album,
        'images': images,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to details of a single product
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def product_variant(request, product_id, variant_id):
    """ A view to details of a single variant
    """

    product = get_object_or_404(Product, pk=product_id)
    variant = get_object_or_404(Variant, pk=variant_id)

    context = {
        'variant': variant,
        'product': product,
    }

    return render(request, 'products/product_variant.html', context)
