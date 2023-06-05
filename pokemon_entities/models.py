from datetime import datetime

from django.db import models  # noqa F401
from django.utils.timezone import now


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name='Название (рус)')
    title_en = models.CharField(max_length=200, verbose_name='Название (англ)', blank=True)
    title_jp = models.CharField(max_length=200, verbose_name='Название (яп)', blank=True)
    photo = models.ImageField(
        upload_to='pokemons', null=True, blank=True, verbose_name='Фото'
    )
    description = models.TextField(verbose_name='Описание', blank=True)
    previous_evolution = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Из кого эволюционировал',
        related_name='pokemons'
    )

    def __str__(self):
        return f'{self.title_ru}, {self.id}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE, verbose_name='Покемон',
        related_name='pokemon_entities'
    )
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(verbose_name='Появился в')
    disappeared_at = models.DateTimeField(verbose_name='Пропал в')
    level = models.IntegerField(verbose_name='Уровень', blank=True, null=True)
    health = models.IntegerField(
        verbose_name='Здоровье', blank=True, null=True
    )
    strength = models.IntegerField(default=1, verbose_name='Сила', blank=True, null=True)
    defence = models.IntegerField(
        verbose_name='Защита', blank=True, null=True
    )
    stamina = models.IntegerField(
        verbose_name='Выносливость', blank=True, null=True
    )
