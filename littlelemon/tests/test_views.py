from django.test import TestCase, Client
from restaurant.models import Menu
import json
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setup(self):
        self.menu_item1 = Menu.objects.create(title = "Tea", price = 6)
        self.menu_item2 = Menu.objects.create(title = "Coffee", price = 4)
        self.client = Client()
        
    def test_getall(self):
        menu_items = Menu.objects.all() 
        serialized_menu = MenuSerializer(menu_items, many = True)
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
