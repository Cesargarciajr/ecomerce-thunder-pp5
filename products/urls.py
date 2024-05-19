from django.urls import path
from . import views
from favorites.views import add_to_favourites


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('add_to_favourites/<int:product_id>/', add_to_favourites, name='add_to_favourites'),
]
