from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product, Category, Review
from .forms import ProductForm


class ProductsAppTests(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', email='test@example.com', password='password'
        )

        # Create a test category
        self.category = Category.objects.create(
            name='Test Category', display_name='Test Category Display Name'
        )

        # Create a test product
        self.product = Product.objects.create(
            category=self.category,
            stock_number='12345',
            name='Test Product',
            description='Test Product Description',
            price=10.99,
            image_url='http://example.com/image.jpg',
            image='path/to/image.jpg'
        )

        # Create a test review
        self.review = Review.objects.create(
            product=self.product,
            user=self.user,
            comment='Test Comment',
            stars=5
        )

    def test_all_products_view(self):
        # Test all products view
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)
        self.assertContains(response, self.category.display_name)

    def test_product_detail_view(self):
        # Test product detail view
        response = self.client.get(reverse('product_detail', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)
        self.assertContains(response, self.product.description)
        self.assertContains(response, self.review.comment)


