# Generated by Django 5.0.4 on 2024-11-17 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simapp', '0026_remove_plant_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='H_max',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='column_distance',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='row_distance',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='size_per_plant',
        ),
    ]