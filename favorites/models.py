from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.

class myFavourites(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.product