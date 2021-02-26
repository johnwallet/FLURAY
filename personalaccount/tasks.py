import random

from FLURAY.celery import app
from personalaccount.apicourse import get_rates
from personalaccount.apicoursecrypto import get_rates_crypto
from personalaccount.models import CurrencyCBRF, Transaction
from django.utils import timezone

from users.models import Profit_Partner_Day, CustomUser, Profit_Partner_Good_Day


@app.task
def update_curse():
    # обновляем курсы национальных валют
    currency = CurrencyCBRF.objects.all()
    iistvalute = ['Russian Rouble', 'Euro']
    curse_val = get_rates()
    for valute in iistvalute:
        for item in curse_val['channel']['item']:
            if item['targetName'] == valute:
                try:
                    currencyview = currency.get(name_currency=item['targetCurrency'])
                    currencyview.base_currency = 1 / float(item['exchangeRate'])
                    currencyview.date_update = timezone.now()
                    currencyview.save()
                except:
                    CurrencyCBRF.objects.create(name_currency=item['targetCurrency'].upper(),
                                                base_currency=1 / float(item['exchangeRate']), )

    # обновляем курсы криптовалют
    currencyjson = get_rates_crypto()
    iistcrypto = ['bitcoin', 'ethereum', 'ethereum-classic', 'monero', 'ripple', 'dash', 'bitcoin-cash', 'litecoin']
    for item in iistcrypto:
        for aut in currencyjson:
            if aut['id'] == item:
                try:
                    currencyview = currency.get(name_currency=aut['symbol'].upper())
                    currencyview.base_currency = aut['current_price']
                    currencyview.date_update = timezone.now()
                    currencyview.save()
                except:
                    CurrencyCBRF.objects.create(name_currency=aut['symbol'].upper(),
                                                base_currency=aut['current_price'], )
    return 'Update curse succes'


@app.task
def update_partner_line():
    # создаем словарь с родителями и суммами для начисления(если сумма больше 0.1$)
    list_all_profit_day = Profit_Partner_Day.objects.filter(profit_day_status=False).order_by('profit_day_parent')
    list_username = {}
    parent = None
    sum = 0
    for item in list_all_profit_day:
        if not item.profit_day_parent == parent:
            parent = item.profit_day_parent
            list_parent = list_all_profit_day.filter(profit_day_parent=parent)
            print(list_parent)
            if len(list_parent) > 1:
                for par in list_parent:
                    sum += par.profit_day_sum
                if sum > round(0.1, 8):
                    list_username[parent] = sum
                    for status in list_parent:
                        status.profit_day_status = True
                        status.save()
                sum = 0

            else:
                if item.profit_day_sum > round(0.1, 8):
                    list_username[parent] = item.profit_day_sum
                    item.profit_day_status = True
                    item.save()

    # всем из словаря начисляем сумму, создаем транзакцию, создаем словарь с дневной прибылью
    for k, v in list_username.items():
        user_profit = CustomUser.objects.get(username=k)

        user_profit.balance += v
        Profit_Partner_Good_Day.objects.create(
            profit_good_user=k,
            profit_good_sum=v,
        )

        Transaction.objects.create(transaction_name='Партнерская премия',
                                   transaction_number=str(random.randint(1000000, 9999999)),
                                   transaction_category='Премия',
                                   date_end_change=timezone.now(),
                                   transaction_type='Пополнение',
                                   transaction_user=k,
                                   transaction_status='Выполнена',
                                   transaction_sum=v,
                                   transaction_sistemchange='Внутренний счет')

        user_profit.save()

    return 'Update partner line succes'
