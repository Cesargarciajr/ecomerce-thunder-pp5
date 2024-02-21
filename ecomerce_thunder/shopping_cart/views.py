from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_shopping_cart(request):
    """ A view that renders the shopping cart contents page """

    return render(request, 'shopping_cart/shopping_cart.html')


def add_to_shopping_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shopping_cart = request.session.get('shopping_cart', {}) # saving temporary items in the shopping cart in the session

    if item_id in list(shopping_cart.keys()):
        shopping_cart[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {shopping_cart[item_id]}')
    else:
        shopping_cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to your shopping cart')

    request.session['shopping_cart'] = shopping_cart
    return redirect(redirect_url)


def adjust_shooping_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    shopping_cart = request.session.get('shopping_cart', {})

    if quantity > 0:
        shopping_cart[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {shopping_cart[item_id]}')
    else:
        shopping_cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your shopping cart')

    request.session['shopping_cart'] = shopping_cart
    return redirect(reverse('view_shopping_cart'))


def remove_from_shopping_cart(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        shopping_cart = request.session.get('shopping_cart', {})
        shopping_cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your shopping cart')
        request.session['shopping_cart'] = shopping_cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)