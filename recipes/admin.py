from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin

from recipes.models import Ingredient, MethodStep, Note, Recipe


class IngredientInline(SortableInlineAdminMixin, admin.StackedInline):
    model = Ingredient
    extra = 0


class MethodStepInline(SortableInlineAdminMixin, admin.StackedInline):
    model = MethodStep
    extra = 0


class NoteInline(admin.StackedInline):
    model = Note
    extra = 0

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, MethodStepInline, NoteInline]
    prepopulated_fields = {"slug": ("title",)}
