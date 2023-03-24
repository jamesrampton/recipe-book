from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path

from recipe_book.views import manifest, offline, service_worker
from recipes.views import RecipeDetailView, RecipeGalleryView, RecipeListView

admin.site.site_header = "Recipe Book Admin"


def trigger_error(request):
    division_by_zero = 1 / 0  # noqa


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", login_required(RecipeListView.as_view())),
    # pwa routes
    path("serviceworker.js", service_worker, name="serviceworker"),
    path("manifest.json", manifest, name="manifest"),
    path("offline/", offline, name="offline"),
    # recipe routes
    path("<slug:slug>/", login_required(RecipeDetailView.as_view()), name="recipe_detail"),
    path(
        "<slug:slug>/gallery/",
        login_required(RecipeGalleryView.as_view()),
        name="recipe_gallery",
    ),
    # other routes
    path("sentry-debug/", login_required(trigger_error)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
