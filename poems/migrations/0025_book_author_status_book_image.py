# Generated by Django 4.0.1 on 2022-05-03 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0024_remove_book_image_remove_poem_collage'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_status',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
