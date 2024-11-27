# Generated by Django 5.0.4 on 2024-10-23 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simapp', '0021_alter_datamodeloutput_yield_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='planting_cost',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plant',
            name='revenue',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]