from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderItem
from products.models import Product, Variant
from bag.contexts import bag_contents

import stripe
import json


def checkout(request):
    """ View to view checkout and form.
    Stops users checking out with an empty bag.
    Creates an order with all the order items and saves them to the
    database.
    """

    # Gets variable from os for stripe
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # POST
    if request.method == 'POST':
        bag = request.session.get('bag', {})

        # Get order form data
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)

        # Check if the order form is valid and save it if it is
        if order_form.is_valid():

            # Commit False stops multiple save events on database.
            order = order_form.save(commit=False)

            payment_id = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = payment_id
            order.original_bag = json.dumps(bag)
            order.save()

            # Cycle through bag items and create an Order Item for each
            for product_id, product_data in bag.items():
                try:
                    product = Product.objects.get(id=product_id)
                    if isinstance(product_data, int):
                        order_item = OrderItem(
                            order=order,
                            product=product,
                            quantity=product_data,
                        )
                        order_item.save()
                    else:
                        if 'product_by_variant' in product_data:
                            for variant_id, quantity in product_data['product_by_variant'].items():
                                variant = Variant.objects.get(id=variant_id)
                                order_item = OrderItem(
                                    order=order,
                                    product=product,
                                    variant=variant,
                                    quantity=quantity,
                                )
                                order_item.save()

                        elif 'product_by_size' in product_data:
                            for size, quantity in product_data['product_by_size'].items():
                                order_item = OrderItem(
                                    order=order,
                                    product=product,
                                    quantity=quantity,
                                    product_size=size,
                                )
                                order_item.save()

                # If Product doesn't exist give feeback and redirect to bag
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            # On successful Orders redirect user to Checkout Success Page
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))

        # If form is invalid tell user their is an error and reload checkout
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
            return redirect(reverse('checkout'))

    # GET
    else:
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


@require_POST
def cache_checkout_data(request):
    """ Handles cashing payment data
    """

    try:
        payment_id = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(
            payment_id,
            metadata={
                'bag': json.dumps(request.session.get('bag', {})),
                'save_info': request.POST.get('save_info'),
                'username': request.user,
            },
        )
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed at this time. Please try again.')
        return HttpResponse(content=e, status=400)


def checkout_success(request, order_number):
    """
    Show user the checkout success page if an order is successfully
    placed and gives them feedback
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, 'Order successful')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
