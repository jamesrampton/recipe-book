from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin

from recipes.forms import IngredientForm
from recipes.models import Ingredient, Location, Note, Recipe


class IngredientInline(SortableInlineAdminMixin, admin.StackedInline):
    model = Ingredient
    form = IngredientForm
    extra = 0


class NoteInline(admin.StackedInline):
    model = Note
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, NoteInline]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass
