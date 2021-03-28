from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, Variant


def bag_contents(request):

    bag_content = []
    bag_item_count = 0
    bag_total = 0
    bag = request.session.get('bag', {})

    for product_id, product_data in bag.items():
        if isinstance(product_data, int):
            product = get_object_or_404(Product, pk=product_id)
            bag_total += product_data * product.price
            bag_item_count += product_data
            bag_content.append({
                'product_id': product_id,
                'quantity': product_data,
                'product': product,
            })

        else:
            product = get_object_or_404(Product, pk=product_id)
            for size, quantity in product_data['product_by_size'].items():
                bag_total += quantity * product.price
                bag_item_count += quantity
                bag_content.append({
                    'item_id': product_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    if bag_total < settings.FREE_DELIVERY_MIN:
        delivery_charge = Decimal(settings.DELIVERY_CHARGE)
        free_delivery_delta = settings.FREE_DELIVERY_MIN - bag_total
    else:
        delivery_charge = 0
        free_delivery_delta = 0

    bag_grand_total = delivery_charge + bag_total

    context = {
        'bag_content': bag_content,
        'bag_item_count': bag_item_count,
        'bag_total': bag_total,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_min': settings.FREE_DELIVERY_MIN,
        'bag_grand_total': bag_grand_total,
        'delivery_charge': delivery_charge,
    }

    return context
