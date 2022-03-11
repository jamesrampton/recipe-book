import re
from collections import OrderedDict

from django.conf import settings
from django.core.files.images import ImageFile
from django.core.files.storage import get_storage_class
from django.db import models
from django.urls import reverse


class Recipe(models.Model):
    class Diet(models.TextChoices):
        MEAT = ("meat", "meat")
        VEGETARIAN = ("vegetarian", "vegetarian")
        VEGAN = ("vegan", "vegan")

    title = models.CharField(max_length=128)
    slug = models.SlugField()
    prep_and_cooking_time = models.PositiveIntegerField(
        default=0,
        help_text="How long this recipe will take to prepare and cook (expressed in minutes)",
    )
    carb_portions = models.FloatField(default=0)
    serves = models.PositiveIntegerField(default=2)
    diet = models.CharField(max_length=11, choices=Diet.choices, default="vegan")
    image = models.ImageField(upload_to='recipe_images/', null=True, blank=True)
    last_eaten = models.DateField(null=True, blank=True)
    method = models.TextField(default="Get cooking!")

    def _get_ingredients_by_attr(self, att):
        ingredients_data = OrderedDict()
        ingredients = self.ingredient_set.all().order_by(att, 'order')
        for ingredient in ingredients:
            ingredients_data.setdefault(getattr(ingredient, att), []).append(ingredient)

        return ingredients_data

    def display_carb_portions(self):
        return f'{self.carb_portions:g}'

    def get_ingredients_by_team(self):
        return self._get_ingredients_by_attr('team')

    def get_ingredients_by_location(self):
        return self._get_ingredients_by_attr('location')

    def get_method_lines(self):
        return [line for line in self.method.splitlines() if line]

    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={"slug": self.slug})

    def get_placeholder_image(self):
        storage_class = get_storage_class(settings.STATICFILES_STORAGE)
        storage = storage_class()
        placeholder = storage.open(f"{settings.STATIC_ROOT}/images/empty_plate.jpg")
        image = ImageFile(placeholder)
        image.storage = storage
        return image

    def __str__(self) -> str:
        return self.title


class Location(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True, blank=True
    )
    name = models.CharField(max_length=128)
    amount = models.CharField(max_length=128, null=True, blank=True)
    preparation = models.CharField(max_length=128, null=True, blank=True)
    team = models.CharField(max_length=128, null=True, blank=True)
    order = models.PositiveIntegerField(default=0, null=False, blank=False)

    class Meta:
        ordering = ['order']

    def amount_with_emoji(self):
        return re.sub("spoon[s]?", "\U0001F944", self.amount)

    def __str__(self) -> str:
        rep = self.name
        if self.amount:
            rep = f"{self.amount} {self.name}"
        return rep


class Note(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    date = models.DateField()
    text = models.TextField()
