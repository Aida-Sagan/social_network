from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

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

    def __str__(self):
        return f'{self.author} - {self.created_date} - {self.caption}'


class Comments(models.Model):
    content = models.TextField(blank=True, verbose_name='Текст комментария')
    post = models.ForeignKey('Post', on_delete=models.PROTECT, null=True, verbose_name='Под постом')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, verbose_name='Автор')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        
    def __str__(self):
        return self.content
