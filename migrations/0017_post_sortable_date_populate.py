# Generated by Django 4.2 on 2023-04-16 10:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

def forwards_func(apps, schema_editor):
    Post = apps.get_model("tougblog", "Post")
    db_alias = schema_editor.connection.alias
    for post in Post.objects.using(db_alias):
        post.sortable_date = post.created
        post.save()

def reverse_func(apps, schema_editor):
    Post = apps.get_model("tougblog", "Post")
    db_alias = schema_editor.connection.alias
    for post in Post.objects.using(db_alias):
        post.sortable_date = None
        post.save()

class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tougblog', '0016_post_sortable_date_alter_image_author')
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]