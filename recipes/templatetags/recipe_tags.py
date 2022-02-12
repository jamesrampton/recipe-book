from collections import OrderedDict
from django import template

register = template.Library()


@register.inclusion_tag("tags/ingredients_tag.html")
def recipe_ingredients(recipe):
    ingredients_data = OrderedDict()
    try:
        ingredients = recipe.ingredient_set.all().order_by('team', 'order')
    except AttributeError:
        ingredients = []  # TODO check the type of recipe and raise a proper exception

    for ingredient in ingredients:
        ingredients_data.setdefault(ingredient.team, []).append(ingredient)

    return {'ingredients_data': ingredients_data}
