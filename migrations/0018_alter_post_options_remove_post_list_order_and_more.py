# Generated by Django 4.2 on 2023-04-16 10:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tougblog', '0017_post_sortable_date_populate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-sticky', '-sortable_date')},
        ),
        migrations.RemoveField(
            model_name='post',
            name='list_order',
        ),
        migrations.AddField(
            model_name='post',
            name='sticky',
            field=models.BooleanField(default=False, help_text='If this post is stuck to the top. This is used before sortable date', verbose_name='sticky'),
        ),
        migrations.AlterField(
            model_name='post',
            name='sortable_date',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='The modifiable date used for sorting. This is the created date by default. To move a post up, select a future date.', null=True, verbose_name='sortable date'),
        ),
    ]
