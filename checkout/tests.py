from django.test import TestCase
from django.conf import settings
from django.utils import timezone
from decimal import Decimal
import uuid

from profiles.models import UserProfile
from products.models import Product
from .models import Order, OrderLineItem

class OrderModelTests(TestCase):

    def setUp(self):
        # Create a test user profile and product
        self.user_profile = UserProfile.objects.create(user_id=1, full_name='John Doe')
        self.product = Product.objects.create(name='Test Product', price=Decimal('100.00'))
        self.order = Order.objects.create(
            user_profile=self.user_profile,
            full_name='John Doe',
            email='john@example.com',
            phone_number='0123456789',
            country='US',
            town_or_city='New York',
            street_address1='123 Fake Street',
            original_shopping_cart='{}',
            stripe_pid='unique_pid'
        )

    def test_order_number_generation(self):
        # Test the automatic order number generation
        order = Order(user_profile=self.user_profile)
        order.save()
        self.assertTrue(isinstance(order.order_number, str))
        self.assertEqual(len(order.order_number), 32)

    def test_order_update_total(self):
        # Create line item and update order total
        line_item = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=2
        )
        self.order.update_total()
        expected_total = Decimal('200.00')  # 2 * 100.00
        self.assertEqual(self.order.order_total, expected_total)

        # Test delivery cost logic
        settings.FREE_DELIVERY_THRESHOLD = Decimal('300.00')
        settings.STANDARD_DELIVERY_PERCENTAGE = Decimal('10.00')
        self.order.update_total()
        expected_delivery_cost = expected_total * Decimal('0.10')
        self.assertEqual(self.order.delivery_cost, expected_delivery_cost)

    def test_order_string_representation(self):
        self.assertEqual(str(self.order), self.order.order_number)

    def test_order_line_item_creation_and_calculation(self):
        line_item = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=1
        )
        line_item.save()
        self.assertEqual(line_item.lineitem_total, Decimal('100.00'))

    def test_order_line_item_string_representation(self):
        line_item = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=1
        )
        expected_string = f'Stock Number {self.product.stock_number} on order {self.order.order_number}'
        self.assertEqual(str(line_item), expected_string)
