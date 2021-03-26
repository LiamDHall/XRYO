from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Category, Product, Variant
# Create your views here.


def all_products(request):
    """ View to return and render all_products as well allow search,
    sorting and filtering
    """

    products = Product.objects.all()
    categories = None
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sort_key = request.GET['sort']
            sort = sort_key
            if sort_key == 'name':
                sort_key = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sort_key = f'-{sort_key}'
            products = products.order_by(sort_key)

        if 'category' in request.GET:
            cats = request.GET['category'].split(',')
            products = products.filter(category__name__in=cats)
            categories = Category.objects.filter(name__in=cats)

        if 'search-text' in request.GET:
            query = request.GET['search-text']
            print(query)
            if not query:
                messages.error(request, "Empty Search")
                return redirect(reverse('home'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    selected_sorting = f'{sort}_{direction}'

    # No of Products
    no_of_products = 0

    if len(products) > 0:
        for product in products:
            if len(product.variant_set.all()) > 0:
                no_of_products += len(product.variant_set.all())
            else:
                no_of_products += 1

    context = {
        'products': products,
        'search_term': query,
        'no_of_products': no_of_products,
        'selected_catergory': categories,
        'selected_sorting': selected_sorting,
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
