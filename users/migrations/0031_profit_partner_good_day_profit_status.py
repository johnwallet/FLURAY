# Generated by Django 3.1 on 2021-02-15 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_auto_20210214_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='profit_partner_good_day',
            name='profit_status',
            field=models.BooleanField(default=False, verbose_name='Статус'),
        ),
    ]
