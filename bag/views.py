from django.shortcuts import render, redirect

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
    bag = request.session.get('bag', {})

    if product_id in list(bag.keys()):
        bag[product_id] += quantity
    else:
        bag[product_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(current_page)
