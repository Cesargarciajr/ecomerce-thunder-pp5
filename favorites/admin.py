from django.contrib import admin
from .models import myFavourites


class myFavouritesAdmin(admin.ModelAdmin):
    """
    My Favourites class to django admin
    """
    list_display = (
            'product',
            'user',
    )

# Added the classes to the admin django panel
admin.site.register(myFavourites, myFavouritesAdmin)