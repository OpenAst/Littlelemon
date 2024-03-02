from django.tests import TestCase
from .views import MenuView, BookingView
from .serializers import MenuSerializer
from .models import Menu
from django.urls import reverse

class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(title='Menu_1', price=10.9, inventory=100)
        Menu.objects.create(name='Menu_2', price=10.5, inventory=50)
        Menu.objects.create(name='Menu_3', price=30.5, inventory=100)
        
    def test_get_item(self):
        response = self.client.get(reverse('menu'))
        serialized_data = MenuSerializer(Menu.objects.all(), many=True).data
        self.assertEqual(response.data, serialized_data)
            