# Generated by Django 3.1 on 2021-02-16 16:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0033_auto_20210216_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='line_program',
            name='line_ref_date',
            field=models.CharField(default=datetime.datetime(2021, 2, 16, 16, 48, 52, 774688, tzinfo=utc), max_length=50, verbose_name='Дата регистрации'),
        ),
        migrations.AddField(
            model_name='line_program',
            name='line_ref_fio',
            field=models.CharField(default='-', max_length=50, verbose_name='ФИО'),
        ),
    ]
