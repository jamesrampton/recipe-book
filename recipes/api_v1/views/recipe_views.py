from django.db.models import F
from recipes.api_v1.serializers.recipe_serializer import RecipeSerializer
from recipes.models import Recipe
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class RecipeViewSet(viewsets.ModelViewSet):
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = Recipe.objects.all().order_by(F('last_eaten').asc(nulls_first=True))
    serializer_class = RecipeSerializer
    lookup_field = 'slug'
