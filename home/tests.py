from django.test import TestCase, Client
from django.urls import reverse
from .models import contactMessage
from .forms import ContactForm

class ContactFormTests(TestCase):

    def test_valid_form(self):
        form_data = {
            'name': 'John',
            'surname': 'Doe',
            'email': 'john@example.com',
            'phone': '1234567890',
            'message': 'Test message'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_phone(self):
        form_data = {
            'name': 'John',
            'surname': 'Doe',
            'email': 'john@example.com',
            'phone': 'abc',
            'message': 'Test message'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('phone', form.errors.keys())
        self.assertEqual(form.errors['phone'][0], 'Phone number must contain only digits.')

class ContactViewTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_get_contact_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/contact.html')

    def test_post_contact_view(self):
        form_data = {
            'name': 'John',
            'surname': 'Doe',
            'email': 'john@example.com',
            'phone': '1234567890',
            'message': 'Test message'
        }
        response = self.client.post(reverse('contact'), form_data)
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertRedirects(response, reverse('home'))  # Redirects to home page
        self.assertEqual(contactMessage.objects.count(), 1)  # Checks if message was saved
