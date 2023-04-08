# Generated by Django 4.1.7 on 2023-04-08 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdchomepage', '0022_alter_placement_show_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='show_author',
            field=models.BooleanField(default=True, help_text='If the author should be shown in the detail view. This is just a flag - the template has to be coded appropriately for this to work', verbose_name='show author'),
        ),
        migrations.AddField(
            model_name='post',
            name='show_created',
            field=models.BooleanField(default=True, help_text='If the creation date should be shown in the detail view. This is just a flag - the template has to be coded appropriately for this to work', verbose_name='show created'),
        ),
        migrations.AlterField(
            model_name='placement',
            name='show_author',
            field=models.BooleanField(default=True, help_text='If the author should be shown in the list of posts. This is just a flag - the template has to be coded appropriately for this to work', verbose_name='show author'),
        ),
        migrations.AlterField(
            model_name='placement',
            name='show_created',
            field=models.BooleanField(default=True, help_text='If the creation date should be shown in the list of posts. This is just a flag - the template has to be coded appropriately for this to work', verbose_name='show created'),
        ),
    ]
