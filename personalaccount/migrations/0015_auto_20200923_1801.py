# Generated by Django 3.1 on 2020-09-23 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalaccount', '0014_auto_20200923_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='in_transfer',
            field=models.CharField(max_length=50, verbose_name='Получатель'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='out_transfer',
            field=models.CharField(max_length=50, verbose_name='Отправитель'),
        ),
    ]
