# Generated by Django 4.0.1 on 2022-05-06 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0028_alter_book_options_book_image_book_poem_image_poem'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='image_genre',
            field=models.CharField(default='', max_length=200),
        ),
    ]
