# Generated by Django 3.1 on 2020-09-20 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0054_auto_20200917_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='requsites_qiwi',
            field=models.CharField(blank=True, max_length=50, verbose_name='Киви-кошелек'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='requsites_sberbank',
            field=models.CharField(blank=True, max_length=50, verbose_name='Сбербанк'),
        ),
    ]
