# Generated by Django 4.1.7 on 2023-04-08 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdchomepage', '0020_rename_show_author_flag_post_show_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='show_author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='show_created',
        ),
        migrations.AddField(
            model_name='placement',
            name='show_author',
            field=models.BooleanField(default=True, help_text='Flag indicating if the author should be shown.  This is just a flag - the template has to be coded appropriately for this to work', verbose_name='show_author'),
        ),
        migrations.AddField(
            model_name='placement',
            name='show_created',
            field=models.BooleanField(default=True, help_text='Flag indicating if the creation date should be shown.  This is just a flag - the template has to be coded appropriately for this to work', verbose_name='show_created'),
        ),
    ]
