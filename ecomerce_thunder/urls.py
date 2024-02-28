"""
URL configuration for ecomerce_thunder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), # including all allauth urls to main url project
    path('', include('home.urls')), # including all urls from home app that renders index.html
    path('products/', include('products.urls')), # including all urls from products app that renders its templates
    path('shopping_cart/', include('shopping_cart.urls')), # including all urls from shopping_cart app that renders its templates
    path('checkout/', include('checkout.urls')), # including all urls from checkout app that renders its templates
    path('profiles/', include('profiles.urls'),) # including all urls from profiles app that renders its templates
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
