from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path
from recipes.views import RecipeDetailView, RecipeListView

admin.site.site_header = 'Recipe Book Admin'
from recipes.autocomplete_views import IngredientNameAutocomplete
from recipes.models import Ingredient


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', login_required(RecipeListView.as_view())),
    path(
        '<slug:slug>', login_required(RecipeDetailView.as_view()), name="recipe_detail"
    ),
    path('sentry-debug/', login_required(trigger_error)),
    # Autocomplete urls
    path(
        'ingredient-name-autocomplete/',
        IngredientNameAutocomplete.as_view(model=Ingredient, create_field="name"),
        name="ingredient-name-autocomplete",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
