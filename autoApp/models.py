from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)
    continent = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    country_of_origin = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.brand} {self.model}'

class Part(models.Model):
    name = models.CharField(max_length=100)
    part_number = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=100)
    compatible_cars = models.ManyToManyField(Car, related_name='parts')

    def __str__(self):
        return self.name
