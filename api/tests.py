## Django
from django.test import TestCase, Client
from django.conf import settings
from django.contrib.auth.models import User

## DRF:
from rest_framework.reverse import reverse

## Tangent:
from tokenauth.authbackends import TokenAuthBackend
from .api import Expense

## Global:
import requests, responses, json

## Here's some example test code to get you started ..

def mock_auth_success():

	url = '{0}/api/v1/users/me/' . format(settings.USERSERVICE_BASE_URL)		
	response_string = '{"username": "TEST"}'
	responses.add(responses.GET, url,
              body=response_string, status=200,
              content_type='application/json')

def mock_auth_failure():

	url = '{0}/api/v1/users/me/' . format(settings.USERSERVICE_BASE_URL)		
	responses.add(responses.GET, url,
              body='', status=401,
              content_type='application/json')

class TokenAuthBackendTestCase(TestCase):

	def setUp(self):
		self.c = Client(Authorization='Token 123')

		self.joe = User.objects.create_user(username='joe_normal', password='test')
		self.joe_admin = User.objects.create_superuser(username='joe_admin', email='joe@example.com', password='test')

	@responses.activate
	def test_token_auth_works(self):

		mock_auth_success()
		url = reverse('expense-list')
		response = self.c.get(url)
		assert response.status_code == 200, 'Expect 200 OK'


	@responses.activate
	def test_get_entry_list_requires_auth(self):

		mock_auth_failure()
		url = reverse('expense-list')
		response = self.c.get(url)
		assert response.status_code == 403, 'Expect permission denied'
	
	def test_get_entry_list_returns_only_logged_in_users_details(self):

		Expense.quick_create(user=self.joe.pk)
		Expense.quick_create(user=self.joe_admin.pk)

		self.c.login(username="joe_normal", password="test")

		url = reverse('expense-list')		
		response = self.c.get(url)			
		assert response.status_code == 200, 'Expect 200 OK'

		jresponse = json.loads(response.content)
		assert len(jresponse) == 1, 'Should only return a single result'
		assert jresponse[0].get("user") == str(self.joe.pk), 'Only return Joe normal\'s Expenses'

	def test_get_entry_list_returns_all_expenses_if_admin(self):

		Expense.quick_create(user=self.joe.pk)
		Expense.quick_create(user=self.joe_admin.pk)

		self.c.login(username="joe_admin", password="test")

		url = reverse('expense-list')		
		response = self.c.get(url)			
		assert response.status_code == 200, 'Expect 200 OK'

		jresponse = json.loads(response.content)
		assert len(jresponse) == 2, 'Should return all results'
		


