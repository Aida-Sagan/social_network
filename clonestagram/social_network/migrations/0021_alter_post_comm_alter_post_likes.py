# Generated by Django 4.0.2 on 2022-04-08 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_network', '0020_profile_bio_profile_first_name_profile_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comm',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
