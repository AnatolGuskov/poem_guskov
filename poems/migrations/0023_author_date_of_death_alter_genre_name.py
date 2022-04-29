# Generated by Django 4.0.1 on 2022-04-19 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0022_alter_author_options_author_city_poem_collage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(help_text='Enter a book genre (e.g. Бог, Війна, Любов etc.)', max_length=30),
        ),
    ]