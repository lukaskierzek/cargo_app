from django.test import TestCase
from airlift.models import PilotsInformations, Pilots, Aircrafts, Destinations, Cargos


class AirliftCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.cargo = Cargos.objects.create(
            name='MGM-140 ATACMS',
            quantity=1000
        )

        cls.destination = Destinations.objects.create(
            from_airport='Rzeszów International Airport',
            to_airport='John Paul II International Airport Kraków-Balice'
        )

        cls.aircraft = Aircrafts.objects.create(
            name='Lockheed C-130 Hercules',
            country='Poland',
            destination_id=1
        )

        cls.pilot = Pilots.objects.create(
            first_name='Jan',
            last_name='Kowalski',
            aircraft_id=1
        )

        cls.pilot_info = PilotsInformations.objects.create(
            pilot_id=1,
            position='First officer',
            rank='Captain',
            age=35,
            country='Poland'
        )

    # ----------tests for Cargos---------- #

    def test_cargo_name(self):
        self.assertEqual(self.cargo._meta.get_field('name').max_length, 255)
        self.assertEqual(self.cargo._meta.get_field('name').help_text, "Enter a cargo name.")
        self.assertEqual(self.cargo._meta.get_field('name').verbose_name, "Cargo name")
        self.assertEqual(self.cargo.name, "MGM-140 ATACMS")

    def test_cargo_quantity(self):
        self.assertEqual(self.cargo._meta.get_field('quantity').help_text, "Enter a cargo quantity.")
        self.assertEqual(self.cargo._meta.get_field('quantity').verbose_name, "Cargo quantity")
        self.assertEqual(self.cargo.quantity, 1000)

    def test_cargo___str__(self):
        self.assertEqual(self.cargo.__str__(), f"{self.cargo.name}: {self.cargo.quantity}")

    def test_cargo_meta(self):
        self.assertEqual(self.cargo._meta.verbose_name, "Cargo")
        self.assertEqual(self.cargo._meta.verbose_name_plural, "Cargos")

    # ----------tests for Destinations---------- #

    def test_destination_from_airport(self):
        self.assertEqual(self.destination._meta.get_field('from_airport').max_length, 255)
        self.assertEqual(
            self.destination._meta.get_field('from_airport').help_text,
            "Enter a airport name from the plane will take off."
        )
        self.assertEqual(
            self.destination._meta.get_field('from_airport').verbose_name,
            "Airport name from the plane will take off"
        )
        self.assertEqual(self.destination.from_airport, "Rzeszów International Airport")

    def test_destination_to_airport(self):
        self.assertEqual(self.destination._meta.get_field('to_airport').max_length, 255)
        self.assertEqual(
            self.destination._meta.get_field('to_airport').help_text,
            "Enter a airport name where the plane will land."
        )
        self.assertEqual(
            self.destination._meta.get_field('to_airport').verbose_name,
            "Airport name where the plane will land"
        )
        self.assertEqual(self.destination.to_airport, "John Paul II International Airport Kraków-Balice")

    def test_destination___str__(self):
        self.assertEqual(
            self.destination.__str__(),
            f"{self.destination.from_airport} - {self.destination.to_airport}"
        )

    def test_destination_meta(self):
        self.assertEqual(self.destination._meta.verbose_name, "Destination")
        self.assertEqual(self.destination._meta.verbose_name_plural, "Destinations")

    # ----------tests for Aircrafts---------- #

    def test_aircraft_name(self):
        self.assertEqual(self.aircraft._meta.get_field('name').max_length, 255)
        self.assertEqual(self.aircraft._meta.get_field('name').help_text, "Enter a aircraft name.")
        self.assertEqual(self.aircraft._meta.get_field('name').verbose_name, "Aircraft name")
        self.assertEqual(self.aircraft.name, "Lockheed C-130 Hercules")

    def test_aircraft_country(self):
        self.assertEqual(self.aircraft._meta.get_field('country').max_length, 255)
        self.assertEqual(
            self.aircraft._meta.get_field('country').help_text,
            "Enter a country name that owns the aircraft."
        )
        self.assertEqual(self.aircraft._meta.get_field('country').verbose_name, "Country name that owns the aircraft")
        self.assertEqual(self.aircraft.country, 'Poland')

    def test_aircraft_destination(self):
        self.assertEqual(self.aircraft.destination_id, 1)

    def test_aircraft___str__(self):
        self.assertEqual(self.aircraft.__str__(), f"{self.aircraft.name} ({self.aircraft.country})")

    def test_aircraft_meta(self):
        self.assertEqual(self.aircraft._meta.verbose_name, "Aircraft")
        self.assertEqual(self.aircraft._meta.verbose_name_plural, "Aircrafts")

    # ----------tests for Pilots---------- #

    def test_pilot_first_name(self):
        self.assertEqual(self.pilot._meta.get_field('first_name').max_length, 255)
        self.assertEqual(self.pilot._meta.get_field('first_name').help_text, "Enter a pilot first name.")
        self.assertEqual(self.pilot._meta.get_field('first_name').verbose_name, "Pilot first name")
        self.assertEqual(self.pilot.first_name, "Jan")

    def test_pilot_last_name(self):
        self.assertEqual(self.pilot._meta.get_field('last_name').max_length, 255)
        self.assertEqual(self.pilot._meta.get_field('last_name').help_text, "Enter a pilot last name.")
        self.assertEqual(self.pilot._meta.get_field('last_name').verbose_name, "Pilot last name")
        self.assertEqual(self.pilot.last_name, "Kowalski")

    def test_pilot_aircraft(self):
        self.assertEqual(self.pilot.aircraft_id, 1)

    def test_pilot___str__(self):
        self.assertEqual(
            self.pilot.__str__(),
            f"{self.pilot.first_name} {self.pilot.last_name}"
        )

    def test_pilot_meta(self):
        self.assertEqual(self.pilot._meta.verbose_name, "Pilot information")
        self.assertEqual(self.pilot._meta.verbose_name_plural, "Pilots informations")

    # ----------tests for PilotsInformations---------- #

    def test_pilot_info_position(self):
        self.assertEqual(self.pilot_info._meta.get_field('position').max_length, 255)
        self.assertEqual(self.pilot_info._meta.get_field('position').help_text, "Enter a pilot position.")
        self.assertEqual(self.pilot_info._meta.get_field('position').verbose_name, "Pilot position")
        self.assertEqual(self.pilot_info.position, "First officer")

    def test_pilot_info_rank(self):
        self.assertEqual(self.pilot_info._meta.get_field('rank').max_length, 255)
        self.assertEqual(self.pilot_info._meta.get_field('rank').help_text, "Enter a pilot rank.")
        self.assertEqual(self.pilot_info._meta.get_field('rank').verbose_name, "Pilot rank")
        self.assertEqual(self.pilot_info.rank, "Captain")

    def test_pilot_info_age(self):
        self.assertEqual(self.pilot_info._meta.get_field('age').help_text, "Enter a pilot age.")
        self.assertEqual(self.pilot_info._meta.get_field('age').verbose_name, "Pilot age")
        self.assertEqual(self.pilot_info.age, 35)

    def test_pilot_info_country(self):
        self.assertEqual(self.pilot_info._meta.get_field('country').max_length, 255)
        self.assertEqual(self.pilot_info._meta.get_field('country').help_text, "Enter a pilot country.")
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
