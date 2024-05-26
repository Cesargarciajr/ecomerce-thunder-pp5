from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django_countries.fields import Country
from django.conf import settings
from django.db import IntegrityError

from products.models import Product
from profiles.models import UserProfile
from .models import Order, OrderLineItem
from .forms import OrderForm


class OrderModelTest(TestCase):

    def setUp(self):
        try:
            user = User.objects.create(username='testuser')
            self.user_profile = UserProfile.objects.create(user=user)
        except IntegrityError:
            self.user_profile = UserProfile.objects.get(user__username='testuser')
        self.product = Product.objects.create(name='Test Product', price=100, stock_number='12345')
        self.order = Order.objects.create(
            user_profile=self.user_profile,
            full_name='Test User',
            email='test@example.com',
            phone_number='1234567890',
            country='US',
            town_or_city='Test City',
            street_address1='123 Test St',
            postcode='12345',
        )

    def test_generate_order_number(self):
        order_number = self.order._generate_order_number()
        self.assertTrue(len(order_number), 32)
        self.assertTrue(order_number.isupper())

    def test_update_total(self):
        OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=2,
        )
        self.order.update_total()
        self.assertEqual(self.order.order_total, 200)
        if self.order.order_total < settings.FREE_DELIVERY:
            self.assertEqual(self.order.delivery_cost, self.order.order_total * settings.STANDARD_DELIVERY / 100)
        else:
            self.assertEqual(self.order.delivery_cost, 0)
        self.assertEqual(self.order.grand_total, self.order.order_total + self.order.delivery_cost)

    def test_save_method(self):
        self.order.save()
        self.assertIsNotNone(self.order.order_number)
        self.assertEqual(len(self.order.order_number), 32)


class OrderLineItemModelTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(name='Test Product', price=100, stock_number='12345')
        self.order = Order.objects.create(
            full_name='Test User',
            email='test@example.com',
            phone_number='1234567890',
            country='US',
            town_or_city='Test City',
            street_address1='123 Test St',
            postcode='12345',
        )
        self.order_line_item = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=2,
        )

    def test_save_method(self):
        self.order_line_item.save()
        self.assertEqual(self.order_line_item.lineitem_total, 200)


class CheckoutViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.product = Product.objects.create(name='Test Product', price=100, stock_number='12345')
        self.client.login(username='testuser', password='testpass')

    def test_checkout_view_get(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

        form_data = {
            'full_name': 'Test User',
            'email': 'test@example.com',
            'phone_number': '1234567890',
            'country': 'US',
            'postcode': '12345',
            'town_or_city': 'Test City',
            'street_address1': '123 Test St',
            'street_address2': '',
            'county': '',
            'client_secret': 'test_client_secret'
        }

        response = self.client.post(reverse('checkout'), data=form_data)
        self.assertRedirects(response, reverse('checkout_success', args=[Order.objects.first().order_number]))


    def test_checkout_success_view(self):
        order = Order.objects.create(
            full_name='Test User',
            email='test@example.com',
            phone_number='1234567890',
            country='US',
            town_or_city='Test City',
            street_address1='123 Test St',
            postcode='12345',
        )
        response = self.client.get(reverse('checkout_success', args=[order.order_number]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')

    def test_cache_checkout_data_view(self):
        session = self.client.session
        session['shopping_cart'] = {self.product.id: 1}
        session.save()

        response = self.client.post(reverse('cache_checkout_data'), data={'client_secret': 'test_secret', 'save_info': True})
        self.assertEqual(response.status_code, 200)


class OrderFormTest(TestCase):

    def test_order_form_valid(self):
        form_data = {
            'full_name': 'Test User',
            'email': 'test@example.com',
            'phone_number': '1234567890',
            'country': 'US',
            'postcode': '12345',
            'town_or_city': 'Test City',
            'street_address1': '123 Test St',
            'street_address2': '',
            'county': '',
        }
        form = OrderForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_order_form_invalid(self):
        form_data = {
            'full_name': '',
            'email': 'test@example.com',
        }
        form = OrderForm(data=form_data)
        self.assertFalse(form.is_valid())
