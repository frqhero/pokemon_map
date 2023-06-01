# Generated by Django 3.1.14 on 2023-06-01 16:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0009_auto_20230530_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 1, 16, 57, 34, 799335, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 1, 16, 57, 34, 799348, tzinfo=utc)),
        ),
    ]
