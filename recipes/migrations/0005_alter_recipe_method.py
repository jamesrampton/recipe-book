# Generated by Django 4.0.4 on 2022-05-07 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipe_method_delete_methodstep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='method',
            field=models.TextField(blank=True, null=True),
        ),
    ]
