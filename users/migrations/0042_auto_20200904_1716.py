# Generated by Django 3.1 on 2020-09-04 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0041_remove_customuser_balance2'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUserId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custuserid', models.CharField(db_index=True, max_length=150, verbose_name='Категория пользователя')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.AddField(
            model_name='customuser',
            name='userid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='users.customuserid'),
        ),
    ]
