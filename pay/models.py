from django.db import models


class Transaction(models.Model):
    transaction_name = models.CharField('Название транзакции', max_length=150)
    transaction_user = models.ForeignKey('users.CustomUser', on_delete=models.PROTECT, default=1,
                                         verbose_name='Логин пользователя')
    transaction_type = models.ForeignKey('TransactionView', on_delete=models.PROTECT, default=1,
                                         verbose_name='Тип транзакции')
    transaction_status = models.ForeignKey('Status', on_delete=models.PROTECT, default=1,
                                           verbose_name='Статус')
    transaction_currency = models.ForeignKey('Currency', on_delete=models.PROTECT, default=1,
                                             verbose_name='Валюта')
    transaction_sum = models.DecimalField('Сумма', default=0, max_digits=13, decimal_places=8)
    transaction_sistemchange = models.ForeignKey('SistemChange', on_delete=models.PROTECT, default=1,
                                                 verbose_name='Платежная система')

    def __str__(self):
        return self.transaction_name

    class Meta:
        verbose_name = 'Транзакцию'
        verbose_name_plural = 'Транзакции'


class Currency(models.Model):
    base_currency = models.CharField('Валюта', db_index=True, max_length=150)

    def __str__(self):
        return self.base_currency

    class Meta:
        verbose_name = 'Валюту'
        verbose_name_plural = 'Валюты'


class TransactionView(models.Model):
    base_transaction = models.CharField('Тип транзакции', db_index=True, max_length=150)

    def __str__(self):
        return self.base_transaction

    class Meta:
        verbose_name = 'Тип транзакции'
        verbose_name_plural = 'Тип транзакции'


class Status(models.Model):
    base_status = models.CharField('Статус', db_index=True, max_length=150)

    def __str__(self):
        return self.base_status

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class SistemChange(models.Model):
    base_sistemchange = models.CharField('Платежная система', db_index=True, max_length=150)

    def __str__(self):
        return self.base_sistemchange

    class Meta:
        verbose_name = 'Платежную систему'
        verbose_name_plural = 'Платежные системы'


class RequestChange(models.Model):
    request_name = models.CharField('Название заявки', max_length=150)
    request_type = models.ForeignKey('TypeChange', on_delete=models.PROTECT, default=1,
                                     verbose_name='Тип заявки')

    request_user = models.ForeignKey('users.CustomUser', on_delete=models.PROTECT, default=1,
                                     verbose_name='Логин пользователя')
    request_status = models.ForeignKey('Status', on_delete=models.PROTECT, default=1,
                                       verbose_name='Статус заявки')
    request_currency = models.ForeignKey('Currency', on_delete=models.PROTECT, default=1,
                                         verbose_name='Валюта')
    request_sum = models.DecimalField('Сумма', default=0, max_digits=13, decimal_places=8)
    request_sistemchange = models.ForeignKey('SistemChange', on_delete=models.PROTECT, default=1,
                                             verbose_name='Платежная система')

    def __str__(self):
        return self.request_name

    class Meta:
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки'


class TypeChange(models.Model):
    base_typechange = models.CharField('Тип заявки', db_index=True, max_length=150)

    def __str__(self):
        return self.base_typechange

    class Meta:
        verbose_name = 'Тип заявки'
        verbose_name_plural = 'Тип заявок'
