from django.http import HttpResponse

from .models import Order, OrderItem
from products.models import Product, Variant
from profiles.models import Profile

import json
import time


class StripeWH_Handler:
    """Handles webhooks recieved from Stripe
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handles all generic or unexpected webhook event
        """

        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """Handles the webhook: payment_intent.succeeded from Stripe
        Creates order if order can't be found in database as the
        checkout out form wasn't submitted but payment was taken by
        Stripe.
        """

        # Get payment intent details
        intent = event.data.object
        payment_id = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Format empty field to None so the model can execpt
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile data if save info was checked by user
        # Profile = None allow no logged in users to checkout
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = Profile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_street_address1 = shipping_details.address.line1
                profile.default_street_address2 = shipping_details.address.line2
                profile.default_county = shipping_details.address.state
                profile.default_town_or_city = shipping_details.address.city
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_country = shipping_details.address.country
                profile.save()

        # Check if order is in database
        # Try five times as their might be a delay
        # If after fifth attempts of getting the order fails, create the order
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    town_or_city__iexact=shipping_details.address.city,
                    county__iexact=shipping_details.address.state,
                    postcode__iexact=shipping_details.address.postal_code,
                    country__iexact=shipping_details.address.country,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=payment_id,
                )

                # If order exists break out of loop
                order_exists = True
                break

            # If order doesn't exist increase attempts
            # Delay the next attempt at getting the order by a second
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} \
                    | SUCCESS: Order in database already',
                status=200
            )

        # Creates order if order isn't found in database
        else:
            order = None
            try:
                order = Order.objects.create(
                    user_profile=profile,
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    town_or_city=shipping_details.address.city,
                    county=shipping_details.address.state,
                    postcode=shipping_details.address.postal_code,
                    country=shipping_details.address.country,
                    original_bag=bag,
                    stripe_pid=payment_id,
                )

                # Cycle through bag items and create an Order Item for each
                for product_id, product_data in json.loads(bag).items():
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

            except Exception as e:
                if order:
                    order.delete()

                return HttpResponse(
                    # Send a 500 response to Stripe
                    # Stripe will automatically try the webhook again.
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500
                )

        return HttpResponse(
            content=f'Webhook received: {event["type"]} \
                | SUCCESS: Order created by webhook',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """Handles the webhook: payment_intent.payment_failed from Stripe
        """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
