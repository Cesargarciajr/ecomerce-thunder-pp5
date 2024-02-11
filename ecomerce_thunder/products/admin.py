from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    """
    Product class to django admin
    """
    list_display = (
        'name',
        'category',
        'price',
        'stock_number',
        'image',
    )

    ordering = ('name',) # determining ordering to be displayed in the list

class CategoryAdmin(admin.ModelAdmin):
    """
    Category class to django admin
    """
    list_display = (
            'display_name',
            'name',
    )

# Added the classes to the admin django panel
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)