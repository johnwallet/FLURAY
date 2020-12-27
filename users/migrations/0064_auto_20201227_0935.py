# Generated by Django 3.1 on 2020-12-27 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0063_auto_20201227_0854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='active_in_skrill_rub',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='comis_in_skrill_rub',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='comis_out_skrill_rub',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='requsites_skrill_rub',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='requsites_width_skrill_rub',
        ),
        migrations.AddField(
            model_name='customuser',
            name='active_in_skrill_eur',
            field=models.BooleanField(default=False, verbose_name='АКТИВНОСТЬ НА ПОПОЛНЕНИЕ СКРИЛЛЕВРО'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='comis_in_skrill_eur',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='КОММИСИЯ НА ПОПОЛНЕНИЕ СКРИЛЛЕВРО'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='comis_out_skrill_eur',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='КОММИСИЯ НА ВЫВОД СКРИЛЛЕВРО'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='requsites_skrill_eur',
            field=models.CharField(blank=True, max_length=50, verbose_name='РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ СКРИЛЛЕВРО'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='requsites_width_skrill_eur',
            field=models.CharField(blank=True, max_length=50, verbose_name='РЕКВИЗИТЫ ДЛЯ ВЫВОДА СКРИЛЛЕВРО'),
        ),
    ]
