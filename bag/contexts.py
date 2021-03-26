from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    bag_content = []
    bag_item_count = 0
    bag_total = 0

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
