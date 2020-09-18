from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView

from pay.apicourse import get_rates
from pay.models import Transaction, RequestChange, CurrencyCBRF
from users.models import CustomUserId, CustomUser


# РЕНДЕРИМ НУЖНЫЙ ШАБЛОН, КАБИНЕТ ПОЛЬЗОВАТЕЛЯ (ДАШБОРД)
class personalaccount(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.userid == CustomUserId.objects.get(pk=1):
                return render(request, 'personalaccount/cabinet/dashboard/dashboardwallet.html')
            elif request.user.userid == CustomUserId.objects.get(pk=2):
                return render(request, 'personalaccount/cabinet/dashboard/dashboardchange.html')
        else:
            return redirect('account_login')


# /КОШЕЛЕК/ СТРАНИЦА ПОПОЛНЕНИЯ
def depositwallet(request):
    return render(request, 'personalaccount/cabinet/deposit/depositwallet.html')


# /КОШЕЛЕК/ СТРАНИЦА ВЫВОДА
def withdrawalwallet(request):
    return render(request, 'personalaccount/cabinet/withdrawal/withdrawalwallet.html')


# /КОШЕЛЕК/ СТРАНИЦА ВНУТРЕННЕГО ПЕРЕВОДА
def transferwallet(request):
    return render(request, 'personalaccount/cabinet/transfer/transferwallet.html')


# /КОШЕЛЕК/ ЗАЯВКИ
class requsetwallet(ListView):
    model = RequestChange
    template_name = 'personalaccount/cabinet/requset/requsetwallet.html'
    context_object_name = 'depexchangereq'


# /КОШЕЛЕК/ ТРАНЗАКЦИИ
def transactionwallet(request):
    tranview = Transaction.objects.all()
    return render(request, 'personalaccount/cabinet/transaction/transactionwallet.html', {'tranview': tranview})


# /КОШЕЛЕК/ РЕКВИЗИТЫ
def rekvisitwallet(request):
    return render(request, 'personalaccount/cabinet/rekvisit/rekvisitwallet.html')


# /КОШЕЛЕК/ ПРОФИЛЬ
def profilewallet(request):
    return render(request, 'personalaccount/cabinet/profile/profilewallet.html')


# /КОШЕЛЕК/ НАСТРОЙКИ
def settingwallet(request):
    return render(request, 'personalaccount/cabinet/setting/settingwallet.html')


# /ОБМЕННИК/ ЗАЯВКИ НА ВЫВОД
def withdrawalexchange(request):
    return render(request, 'personalaccount/cabinet/withdrawal/withdrawalexchange.html')


# /ОБМЕННИК/ ЗАЯВКИ НА ПОПОЛНЕНИЕ
class depositexchange(ListView):
    model = RequestChange
    template_name = 'personalaccount/cabinet/deposit/depositexchange.html'
    context_object_name = 'depexchange'

    def get_queryset(self):
        return RequestChange.objects.all()


# /ОБМЕННИК/ ПРОСМОТР ЗАЯВКИ НА ПОПОЛНЕНИЕ, ДЕТАЛЬНЫЙ ПРОСМОТР
class depositexchangerequest(DetailView):
    model = RequestChange
    template_name = 'personalaccount/cabinet/deposit/depositexchangerequest.html'
    context_object_name = 'depexchangerequest'


# /ОБМЕННИК/ ИСПОЛНЕНИЕ ЗАЯВКИ НА ПОПОЛНЕНИЕ, НАЧИСЛЕНИЕ СРЕДСТВ, СМЕНА СТАТУСА У ЗАЯВКИ И ТРАНЗАКЦИИ
def depositexchangerequestupdate(request, pk):
    if request.method == "POST":
        update = RequestChange.objects.get(pk=pk)
        update_tran = Transaction.objects.get(transaction_name=update.request_name)
        update_balance = CustomUser.objects.get(username=update.request_user)
        if str(update.request_currency) == "RUB":
            curup = CurrencyCBRF.objects.get(name_currency="RUB")
            update_balance.balance += (update.request_sum / curup.base_currency)
        if str(update.request_currency) == "USD":
            update_balance.balance += update.request_sum
        if str(update.request_currency) == "EUR":
            curup = CurrencyCBRF.objects.get(name_currency="EUR")
            update_balance.balance += (update.request_sum / curup.base_currency)

        update.date_end_change = timezone.now()
        update_tran.date_end_change = timezone.now()
        update_tran.transaction_status = 'Выполнена'
        update.request_status = 'Выполнена'
        update_balance.save()
        update_tran.save()
        update.save()
        return redirect('depositexchange')


# /ОБМЕННИК/ ОБРАТНАЯ СМЕНА СТАТУСА У ЗАЯВКИ И ТРАНЗАКЦИИ НА ПОПОЛНЕНИЕ ==/ТЕСТ/==
def depositexchangerequestupdateno(request, pk):
    if request.method == "POST":
        update = RequestChange.objects.get(pk=pk)
        update_tran = Transaction.objects.get(transaction_name=update.request_name)
        update_tran.transaction_status = 'В обработке'
        update.request_status = 'В обработке'
        update_tran.save()
        update.save()
        return redirect('depositexchange')


# /ОБМЕННИК/ ПОПОЛНЕНИЕ РЕЗЕРВА
def depositreservchange(request):
    return render(request, 'personalaccount/cabinet/deposit/depositreservchange.html')


# /ОБМЕННИК/ ВЫВОД РЕЗЕРВА
def withdrawalreservchange(request):
    return render(request, 'personalaccount/cabinet/withdrawal/withdrawalreservchange.html')


# /ОБМЕННИК/ ТРАНЗАКЦИИ
def transactionchange(request):
    tranviewchange = Transaction.objects.all()
    return render(request, 'personalaccount/cabinet/transaction/transactionchange.html',
                  {'tranviewchange': tranviewchange})


# /ОБМЕННИК/ КУРСЫ ВАЛЮТ
def coursechange(request):
    currencyview = CurrencyCBRF.objects.all()
    return render(request, 'personalaccount/cabinet/course/coursechange.html', {'currencyview': currencyview})


# /ОБМЕННИК/ ОБНОВЛЕНИЕ И ДОБАВЛЕНИЕ КУРСОВ ВАЛЮТ
def coursechangeupdate(request):
    # добавляем новый курс в базу
    #    i = get_rates(section_id='Russian Rouble')
    #    CurrencyCBRF.objects.create(name_currency=i.name, base_currency=i.rate)

    # обновляем курс RUB
    irub = get_rates(section_id='Russian Rouble')
    currencyviewusd = CurrencyCBRF.objects.get(name_currency=irub.name)
    currencyviewusd.base_currency = irub.rate
    currencyviewusd.save()
    # обновляем курс EUR
    ieur = get_rates(section_id='Euro')
    currencyvieweur = CurrencyCBRF.objects.get(name_currency=ieur.name)
    currencyvieweur.base_currency = ieur.rate
    currencyvieweur.save()
    return redirect('coursechange')


# /ОБМЕННИК/ РЕКВИЗИТЫ
def rekvisitchange(request):
    return render(request, 'personalaccount/cabinet/rekvisit/rekvisitchange.html')


# /ОБМЕННИК/ ПРОФИЛЬ
def profilechange(request):
    return render(request, 'personalaccount/cabinet/profile/profilechange.html')


# /ОБМЕННИК/ НАСТРОЙКИ
def settingchange(request):
    return render(request, 'personalaccount/cabinet/setting/settingchange.html')
