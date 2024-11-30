from django.db import models

# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=30)
    balance = models.DecimalField
    age = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField
    cost = models.DecimalField
    size = models.DecimalField
    description = models.TextField
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer)

    def __str__(self):
        return self.title





