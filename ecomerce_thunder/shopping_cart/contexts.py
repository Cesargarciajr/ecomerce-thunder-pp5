from decimal import Decimal
from django.conf import settings


# Context processor to make this dictionary available through the entire application which added in the settings.py context processor array


def shopping_cart_contents(request):

    shopping_cart_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_DELIVERY:
        delivery = total * Decimal(settings.STANDARD_DELIVERY)
        get_free_delivery = settings.FREE_DELIVERY - total
    else:
        delivery = 0
        get_free_delivery = 0

    grand_total = delivery + total

    context = {
        'shopping_cart_items': shopping_cart_items,
        'total': total,
        'product_count': product_count,
        'get_free_delivery': get_free_delivery,
        'free_delivery': settings.FREE_DELIVERY,
        'grand_total': grand_total,
    }

    return context