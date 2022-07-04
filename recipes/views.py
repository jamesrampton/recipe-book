from django.views.generic import ListView, DetailView
from django.db.models import F
from recipes.models import Recipe


class RecipeListView(ListView):
    queryset = Recipe.objects.filter(archived=False).order_by(
        F("last_eaten").asc(nulls_first=True)
    )


class RecipeDetailView(DetailView):
    model = Recipe
