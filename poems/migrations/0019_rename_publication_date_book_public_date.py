# Generated by Django 4.0.1 on 2022-03-31 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0018_book_publication_date_alter_author_first_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publication_date',
            new_name='public_date',
        ),
    ]
