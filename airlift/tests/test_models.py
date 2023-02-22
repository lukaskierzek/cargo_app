from django.test import TestCase
from airlift.models import PilotsInformations


class PilotsInformationsCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.pilot = Pilots.objects.create(

        )

        cls.pilot_info = PilotsInformations.objects.create(
            pilot_id=1,
            position='First officer',
            rank='Captain',
            age=35,
            country='Poland'
        )

    def test_pilot_id(self):
        self.assertEqual(self.pilot_info.pilot_id, 1)

    def test_position(self):
        self.assertEqual(self.pilot_info._meta.get_field('position').max_length, 50)
        self.assertEqual(self.pilot_info._meta.get_field('position').help_text, "Enter a pilot position")
        self.assertEqual(self.pilot_info._meta.get_field('position').verbose_name, "Pilot position")
        self.assertEqual(self.pilot_info.position, "First officer")

    def test_rank(self):
        self.assertEqual(self.pilot_info._meta.get_field('rank').max_length, 50)
        self.assertEqual(self.pilot_info._meta.get_field('rank').help_text, "Enter a pilot rank")
        self.assertEqual(self.pilot_info._meta.get_field('rank').verbose_name, "Pilot rank")
        self.assertEqual(self.pilot_info.rank, "Captain")

    def test_age(self):
        self.assertEqual(self.pilot_info._meta.get_field('age').max_length, 50)
        self.assertEqual(self.pilot_info._meta.get_field('age').help_text, "Enter a pilot age")
        self.assertEqual(self.pilot_info._meta.get_field('age').verbose_name, "Pilot age")
        self.assertEqual(self.pilot_info.age, 35)

    def test_country(self):
        self.assertEqual(self.pilot_info._meta.get_field('country').max_length, 50)
        self.assertEqual(self.pilot_info._meta.get_field('country').help_text, "Enter a pilot country")
        self.assertEqual(self.pilot_info._meta.get_field('country').verbose_name, "Pilot country")
        self.assertEqual(self.pilot_info.country, "Poland")

    def test___str__(self):
        self.assertEqual(
            self.pilot_info.__str__(),
            f"{self.pilot_info.position}\n{self.pilot_info.rank}\n{self.pilot_info.age}\n{self.pilot_info.country}"
        )

    def test_meta(self):
        self.assertEqual(self.pilot_info._meta.verbose_name, "Pilot information")
        self.assertEqual(self.pilot_info._meta.verbose_name_plural, "Pilots informations")
