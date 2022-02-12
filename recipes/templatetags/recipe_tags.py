from collections import OrderedDict
from django import template

register = template.Library()


@register.inclusion_tag("tags/ingredients_by_team_tag.html")
def recipe_ingredients_by_team(recipe):
    ingredients_data = OrderedDict()
    try:
        ingredients = recipe.ingredient_set.all().order_by('team', 'order')
    except AttributeError:
        ingredients = []  # TODO check the type of recipe and raise a proper exception

    for ingredient in ingredients:
        ingredients_data.setdefault(ingredient.team, []).append(ingredient)

    return {'ingredients_data': ingredients_data}


@register.inclusion_tag("tags/ingredients_by_location_tag.html")
def recipe_ingredients_by_location(recipe):
    ingredients_data = OrderedDict()
    try:
        ingredients = recipe.ingredient_set.all().order_by('location', 'order')
    except AttributeError:
        ingredients = []  # TODO check the type of recipe and raise a proper exception

    for ingredient in ingredients:
        ingredients_data.setdefault(ingredient.location, []).append(ingredient)

    return {'ingredients_data': ingredients_data}
