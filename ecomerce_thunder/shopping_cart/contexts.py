from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

# Context processor to make this dictionary available through the entire application which added in the settings.py context processor array


def shopping_cart_contents(request):

    shopping_cart_items = []
    total = 0
    product_count = 0
    shopping_cart = request.session.get('shopping_cart', {})

    for item_id, quantity in shopping_cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        shopping_cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY:
        delivery = total * Decimal(settings.STANDARD_DELIVERY / 100)
        free_delivery_delta = settings.FREE_DELIVERY - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'shopping_cart_items': shopping_cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY,
        'grand_total': grand_total,
    }

    return context