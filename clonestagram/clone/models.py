from tabnanny import verbose
from django.conf import settings
from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото')
    caption = models.CharField(max_length=200, verbose_name='Подпись')
    text = models.TextField(blank=True, verbose_name='Текст поста')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'