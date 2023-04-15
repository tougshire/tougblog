# Generated by Django 4.2 on 2023-04-15 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tougblog', '0014_remove_event_above_content_target_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='above_content_attributes',
        ),
        migrations.RemoveField(
            model_name='event',
            name='below_content_attributes',
        ),
        migrations.RemoveField(
            model_name='page',
            name='above_content_attributes',
        ),
        migrations.RemoveField(
            model_name='page',
            name='below_content_attributes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='above_content_attributes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='below_content_attributes',
        ),
        migrations.AddField(
            model_name='event',
            name='above_content_image_attributes',
            field=models.CharField(blank=True, help_text='The attributes (ie style="width:60%") for the image for the image displayed above content', max_length=70, verbose_name='above content image attributes'),
        ),
        migrations.AddField(
            model_name='event',
            name='above_content_link_attributes',
            field=models.CharField(blank=True, help_text='The attributes (ie target="_blank") for the link for the image displayed above content', max_length=70, verbose_name='above content link attributes'),
        ),
        migrations.AddField(
            model_name='event',
            name='below_content_image_attributes',
            field=models.CharField(blank=True, help_text='The attributes (ie style="width:60%") for the image for the image displayed below content', max_length=70, verbose_name='below content image attributes'),
        ),
        migrations.AddField(
            model_name='event',
            name='below_content_link_attributes',
            field=models.CharField(blank=True, help_text='The attributes (ie target="_blank") for the link for the image displayed below content', max_length=70, verbose_name='below content link attributes'),
        ),
        migrations.AddField(
            model_name='page',
            name='above_content_link_attributes',
            field=models.CharField(blank=True, help_text='The attributes (ie target="_blank") for the link for the image displayed above content', max_length=70, verbose_name='above content attributes'),
        ),
        migrations.AddField(
            model_name='page',
            name='below_content_link_attributes',
            field=models.CharField(blank=True, help_text='The attributes (ie target="_blank") for the link for the image displayed below content', max_length=70, verbose_name='below content attributes'),
        ),
        migrations.AddField(
            model_name='post',
            name='above_content_image_attributes',
            field=models.CharField(blank=True, help_text='The attributes (ie style="width:60%") for the image for the image displayed above content', max_length=70, verbose_name='above content image attributes'),
        ),
        migrations.AddField(
            model_name='post',
            name='above_content_link_attributes',
            field=models.CharField(blank=True, help_text='The attributes (ie target="_blank") for the link for the image displayed above content', max_length=70, verbose_name='above content link attributes'),
        ),
        migrations.AddField(
            model_name='post',
            name='below_content_image_attributes',
            field=models.CharField(blank=True, help_text='The attributes (ie style="width:60%") for the image for the image displayed below content', max_length=70, verbose_name='below content image attributes'),
        ),
        migrations.AddField(
            model_name='post',
            name='below_content_link_attributes',
            field=models.CharField(blank=True, help_text='The attributes (ie target="_blank") for the link for the image displayed below content', max_length=70, verbose_name='below content link attributes'),
        ),
    ]
