# Generated by Django 4.1.7 on 2023-04-08 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdchomepage', '0012_post_title_image_post_title_image_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='placement',
            options={'ordering': ('list_order', 'title')},
        ),
        migrations.RemoveField(
            model_name='placement',
            name='place',
        ),
        migrations.AddField(
            model_name='placement',
            name='list_order',
            field=models.CharField(blank=True, default='~', help_text='A character to determine the place on the list. Numbers are higher than capital letters, which are higher than small letters', max_length=1),
        ),
    ]
