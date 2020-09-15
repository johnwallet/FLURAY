from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView

from pay.apicbrf import get_rates
from pay.models import Transaction, RequestChange, CurrencyCBRF
from users.models import CustomUserId, CustomUser


# проверяем, если пользователь залогинен и владелец кошелька или обменника, выдаем нужный шаблон
class personalaccount(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.userid == CustomUserId.objects.get(pk=1):
                return render(request, 'personalaccount/cabinet/dashboard/dashboardwallet.html')
            elif request.user.userid == CustomUserId.objects.get(pk=2):
                return render(request, 'personalaccount/cabinet/dashboard/dashboardchange.html')
        else:
            return redirect('account_login')


def depositwallet(request):
    return render(request, 'personalaccount/cabinet/deposit/depositwallet.html')


def withdrawalwallet(request):
    return render(request, 'personalaccount/cabinet/withdrawal/withdrawalwallet.html')


def transferwallet(request):
    return render(request, 'personalaccount/cabinet/transfer/transferwallet.html')


class requsetwallet(ListView):
    model = RequestChange
    template_name = 'personalaccount/cabinet/requset/requsetwallet.html'
    context_object_name = 'depexchangereq'


def transactionwallet(request):
    tranview = Transaction.objects.all()
    return render(request, 'personalaccount/cabinet/transaction/transactionwallet.html', {'tranview': tranview})


def rekvisitwallet(request):
    return render(request, 'personalaccount/cabinet/rekvisit/rekvisitwallet.html')


def profilewallet(request):
    return render(request, 'personalaccount/cabinet/profile/profilewallet.html')


def settingwallet(request):
    return render(request, 'personalaccount/cabinet/setting/settingwallet.html')


def withdrawalexchange(request):
    return render(request, 'personalaccount/cabinet/withdrawal/withdrawalexchange.html')


class depositexchange(ListView):
    model = RequestChange
    template_name = 'personalaccount/cabinet/deposit/depositexchange.html'
    context_object_name = 'depexchange'

    def get_queryset(self):
        return RequestChange.objects.all()


class depositexchangerequest(DetailView):
    model = RequestChange
    template_name = 'personalaccount/cabinet/deposit/depositexchangerequest.html'
    context_object_name = 'depexchangerequest'


def depositexchangerequestupdate(request, pk):
    update_data = RequestChange.objects.all()
    update_data_tran = Transaction.objects.all()
    update_balance_i = CustomUser.objects.all()
    if request.method == "POST":
        update = update_data.get(pk=pk)
        update_tran = update_data_tran.get(transaction_name=update.request_name)
        update_balance = update_balance_i.get(username=update.request_user)
        if str(update.request_currency) == "USD":
            update_balance.balanceusd += update.request_sum
            curup = CurrencyCBRF.objects.get(name_currency="USD")
            update_balance.balance += (update.request_sum * curup.base_currency)
        if str(update.request_currency) == "RUB":
            update_balance.balancerub += update.request_sum
            update_balance.balance += update.request_sum
        if str(update.request_currency) == "EUR":
            update_balance.balanceeur += update.request_sum
            curup = CurrencyCBRF.objects.get(name_currency="EUR")
            update_balance.balance += (update.request_sum * curup.base_currency)

        update_tran.transaction_status = 'Выполнена'
        update.request_status = 'Выполнена'
        update_balance.save()
        update_tran.save()
        update.save()
        return redirect('depositexchange')


def depositexchangerequestupdateno(request, pk):
    update_data = RequestChange.objects.all()
    update_data_tran = Transaction.objects.all()
    if request.method == "POST":
        update = update_data.get(pk=pk)
        update_tran = update_data_tran.get(transaction_name=update.request_name)
        update_tran.transaction_status = 'В обработке'
        update.request_status = 'В обработке'
        update_tran.save()
        update.save()
        return redirect('depositexchange')


def depositreservchange(request):
    return render(request, 'personalaccount/cabinet/deposit/depositreservchange.html')


def withdrawalreservchange(request):
    return render(request, 'personalaccount/cabinet/withdrawal/withdrawalreservchange.html')


def transactionchange(request):
    tranviewchange = Transaction.objects.all()
    return render(request, 'personalaccount/cabinet/transaction/transactionchange.html',
                  {'tranviewchange': tranviewchange})


def coursechange(request):
    currencyview = CurrencyCBRF.objects.all()
    return render(request, 'personalaccount/cabinet/course/coursechange.html', {'currencyview': currencyview})


def coursechangeupdate(request):
    # добавляем новый курс в базу
    #    i = get_rates(section_id='R01235')
    #    CurrencyCBRF.objects.create(name_currency=i.name, base_currency=i.rate)

    # обновляем курс USD
    iusd = get_rates(section_id='R01235')
    currencyviewusd = CurrencyCBRF.objects.get(name_currency=iusd.name)
    currencyviewusd.base_currency = iusd.rate
    currencyviewusd.save()
    # обновляем курс EUR
    ieur = get_rates(section_id='R01239')
    currencyvieweur = CurrencyCBRF.objects.get(name_currency=ieur.name)
    currencyvieweur.base_currency = ieur.rate
    currencyvieweur.save()
    return redirect('coursechange')


def rekvisitchange(request):
    return render(request, 'personalaccount/cabinet/rekvisit/rekvisitchange.html')


def profilechange(request):
    return render(request, 'personalaccount/cabinet/profile/profilechange.html')


def settingchange(request):
    return render(request, 'personalaccount/cabinet/setting/settingchange.html')
