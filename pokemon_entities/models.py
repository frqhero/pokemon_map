from datetime import datetime

from django.db import models  # noqa F401
from django.utils.timezone import now


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name='Название (рус)')
    title_en = models.CharField(
        max_length=200, verbose_name='Название (англ)'
    )
    title_jp = models.CharField(max_length=200, verbose_name='Название (яп)')
    photo = models.ImageField(
        upload_to='pokemons', null=True, blank=True, verbose_name='Фото'
    )
    description = models.TextField(verbose_name='Описание')
    previous_evolution = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Из кого эволюционировал',
    )

    def __str__(self):
        return f'{self.title_ru}, {self.id}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='Покемон')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(default=now(), verbose_name='Появился в')
    disappeared_at = models.DateTimeField(default=now(), verbose_name='Пропал в')
    level = models.IntegerField(default=1, verbose_name='Уровень')
    health = models.IntegerField(default=1, verbose_name='Здоровье')
    strength = models.IntegerField(default=1, verbose_name='Сила')
    defence = models.IntegerField(default=1, verbose_name='Защита')
    stamina = models.IntegerField(default=1, verbose_name='Выносливость')
