from django.shortcuts import render

# Create your views here.

def view_shopping_cart(request):
    """ A view that renders the shopping cart contents page """

    return render(request, 'shopping_cart/shopping_cart.html')