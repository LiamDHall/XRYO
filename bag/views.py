from django.shortcuts import render, redirect, reverse, HttpResponse

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
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    bag = request.session.get('bag', {})

    if size:
        if product_id in list(bag.keys()):
            if size in bag[product_id]['product_by_size'].keys():
                bag[product_id]['product_by_size'][size] += quantity
            else:
                bag[product_id]['product_by_size'][size] = quantity
        else:
            bag[product_id] = {'product_by_size': {size: quantity}}
    else:
        if product_id in list(bag.keys()):
            bag[product_id] += quantity
        else:
            bag[product_id] = quantity

    request.session['bag'] = bag
    return redirect(current_page)


def update_bag(request, product_id):
    """ Updates the quantity of a specific product
    """

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    bag = request.session.get('bag', {})

    if size:
        bag[product_id]['product_by_size'][size] = quantity
    else:
        bag[product_id] = quantity

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_product(request, product_id):
    """Remove a product from the bag
    """

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[product_id]['product_by_size'][size]
            if not bag[product_id]['product_by_size']:
                bag.pop(product_id)
        else:
            bag.pop(product_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
