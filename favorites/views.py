from django.shortcuts import render
from favorites.models import myFavourites
from products.models import Product
from django.contrib.auth.models import User

# Create your views here.

def view_my_favourites(request):
    """ A view that renders the my favourites contents page """
    my_favourite_item = myFavourites.objects.all()
    print(my_favourite_item)
    return render(request, 'my_favourites/my_favourites.html', {'myFavourites': my_favourite_item})

    