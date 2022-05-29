from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path
from recipes.api_v1.views.recipe_views import RecipeViewSet
from recipes.views import RecipeDetailView, RecipeListView
from rest_framework import routers, serializers, viewsets

admin.site.site_header = 'Recipe Book Admin'


def trigger_error(request):
    division_by_zero = 1 / 0


router = routers.DefaultRouter()
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', login_required(RecipeListView.as_view())),
    path('api/v1/', include(router.urls)),
    path(
        '<slug:slug>', login_required(RecipeDetailView.as_view()), name="recipe_detail"
    ),
    path('sentry-debug/', login_required(trigger_error)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
