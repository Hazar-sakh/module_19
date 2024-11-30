from django.db import models

# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=30)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    age = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.name}, {self.age}'


class Game(models.Model):
    title = models.CharField(max_length=300, default='Game')
    cost = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    size = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    description = models.TextField(default='Play for free')
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games', default=None)

    def __str__(self):
        return self.title


