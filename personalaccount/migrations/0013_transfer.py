# Generated by Django 3.1 on 2020-09-23 14:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('personalaccount', '0012_auto_20200922_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_transfer', models.CharField(max_length=50, verbose_name='Название')),
                ('date_transfer', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата')),
                ('base_currency', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма')),
            ],
        ),
    ]
