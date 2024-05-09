from django.contrib import admin
from .models import Product, Category, Review

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

class ReviewAdmin(admin.ModelAdmin):
    """
    Review class to django admin
    """
    list_display = (
            'product',
            'comment',
            'stars',
            'created_on',
            'user',
    )


# Added the classes to the admin django panel
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)