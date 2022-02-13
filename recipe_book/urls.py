from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from recipes.views import RecipeListView, RecipeDetailView
from django.contrib.auth.decorators import login_required

admin.site.site_header = 'Recipe Book Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_required, RecipeListView.as_view()),
    path('<slug:slug>', login_required, RecipeDetailView.as_view(), name="recipe_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
