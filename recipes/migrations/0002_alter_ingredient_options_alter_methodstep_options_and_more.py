# Generated by Django 4.0.2 on 2022-02-06 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='methodstep',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='ingredient',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='methodstep',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]