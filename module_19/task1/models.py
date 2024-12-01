from django.db import models

# Create your models here.


class Team(models.Model):
    title = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    age = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.title}, {self.city}'


class Player(models.Model):
    first_name = models.CharField(max_length=30, default='Ivan')
    patronymic = models.CharField(max_length=30, default='Ivanovich')
    family = models.CharField(max_length=30, default='Ivanov')
    city = models.CharField(max_length=30, default='Burevestnik')
    age = models.IntegerField(default=18, max_length=3)
    teams = models.ManyToManyField(Team, related_name='teams', default=None)

    def __str__(self):
        lst = list(self.first_name)
        return f'{self.family} {lst[0]}. - {self.city}'
