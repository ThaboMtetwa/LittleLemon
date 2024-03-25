from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer  # Corrected import

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create test instances of the Menu model
        Menu.objects.create(title='Item 1', price=10.99, inventory=20)
        Menu.objects.create(title='Item 2', price=15.99, inventory=30)
        Menu.objects.create(title='Item 3', price=8.99, inventory=25)

    def test_getall(self):
        # Retrieve all Menu objects
        response = self.client.get(reverse('menu-list'))
        menus = Menu.objects.all()
        serializer = MenuItemSerializer(menus, many=True)  # Corrected serializer name
        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if the serialized data equals the response data
        self.assertEqual(response.data, serializer.data)
