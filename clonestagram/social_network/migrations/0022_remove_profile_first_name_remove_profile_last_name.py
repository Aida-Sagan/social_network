# Generated by Django 4.0.3 on 2022-04-15 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_network', '0021_alter_post_comm_alter_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]