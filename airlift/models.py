from django.db import models


class Cargos(models.Model):
    name = models.CharField(
        max_length=50,
        help_text="Enter a cargo name",
        verbose_name="Cargo name"
    )

    quantity = models.PositiveIntegerField(
        help_text="Enter a cargo quantity",
        verbose_name="Cargo quantity"
    )

    def __str__(self):
        return f"{self.name}: {self.quantity}"

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"


class Destinations(models.Model):
    from_airport = models.CharField(
        max_length=50,
        help_text="Enter a airport name from the plane will take off",
        verbose_name="Airport name from the plane will take off"
    )

    to_airport = models.CharField(
        max_length=50,
        help_text="Enter a airport name where the plane will land",
        verbose_name="Airport name where the plane will land"
    )

    def __str__(self):
        return f"{self.from_airport} - {self.to_airport}"

    class Meta:
        verbose_name = "Destination"
        verbose_name_plural = "Destinations"


class Aircrafts(models.Model):
    name = models.CharField(
        max_length=50,
        help_text="Enter a aircraft name",
        verbose_name="Aircraft name"
    )

    country = models.CharField(
        max_length=50,
        help_text="Enter a country name that owns the aircraft",
        verbose_name="Country name that owns the aircraft"
    )

    destination = models.ForeignKey(
        to=Destinations,
        on_delete=models.SET_NULL,
        null=True
    )

    cargo = models.ManyToManyField(
        to=Cargos
    )

    def __str__(self):
        return f"{self.name} ({self.country})"

    class Meta:
        verbose_name = "Aircraft"
        verbose_name_plural = "Aircrafts"


class Pilots(models.Model):
    first_name = models.CharField(
        max_length=50,
        help_text="Enter a pilot first name",
        verbose_name="Pilot first name"
    )

    last_name = models.CharField(
        max_length=50,
        help_text="Enter a pilot last name",
        verbose_name="Pilot last name"
    )

    aircraft = models.ForeignKey(
        to=Aircrafts,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Pilot information"
        verbose_name_plural = "Pilots informations"


class PilotsInformations(models.Model):
    pilot = models.OneToOneField(
        to=Pilots,
        on_delete=models.CASCADE,
        primary_key=True
    )

    position = models.CharField(
        max_length=50,
        help_text='Enter a pilot position',
        verbose_name='Pilot position'
    )

    rank = models.CharField(
        max_length=50,
        help_text='Enter a pilot rank',
        verbose_name='Pilot rank'
    )

    age = models.CharField(
        max_length=50,
        help_text='Enter a pilot age',
        verbose_name='Pilot age'
    )

    country = models.CharField(
        max_length=50,
        help_text='Enter a pilot country',
        verbose_name='Pilot country'
    )

    def __str__(self):
        return f"{self.position}\n{self.rank}\n{self.age}\n{self.country}"

    class Meta:
        verbose_name = 'Pilot additional information'
        verbose_name_plural = 'Pilot additional informations'
