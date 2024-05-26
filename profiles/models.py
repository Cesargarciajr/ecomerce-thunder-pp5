from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from profiles.models import UserProfile

class ProfilesAppTests(TestCase):
    def setUp(self):
        User = get_user_model()
        # Create a test user if it doesn't exist
        self.user, created = User.objects.get_or_create(
            username='testuser', email='test@example.com', password='password'
        )
        # Check if UserProfile already exists for the user
        if not hasattr(self.user, 'userprofile'):
            # Create a test profile
            self.profile = UserProfile.objects.create(
                user=self.user,
                default_phone_number='1234567890',
                default_street_address1='123 Test St',
                default_town_or_city='Test City',
                default_county='Test County',
                default_postcode='12345',
                default_country='US'
            )

    def test_profile_view(self):
        # Log in as the test user
        self.client.login(username='testuser', password='password')

        # Test profile view
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

        # Check if profile data is displayed
        self.assertContains(response, '1234567890')  # Check if phone number is displayed
        self.assertContains(response, '123 Test St')  # Check if street address is displayed
        # Add more assertions to check other fields as needed

        # Test profile update
        updated_data = {
            'default_phone_number': '9876543210',
            'default_street_address1': '456 Updated St',
            # Add more updated fields as needed
        }
        response = self.client.post(reverse('profile'), updated_data)
        self.assertEqual(response.status_code, 302)  # Check if redirect happens after profile update

        # Check if profile data is updated in the database
        updated_profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(updated_profile.default_phone_number, '9876543210')
        self.assertEqual(updated_profile.default_street_address1, '456 Updated St')
        # Add more assertions to check other updated fields as needed

    def test_order_history_view(self):
        # Test order history view
        # You may need to update this test according to your actual implementation
        # For now, let's just check if the URL can be accessed
        response = self.client.get(reverse('order_history', args=['dummy-order-number']))
        self.assertEqual(response.status_code, 200)
