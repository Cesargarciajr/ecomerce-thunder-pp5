from django.contrib import admin
from .models import contactMessage


class ContactAdmin(admin.ModelAdmin):
    """
    Review class to django admin
    """
    list_display = (
            'created_at',
            'name',
            'surname',
            'phone',
            'email',
            'message',
    )
    ordering = ['-created_at']

# Register your models here.
admin.site.register(contactMessage, ContactAdmin)