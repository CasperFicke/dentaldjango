# Generated by Django 3.1.1 on 2021-03-03 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energie', '0002_auto_20210303_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='meter',
            name='eenheid',
            field=models.CharField(default='KWh', max_length=10, verbose_name='Meter Eenheid'),
        ),
        migrations.AddField(
            model_name='meter',
            name='medium',
            field=models.CharField(default='water', max_length=100, verbose_name='Meter Medium'),
        ),
    ]
