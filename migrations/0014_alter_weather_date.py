# Generated by Django 5.0.4 on 2024-10-14 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simapp', '0013_weather_date_weather_rain_weather_temperature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='date',
            field=models.CharField(max_length=100),
        ),
    ]