# Generated by Django 4.2.13 on 2024-06-21 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='depositmodels',
            name='user',
        ),
    ]
