# Generated by Django 3.1 on 2020-08-27 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_auto_20200827_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='balance',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=10, verbose_name='баланс'),
        ),
    ]
