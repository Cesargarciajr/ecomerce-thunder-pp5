from django.urls import path
from . import views

urlpatterns = [
    path('view_my_favourites/', views.view_my_favourites, name='view_my_favourites'),
    path('remove_from_favourites/<int:product_id>/', views.remove_from_favourites, name='remove_from_favourites'),
]