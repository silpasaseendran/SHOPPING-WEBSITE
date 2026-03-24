from django.db import models


# Create your models here.
class Dress(models.Model):
    name = models.CharField(max_length=125)
    price = models.FloatField()
    image = models.CharField(max_length=3000)


class Kids(models.Model):
    name=models.CharField(max_length=125)
    price=models.FloatField()
    image=models.CharField(max_length=3000)
