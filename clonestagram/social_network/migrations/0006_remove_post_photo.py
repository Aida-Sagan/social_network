# Generated by Django 4.0.2 on 2022-03-29 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_network', '0005_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='photo',
        ),
    ]