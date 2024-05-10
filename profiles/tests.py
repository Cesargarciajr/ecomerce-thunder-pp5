from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile
from django_countries.fields import Country

class UserProfileTests(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', password='12345'
        )

    def test_user_profile_creation(self):
        # Check that a UserProfile instance has been created
        self.assertTrue(UserProfile.objects.filter(user=self.user).exists())

    def test_user_profile_fields(self):
        # Access user profile
        profile = UserProfile.objects.get(user=self.user)
        # Set fields
        profile.default_phone_number = "123456789"
        profile.default_street_address1 = "123 Elm Street"
        profile.default_town_or_city = "Gotham"
        profile.default_country = Country('US')
        profile.save()
        # Fetch again to ensure data is saved
        profile = UserProfile.objects.get(user=self.user)
        # Verify fields
        self.assertEqual(profile.default_phone_number, "123456789")
        self.assertEqual(profile.default_street_address1, "123 Elm Street")
        self.assertEqual(profile.default_town_or_city, "Gotham")
        self.assertEqual(profile.default_country.code, 'US')

    def test_user_profile_str(self):
        # Check the string representation
        profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(str(profile), 'testuser')

    def test_profile_update_signal_on_user_creation(self):
        # Verify signal functionality on user creation
        new_user = User.objects.create_user('newuser', 'newpass')
        new_profile = UserProfile.objects.get(user=new_user)
        self.assertIsNotNone(new_profile)

    def test_profile_update_signal_on_user_update(self):
        # Verify signal functionality on updating user triggers profile save
        user = User.objects.get(username='testuser')
        user.first_name = 'UpdatedName'
        user.save()
        # Triggering user save should not create a new profile
        self.assertFalse(UserProfile.objects.filter(user=user).count() > 1)
