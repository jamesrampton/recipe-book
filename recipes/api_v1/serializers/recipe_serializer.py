from recipes.models import Recipe
from rest_framework import serializers


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ["id", "title", "slug", "method", "last_eaten", "image", "diet"]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
