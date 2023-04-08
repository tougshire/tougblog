# Generated by Django 4.1.7 on 2023-04-07 23:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The title of the thread', max_length=50, verbose_name='Title')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='The date/time this therad was created', verbose_name='created')),
                ('content', models.TextField(help_text='The content of the post', verbose_name='content')),
                ('author', models.ForeignKey(help_text='The user who created ths thread', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
