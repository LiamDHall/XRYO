from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings


from .forms import OrderForm


def checkout(request):
    """ View to view checkout and form.
    Stops users checking out with an empty bag.
    """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    # Stops users accessing checkout via url with an empty bag
    if not bag:
        messages.error(request, "Can't Checkout: Your Bag is Empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'stripe_client_secret': 'test key test',
    }

    return render(request, 'checkout/checkout.html', context)
