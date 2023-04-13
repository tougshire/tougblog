# Generated by Django 4.1.7 on 2023-04-13 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tougblog', '0006_alter_event_managers_alter_page_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='event',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='page',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='post',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='draft_status',
            field=models.IntegerField(choices=[(7, 'published'), (0, 'draft')], default=0, help_text='If this post is a draft, which only displays in preview mode', verbose_name='draft status'),
        ),
        migrations.AlterField(
            model_name='post',
            name='draft_status',
            field=models.IntegerField(choices=[(7, 'published'), (0, 'draft')], default=0, help_text='If this post is a draft, which only displays in preview mode', verbose_name='draft status'),
        ),
    ]