from adminsortable2.admin import SortableAdminBase, SortableStackedInline
from django.contrib import admin

from recipes.models import Ingredient, Location, Note, Recipe, RecipeImage


class IngredientInline(SortableStackedInline):
    model = Ingredient
    extra = 0


class NoteInline(admin.StackedInline):
    model = Note
    extra = 0


class RecipeImageInline(admin.StackedInline):
    model = RecipeImage
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [RecipeImageInline, IngredientInline, NoteInline]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ["title", "ingredient__name"]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass
