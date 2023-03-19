from django.test import TestCase
from django.urls import reverse
from airlift.models import Destinations


class ViewsTest(TestCase):
    fixtures = ['airlift_fixture.json']

    # ----------tests for main page---------- #

    def test_get_index_view(self):
        response = self.client.get(reverse('airlift:index_view'))
        self.assertEqual(response.status_code, 200)

    # ----------tests for Destinations---------- #

    def test_get_destination_detail(self):
        response = self.client.get(reverse('airlift:destinations_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_get_destinations_list(self):
        response = self.client.get(reverse('airlift:destinations'))
        self.assertEqual(response.status_code, 200)

    # ----------tests for Aircrafts---------- #

    def test_get_aircraft_detail(self):
        response = self.client.get(reverse('airlift:aircrafts_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_get_aircrafts_list(self):
        response = self.client.get(reverse('airlift:aircrafts'))
        self.assertEqual(response.status_code, 200)

    # ----------tests for Pilots---------- #

    def test_get_pilot_detail(self):
        response = self.client.get(reverse('airlift:pilots_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_get_pilots_list(self):
        response = self.client.get(reverse('airlift:pilots'))
        self.assertEqual(response.status_code, 200)

    # ----------tests for Cargos---------- #

    def test_get_cargo_detail(self):
        response = self.client.get(reverse('airlift:cargos_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_get_cargos_list(self):
        response = self.client.get(reverse('airlift:cargos'))
        self.assertEqual(response.status_code, 200)
