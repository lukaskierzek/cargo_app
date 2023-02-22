from django.test import TestCase
from airlift.models import PilotsInformations, Pilots


class AirliftCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.pilot = Pilots.objects.create(
            first_name='Jan',
            last_name='Kowalski'
        )

        cls.pilot_info = PilotsInformations.objects.create(
            pilot_id=1,
            position='First officer',
            rank='Captain',
            age=35,
            country='Poland'
        )

    def test_pilot_first_name(self):
        self.assertEqual(self.pilot._meta.get_field('first_name').max_length, 50)
        self.assertEqual(self.pilot._meta.get_field('first_name').help_text, "Enter a pilot first name")
        self.assertEqual(self.pilot._meta.get_field('first_name').verbose_name, "Pilot first name")
        self.assertEqual(self.pilot.first_name, "Jan")

    def test_pilot_last_name(self):
        self.assertEqual(self.pilot._meta.get_field('last_name').max_length, 50)
        self.assertEqual(self.pilot._meta.get_field('last_name').help_text, "Enter a pilot last name")
        self.assertEqual(self.pilot._meta.get_field('last_name').verbose_name, "Pilot last name")
        self.assertEqual(self.pilot.last_name, "Kowalski")

    def test_pilot___str__(self):
        self.assertEqual(
            self.pilot.__str__(),
            f"{self.pilot.first_name} {self.pilot.last_name}"
        )

    def test_pilot_meta(self):
        self.assertEqual(self.pilot._meta.verbose_name, "Pilot information")
        self.assertEqual(self.pilot._meta.verbose_name_plural, "Pilots informations")

    def test_pilot_info_position(self):
        self.assertEqual(self.pilot_info._meta.get_field('position').max_length, 50)
        self.assertEqual(self.pilot_info._meta.get_field('position').help_text, "Enter a pilot position")
        self.assertEqual(self.pilot_info._meta.get_field('position').verbose_name, "Pilot position")
        self.assertEqual(self.pilot_info.position, "First officer")

    def test_pilot_info_rank(self):
        self.assertEqual(self.pilot_info._meta.get_field('rank').max_length, 50)
        self.assertEqual(self.pilot_info._meta.get_field('rank').help_text, "Enter a pilot rank")
        self.assertEqual(self.pilot_info._meta.get_field('rank').verbose_name, "Pilot rank")
        self.assertEqual(self.pilot_info.rank, "Captain")

    def test_pilot_info_age(self):
        self.assertEqual(self.pilot_info._meta.get_field('age').max_length, 50)
        self.assertEqual(self.pilot_info._meta.get_field('age').help_text, "Enter a pilot age")
        self.assertEqual(self.pilot_info._meta.get_field('age').verbose_name, "Pilot age")
        self.assertEqual(self.pilot_info.age, 35)

    def test_pilot_info_country(self):
        self.assertEqual(self.pilot_info._meta.get_field('country').max_length, 50)
        self.assertEqual(self.pilot_info._meta.get_field('country').help_text, "Enter a pilot country")
        self.assertEqual(self.pilot_info._meta.get_field('country').verbose_name, "Pilot country")
        self.assertEqual(self.pilot_info.country, "Poland")

    def test_pilot_info___str__(self):
        self.assertEqual(
            self.pilot_info.__str__(),
            f"{self.pilot_info.position}\n{self.pilot_info.rank}\n{self.pilot_info.age}\n{self.pilot_info.country}"
        )

    def test_pilot_info_meta(self):
        self.assertEqual(self.pilot_info._meta.verbose_name, "Pilot additional information")
        self.assertEqual(self.pilot_info._meta.verbose_name_plural, "Pilot additional informations")
