# Generated by Django 3.1.5 on 2021-01-22 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0100_recipe_servings_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='storage',
            name='path',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
    ]
