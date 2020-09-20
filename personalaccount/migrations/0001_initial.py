# Generated by Django 3.1 on 2020-09-20 12:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CriteriChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_criteri', models.CharField(db_index=True, max_length=150, verbose_name='Критерий')),
            ],
            options={
                'verbose_name': 'Критерий',
                'verbose_name_plural': 'Критерии',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_currency', models.CharField(db_index=True, max_length=150, verbose_name='Валюта')),
            ],
            options={
                'verbose_name': 'Валюту',
                'verbose_name_plural': 'Валюты',
            },
        ),
        migrations.CreateModel(
            name='CurrencyCBRF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_currency', models.CharField(max_length=50, verbose_name='Название валюты')),
                ('base_currency', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Курс  валюты')),
            ],
        ),
        migrations.CreateModel(
            name='SistemChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_sistemchange', models.CharField(db_index=True, max_length=150, verbose_name='Платежная система')),
            ],
            options={
                'verbose_name': 'Платежную систему',
                'verbose_name_plural': 'Платежные системы',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined_change', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Заявка создана')),
                ('date_end_change', models.DateTimeField(blank=True, null=True, verbose_name='Дата исполнения')),
                ('transaction_name', models.CharField(max_length=150, verbose_name='Название транзакции')),
                ('transaction_user', models.CharField(max_length=150, verbose_name='Логин пользователя')),
                ('transaction_userchange', models.CharField(blank=True, max_length=150, verbose_name='Обработчик')),
                ('transaction_type', models.CharField(max_length=150, verbose_name='Тип транзакции')),
                ('transaction_status', models.CharField(default='выполнена', max_length=150, verbose_name='Статус')),
                ('transaction_sum', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Сумма')),
                ('transaction_currency', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='personalaccount.currency', verbose_name='Валюта')),
                ('transaction_sistemchange', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='personalaccount.sistemchange', verbose_name='Платежная система')),
            ],
            options={
                'verbose_name': 'Транзакцию',
                'verbose_name_plural': 'Транзакции',
            },
        ),
        migrations.CreateModel(
            name='RequestChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_userchange', models.CharField(blank=True, max_length=150, verbose_name='Обработчик заявки')),
                ('date_joined_change', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('date_end_change', models.DateTimeField(blank=True, null=True, verbose_name='Дата исполнения')),
                ('request_name', models.CharField(max_length=150, verbose_name='Название заявки')),
                ('request_user', models.CharField(max_length=150, verbose_name='Логин пользователя')),
                ('request_status', models.CharField(default='В обработке', max_length=150, verbose_name='Статус заявки')),
                ('request_sum', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма')),
                ('criteri', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='personalaccount.criterichange', verbose_name='Критерий')),
                ('request_currency', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='personalaccount.currency', verbose_name='Валюта')),
                ('request_sistemchange', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='personalaccount.sistemchange', verbose_name='Платежная система')),
            ],
            options={
                'verbose_name': 'Заявку',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]
