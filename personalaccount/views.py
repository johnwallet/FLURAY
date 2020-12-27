import random

from django.core.files.storage import FileSystemStorage
from django.http import Http404
from django.shortcuts import render, redirect
from django.utils import timezone
from personalaccount.apicourse import get_rates
from personalaccount.apicoursecrypto import get_rates_crypto
from personalaccount.models import Transaction, RequestChange, CurrencyCBRF
from personalaccount.forms import RequestForm, RequisitesForm2, WithdrawalForm, TransferForm, RequisitesForm1, \
    CommissionForm, ActivePSForm
from users.models import CustomUserId, CustomUser


# РЕНДЕРИМ НУЖНЫЙ ШАБЛОН, КАБИНЕТ ПОЛЬЗОВАТЕЛЯ (ДАШБОРД)
def personalaccount(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=1):
            dash_tran = Transaction.objects.filter(transaction_user=request.user)
            dash_cour = CurrencyCBRF.objects.all()
            context = {
                'dash_tran': dash_tran,
                'dash_cour': dash_cour,
            }
            return render(request, 'personalaccount/cabinet/dashboard/dashboardwallet.html', context)
        elif request.user.userid == CustomUserId.objects.get(pk=2):
            dash_tran = Transaction.objects.filter(transaction_user=request.user)
            dash_cour = CurrencyCBRF.objects.all()
            context = {
                'dash_tran': dash_tran,
                'dash_cour': dash_cour,
            }
            return render(request, 'personalaccount/cabinet/dashboard/dashboardchange.html', context)
    else:
        return redirect('account_login')


# /КОШЕЛЕК/ ПОПОЛНЕНИЕ
def depositwalletform(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=1):
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
        else:
            raise Http404
    else:
        return redirect('account_login')


# /КОШЕЛЕК/ ВЫВОД
def withdrawalwallet(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=1):
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
        else:
            raise Http404
    else:
        return redirect('account_login')


# /КОШЕЛЕК/ ВНУТРЕННИЙ ПЕРЕВОД
def transferwallet(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=1):
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
        else:
            raise Http404
    else:
        return redirect('account_login')


# /КОШЕЛЕК/ ЗАЯВКИ
def requsetwallet(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=1):
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
        else:
            raise Http404
    else:
        return redirect('account_login')


# /КОШЕЛЕК/ ПОДТВЕРЖДЕНИЕ ОПЛАТЫ КЛИЕНТОМ
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
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=1):
            tranview = Transaction.objects.filter(transaction_user=request.user)
            return render(request, 'personalaccount/cabinet/transaction/transactionwallet.html', {'tranview': tranview})
        else:
            raise Http404
    else:
        return redirect('account_login')


# /КОШЕЛЕК/ ПРОФИЛЬ
def profilewallet(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=1):
            if request.method == 'POST' and request.FILES['avatar']:
                avauser = CustomUser.objects.get(username=request.user)
                file = request.FILES['avatar']
                fs = FileSystemStorage()
                avauser.avatar = fs.save(file.name, file)
                avauser.save()
                return redirect('profilewallet')
            return render(request, 'personalaccount/cabinet/profile/profilewallet.html')
        else:
            raise Http404
    else:
        return redirect('account_login')


# /КОШЕЛЕК/ НАСТРОЙКИ
def settingwallet(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=1):
            return render(request, 'personalaccount/cabinet/setting/settingwallet.html')
        else:
            raise Http404
    else:
        return redirect('account_login')


# ===========/ОБМЕННИК/=============


# /ОБМЕННИК/ ЗАЯВКИ НА ВЫВОД
def withdrawalexchange(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=2):
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
        else:
            raise Http404
    else:
        return redirect('account_login')


# /ОБМЕННИК/ ПРОСМОТР ЗАЯВКИ НА ВЫВОД, ДЕТАЛЬНЫЙ ПРОСМОТР
def withdrawalexchangerequest(request, pk):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=2):
            wi = RequestChange.objects.get(pk=pk)
            return render(request, 'personalaccount/cabinet/withdrawal/withdrawalexchangerequest.html', {'wi': wi})
        else:
            raise Http404
    else:
        return redirect('account_login')


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
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=2):
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
        else:
            raise Http404
    else:
        return redirect('account_login')


# /ОБМЕННИК/ ПРОСМОТР ЗАЯВКИ НА ПОПОЛНЕНИЕ, ДЕТАЛЬНЫЙ ПРОСМОТР
def depositexchangerequest(request, pk):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=2):
            depexchangerequest = RequestChange.objects.get(pk=pk)
            return render(request, 'personalaccount/cabinet/deposit/depositexchangerequest.html',
                          {'depexchangerequest': depexchangerequest})
        else:
            raise Http404
    else:
        return redirect('account_login')


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
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=2):
            return render(request, 'personalaccount/cabinet/deposit/depositreservchange.html')
        else:
            raise Http404
    else:
        return redirect('account_login')


# /ОБМЕННИК/ ВЫВОД РЕЗЕРВА
def withdrawalreservchange(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=2):
            return render(request, 'personalaccount/cabinet/withdrawal/withdrawalreservchange.html')
        else:
            raise Http404
    else:
        return redirect('account_login')


# /ОБМЕННИК/ ТРАНЗАКЦИИ
def transactionchange(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=2):
            tranviewchange = Transaction.objects.filter(transaction_user=request.user)
            return render(request, 'personalaccount/cabinet/transaction/transactionchange.html',
                          {'tranviewchange': tranviewchange})
        else:
            raise Http404
    else:
        return redirect('account_login')

# /ОБМЕННИК/ РЕЗЕРВ
def reservchange(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=2):
            return render(request, 'personalaccount/cabinet/reserv/reservchange.html')
        else:
            raise Http404
    else:
        return redirect('account_login')

# /ОБМЕННИК/ АКТИВНОСТЬ
def activechange(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=2):
            active = CustomUser.objects.get(username=request.user)
            return render(request, 'personalaccount/cabinet/active/activechange.html', {'active': active})
        else:
            raise Http404
    else:
        return redirect('account_login')

# /ОБМЕННИК/ АКТИВНОСТЬ / СМЕНА СТАТУСА ОБМЕННИКА
def activechangestch(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=2):
            return render(request, 'personalaccount/cabinet/active/activechangestch.html')
        else:
            raise Http404
    else:
        return redirect('account_login')

# /ОБМЕННИК/ АКТИВНОСТЬ / СМЕНА СТАТУСА ОБМЕННИКА
def activechangestchtoggle(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=2):
            userstatus = CustomUser.objects.get(username=request.user)
            if userstatus.is_active_change == True:
                userstatus.is_active_change = False
                userstatus.save()
                return redirect('activechange')
            elif userstatus.is_active_change == False:
                userstatus.is_active_change = True
                userstatus.save()
                return redirect('activechange')
            return render(request, 'personalaccount/cabinet/active/activechangestch.html')
        else:
            raise Http404
    else:
        return redirect('account_login')



# /ОБМЕННИК/ АКТИВНОСТЬ / СМЕНА СТАТУСА ПС
def activechangestps(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=2):
            rekvis = CustomUser.objects.get(username=request.user)
            context = {
                'rekvis': rekvis,
                'form': ActivePSForm(instance=rekvis),
            }
            if request.method == "POST":
                form = ActivePSForm(request.POST, instance=rekvis)
                if form.is_valid():
                    forme = form.save(commit=False)
                    rekvis.active_in_sberbank_rub = forme.active_in_sberbank_rub
                    rekvis.active_in_psb_rub = forme.active_in_psb_rub
                    rekvis.active_in_tinkoff_rub = forme.active_in_tinkoff_rub
                    rekvis.active_in_gazprombank_rub = forme.active_in_gazprombank_rub
                    rekvis.active_in_alfabank_rub = forme.active_in_alfabank_rub
                    rekvis.active_in_russtandart_rub = forme.active_in_russtandart_rub
                    rekvis.active_in_vtb_rub = forme.active_in_vtb_rub
                    rekvis.active_in_rosselhoz_rub = forme.active_in_rosselhoz_rub
                    rekvis.active_in_raifaizen_rub = forme.active_in_raifaizen_rub
                    rekvis.active_in_roketbank_rub = forme.active_in_roketbank_rub
                    rekvis.active_in_otkritie_rub = forme.active_in_otkritie_rub
                    rekvis.active_in_pochtabank_rub = forme.active_in_pochtabank_rub
                    rekvis.active_in_rnkb_rub = forme.active_in_rnkb_rub
                    rekvis.active_in_rosbank_rub = forme.active_in_rosbank_rub
                    rekvis.active_in_mtsbank_rub = forme.active_in_mtsbank_rub
                    rekvis.active_in_qiwi_rub = forme.active_in_qiwi_rub
                    rekvis.active_in_qiwi_usd = forme.active_in_qiwi_usd
                    rekvis.active_in_payeer_rub = forme.active_in_payeer_rub
                    rekvis.active_in_payeer_usd = forme.active_in_payeer_usd
                    rekvis.active_in_payeer_eur = forme.active_in_payeer_eur
                    rekvis.active_in_webmoney_rub = forme.active_in_webmoney_rub
                    rekvis.active_in_webmoney_usd = forme.active_in_webmoney_usd
                    rekvis.active_in_webmoney_eur = forme.active_in_webmoney_eur
                    rekvis.active_in_pm_btc = forme.active_in_pm_btc
                    rekvis.active_in_pm_usd = forme.active_in_pm_usd
                    rekvis.active_in_pm_eur = forme.active_in_pm_eur
                    rekvis.active_in_skrill_eur = forme.active_in_skrill_eur
                    rekvis.active_in_skrill_usd = forme.active_in_skrill_usd
                    rekvis.active_in_paypal_rub = forme.active_in_paypal_rub
                    rekvis.active_in_paypal_usd = forme.active_in_paypal_usd
                    rekvis.active_in_paypal_eur = forme.active_in_paypal_eur
                    rekvis.active_in_umoney_rub = forme.active_in_umoney_rub
                    rekvis.active_in_btc = forme.active_in_btc
                    rekvis.active_in_xrp = forme.active_in_xrp
                    rekvis.active_in_ltc = forme.active_in_ltc
                    rekvis.active_in_bch = forme.active_in_bch
                    rekvis.active_in_xmr = forme.active_in_xmr
                    rekvis.active_in_eth = forme.active_in_eth
                    rekvis.active_in_etc = forme.active_in_etc
                    rekvis.active_in_dash = forme.active_in_dash
                    rekvis.active_out_sberbank_rub = forme.active_out_sberbank_rub
                    rekvis.active_out_psb_rub = forme.active_out_psb_rub
                    rekvis.active_out_tinkoff_rub = forme.active_out_tinkoff_rub
                    rekvis.active_out_gazprombank_rub = forme.active_out_gazprombank_rub
                    rekvis.active_out_alfabank_rub = forme.active_out_alfabank_rub
                    rekvis.active_out_russtandart_rub = forme.active_out_russtandart_rub
                    rekvis.active_out_vtb_rub = forme.active_out_vtb_rub
                    rekvis.active_out_rosselhoz_rub = forme.active_out_rosselhoz_rub
                    rekvis.active_out_raifaizen_rub = forme.active_out_raifaizen_rub
                    rekvis.active_out_roketbank_rub = forme.active_out_roketbank_rub
                    rekvis.active_out_otkritie_rub = forme.active_out_otkritie_rub
                    rekvis.active_out_pochtabank_rub = forme.active_out_pochtabank_rub
                    rekvis.active_out_rnkb_rub = forme.active_out_rnkb_rub
                    rekvis.active_out_rosbank_rub = forme.active_out_rosbank_rub
                    rekvis.active_out_mtsbank_rub = forme.active_out_mtsbank_rub
                    rekvis.active_out_qiwi_rub = forme.active_out_qiwi_rub
                    rekvis.active_out_qiwi_usd = forme.active_out_qiwi_usd
                    rekvis.active_out_payeer_rub = forme.active_out_payeer_rub
                    rekvis.active_out_payeer_usd = forme.active_out_payeer_usd
                    rekvis.active_out_payeer_eur = forme.active_out_payeer_eur
                    rekvis.active_out_webmoney_rub = forme.active_out_webmoney_rub
                    rekvis.active_out_webmoney_usd = forme.active_out_webmoney_usd
                    rekvis.active_out_webmoney_eur = forme.active_out_webmoney_eur
                    rekvis.active_out_pm_btc = forme.active_out_pm_btc
                    rekvis.active_out_pm_usd = forme.active_out_pm_usd
                    rekvis.active_out_pm_eur = forme.active_out_pm_eur
                    rekvis.active_out_skrill_eur = forme.active_out_skrill_eur
                    rekvis.active_out_skrill_usd = forme.active_out_skrill_usd
                    rekvis.active_out_paypal_rub = forme.active_out_paypal_rub
                    rekvis.active_out_paypal_usd = forme.active_out_paypal_usd
                    rekvis.active_out_paypal_eur = forme.active_out_paypal_eur
                    rekvis.active_out_umoney_rub = forme.active_out_umoney_rub
                    rekvis.active_out_btc = forme.active_out_btc
                    rekvis.active_out_xrp = forme.active_out_xrp
                    rekvis.active_out_ltc = forme.active_out_ltc
                    rekvis.active_out_bch = forme.active_out_bch
                    rekvis.active_out_xmr = forme.active_out_xmr
                    rekvis.active_out_eth = forme.active_out_eth
                    rekvis.active_out_etc = forme.active_out_etc
                    rekvis.active_out_dash = forme.active_out_dash
                    rekvis.save()
                    return redirect('activechange')
            return render(request, 'personalaccount/cabinet/active/activechangestps.html', context)
        else:
            raise Http404
    else:
        return redirect('account_login')




# /ОБМЕННИК/ КОММИСИИ
def coursechange(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=2):
            currencyview = CurrencyCBRF.objects.all()
            return render(request, 'personalaccount/cabinet/course/coursechange.html', {'currencyview': currencyview})
        else:
            raise Http404
    else:
        return redirect('account_login')


# /ОБМЕННИК/ РЕКВИЗИТЫ
def rekvisitchange(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=2):
            rekvis = CustomUser.objects.get(username=request.user)
            context = {
                'rekvis': rekvis,
                'form1': RequisitesForm1(instance=rekvis),
                'form2': RequisitesForm2(instance=rekvis),
            }
            if request.method == "POST":
                if 'deposit' in request.POST:
                    form = RequisitesForm1(request.POST, instance=rekvis)
                    if form.is_valid():
                        forme = form.save(commit=False)
                        rekvis.requsites_sberbank_rub = forme.requsites_sberbank_rub
                        rekvis.requsites_psb_rub = forme.requsites_psb_rub
                        rekvis.requsites_tinkoff_rub = forme.requsites_tinkoff_rub
                        rekvis.requsites_gazprombank_rub = forme.requsites_gazprombank_rub
                        rekvis.requsites_alfabank_rub = forme.requsites_alfabank_rub
                        rekvis.requsites_russtandart_rub = forme.requsites_russtandart_rub
                        rekvis.requsites_vtb_rub = forme.requsites_vtb_rub
                        rekvis.requsites_rosselhoz_rub = forme.requsites_rosselhoz_rub
                        rekvis.requsites_raifaizen_rub = forme.requsites_raifaizen_rub
                        rekvis.requsites_roketbank_rub = forme.requsites_roketbank_rub
                        rekvis.requsites_otkritie_rub = forme.requsites_otkritie_rub
                        rekvis.requsites_pochtabank_rub = forme.requsites_pochtabank_rub
                        rekvis.requsites_rnkb_rub = forme.requsites_rnkb_rub
                        rekvis.requsites_rosbank_rub = forme.requsites_rosbank_rub
                        rekvis.requsites_mtsbank_rub = forme.requsites_mtsbank_rub
                        rekvis.requsites_qiwi_rub = forme.requsites_qiwi_rub
                        rekvis.requsites_qiwi_usd = forme.requsites_qiwi_usd
                        rekvis.requsites_payeer_rub = forme.requsites_payeer_rub
                        rekvis.requsites_payeer_usd = forme.requsites_payeer_usd
                        rekvis.requsites_payeer_eur = forme.requsites_payeer_eur
                        rekvis.requsites_webmoney_rub = forme.requsites_webmoney_rub
                        rekvis.requsites_webmoney_usd = forme.requsites_webmoney_usd
                        rekvis.requsites_webmoney_eur = forme.requsites_webmoney_eur
                        rekvis.requsites_pm_btc = forme.requsites_pm_btc
                        rekvis.requsites_pm_usd = forme.requsites_pm_usd
                        rekvis.requsites_pm_eur = forme.requsites_pm_eur
                        rekvis.requsites_skrill_eur = forme.requsites_skrill_eur
                        rekvis.requsites_skrill_usd = forme.requsites_skrill_usd
                        rekvis.requsites_paypal_rub = forme.requsites_paypal_rub
                        rekvis.requsites_paypal_usd = forme.requsites_paypal_usd
                        rekvis.requsites_paypal_eur = forme.requsites_paypal_eur
                        rekvis.requsites_umoney_rub = forme.requsites_umoney_rub
                        rekvis.requsites_btc = forme.requsites_btc
                        rekvis.requsites_xrp = forme.requsites_xrp
                        rekvis.requsites_ltc = forme.requsites_ltc
                        rekvis.requsites_bch = forme.requsites_bch
                        rekvis.requsites_xmr = forme.requsites_xmr
                        rekvis.requsites_eth = forme.requsites_eth
                        rekvis.requsites_etc = forme.requsites_etc
                        rekvis.requsites_dash = forme.requsites_dash
                        rekvis.save()
                        return redirect('rekvisitchange')
                if 'widthdrawal' in request.POST:
                    form = RequisitesForm2(request.POST, instance=rekvis)
                    if form.is_valid():
                        forme = form.save(commit=False)
                        rekvis.requsites_width_sberbank_rub = forme.requsites_width_sberbank_rub
                        rekvis.requsites_width_psb_rub = forme.requsites_width_psb_rub
                        rekvis.requsites_width_tinkoff_rub = forme.requsites_width_tinkoff_rub
                        rekvis.requsites_width_gazprombank_rub = forme.requsites_width_gazprombank_rub
                        rekvis.requsites_width_alfabank_rub = forme.requsites_width_alfabank_rub
                        rekvis.requsites_width_russtandart_rub = forme.requsites_width_russtandart_rub
                        rekvis.requsites_width_vtb_rub = forme.requsites_width_vtb_rub
                        rekvis.requsites_width_rosselhoz_rub = forme.requsites_width_rosselhoz_rub
                        rekvis.requsites_width_raifaizen_rub = forme.requsites_width_raifaizen_rub
                        rekvis.requsites_width_roketbank_rub = forme.requsites_width_roketbank_rub
                        rekvis.requsites_width_otkritie_rub = forme.requsites_width_otkritie_rub
                        rekvis.requsites_width_pochtabank_rub = forme.requsites_width_pochtabank_rub
                        rekvis.requsites_width_rnkb_rub = forme.requsites_width_rnkb_rub
                        rekvis.requsites_width_rosbank_rub = forme.requsites_width_rosbank_rub
                        rekvis.requsites_width_mtsbank_rub = forme.requsites_width_mtsbank_rub
                        rekvis.requsites_width_qiwi_rub = forme.requsites_width_qiwi_rub
                        rekvis.requsites_width_qiwi_usd = forme.requsites_width_qiwi_usd
                        rekvis.requsites_width_payeer_rub = forme.requsites_width_payeer_rub
                        rekvis.requsites_width_payeer_usd = forme.requsites_width_payeer_usd
                        rekvis.requsites_width_payeer_eur = forme.requsites_width_payeer_eur
                        rekvis.requsites_width_webmoney_rub = forme.requsites_width_webmoney_rub
                        rekvis.requsites_width_webmoney_usd = forme.requsites_width_webmoney_usd
                        rekvis.requsites_width_webmoney_eur = forme.requsites_width_webmoney_eur
                        rekvis.requsites_width_pm_btc = forme.requsites_width_pm_btc
                        rekvis.requsites_width_pm_usd = forme.requsites_width_pm_usd
                        rekvis.requsites_width_pm_eur = forme.requsites_width_pm_eur
                        rekvis.requsites_width_skrill_eur = forme.requsites_width_skrill_eur
                        rekvis.requsites_width_skrill_usd = forme.requsites_width_skrill_usd
                        rekvis.requsites_width_paypal_rub = forme.requsites_width_paypal_rub
                        rekvis.requsites_width_paypal_usd = forme.requsites_width_paypal_usd
                        rekvis.requsites_width_paypal_eur = forme.requsites_width_paypal_eur
                        rekvis.requsites_width_umoney_rub = forme.requsites_width_umoney_rub
                        rekvis.requsites_width_btc = forme.requsites_width_btc
                        rekvis.requsites_width_xrp = forme.requsites_width_xrp
                        rekvis.requsites_width_ltc = forme.requsites_width_ltc
                        rekvis.requsites_width_bch = forme.requsites_width_bch
                        rekvis.requsites_width_xmr = forme.requsites_width_xmr
                        rekvis.requsites_width_eth = forme.requsites_width_eth
                        rekvis.requsites_width_etc = forme.requsites_width_etc
                        rekvis.requsites_width_dash = forme.requsites_width_dash
                        rekvis.save()
                        return redirect('rekvisitchange')
            return render(request, 'personalaccount/cabinet/rekvisit/rekvisitchange.html', context)
        else:
            raise Http404
    else:
        return redirect('account_login')


# /ОБМЕННИК/ ПРОФИЛЬ
def profilechange(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=2):
            if request.method == 'POST' and request.FILES['avatar']:
                avauser = CustomUser.objects.get(username=request.user)
                file = request.FILES['avatar']
                fs = FileSystemStorage()
                avauser.avatar = fs.save(file.name, file)
                avauser.save()
                return redirect('profilechange')
            return render(request, 'personalaccount/cabinet/profile/profilechange.html')
        else:
            raise Http404
    else:
        return redirect('account_login')


# /ОБМЕННИК/ НАСТРОЙКИ
def settingchange(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=2):
            return render(request, 'personalaccount/cabinet/setting/settingchange.html')
        else:
            raise Http404
    else:
        return redirect('account_login')


# ===============/ДРУГОЕ/==================


# ИЗМЕНЕНИЕ КОММИСИИ ОБРАБОТЧИКА В ЛИЧНОМ КАБИНЕТЕ
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
            comis.comis_in_sberbank_rub = forme.comis_in_sberbank_rub
            comis.comis_in_psb_rub = forme.comis_in_psb_rub
            comis.comis_in_tinkoff_rub = forme.comis_in_tinkoff_rub
            comis.comis_in_gazprombank_rub = forme.comis_in_gazprombank_rub
            comis.comis_in_alfabank_rub = forme.comis_in_alfabank_rub
            comis.comis_in_russtandart_rub = forme.comis_in_russtandart_rub
            comis.comis_in_vtb_rub = forme.comis_in_vtb_rub
            comis.comis_in_rosselhoz_rub = forme.comis_in_rosselhoz_rub
            comis.comis_in_raifaizen_rub = forme.comis_in_raifaizen_rub
            comis.comis_in_roketbank_rub = forme.comis_in_roketbank_rub
            comis.comis_in_otkritie_rub = forme.comis_in_otkritie_rub
            comis.comis_in_pochtabank_rub = forme.comis_in_pochtabank_rub
            comis.comis_in_rnkb_rub = forme.comis_in_rnkb_rub
            comis.comis_in_rosbank_rub = forme.comis_in_rosbank_rub
            comis.comis_in_mtsbank_rub = forme.comis_in_mtsbank_rub
            comis.comis_in_qiwi_rub = forme.comis_in_qiwi_rub
            comis.comis_in_qiwi_usd = forme.comis_in_qiwi_usd
            comis.comis_in_payeer_rub = forme.comis_in_payeer_rub
            comis.comis_in_payeer_usd = forme.comis_in_payeer_usd
            comis.comis_in_payeer_eur = forme.comis_in_payeer_eur
            comis.comis_in_webmoney_rub = forme.comis_in_webmoney_rub
            comis.comis_in_webmoney_usd = forme.comis_in_webmoney_usd
            comis.comis_in_webmoney_eur = forme.comis_in_webmoney_eur
            comis.comis_in_pm_btc = forme.comis_in_pm_btc
            comis.comis_in_pm_usd = forme.comis_in_pm_usd
            comis.comis_in_pm_eur = forme.comis_in_pm_eur
            comis.comis_in_skrill_eur = forme.comis_in_skrill_eur
            comis.comis_in_skrill_usd = forme.comis_in_skrill_usd
            comis.comis_in_paypal_rub = forme.comis_in_paypal_rub
            comis.comis_in_paypal_usd = forme.comis_in_paypal_usd
            comis.comis_in_paypal_eur = forme.comis_in_paypal_eur
            comis.comis_in_umoney_rub = forme.comis_in_umoney_rub
            comis.comis_in_btc = forme.comis_in_btc
            comis.comis_in_xrp = forme.comis_in_xrp
            comis.comis_in_ltc = forme.comis_in_ltc
            comis.comis_in_bch = forme.comis_in_bch
            comis.comis_in_xmr = forme.comis_in_xmr
            comis.comis_in_eth = forme.comis_in_eth
            comis.comis_in_etc = forme.comis_in_etc
            comis.comis_in_dash = forme.comis_in_dash

            comis.comis_out_sberbank_rub = forme.comis_out_sberbank_rub
            comis.comis_out_psb_rub = forme.comis_out_psb_rub
            comis.comis_out_tinkoff_rub = forme.comis_out_tinkoff_rub
            comis.comis_out_gazprombank_rub = forme.comis_out_gazprombank_rub
            comis.comis_out_alfabank_rub = forme.comis_out_alfabank_rub
            comis.comis_out_russtandart_rub = forme.comis_out_russtandart_rub
            comis.comis_out_vtb_rub = forme.comis_out_vtb_rub
            comis.comis_out_rosselhoz_rub = forme.comis_out_rosselhoz_rub
            comis.comis_out_raifaizen_rub = forme.comis_out_raifaizen_rub
            comis.comis_out_roketbank_rub = forme.comis_out_roketbank_rub
            comis.comis_out_otkritie_rub = forme.comis_out_otkritie_rub
            comis.comis_out_pochtabank_rub = forme.comis_out_pochtabank_rub
            comis.comis_out_rnkb_rub = forme.comis_out_rnkb_rub
            comis.comis_out_rosbank_rub = forme.comis_out_rosbank_rub
            comis.comis_out_mtsbank_rub = forme.comis_out_mtsbank_rub
            comis.comis_out_qiwi_rub = forme.comis_out_qiwi_rub
            comis.comis_out_qiwi_usd = forme.comis_out_qiwi_usd
            comis.comis_out_payeer_rub = forme.comis_out_payeer_rub
            comis.comis_out_payeer_usd = forme.comis_out_payeer_usd
            comis.comis_out_payeer_eur = forme.comis_out_payeer_eur
            comis.comis_out_webmoney_rub = forme.comis_out_webmoney_rub
            comis.comis_out_webmoney_usd = forme.comis_out_webmoney_usd
            comis.comis_out_webmoney_eur = forme.comis_out_webmoney_eur
            comis.comis_out_pm_btc = forme.comis_out_pm_btc
            comis.comis_out_pm_usd = forme.comis_out_pm_usd
            comis.comis_out_pm_eur = forme.comis_out_pm_eur
            comis.comis_out_skrill_eur = forme.comis_out_skrill_eur
            comis.comis_out_skrill_usd = forme.comis_out_skrill_usd
            comis.comis_out_paypal_rub = forme.comis_out_paypal_rub
            comis.comis_out_paypal_usd = forme.comis_out_paypal_usd
            comis.comis_out_paypal_eur = forme.comis_out_paypal_eur
            comis.comis_out_umoney_rub = forme.comis_out_umoney_rub
            comis.comis_out_btc = forme.comis_out_btc
            comis.comis_out_xrp = forme.comis_out_xrp
            comis.comis_out_ltc = forme.comis_out_ltc
            comis.comis_out_bch = forme.comis_out_bch
            comis.comis_out_xmr = forme.comis_out_xmr
            comis.comis_out_eth = forme.comis_out_eth
            comis.comis_out_etc = forme.comis_out_etc
            comis.comis_out_dash = forme.comis_out_dash

            comis.save()
            return redirect('coursechange')
    return render(request, 'personalaccount/cabinet/course/coursechangecommission.html', context)

# ОБНОВЛЕНИЕ И ДОБАВЛЕНИЕ КУРСОВ ВАЛЮТ
def coursechangeupdate(request):
    # добавляем новый курс в базу из национальных валют
    # i = get_rates(section_id='Euro')
    # CurrencyCBRF.objects.create(name_currency=i.name, base_currency=i.rate)
    # return redirect('coursechange')

    # добавляем новый курс в базу из криптовалют
    # i = get_rates_crypto(section_id='litecoin')
    # CurrencyCBRF.objects.create(name_currency=i.name, base_currency=i.rate)
    # return redirect('coursechange')


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

    # обновляем курсы криптовалют
    currencyjson = get_rates_crypto()
    iistcrypto = ['bitcoin', 'ethereum', 'ethereum-classic', 'monero', 'ripple', 'dash', 'bitcoin-cash', 'litecoin']
    for item in iistcrypto:
        for aut in currencyjson:
            if aut['id'] == item:
                currencyvieweur = CurrencyCBRF.objects.get(name_currency=aut['symbol'].upper())
                currencyvieweur.base_currency = aut['current_price']
                currencyvieweur.save()
    return redirect('coursechange')
