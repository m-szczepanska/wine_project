from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from django_countries.fields import CountryField


class Wine(models.Model):
    class Sweetness(models.TextChoices):
        DRY = ('Dry', 'Dry')
        SEMIDRY = ('Semi-dry', 'Semi-dry')
        SEMISWEET = ('Semi-sweet', 'Semi-sweet')
        SWEET = ('Sweet', 'Sweet')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    sweetness = models.CharField(max_length=255, choices=Sweetness.choices)
    grape_variety = models.CharField(max_length=255)  # TODO: separate model/enum?
    production_year = models.IntegerField()
    country = CountryField()
    url = models.URLField()
    image_url = models.URLField(null=True, blank=True)
    price = models.IntegerField()  # in lowest denomination, e.g. cents
    description = models.TextField()
    grade = models.IntegerField(
        validators=[
            MaxValueValidator(10, message='Grades are on a scale of 0-10'),
            MinValueValidator(0, message='Grades are on a scale of 0-10')
        ]
    )
    favourite = models.BooleanField(null=True, default=None)




