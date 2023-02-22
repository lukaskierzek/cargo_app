from django.db import models


# Create your models here.


class Pilots(models.Model):
    pass


class PilotsInformations(models.Model):
    pilot = models.OneToOneField(
        to=Pilots,
        on_delete=models.RESTRICT,
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
        verbose_name = 'Pilot information'
        verbose_name_plural = 'Pilots informations'
