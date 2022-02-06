from django.contrib import admin

from recipes.models import Ingredient, MethodStep, Note, Recipe


class IngredientInline(admin.StackedInline):
    model = Ingredient
    extra = 1


class MethodStepInline(admin.StackedInline):
    model = MethodStep
    extra = 1


class NoteInline(admin.StackedInline):
    model = Note
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, MethodStepInline, NoteInline]
    prepopulated_fields = {"slug": ("title",)}
