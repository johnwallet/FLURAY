# Generated by Django 3.1 on 2020-09-22 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalaccount', '0007_auto_20200922_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestchange',
            name='request_status',
            field=models.CharField(max_length=150, verbose_name='Статус заявки'),
        ),
    ]
