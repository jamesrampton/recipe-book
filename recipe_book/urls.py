from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from recipes.views import RecipeListView, RecipeDetailView

admin.site.site_header = 'Recipe Book Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RecipeListView.as_view()),
    path('<slug:slug>', RecipeDetailView.as_view(), name="recipe_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
