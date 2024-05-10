from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Product, Review, Rating

class TestModels(TestCase):

    def setUp(self):
        # Creating instances for the test
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password')
        self.category = Category.objects.create(name='Electronics', display_name='Electronic Goods')
        self.product = Product.objects.create(
            category=self.category,
            stock_number='SN123456',
            name='Laptop',
            description='A high performance laptop',
            price=999.99
        )
        self.review = Review.objects.create(
            product=self.product,
            user=self.user,
            comment='Great laptop!'
        )
        self.rating = Rating.objects.create(
            user=self.user,
            product=self.product,
            stars=5
        )

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Electronics')

    def test_product_str(self):
        self.assertEqual(str(self.product), 'Laptop')

    def test_review_str(self):
        self.assertEqual(str(self.review), f'Review Great laptop! by testuser')

    def test_rating_str(self):
        self.assertEqual(self.rating.number_of_stars(), 5)

    def test_get_display_name(self):
        self.assertEqual(self.category.get_display_name(), 'Electronic Goods')

    def test_category_verbose_name_plural(self):
        self.assertEqual(self.category._meta.verbose_name_plural, 'Categories')

    def test_review_ordering(self):
        new_review = Review.objects.create(
            product=self.product,
            user=self.user,
            comment='Okay performance.'
        )
        reviews = list(Review.objects.all())
        self.assertTrue(reviews.index(new_review) > reviews.index(self.review))

