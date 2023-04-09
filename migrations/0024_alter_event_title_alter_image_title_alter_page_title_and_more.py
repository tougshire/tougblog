# Generated by Django 4.1.7 on 2023-04-09 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdchomepage', '0023_post_show_author_post_show_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(help_text='The title of the thread', max_length=100, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(help_text='The title of the thread', max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(help_text='The title of the thread', max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='placement',
            name='title',
            field=models.CharField(blank=True, help_text='The title to be displayed for this placement', max_length=100, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='The title of the thread', max_length=100, verbose_name='Title'),
        ),
    ]