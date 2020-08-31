# Generated by Django 3.1 on 2020-08-27 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0032_auto_20200827_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='balance',
            field=models.DecimalField(decimal_places=8, default=1e-08, max_digits=10, verbose_name='баланс'),
        ),
    ]
