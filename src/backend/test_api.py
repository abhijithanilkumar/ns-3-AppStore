import json
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from apps.models import App


class AppSearchAPIViewTestCase(APITestCase):
	url = reverse("backend:search")

	def test_search(self):

		# exisiting application
		response = self.client.post(self.url, {'q':'gym', 'ns':'ns-3.29'})
		self.assertEqual(200, response.status_code)

		# when no params are passed, returns all the apps
		response = self.client.post(self.url)
		self.assertEqual(200, response.status_code)

		# random keyword, no such app found
		response = self.client.post(self.url, {'q':'abcdefghi', 'ns': 'ns-3.21'})
		self.assertTrue(len(json.loads(response.content)) == 0)

		# when keyword is empty, no app found
		response = self.client.post(self.url, {'ns': 'ns-3.21'})
		self.assertTrue(len(json.loads(response.content)) == 0)


class AppInstallAPIViewTestCase(APITestCase):
	url = reverse("backend:install")

	def test_install(self):
		
		response = self.client.post(self.url, {'module_name':'ns3-gym', 'ns':'ns-3.29'})
		self.assertEqual(404, response.status_code)

		response = self.client.post(self.url, {'module_name':'abcdeghi', 'ns':'[ns-3.29, ns-3.27]'})
		self.assertEqual(404, response.status_code)

		response = self.client.post(self.url, {'module_name':'abcdeghi', 'version': '1.10', 'ns':'[ns-3.29, ns-3.27]'})
		self.assertEqual(404, response.status_code)