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

    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return self.title


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    amount = models.CharField(max_length=128, null=True, blank=True)
    preparation = models.CharField(max_length=128, null=True, blank=True)
    team = models.CharField(max_length=128, null=True, blank=True)
    order = models.PositiveIntegerField(default=0, null=False, blank=False)

    class Meta:
        ordering = ['order']

    def __str__(self) -> str:
        rep = self.name
        if self.amount:
            rep = f"{self.amount} {self.name}"
        return rep


class MethodStep(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    text = models.TextField()
    order = models.PositiveIntegerField(default=0, null=False, blank=False)

    class Meta:
        ordering = ['order']


class Note(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    date = models.DateField()
    text = models.TextField()
