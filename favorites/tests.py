from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from products.models import Product
from favorites.models import myFavourites

class MyFavouritesTests(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Create a test product
        self.product = Product.objects.create(name='Test Product', price=10.0)

    def test_view_my_favourites(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')
        # Add a product to favourites
        myFavourites.objects.create(product=self.product, user=self.user)
        # Send a GET request to view my favourites
        response = self.client.get(reverse('view_my_favourites'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_favourites/my_favourites.html')
        self.assertContains(response, self.product.name)

    def test_add_to_favourites(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')
        # Send a POST request to add the product to favourites
        response = self.client.post(reverse('add_to_favourites', args=[self.product.id]))
        self.assertRedirects(response, reverse('products'))
        self.assertTrue(myFavourites.objects.filter(product=self.product, user=self.user).exists())

    def test_add_to_favourites_already_exists(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')
        # Add the product to favourites
        myFavourites.objects.create(product=self.product, user=self.user)
        # Send a POST request to add the product to favourites again
        response = self.client.post(reverse('add_to_favourites', args=[self.product.id]))
        self.assertRedirects(response, reverse('products'))
        self.assertContains(response, 'This product is already in your favourites!')

    def test_remove_from_favourites(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')
        # Add the product to favourites
        myFavourites.objects.create(product=self.product, user=self.user)
        # Send a POST request to remove the product from favourites
        response = self.client.post(reverse('remove_from_favourites', args=[self.product.id]))
        self.assertRedirects(response, reverse('view_my_favourites'))
        self.assertFalse(myFavourites.objects.filter(product=self.product, user=self.user).exists())

    def test_remove_from_favourites_not_exists(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')
        # Send a POST request to remove the product from favourites which is not in the list
        response = self.client.post(reverse('remove_from_favourites', args=[self.product.id]))
        self.assertRedirects(response, reverse('view_my_favourites'))
        self.assertContains(response, 'This product is not in your favourites!')

    def tearDown(self):
        self.user.delete()
        self.product.delete()
