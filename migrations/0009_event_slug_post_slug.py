# Generated by Django 4.1.7 on 2023-04-14 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tougblog', '0008_alter_event_draft_status_alter_page_draft_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(help_text='The code that provides a character based ID for this page', null=True, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(help_text='The code that provides a character based ID for this page', null=True, unique=True),
        ),
    ]