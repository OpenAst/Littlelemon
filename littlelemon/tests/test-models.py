from django.tests import TestCase
from .models import Menu, Booking

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=89, inventory=100)
        self.assertEqual(item, "IceCream : 80")