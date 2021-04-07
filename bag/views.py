from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product, Variant

# Create your views here.


def view_bag(request):
    """ View to display content of a users bag
    """

    return render(request, 'bag/bag.html')


def product_to_bag(request, product_id):
    """ Add products without variants to bag
    """

    quantity = 1
    current_page = request.POST.get('current_page')
    size = None
    variant_id = None

    product = get_object_or_404(Product, pk=product_id)
    product_name = product.name.title()

    if 'product_variant' in request.POST:
        variant_id = request.POST['product_variant']
        variant = get_object_or_404(Variant, pk=variant_id)
        variant_name = variant.name.title()

    if 'product_size' in request.POST:
        size = request.POST['product_size']
        size_cap = size.upper()

    bag = request.session.get('bag', {})

    if variant_id:
        if product_id in list(bag.keys()):
            if variant_id in bag[product_id]['product_by_variant'].keys():
                bag[product_id]['product_by_variant'][variant_id] += quantity
                messages.success(request, f'Updated {product_name} - {variant_name} qauntity')
            else:
                bag[product_id]['product_by_variant'][variant_id] = quantity
                messages.success(request, f'Added {product_name} - {variant_name} to your bag')
        else:
            bag[product_id] = {'product_by_variant': {variant_id: quantity}}
            messages.success(request, f'Added: {product_name} - {variant_name} to your bag')

    elif size:
        if product_id in list(bag.keys()):
            if size in bag[product_id]['product_by_size'].keys():
                bag[product_id]['product_by_size'][size] += quantity
                messages.success(request, f'Updated: {product_name} - {size_cap} qauntity')
            else:
                bag[product_id]['product_by_size'][size] = quantity
                messages.success(request, f'Added: {product_name} - {size_cap} to your bag')
        else:
            bag[product_id] = {'product_by_size': {size: quantity}}
            messages.success(request, f'Added: {product_name} - {size_cap} to your bag')
    else:
        if product_id in list(bag.keys()):
            bag[product_id] += quantity
            messages.success(request, f'Updated: {product_name} qauntity')
        else:
            bag[product_id] = quantity
            messages.success(request, f'Added: {product_name} to your bag')

    request.session['bag'] = bag
    return redirect(current_page)


def update_bag(request, product_id):
    """ Updates the quantity of a specific product
    """

    quantity = int(request.POST.get('quantity'))
    variant_id = None
    size = None

    product = get_object_or_404(Product, pk=product_id)
    product_name = product.name.title()

    if 'product_variant' in request.POST:
        variant_id = request.POST['product_variant']
        variant = get_object_or_404(Variant, pk=variant_id)
        variant_name = variant.name.title()

    elif 'product_size' in request.POST:
        size = request.POST['product_size']
        size_cap = size.upper()

    bag = request.session.get('bag', {})

    if variant_id:
        bag[product_id]['product_by_variant'][variant_id] = quantity
        messages.success(request, f'Updated: {product_name} - {variant_name} qauntity')
    elif size:
        bag[product_id]['product_by_size'][size] = quantity
        messages.success(request, f'Updated: {product_name} - {size_cap} qauntity')
    else:
        bag[product_id] = quantity
        messages.success(request, f'Updated: {product_name} qauntity')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_product(request, product_id):
    """Remove a product from the bag
    """

    try:
        variant_id = None
        size = None

        if 'product_variant' in request.POST:
            variant_id = request.POST['product_variant']

        if 'product_size' in request.POST:
            size = request.POST['product_size']

        bag = request.session.get('bag', {})
        if variant_id:
            del bag[product_id]['product_by_variant'][variant_id]
            if not bag[product_id]['product_by_variant']:
                bag.pop(product_id)

        elif size:
            del bag[product_id]['product_by_size'][size]
            if not bag[product_id]['product_by_size']:
                bag.pop(product_id)
        else:
            bag.pop(product_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.success(request, f'Error removing product: {e}')
        return HttpResponse(status=500)
