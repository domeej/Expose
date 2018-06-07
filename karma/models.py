from django.db import models

# Create your models here.


class Player(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Alias(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    alias_name = models.CharField(max_length=20, rel='aliases')


class Game(models.Model):
    game_date = models.DateTimeField('date of the Game')


class Rank(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    position = models.IntegerField()
