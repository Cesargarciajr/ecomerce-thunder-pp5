from django.db import models
from profiles.models import UserProfile
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    
    class Meta:
        verbose_name_plural = 'Categories' # Fixing how 'Categories' will be displayed on Django Admin

    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    stock_number = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, blank=False, null=False)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    image_url = models.URLField(max_length=1024, null=False, blank=False)
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=300, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    stars = models.IntegerField(default=0)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review {self.comment} by {self.user.username}"

    def number_of_stars(self):
        return self.stars
