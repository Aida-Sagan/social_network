# Generated by Django 4.0.2 on 2022-04-04 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_network', '0007_post_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.TextField(verbose_name='Подпись'),
        ),
    ]
