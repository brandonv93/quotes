# Generated by Django 2.2 on 2020-03-24 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appOne', '0002_auto_20200324_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_of_birth',
        ),
    ]
