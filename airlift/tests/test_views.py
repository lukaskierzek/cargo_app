from django.test import TestCase
from django.urls import reverse
from airlift.models import Destinations


class ViewsTest(TestCase):
    fixtures = ['airlift_fixture.json']

    def test_get_index_view(self):
        response = self.client.get(reverse('airlift:index_view'))
        self.assertEqual(response.status_code, 200)

    def test_get_destination_detail(self):
        response = self.client.get(reverse('airlift:destinations_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_get_destinations_list(self):
        response = self.client.get(reverse('airlift:destinations'))
        self.assertEqual(response.status_code, 200)

    def test_get_aircrafts_list(self):
        response = self.client.get(reverse('airlift:aircrafts'))
        self.assertEqual(response.status_code, 200)
