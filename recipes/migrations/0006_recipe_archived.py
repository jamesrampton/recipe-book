# Generated by Django 4.0.4 on 2022-07-04 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_recipe_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
