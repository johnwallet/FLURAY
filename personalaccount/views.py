import random

from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView

from personalaccount.apicourse import get_rates
from personalaccount.models import Transaction, RequestChange, CurrencyCBRF

from personalaccount.forms import RequestForm, CommissionForm, RequisitesForm, WithdrawalForm, TransferForm
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


# ЗАЯВКА НА ПОПОЛНЕНИЕ ДЛЯ ОБРАБОТЧИКА
def depositwalletform(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        # получаем номер завки
        n = random.randint(1000000, 9999999)

        if form.is_valid():
            post = form.save(commit=False)
            post.request_user = request.user
            post.request_name = str(n)
            post.request_type = 'Заявка на пополнение'
            post.request_status = 'Ожидает оплаты'

            # получаем обработчика заявки
            itemchange = CustomUser.objects.filter(userid__custuserid='Владелец Обменника')

            # список обменников у кого хватает баланса на обработку заявки, и проверяем критерий
            base_comis = 99
            base_time = 1000
            itemchangeset = ''
            for i in itemchange:
                if str(post.request_currency) == "RUB":
                    c = CurrencyCBRF.objects.get(name_currency=post.request_currency)
                    if c.base_currency * i.balance > post.request_sum:
                        if str(post.criteri) == 'Лучший курс':
                            if i.valute_rub < base_comis:
                                itemchangeset = i.username
                                base_comis = i.valute_rub
                                post.request_commission = base_comis
                        if str(post.criteri) == 'Быстрый обмен':
                            timechange = RequestChange.objects.filter(request_userchange=i.username)
                            if timechange:
                                chartime = []
                                for time in timechange:
                                    if time.date_end_change and time.request_type == 'Заявка на пополнение':
                                        timelimit = time.date_end_change - time.date_joined_change
                                        timebase = timelimit.seconds / 60
                                        chartime += [timebase]
                                if len(chartime) >= 1:
                                    itemchar = float(0)
                                    for ichar in chartime:
                                        itemchar = itemchar + ichar
                                    timedef = itemchar / float(len(chartime))
                                    if timedef < base_time:
                                        itemchangeset = i.username
                                        base_time = timedef
                                        post.request_commission = i.valute_rub

                if str(post.request_currency) == "EUR":
                    c = CurrencyCBRF.objects.get(name_currency=post.request_currency)
                    if c.base_currency * i.balance > post.request_sum:
                        if str(post.criteri) == 'Лучший курс':
                            if i.valute_eur < base_comis:
                                itemchangeset = i.username
                                base_comis = i.valute_eur
                                post.request_commission = base_comis
                        if str(post.criteri) == 'Быстрый обмен':
                            timechange = RequestChange.objects.filter(request_userchange=i.username)
                            if timechange:
                                chartime = []
                                for time in timechange:
                                    if time.date_end_change and time.request_type == 'Заявка на пополнение':
                                        timelimit = time.date_end_change - time.date_joined_change
                                        timebase = timelimit.seconds / 60
                                        chartime += [timebase]
                                if len(chartime) >= 1:
                                    itemchar = float(0)
                                    for ichar in chartime:
                                        itemchar = itemchar + ichar
                                    timedef = itemchar / float(len(chartime))
                                    if timedef < base_time:
                                        itemchangeset = i.username
                                        base_time = timedef
                                        post.request_commission = i.valute_eur

                if str(post.request_currency) == "USD":
                    if i.balance > post.request_sum:
                        if str(post.criteri) == 'Лучший курс':
                            if i.valute_usd < base_comis:
                                itemchangeset = i.username
                                base_comis = i.valute_usd
                                post.request_commission = base_comis
                        if str(post.criteri) == 'Быстрый обмен':
                            timechange = RequestChange.objects.filter(request_userchange=i.username)
                            if timechange:
                                chartime = []
                                for time in timechange:
                                    if time.date_end_change and time.request_type == 'Заявка на пополнение':
                                        timelimit = time.date_end_change - time.date_joined_change
                                        timebase = timelimit.seconds / 60
                                        chartime += [timebase]
                                if len(chartime) >= 1:
                                    itemchar = float(0)
                                    for ichar in chartime:
                                        itemchar = itemchar + ichar
                                    timedef = itemchar / float(len(chartime))
                                    if timedef < base_time:
                                        itemchangeset = i.username
                                        base_time = timedef
                                        post.request_commission = i.valute_usd

            post.request_userchange = itemchangeset
            post.request_good_sum = post.request_sum + ((post.request_sum/100)*post.request_commission)

            # добавляем реквизиты обменника, если есть имя в списке
            if itemchangeset:
                requisit = CustomUser.objects.get(username=itemchangeset)
                if str(post.request_sistemchange) == 'SBERBANK':
                    post.requisites = requisit.requsites_sberbank
                if str(post.request_sistemchange) == 'QIWI':
                    post.requisites = requisit.requsites_qiwi

            # создаем транзакцию
            Transaction.objects.create(transaction_name=str(n),
                                       transaction_user=post.request_user,
                                       transaction_userchange=itemchangeset,
                                       transaction_type='Пополнение кошелька',
                                       transaction_status=post.request_status,
                                       transaction_currency=post.request_currency,
                                       transaction_sum=post.request_sum,
                                       transaction_sistemchange=post.request_sistemchange)
            post.save()
            return redirect('requsetwallet')
    else:
        form = RequestForm()
    return render(request, 'personalaccount/cabinet/deposit/depositwallet.html', {'form': form})


# /КОШЕЛЕК/ СТРАНИЦА ВЫВОДА
def withdrawalwallet(request):
    if request.method == "POST":
        form = WithdrawalForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            n = random.randint(1000000, 9999999)
            post.request_user = request.user
            post.request_name = str(n)
            post.request_type = 'Заявка на вывод'
            post.request_status = 'Ожидает оплаты'

            # получаем обработчика заявки
            itemchange = CustomUser.objects.filter(userid__custuserid='Владелец Обменника')

            # список обменников у кого хватает баланса на обработку заявки, и проверяем критерий
            base_comis = 99
            base_time = 1000
            itemchangeset = 'None'
            for i in itemchange:
                if str(post.request_currency) == "RUB":
                    c = CurrencyCBRF.objects.get(name_currency=post.request_currency)
                    if c.base_currency * i.balance > post.request_sum:
                        if str(post.criteri) == 'Лучший курс':
                            if i.valute_with_rub < base_comis:
                                itemchangeset = i.username
                                base_comis = i.valute_with_rub
                                post.request_commission = base_comis
                        if str(post.criteri) == 'Быстрый обмен':
                            timechange = RequestChange.objects.filter(request_userchange=i.username)
                            if timechange:
                                chartime = []
                                for time in timechange:
                                    if time.date_end_change and time.request_type == 'Заявка на вывод':
                                        timelimit = time.date_end_change - time.date_joined_change
                                        timebase = timelimit.seconds / 60
                                        chartime += [timebase]
                                if len(chartime) >= 1:
                                    itemchar = float(0)
                                    for ichar in chartime:
                                        itemchar = itemchar + ichar
                                    timedef = itemchar / float(len(chartime))
                                    if timedef < base_time:
                                        itemchangeset = i.username
                                        base_time = timedef
                                        post.request_commission = i.valute_with_rub

                if str(post.request_currency) == "EUR":
                    c = CurrencyCBRF.objects.get(name_currency=post.request_currency)
                    if c.base_currency * i.balance > post.request_sum:
                        if str(post.criteri) == 'Лучший курс':
                            if i.valute_with_eur < base_comis:
                                itemchangeset = i.username
                                base_comis = i.valute_with_eur
                                post.request_commission = base_comis
                        if str(post.criteri) == 'Быстрый обмен':
                            timechange = RequestChange.objects.filter(request_userchange=i.username)
                            if timechange:
                                chartime = []
                                for time in timechange:
                                    if time.date_end_change and time.request_type == 'Заявка на вывод':
                                        timelimit = time.date_end_change - time.date_joined_change
                                        timebase = timelimit.seconds / 60
                                        chartime += [timebase]
                                if len(chartime) >= 1:
                                    itemchar = float(0)
                                    for ichar in chartime:
                                        itemchar = itemchar + ichar
                                    timedef = itemchar / float(len(chartime))
                                    if timedef < base_time:
                                        itemchangeset = i.username
                                        base_time = timedef
                                        post.request_commission = i.valute_with_eur

                if str(post.request_currency) == "USD":
                    if i.balance > post.request_sum:
                        if str(post.criteri) == 'Лучший курс':
                            if i.valute_with_usd < base_comis:
                                itemchangeset = i.username
                                base_comis = i.valute_with_usd
                                post.request_commission = base_comis
                        if str(post.criteri) == 'Быстрый обмен':
                            timechange = RequestChange.objects.filter(request_userchange=i.username)
                            if timechange:
                                chartime = []
                                for time in timechange:
                                    if time.date_end_change and time.request_type == 'Заявка на вывод':
                                        timelimit = time.date_end_change - time.date_joined_change
                                        timebase = timelimit.seconds / 60
                                        chartime += [timebase]
                                if len(chartime) >= 1:
                                    itemchar = float(0)
                                    for ichar in chartime:
                                        itemchar = itemchar + ichar
                                    timedef = itemchar / float(len(chartime))
                                    if timedef < base_time:
                                        itemchangeset = i.username
                                        base_time = timedef
                                        post.request_commission = i.valute_with_usd

            post.request_userchange = itemchangeset
            post.request_good_sum = post.request_sum - ((post.request_sum / 100) * post.request_commission)

            # списываем с баланса сумму заявки
            if itemchangeset:
                g = CustomUser.objects.get(username=post.request_user)
                if str(post.request_currency) == "RUB":
                    c = CurrencyCBRF.objects.get(name_currency=post.request_currency)
                    g.balance = g.balance - (post.request_sum / c.base_currency)
                if str(post.request_currency) == "EUR":
                    c = CurrencyCBRF.objects.get(name_currency=post.request_currency)
                    g.balance = g.balance - (post.request_sum / c.base_currency)
                if str(post.request_currency) == "USD":
                    g.balance = g.balance - post.request_sum
                g.save()

            # создаем транзакцию
            Transaction.objects.create(transaction_name=str(n),
                                       transaction_user=post.request_user,
                                       transaction_userchange=itemchangeset,
                                       transaction_type='Вывод из кошелька',
                                       transaction_status=post.request_status,
                                       transaction_currency=post.request_currency,
                                       transaction_sum=post.request_sum,
                                       transaction_sistemchange=post.request_sistemchange)
            post.save()
            return redirect('requsetwallet')

    else:
        form = WithdrawalForm()
    return render(request, 'personalaccount/cabinet/withdrawal/withdrawalwallet.html', {'form': form})


# /КОШЕЛЕК/ СТРАНИЦА ВНУТРЕННЕГО ПЕРЕВОДА
def transferwallet(request):
    if request.method == "POST":
        form = TransferForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            n = random.randint(10000, 999999)
            post.transfer_out = request.user
            post.transfer_name = str(n)
            usertranout = CustomUser.objects.get(username=post.transfer_out)
            usertranall = CustomUser.objects.all()
            for i in usertranall:
                if i.username == post.transfer_in:
                    usertranin = CustomUser.objects.get(username=post.transfer_in)
                    if usertranout.balance > post.transfer_sum:
                        usertranout.balance -= post.transfer_sum
                        usertranin.balance += post.transfer_sum

                        # создаем транзакцию
                        Transaction.objects.create(transaction_name=str(n),
                                                   transaction_user=post.transfer_out,
                                                   transaction_userchange=post.transfer_in,
                                                   transaction_type='Внутренний перевод',
                                                   transaction_status='Выполнен',
                                                   date_end_change=timezone.now(),
                                                   transaction_currency='USD',
                                                   transaction_sum=post.transfer_sum,
                                                   transaction_sistemchange='Внутренний')
                        usertranout.save()
                        usertranin.save()
                        post.save()
                    break
            return redirect('transferwallet')
    else:
        form = TransferForm()
    return render(request, 'personalaccount/cabinet/transfer/transferwallet.html', {'form': form})


# /КОШЕЛЕК/ ЗАЯВКИ
def requsetwallet(request):
    status_reque = False
    base_reque = RequestChange.objects.filter(request_user=request.user)
    for i in base_reque:
        if i.request_status != 'Выполнена':
            status_reque = True
            break
    context = {
        'status_reque': status_reque,
        'base_reque': base_reque,
    }
    return render(request, 'personalaccount/cabinet/requset/requsetwallet.html', context)


# /КОШЕЛЕК/ ЗАЯВКИ/ КНОПКА ОПЛАТИЛ
def requsetwalletsuccess(request, pk):
    succ = RequestChange.objects.get(pk=pk)
    succtran = Transaction.objects.get(transaction_name=succ.request_name)
    succ.request_status = 'Оплачена клиентом'
    succtran.transaction_status = 'Оплачена клиентом'
    succ.save()
    succtran.save()
    return redirect('requsetwallet')


# /КОШЕЛЕК/ ТРАНЗАКЦИИ
def transactionwallet(request):
    tranview = Transaction.objects.all()
    return render(request, 'personalaccount/cabinet/transaction/transactionwallet.html', {'tranview': tranview})


# /КОШЕЛЕК/ РЕКВИЗИТЫ / ФОРМА
def rekvisitwallet(request):
    rekvis = CustomUser.objects.get(username=request.user)
    context = {
        'rekvis': rekvis,
        'form': RequisitesForm(instance=rekvis),
    }
    if request.method == "POST":
        form = RequisitesForm(request.POST, instance=rekvis)
        if form.is_valid():
            forme = form.save(commit=False)
            rekvis.requsites_sberbank = forme.requsites_sberbank
            rekvis.requsites_qiwi = forme.requsites_qiwi
            rekvis.save()
            return redirect('rekvisitwallet')
    return render(request, 'personalaccount/cabinet/rekvisit/rekvisitwallet.html', context)


# /КОШЕЛЕК/ ПРОФИЛЬ
def profilewallet(request):
    return render(request, 'personalaccount/cabinet/profile/profilewallet.html')


# /КОШЕЛЕК/ НАСТРОЙКИ
def settingwallet(request):
    return render(request, 'personalaccount/cabinet/setting/settingwallet.html')


# /ОБМЕННИК/ ЗАЯВКИ НА ВЫВОД
def withdrawalexchange(request):
    status_reque = False
    withchang = RequestChange.objects.filter(request_userchange=request.user)
    withchange = withchang.filter(request_type='Заявка на вывод')
    for i in withchange:
        if i.request_status != 'Выполнена':
            status_reque = True
            break
    context = {
        'status_reque': status_reque,
        'withchange': withchange,
    }
    return render(request, 'personalaccount/cabinet/withdrawal/withdrawalexchange.html', context)


# /ОБМЕННИК/ ПРОСМОТР ЗАЯВКИ НА ВЫВОД, ДЕТАЛЬНЫЙ ПРОСМОТР
class withdrawalexchangerequest(DetailView):
    model = RequestChange
    template_name = 'personalaccount/cabinet/withdrawal/withdrawalexchangerequest.html'
    context_object_name = 'withdrawalexchangerequest'


# /ОБМЕННИК/ ИСПОЛНЕНИЕ ЗАЯВКИ НА ВЫВОД, НАЧИСЛЕНИЕ СРЕДСТВ, СМЕНА СТАТУСА У ЗАЯВКИ И ТРАНЗАКЦИИ
def withdrawalexchangerequestupdate(request, pk):
    update = RequestChange.objects.get(pk=pk)
    update_tran = Transaction.objects.get(transaction_name=update.request_name)
    update_balance_change = CustomUser.objects.get(username=request.user)
    if str(update.request_currency) == "RUB":
        curup = CurrencyCBRF.objects.get(name_currency="RUB")
        update_balance_change.balance += (update.request_sum / curup.base_currency)
    if str(update.request_currency) == "USD":
        update_balance_change.balance += update.request_sum
    if str(update.request_currency) == "EUR":
        curup = CurrencyCBRF.objects.get(name_currency="EUR")
        update_balance_change.balance += (update.request_sum / curup.base_currency)

    update.date_end_change = timezone.now()
    update_tran.date_end_change = timezone.now()
    update_tran.transaction_status = 'Выполнена'
    update.request_status = 'Выполнена'
    update_balance_change.save()
    update_tran.save()
    update.save()
    return redirect('withdrawalexchange')


# /ОБМЕННИК/ ЗАЯВКИ НА ПОПОЛНЕНИЕ
def depositexchange(request):
    status_reque = False
    withchang = RequestChange.objects.filter(request_userchange=request.user)
    depexchange = withchang.filter(request_type='Заявка на пополнение')
    for i in depexchange:
        if i.request_status != 'Выполнена' and i.request_status != 'Ожидает оплаты':
            status_reque = True
            break
    context = {
        'status_reque': status_reque,
        'depexchange': depexchange,
    }
    return render(request, 'personalaccount/cabinet/deposit/depositexchange.html', context)


# /ОБМЕННИК/ ПРОСМОТР ЗАЯВКИ НА ПОПОЛНЕНИЕ, ДЕТАЛЬНЫЙ ПРОСМОТР
class depositexchangerequest(DetailView):
    model = RequestChange
    template_name = 'personalaccount/cabinet/deposit/depositexchangerequest.html'
    context_object_name = 'depexchangerequest'


# /ОБМЕННИК/ ИСПОЛНЕНИЕ ЗАЯВКИ НА ПОПОЛНЕНИЕ, НАЧИСЛЕНИЕ СРЕДСТВ, СМЕНА СТАТУСА У ЗАЯВКИ И ТРАНЗАКЦИИ
def depositexchangerequestupdate(request, pk):
    update = RequestChange.objects.get(pk=pk)
    update_tran = Transaction.objects.get(transaction_name=update.request_name)
    update_balance = CustomUser.objects.get(username=update.request_user)
    update_balance_change = CustomUser.objects.get(username=request.user)
    if str(update.request_currency) == "RUB":
        curup = CurrencyCBRF.objects.get(name_currency="RUB")
        update_balance.balance += (update.request_sum / curup.base_currency)
        update_balance_change.balance -= (update.request_sum / curup.base_currency)
    if str(update.request_currency) == "USD":
        update_balance.balance += update.request_sum
        update_balance_change.balance -= update.request_sum
    if str(update.request_currency) == "EUR":
        curup = CurrencyCBRF.objects.get(name_currency="EUR")
        update_balance.balance += (update.request_sum / curup.base_currency)
        update_balance_change.balance -= (update.request_sum / curup.base_currency)

    update.date_end_change = timezone.now()
    update_tran.date_end_change = timezone.now()
    update_tran.transaction_status = 'Выполнена'
    update.request_status = 'Выполнена'
    update_balance_change.save()
    update_balance.save()
    update_tran.save()
    update.save()
    return redirect('depositexchange')


# /ОБМЕННИК/ ОБРАТНАЯ СМЕНА СТАТУСА У ЗАЯВКИ И ТРАНЗАКЦИИ НА ПОПОЛНЕНИЕ ==/ТЕСТ/==
def depositexchangerequestupdateno(request, pk):
    update = RequestChange.objects.get(pk=pk)
    update_tran = Transaction.objects.get(transaction_name=update.request_name)
    update_tran.transaction_status = 'Ожидает оплаты'
    update.request_status = 'Ожидает оплаты'
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


# ИЗМЕНЕНИЕ ПРИБЫЛИ ОБРАБОТЧИКА В ЛИЧНОМ КАБИНЕТЕ
def coursechangecommission(request):
    comis = CustomUser.objects.get(username=request.user)
    context = {
        'comis': comis,
        'form': CommissionForm(instance=comis),
    }
    if request.method == "POST":
        form = CommissionForm(request.POST, instance=comis)
        if form.is_valid():
            forme = form.save(commit=False)
            comis.valute_usd = forme.valute_usd
            comis.valute_rub = forme.valute_rub
            comis.valute_eur = forme.valute_eur
            comis.valute_with_usd = forme.valute_with_usd
            comis.valute_with_rub = forme.valute_with_rub
            comis.valute_with_eur = forme.valute_with_eur
            comis.save()
            return redirect('coursechange')
    return render(request, 'personalaccount/cabinet/course/coursechangecommission.html', context)


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
    rekvis = CustomUser.objects.get(username=request.user)
    context = {
        'rekvis': rekvis,
        'form': RequisitesForm(instance=rekvis),
    }
    if request.method == "POST":
        form = RequisitesForm(request.POST, instance=rekvis)
        if form.is_valid():
            forme = form.save(commit=False)
            rekvis.requsites_sberbank = forme.requsites_sberbank
            rekvis.requsites_qiwi = forme.requsites_qiwi
            rekvis.save()
            return redirect('rekvisitchange')
    return render(request, 'personalaccount/cabinet/rekvisit/rekvisitchange.html', context)


# /ОБМЕННИК/ ПРОФИЛЬ
def profilechange(request):
    return render(request, 'personalaccount/cabinet/profile/profilechange.html')


# /ОБМЕННИК/ НАСТРОЙКИ
def settingchange(request):
    return render(request, 'personalaccount/cabinet/setting/settingchange.html')
