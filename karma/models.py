from django.db import models

# Create your models here.


class Player(models.Model):
    name = models.CharField(max_length=20)


class Alias(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    alias_name = models.CharField(max_length=20)


class Game(models.Model):
    game_date = models.DateTimeField('date of the Game')



