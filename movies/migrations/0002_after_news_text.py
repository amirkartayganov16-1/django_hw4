# Generated by Django 4.0.4 on 2022-05-24 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_options_alter_movie_director'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='director',
            options={'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['title', 'descriptions', 'created_at', 'updated_at'], 'verbose_name': 'Кино', 'verbose_name_plural': 'Кино'},
        ),
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(null=True, upload_to='movie'),
        ),
    ]