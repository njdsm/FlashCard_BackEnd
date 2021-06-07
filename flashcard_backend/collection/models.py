from django.db import models

# Create your models here.


class Collection(models.Model):
    name = models.CharField(max_length=50)
    numberOfCards = models.IntegerField(0)
    description = models.CharField(max_length=250)


