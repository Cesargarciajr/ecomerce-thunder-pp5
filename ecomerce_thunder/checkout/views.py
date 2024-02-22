from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    shopping_cart = request.session.get('shopping_cart', {})
    if not shopping_cart:
        messages.error(request, "There's nothing in your shopping cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OmPWUI8NvNINQ7FUSsIoYm6FsgdeACAJ1UJtpX5FFVYcsqlUnr8CYWL6oKUxaRNj8EIVGcwqF8pUJlFFa9T0Fd500Vg9iABpQ',
        'client_secret': 'sk_test_51OmPWUI8NvNINQ7Fy55CSLbchccuFkEP6aovwH2k8xTFXPj6NYDuLhDa1jXv608hJ8QV7FtptrHud7jnNO7BJeT1008lnVR3tW',
    }

    return render(request, template, context)