# Generated by Django 5.0.4 on 2024-10-14 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simapp', '0011_alter_datamodelinput_testingkey_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
