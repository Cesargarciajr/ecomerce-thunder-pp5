from django.db import models

class contactMessage(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    surname = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(null=False, blank=False)
    message = models.CharField(max_length=300, null=False, blank=False)
