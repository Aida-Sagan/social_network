# Generated by Django 4.0.3 on 2022-04-15 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_network', '0022_remove_profile_first_name_remove_profile_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.TextField(blank=True, verbose_name='Подпись'),
        ),
    ]
