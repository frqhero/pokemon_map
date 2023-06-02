from datetime import datetime

from django.db import models  # noqa F401
from django.utils.timezone import now


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    title_jp = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='pokemons', null=True, blank=True)
    description = models.TextField()
    previous_evolution = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return f'{self.title_ru}, {self.id}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(default=now())
    disappeared_at = models.DateTimeField(default=now())
    level = models.IntegerField(default=1)
    health = models.IntegerField(default=1)
    strength = models.IntegerField(default=1)
    defence = models.IntegerField(default=1)
    stamina = models.IntegerField(default=1)
