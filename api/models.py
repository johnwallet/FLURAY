from django.db import models
from django.utils import timezone


class Merchant(models.Model):
    merchant_id = models.CharField('ID мерчанта', max_length=50, unique=True)
    merchant_date_joined = models.DateTimeField('Дата создания мерчанта', default=timezone.now)
    merchant_user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, verbose_name='Владелец мерчанта')
    merchant_secret_key = models.CharField('Секретный ключ', max_length=100, unique=True)
    merchant_name = models.CharField('Название', max_length=150)
    merchant_site = models.CharField('Домен', max_length=100)

    def __str__(self):
        return self.merchant_user.username

    class Meta:
        verbose_name = 'Мерчант'
        verbose_name_plural = 'Мерчанты'
