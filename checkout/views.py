from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings


from .forms import OrderForm
from .models import Order, OrderItem
from products.models import Product
from bag.contexts import bag_contents

import stripe


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

    current_bag = bag_contents(request)
    bag_total = current_bag['bag_grand_total']

    # Round total as Stripe charges in pennies
    # ie. £23.51 is equal to 2351p
    stripe_total = round(bag_total * 100)
    stripe.api_key = stripe_secret_key

    # Create Payment Intent
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
    """
    Show user the checkout success page if an order is successfully
    placed and gives them feedback
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successful \
        Your order number: {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)