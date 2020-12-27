# Generated by Django 3.1 on 2020-12-24 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0061_auto_20201224_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='active_in_vtb_rub',
            field=models.BooleanField(default=False, verbose_name='АКТИВНОСТЬ НА ПОПОЛНЕНИЕ ВТБ'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='active_out_vtb_rub',
            field=models.BooleanField(default=False, verbose_name='АКТИВНОСТЬ НА ВЫВОД ВТБ'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='comis_out_vtb_rub',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='КОММИСИЯ НА ВЫВОД ВТБ'),
        ),
    ]
