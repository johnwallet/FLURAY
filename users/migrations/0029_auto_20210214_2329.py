# Generated by Django 3.1 on 2021-02-14 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_profit_partner_day_profit_partner_good_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profit_partner_good_day',
            name='profit_good_sum',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Сумма'),
        ),
    ]
