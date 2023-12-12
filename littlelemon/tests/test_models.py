from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(name="IceCream", price=80)
        self.assertEqual(item.name, "IceCream")
        self.assertEqual(item.price, 80)

# python manage.py test