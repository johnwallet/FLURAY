# Generated by Django 3.1 on 2020-08-27 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0035_auto_20200827_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='balance',
        ),
    ]
