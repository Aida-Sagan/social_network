from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Создатель', verbose_name='Создатель')
    name = models.TextField(default='lobby', verbose_name='Имя')
    key = models.TextField(default='lobby', verbose_name='Ключ')
    members = models.ManyToManyField(User, verbose_name='Участники')
    is_private = models.BooleanField(default=True, verbose_name='Приватный')

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Автор')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, null=True, verbose_name='Чат')
    text = models.TextField(default='', verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.text
