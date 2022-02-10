from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

# Create your tests here.

class MyTest(APITestCase):

    def test_user_model(self):
        user = User.objects.create(username='test', email='test@test.com', password='test12345')

        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'test@test.com')
        self.assertFalse(user.is_staff)