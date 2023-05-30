from .models import Pokemon, PokemonEntity

from django.contrib import admin

class PokemonEntityAdmin(admin.ModelAdmin):
    list_display = [x.name for x in PokemonEntity._meta.get_fields()]


admin.site.register(Pokemon)
admin.site.register(PokemonEntity, PokemonEntityAdmin)
