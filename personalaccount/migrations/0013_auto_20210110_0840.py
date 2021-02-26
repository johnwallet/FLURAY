# Generated by Django 3.1 on 2021-01-10 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalaccount', '0012_staticdailyprofit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticdailyprofit',
            name='dailyprofit_value',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Значение'),
        ),
    ]
