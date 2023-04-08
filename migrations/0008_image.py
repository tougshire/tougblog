# Generated by Django 4.1.7 on 2023-04-08 03:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sdchomepage', '0007_alter_post_options_post_content_format_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The title of the thread', max_length=50, verbose_name='Title')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='The date/time this therad was created', verbose_name='created')),
                ('file', models.ImageField(upload_to='gallery/')),
                ('author', models.ForeignKey(help_text='The user who created ths thread', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
