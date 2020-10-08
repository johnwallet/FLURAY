from django.db import models
from django.utils import timezone


class Message:
    time_change = models.DateTimeField('Время отправки', default=timezone.now)
    user_out = models.CharField('Отправитель', max_length=150)
    user_in = models.CharField('Получатель', max_length=150)
    text = models.TextField('Сообщение', max_length=450)

    def __str__(self):
        return self.text
