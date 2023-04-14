# Generated by Django 4.1.7 on 2023-04-14 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tougblog', '0009_event_slug_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(help_text='The code that provides a character based ID for this page', unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(help_text='The code that provides a character based ID for this page', unique=True),
        ),
    ]
