from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q # optimises search criteria for name or description
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None

    if request.GET: # checkinf if there is a search being made at the search bar/form 
        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(request, "Please enter a search!")
                return redirect(reverse('products'))

            # checking if search criteria is in the name or description of a product. the 'icontains' make it case-insentive
            queries = Q(name__icontains=query) | Q(description__icontains=query) 
            products = products.filter(queries)

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)