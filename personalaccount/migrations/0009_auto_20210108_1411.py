# Generated by Django 3.1 on 2021-01-08 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalaccount', '0008_auto_20210108_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestchange',
            name='request_good_sum',
            field=models.DecimalField(decimal_places=8, max_digits=16, verbose_name='Итоговая сумма пользователя'),
        ),
        migrations.AlterField(
            model_name='requestchange',
            name='request_good_sum_change',
            field=models.DecimalField(decimal_places=8, max_digits=16, verbose_name='Итоговая сумма обменника'),
        ),
    ]
