from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Account
from rest_framework import status


class AccountsTest(APITestCase):
    def setUp(self):
        self.test_account = Account.objects.create_user('Test_First_Name',
                                                        'Test_Last_Name',
                                                        'test_user@example.com',
                                                        'Password')

        # URL for creating an account.
        self.create_url = reverse('register')

    def test_create_account(self):
        """
        Ensure we can create a new user and a valid token is created with it.
        """
        data = {
            'first_name':'Test_First_Name_1',
            'last_name': 'Test_Last_Name_1',
            'email': 'test_email_1@example.com',
            'password': 'Password'
        }

        response = self.client.post(self.create_url, data, format='json')

        # We want to make sure we have two users in the database.
        self.assertEqual(Account.objects.count(), 2)
        # And that we're returning a 201 created code.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['first_name'], data['first_name'])
        self.assertEqual(response.data['last_name'], data['last_name'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertFalse('password' in response.data)