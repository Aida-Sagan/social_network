# Generated by Django 4.0.2 on 2022-03-15 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0003_remove_post_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(default='default', upload_to='photos/%Y/%m/%d', verbose_name='Фото'),
            preserve_default=False,
        ),
    ]
