# Generated by Django 4.0.10 on 2023-03-31 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_recipe_favourite'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipeimage',
            options={'ordering': ['-date']},
        ),
    ]
