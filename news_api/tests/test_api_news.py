from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status

from news_api.models import UserProfile
from news_api.models import News


ROOT_URL = '/api/news/'
ITEM_URL = '/api/news/1/'


class NewsApiTests(TestCase):
    """Ensure authenticated users can manipulate their news objects"""

    def setUp(self):
        self.client = APIClient()
        self.user = UserProfile.objects.create(
            name='test', 
            email='test@mail.com', 
            password='1'
        )
        self.client.force_authenticate(user=self.user)
        self.data = {
            'title':'Zen of Python',
            'text':'Beautiful is better than ugly'
        }
        self.request = self.client.post(ROOT_URL, self.data)

    def test_create(self):
        self.assertEqual(self.request.status_code, status.HTTP_201_CREATED)

    def test_list(self):
        request = self.client.get(ROOT_URL)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_retrieve(self):
        request = self.client.get(ITEM_URL)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_update(self):
        request = self.client.put(ITEM_URL, self.data)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_partial_update(self):
        request = self.client.patch(ITEM_URL, self.data)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_delete(self):
        request = self.client.delete(ITEM_URL)
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)


class NotAuthNewsApiTests(TestCase):
    """Ensure no authenticated users can not manipulate news objects"""

    def setUp(self):
        self.client = APIClient()
        self.user = UserProfile.objects.create(
            name='test', 
            email='test@mail.com', 
            password='1'
        )
        self.data = {
            'title':'Zen of Python',
            'text':'Beautiful is better than ugly'
        }
        self.request = self.client.post(ROOT_URL, self.data)

    def test_create(self):
        self.assertEqual(self.request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list(self):
        request = self.client.get(ROOT_URL)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_retrieve(self):
        request = self.client.get(ITEM_URL)
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)

    def test_update(self):
        request = self.client.put(ITEM_URL, self.data)
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_partial_update(self):
        request = self.client.patch(ITEM_URL, self.data)
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete(self):
        request = self.client.delete(ITEM_URL)
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)


class NotOwnerNewsApiTests(TestCase):
    """Ensure that users do not manipulate other user's news objects"""

    def setUp(self):
        self.client = APIClient()
        self.user = UserProfile.objects.create(
            name='test', 
            email='test@mail.com', 
            password='1'
        )
        self.client.force_authenticate(user=self.user)
        self.data = {
            'title':'Zen of Python',
            'text':'Beautiful is better than ugly'
        }
        self.request = self.client.post(ROOT_URL, self.data)
        self.client.logout()

        self.user2 = UserProfile.objects.create(
            name='test2', 
            email='test2@mail.com', 
            password='1'
        )
        self.client.force_authenticate(user=self.user2)
        self.data2 = {
            'title':'Zen of Python2',
            'text':'Beautiful is better than ugly2'
        }
        self.request = self.client.post(ROOT_URL, self.data)

    def test_list(self):
        request = self.client.get(ROOT_URL)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_retrieve(self):
        request = self.client.get(ITEM_URL)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_update(self):
        request = self.client.put(ITEM_URL, self.data)
        self.assertEqual(request.status_code, status.HTTP_403_FORBIDDEN)

    def test_partial_update(self):
        request = self.client.patch(ITEM_URL, self.data)
        self.assertEqual(request.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete(self):
        request = self.client.delete(ITEM_URL)
        self.assertEqual(request.status_code, status.HTTP_403_FORBIDDEN)
