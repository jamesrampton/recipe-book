from django.views.generic import ListView, DetailView
from recipes.models import Recipe


class RecipeListView(ListView):
    queryset = Recipe.objects.order_by('-last_eaten')


class RecipeDetailView(DetailView):
    model = Recipe
