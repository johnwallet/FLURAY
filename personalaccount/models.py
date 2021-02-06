from django.db import models
from django.utils import timezone


class Transaction(models.Model):
    date_joined_change = models.DateTimeField('Создана', default=timezone.now)
    date_end_change = models.DateTimeField('Исполнена', blank=True, null=True)
    transaction_name = models.CharField('Название', max_length=150)
    transaction_number = models.CharField('Номер', max_length=150)
    transaction_user = models.CharField('Логин пользователя', max_length=150)
    transaction_status = models.CharField('Статус', max_length=150, default="Выполнена")
    transaction_sum = models.CharField('Сумма', max_length=150)
    transaction_sistemchange = models.CharField('Платежная система', max_length=150)

    def __str__(self):
        return self.transaction_name

    class Meta:
        verbose_name = 'Транзакцию'
        verbose_name_plural = 'Транзакции'


class RequestChange(models.Model):
    request_userchange = models.CharField('Обработчик заявки', max_length=150)
    date_joined_change = models.DateTimeField('Дата создания', default=timezone.now)
    date_end_change = models.DateTimeField('Дата исполнения', blank=True, null=True)
    request_name = models.CharField('Номер заявки', max_length=150)
    request_type = models.CharField('Тип заявки', max_length=150)
    request_user = models.CharField('Логин пользователя', max_length=150)
    request_status = models.CharField('Статус заявки', max_length=150)
    request_sistemchange = models.CharField('Платежная система', max_length=150)
    criteri = models.CharField('Критерий', max_length=150)
    requisites = models.CharField('Реквизиты', max_length=50)
    request_commission = models.DecimalField('Комиссия общая', max_digits=4, decimal_places=2)
    request_commission_change = models.DecimalField('Комиссия обменника', max_digits=4, decimal_places=2)
    request_curse = models.DecimalField('Курс', max_digits=10, decimal_places=4)

    request_type_valute = models.CharField('Тип валюты', max_length=50)

    request_sum = models.DecimalField('Требуемая сумма', max_digits=16, decimal_places=8)
    request_sum_valute = models.DecimalField('Требуемая сумма нац валюта', max_digits=10, decimal_places=2)

    request_good_sum = models.DecimalField('Итоговая сумма пользователя', max_digits=16, decimal_places=8)
    request_good_sum_valute = models.DecimalField('Итоговая сумма пользователя нац валюта', max_digits=10, decimal_places=2)

    request_good_sum_change = models.DecimalField('Итоговая сумма обменника', max_digits=16, decimal_places=8)
    request_good_sum_change_valute = models.DecimalField('Итоговая сумма обменника нац валюта', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.request_name

    class Meta:
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки'


class CurrencyCBRF(models.Model):
    name_currency = models.CharField('Название валюты', max_length=50)
    base_currency = models.DecimalField('Курс валюты', max_digits=10, decimal_places=4)

    def __str__(self):
        return self.name_currency

    class Meta:
        verbose_name = 'Курс валюты'
        verbose_name_plural = 'Курсы валют'


class Transfer(models.Model):
    transfer_name = models.CharField('Название', max_length=50)
    transfer_out = models.CharField('Отправитель', max_length=50)
    transfer_in = models.CharField('Получатель', max_length=50)
    transfer_date = models.DateTimeField('Дата', default=timezone.now)
    transfer_sum = models.DecimalField('Сумма', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.transfer_name

    class Meta:
        verbose_name = 'Внутренний перевод'
        verbose_name_plural = 'Внутренний перевод'


class StaticDailyProfit(models.Model):
    dailyprofit_user = models.CharField('Пользователь', max_length=50)
    dailyprofit_value = models.DecimalField('Значение', max_digits=10, decimal_places=2)
    dailyprofit_date = models.DateField('Дата', default=timezone.now)

    def __str__(self):
        return self.dailyprofit_user

    class Meta:
        verbose_name = 'Статистику прибыли'
        verbose_name_plural = 'Статистика прибыли'


class News(models.Model):
    news_date_joined = models.DateTimeField('Дата публикации', default=timezone.now)
    news_is_publish = models.BooleanField('Опубликовано', default=False)
    news_header = models.CharField('Заголовок', max_length=50)
    news_content = models.TextField('Контент', max_length=800)
    news_img = models.ImageField('Изображение', upload_to='news/')
    news_instagram = models.URLField('Пост в инстаграме', default='https://www.instagram.com/')
    news_telegram = models.URLField('Пост в инстаграме', default='https://www.telegram.org/')

    def __str__(self):
        return self.news_header

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
