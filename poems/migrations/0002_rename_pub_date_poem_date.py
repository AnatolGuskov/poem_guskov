# Generated by Django 4.0.1 on 2022-01-19 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poem',
            old_name='pub_date',
            new_name='date',
        ),
    ]
