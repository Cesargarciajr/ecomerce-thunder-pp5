from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from favorites.models import myFavourites
from products.models import Product


@login_required
def view_my_favourites(request):
    """ A view that renders the my favourites contents page """
    # Filtrar os itens de favoritos do usuário logado
    my_favourite_items = myFavourites.objects.filter(user=request.user)
    return render(request, 'my_favourites/my_favourites.html', {'myFavourites': my_favourite_items})

@login_required
def add_to_favourites(request, product_id):
    """ A view to add product to my favourites """
    product = get_object_or_404(Product, pk=product_id)
    user = request.user

    if myFavourites.objects.filter(product=product, user=user).exists():
        messages.info(request, 'This product is already in your favourites!')
    else:
        favourite_product = myFavourites.objects.create(product=product, user=user)
        messages.success(request, f'Added {product.name} to your favourites!')
    
    return redirect(reverse('products'))


@login_required
def remove_from_favourites(request, product_id):
    """ A view to remove product from my favourites """
    product = get_object_or_404(Product, pk=product_id)
    user = request.user

    favourite_item = myFavourites.objects.filter(product=product, user=user).first()
    if favourite_item:
        favourite_item.delete()
        messages.success(request, f'Removed {product.name} from your favourites!')
    else:
        messages.info(request, 'This product is not in your favourites!')

    return redirect(reverse('view_my_favourites'))