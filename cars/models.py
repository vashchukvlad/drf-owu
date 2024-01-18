from django.db import models


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=50)
    year = models.IntegerField()
    number_of_seats = models.IntegerField()
    body_type = models.CharField(max_length=20)
    engine_volume = models.FloatField()