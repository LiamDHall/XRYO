from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """ View to view checkout.
    Stops users checking out with an empty bag.
    """
    bag = request.session.get('bag', {})

    # Stops users accessing checkout via url with an empty bag
    if not bag:
        messages.error(request, "Can't Checkout: Your Bag is Empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    context = {
        'order_form': order_form,
    }

    return render(request, 'checkout/checkout.html', context)
