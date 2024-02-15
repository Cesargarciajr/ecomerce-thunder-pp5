from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_shopping_cart(request):
    """ A view that renders the shopping cart contents page """

    return render(request, 'shopping_cart/shopping_cart.html')

def add_to_shopping_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shopping_cart = request.session.get('shopping_cart', {}) # saving temporary items in the shopping cart in the session

    if item_id in list(shopping_cart.keys()):
        shopping_cart[item_id] += quantity
    else:
        shopping_cart[item_id] = quantity

    request.session['shopping_cart'] = shopping_cart
    print(request.session['shopping_cart'])
    print(request.session['shopping_cart'])
    return redirect(reverse('shopping_cart'))