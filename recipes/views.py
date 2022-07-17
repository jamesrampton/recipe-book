from django.db.models import F
from django.views.generic import DetailView, ListView, TemplateView

from recipes.models import Recipe


class RecipeListView(ListView):
    queryset = Recipe.objects.filter(archived=False).order_by(
        F("last_eaten").asc(nulls_first=True)
    )


class RecipeDetailView(DetailView):
    model = Recipe


class RecipeGalleryView(DetailView):
    model = Recipe

    template_name = 'recipes/gallery.html'
