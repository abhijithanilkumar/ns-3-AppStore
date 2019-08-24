import json
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from apps.models import App, NsRelease, Release
from django.core.files.uploadedfile import SimpleUploadedFile


class AppSearchAPIViewTestCase(APITestCase):
	url = reverse("backend:search")

	def setUp(self):
		DApp = App.objects.create(name='ns-3-gym',
							title='Gym',
							app_type='F',
							abstract='This is a test App for Development',
							description='This is a test App for Development')

		ns=NsRelease.objects.create(name='ns-3.29',url='https://www.nsnam.org/')
		Release.objects.create(app=DApp,version='TestVersion',require=ns,date= '2018-12-27',notes= 'TestNote',filename = SimpleUploadedFile('filename.txt',''),url='https://www.nsnam.org/')

	def test_search(self):
		"""
		Test to verify the search API Functionality
		"""
		# exisiting application
		response = self.client.post(self.url, {'q':'gym', 'ns':'ns-3.29'})
		self.assertEqual(200, response.status_code)

		# when no params are passed, returns all the apps
		response = self.client.post(self.url)
		self.assertEqual(200, response.status_code)
		self.assertTrue(len(json.loads(response.content)) > 0)

		# random keyword, no such app found
		response = self.client.post(self.url, {'q':'abcdefghi', 'ns': 'ns-3.21'})
		self.assertTrue(len(json.loads(response.content)) == 0)

		# when keyword is empty, no app found
		response = self.client.post(self.url, {'ns': 'ns-3.21'})
		self.assertTrue(len(json.loads(response.content)) == 0)


class AppInstallAPIViewTestCase(APITestCase):
	url = reverse("backend:install")

	def setUp(self):
		DApp = App.objects.create(name='ns3-gym',
							title='Gym',
							app_type='F',
							abstract='This is a test App for Development',
							description='This is a test App for Development')

		ns=NsRelease.objects.create(name='3.29',url='https://www.nsnam.org/')
		Release.objects.create(app=DApp,version='TestVersion',require=ns,date= '2018-12-27',notes= 'TestNote',filename = SimpleUploadedFile('filename.txt',''),url='https://www.nsnam.org/')


	def test_install(self):
		"""
		Test to verify the install API Functionality
		"""

		# when the app exists
		response = self.client.post(self.url, {'module_name':'ns3-gym', 'ns':'ns-3.29'})
		self.assertEqual(200, response.status_code)

		# app exists, with multiple ns versions
		response = self.client.post(self.url, {'module_name':'ns3-gym', 'ns':'[ns-3.29, ns-3.27]'})
		self.assertEqual(200, response.status_code)

		# random keyword, no such app found
		response = self.client.post(self.url, {'module_name':'abcdeghi', 'ns':'[ns-3.29, ns-3.27]'})
		self.assertEqual(404, response.status_code)

		# random with multiple ns versions, no such app found
		response = self.client.post(self.url, {'module_name':'abcdeghi', 'version': '1.10', 'ns':'[ns-3.29, ns-3.27]'})
		self.assertEqual(404, response.status_code)