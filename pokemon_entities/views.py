import folium

from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime

from .models import Pokemon


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    now = localtime()

    pokemons = Pokemon.objects.all().select_related('previous_evolution')

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
        for pokemon_entity in pokemon.pokemon_entities.filter(
            appeared_at__lte=now, disappeared_at__gt=now
        ):
            add_pokemon(
                folium_map,
                pokemon_entity.lat,
                pokemon_entity.lon,
                request.build_absolute_uri(pokemon.photo.url),
            )
    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append(
            {
                'pokemon_id': pokemon.id,
                'img_url': request.build_absolute_uri(pokemon.photo.url)
                if pokemon.photo
                else DEFAULT_IMAGE_URL,
                'title_ru': pokemon.title_ru,
            }
        )

    return render(
        request,
        'mainpage.html',
        context={
            'map': folium_map._repr_html_(),
            'pokemons': pokemons_on_page,
        },
    )


def show_pokemon(request, pokemon_id):
    requested_pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    pokemon = {
        'pokemon_id': requested_pokemon.id,
        'img_url': request.build_absolute_uri(requested_pokemon.photo.url)
        if requested_pokemon.photo
        else DEFAULT_IMAGE_URL,
        'title_ru': requested_pokemon.title_ru,
        'title_en': requested_pokemon.title_en,
        'title_jp': requested_pokemon.title_jp,
        'description': requested_pokemon.description,
    }
    if requested_pokemon.previous_evolution:
        pokemon['previous_evolution'] = {
            'pokemon_id': requested_pokemon.previous_evolution.id,
            'title_ru': requested_pokemon.previous_evolution.title_ru,
            'img_url': request.build_absolute_uri(
                requested_pokemon.previous_evolution.photo.url
            )
            if requested_pokemon.photo
            else DEFAULT_IMAGE_URL,
        }
    descendants = requested_pokemon.pokemons.all()
    if descendants:
        descendant = descendants[0]
        pokemon['next_evolution'] = {
            'pokemon_id': descendant.id,
            'title_ru': descendant.title_ru,
            'img_url': request.build_absolute_uri(
                descendant.photo.url
            )
            if descendant.photo
            else DEFAULT_IMAGE_URL,
        }

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in requested_pokemon.pokemon_entities.all():
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            pokemon['img_url'],
        )

    return render(
        request,
        'pokemon.html',
        context={'map': folium_map._repr_html_(), 'pokemon': pokemon},
    )
