import random

from django.core.cache import cache
from django.core.files.storage import FileSystemStorage
from django.http import Http404
from django.shortcuts import render, redirect
from django.utils import timezone
from personalaccount.apicourse import get_rates
from personalaccount.apicoursecrypto import get_rates_crypto
from personalaccount.message import message_success
from personalaccount.metodviews import depositsortchangeps, depositsortbalanceps, depositsortcritery, widthsortchangeps, \
    widthsortbalanceps, widthsortcritery, activepsuser, requestchangeon, dailyprofitcount, totalprofitstatic, \
    requesttotal, walrequestchangeon, active_deposit_ps_global, active_width_ps_global, range_deposit_ps_global, \
    min_and_max_sum_request, range_width_ps_global
from personalaccount.models import Transaction, RequestChange, CurrencyCBRF, StaticDailyProfit, News
from personalaccount.forms import RequestForm, WithdrawalForm, TransferForm, RequisitesForm, CommissionForm, \
    ActivePSForm, ReservChangeForm, ProfileForm, RangeDepositForm, RangeWidthForm
from users.models import CustomUserId, CustomUser, RangeSumDeposit, RangeSumWidth


# РЕНДЕРИМ НУЖНЫЙ ШАБЛОН, КАБИНЕТ ПОЛЬЗОВАТЕЛЯ (ДАШБОРД)
def personalaccount(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=1):
            if request.user.verifications_level_one == False:
                data_user = CustomUser.objects.get(username=request.user)
                data_error = False
                if request.method == 'POST':
                    form = ProfileForm(request.POST, request.FILES, instance=data_user)
                    if form.is_valid():
                        flag_good = True
                        post = form.save(commit=False)
                        if not post.first_name:
                            flag_good = False
                        if not post.last_name:
                            flag_good = False
                        if not post.middle_name:
                            flag_good = False
                        if not post.phone_number:
                            flag_good = False
                        if not post.telegram_username:
                            flag_good = False

                        if flag_good == True:
                            post.verifications_level_one = True
                            post.save()
                            return redirect('personalaccount')
                        else:
                            data_error = True
                context = {
                    'form': ProfileForm(instance=data_user),
                    'data_error': data_error,
                }
                return render(request, 'personalaccount/cabinet/setting/settingwallet_verif_level_one.html', context)
            else:
                list_news = News.objects.filter(news_is_publish=True)
                dash_tran = Transaction.objects.filter(transaction_user=request.user)
                dash_cour = CurrencyCBRF.objects.all()
                requeston = walrequestchangeon(usernamereq=request.user)
                context = {
                    'dash_tran': dash_tran,
                    'dash_cour': dash_cour,
                    'requeston': requeston,
                    'list_news': list_news,
                }
                return render(request, 'personalaccount/cabinet/dashboard/dashboardwallet.html', context)
        elif request.user.userid == CustomUserId.objects.get(pk=2):
            if request.user.verifications_level_one == False:
                data_user = CustomUser.objects.get(username=request.user)
                data_error = False
                if request.method == 'POST':
                    form = ProfileForm(request.POST, request.FILES, instance=data_user)
                    if form.is_valid():
                        flag_good = True
                        post = form.save(commit=False)
                        if not post.first_name:
                            flag_good = False
                        if not post.last_name:
                            flag_good = False
                        if not post.middle_name:
                            flag_good = False
                        if not post.phone_number:
                            flag_good = False
                        if not post.telegram_username:
                            flag_good = False

                        if flag_good == True:
                            post.verifications_level_one = True
                            post.save()
                            return redirect('personalaccount')
                        else:
                            data_error = True
                context = {
                    'form': ProfileForm(instance=data_user),
                    'data_error': data_error,
                }
                return render(request, 'personalaccount/cabinet/setting/settingchange_verif_level_one.html', context)
            else:
                list_news = News.objects.filter(news_is_publish=True)
                dash_tran = Transaction.objects.filter(transaction_user=request.user)
                dash_cour = CurrencyCBRF.objects.all()
                activeps = activepsuser(usernameactiveps=request.user)
                requeston = requestchangeon(usernamereq=request.user)
                valuestatic = dailyprofitcount(usernamedailyprofit=request.user)
                totalprofitstat = totalprofitstatic(usernametotalstatic=request.user)
                requesttot = requesttotal(usernamerequesttotal=request.user)
                status_data = True
                datajsontable = {
                    'data': valuestatic['staticdata'],
                    'value': valuestatic['staticvalue']
                }
                context = {
                    'dash_tran': dash_tran,
                    'dash_cour': dash_cour,
                    'activeps': activeps,
                    'requeston': requeston,
                    'datajsontable': datajsontable,
                    'totalprofitstat': totalprofitstat,
                    'requesttot': requesttot,
                    'status_data': status_data,
                    'list_news': list_news,
                }
                return render(request, 'personalaccount/cabinet/dashboard/dashboardchange.html', context)
    else:
        return redirect('account_login')


# data_message = None
# message_status = False
# if cache.get('info_message'):
#     data_message = cache.get('info_message')
#     message_status = True
# context = {
#     'data_message': data_message,
#     'message_status': message_status,
# }
# cache.delete('info_message')
# /КОШЕЛЕК/ ПОПОЛНЕНИЕ
def depositwalletform(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=1):
            message_status = False
            data_message = None
            active_ps = active_deposit_ps_global()
            range_ps = range_deposit_ps_global(list_active=active_ps['list_active_reserve_ps'], active_list_ps=active_ps['list_active_change_ps'])
            if request.method == "POST":
                form = RequestForm(request.POST)
                if form.is_valid():
                    # получаем номер завки
                    n = random.randint(1000000, 9999999)
                    post = form.save(commit=False)
                    range_list = min_and_max_sum_request(ps_request=post.request_sistemchange, range_ps=range_ps)
                    if range_list['min_sum'] <= post.request_sum <= range_list['max_sum']:
                        post.request_user = request.user
                        post.request_name = str(n)
                        post.request_type = 'Заявка на пополнение'
                        post.request_status = 'Ожидает оплаты'
                        # получаем обработчика заявки(активность=true, активность направления=true), пример({'changeq': [<CustomUser: Obmen>], 'valute': 'RUB'})
                        changerequest = depositsortchangeps(nameps=post.request_sistemchange)
                        if len(changerequest['changeq']) > 0:
                            # проверяем основной баланс, пример ([<CustomUser: Obmen>])
                            balancerequest = depositsortbalanceps(userps=changerequest['changeq'], balanceps=post.request_sum, valuteps=changerequest['valute'])
                            if len(balancerequest) > 0:
                                request_good = CurrencyCBRF.objects.get(name_currency=changerequest['valute'])
                                # получаем победителя {'usernameps': usernameps, 'base_comis': base_comis, 'rekvesites': rekvesites}
                                usernamepsch = depositsortcritery(userps=balancerequest, critery=post.criteri, nameps=post.request_sistemchange)

                                usernamepschange = usernamepsch['usernameps']
                                post.request_commission = float(usernamepsch['base_comis']) + 0.5
                                post.request_commission_change = float(usernamepsch['base_comis'])
                                post.requisites = usernamepsch['rekvesites']
                                post.request_userchange = usernamepschange.username
                                request_summe = float(post.request_sum) - ((float(post.request_sum) / 100) * post.request_commission)
                                post.request_good_sum = request_summe * float(request_good.base_currency)
                                request_good_summe = float(post.request_sum) - ((float(post.request_sum) / 100) * post.request_commission_change)
                                post.request_good_sum_change = request_good_summe * float(request_good.base_currency)

                                post.request_type_valute = changerequest['valute']
                                post.request_sum_valute = post.request_sum
                                post.request_good_sum_valute = post.request_good_sum
                                post.request_good_sum_change_valute = post.request_good_sum_change
                                post.request_curse = request_good.base_currency

                                post.save()
                                return redirect('requsetwallet')
                            else:
                                return redirect('depositwallet')
                        else:
                            return redirect('depositwallet')
                    else:
                        if range_list['min_sum'] > post.request_sum < range_list['max_sum']:
                            data_message = {
                                'message': 'Введеная сумма меньше минимальной',
                                'message_type': 'Error'
                            }
                            message_status = True
                        elif range_list['min_sum'] < post.request_sum > range_list['max_sum']:
                            data_message = {
                                'message': 'Введеная сумма больше максимальной',
                                'message_type': 'Error'
                            }
                            message_status = True
            context = {
                'form': RequestForm(),
                'list_active_ps': range_ps['active_list_ps'],
                'list_reserve_ps': active_ps['list_active_reserve_ps'],
                'range_min_list': range_ps['list_range_min_reserve_ps'],
                'range_max_list': range_ps['list_range_max_reserve_ps'],
                'message_status': message_status,
                'data_message': data_message,
            }
            return render(request, 'personalaccount/cabinet/deposit/depositwallet.html', context)
        else:
            raise Http404
    else:
        return redirect('account_login')


# /КОШЕЛЕК/ ВЫВОД
def withdrawalwallet(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=1):
            message_status = False
            data_message = None
            userwidth = CustomUser.objects.get(username=request.user)
            active_ps = active_width_ps_global()
            range_ps = range_width_ps_global(list_active=active_ps['list_active_reserve_ps'], active_list_ps=active_ps['list_active_change_ps'], balance=userwidth.balance)
            if request.method == "POST":
                form = WithdrawalForm(request.POST)
                if form.is_valid():
                    # получаем номер завки
                    n = random.randint(1000000, 9999999)
                    post = form.save(commit=False)
                    range_list = min_and_max_sum_request(ps_request=post.request_sistemchange, range_ps=range_ps)
                    if range_list['min_sum'] <= post.request_sum <= range_list['max_sum']:
                        post.request_user = request.user
                        post.request_name = str(n)
                        post.request_type = 'Заявка на вывод'
                        post.request_status = 'Ожидает оплаты'
                        # получаем обработчика заявки(активность=true, активность направления=true), пример({'changeq': [<CustomUser: Obmen>], 'valute': 'RUB'})
                        changerequest = widthsortchangeps(nameps=post.request_sistemchange)
                        if len(changerequest['changeq']) > 0:
                            # проверяем основной баланс и остаток резерва, пример ([<CustomUser: Obmen>])
                            balancerequest = widthsortbalanceps(userps=changerequest['changeq'], balanceps=post.request_sum, nameps=post.request_sistemchange, valuteps=changerequest['valute'])
                            if len(balancerequest) > 0:
                                request_good = CurrencyCBRF.objects.get(name_currency=changerequest['valute'])
                                # получаем победителя {'usernameps': usernameps, 'base_comis': base_comis, 'rekvesites': rekvesites}
                                usernamepsch = widthsortcritery(userps=balancerequest, critery=post.criteri, nameps=post.request_sistemchange, valuteps=changerequest['valute'], balanceps=post.request_sum)

                                usernamepschange = usernamepsch['usernameps']
                                userwidth.balance -= post.request_sum
                                post.request_commission = float(usernamepsch['base_comis']) + 0.5
                                post.request_commission_change = float(usernamepsch['base_comis'])
                                post.request_userchange = usernamepschange.username
                                request_summe = float(post.request_sum) - ((float(post.request_sum) / 100) * post.request_commission)
                                post.request_good_sum = request_summe / float(request_good.base_currency)
                                post.request_good_sum_change = float(post.request_sum) - ((float(post.request_sum) / 100) * 0.5)

                                post.request_type_valute = changerequest['valute']
                                post.request_sum_valute = post.request_sum
                                post.request_good_sum_valute = post.request_good_sum
                                post.request_good_sum_change_valute = post.request_good_sum_change
                                post.request_curse = request_good.base_currency

                                # создаем транзакцию для получателя вывода
                                Transaction.objects.create(transaction_name='Заявка на вывод № ' + str(n),
                                                           transaction_number=str(n),
                                                           transaction_user=request.user.username,
                                                           transaction_status='В обработке',
                                                           transaction_sum='- ' + str(post.request_sum) + ' $',
                                                           transaction_sistemchange=post.request_sistemchange)
                                userwidth.save()
                                post.save()
                                return redirect('requsetwallet')
                            else:
                                return redirect('withdrawalwallet')
                        else:
                            return redirect('withdrawalwallet')
                    else:
                        if range_list['min_sum'] > post.request_sum < range_list['max_sum']:
                            data_message = {
                                'message': 'Введеная сумма меньше минимальной',
                                'message_type': 'Error'
                            }
                            message_status = True
                        elif range_list['min_sum'] < post.request_sum > range_list['max_sum']:
                            data_message = {
                                'message': 'Введеная сумма больше максимальной',
                                'message_type': 'Error'
                            }
                            message_status = True
            context = {
                'form': WithdrawalForm(),
                'list_active_ps': range_ps['active_list_ps'],
                'list_reserve_ps': active_ps['list_active_reserve_ps'],
                'range_min_list': range_ps['list_range_min_reserve_ps'],
                'range_max_list': range_ps['list_range_max_reserve_ps'],
                'message_status': message_status,
                'data_message': data_message,
            }
            return render(request, 'personalaccount/cabinet/withdrawal/withdrawalwallet.html', context)
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
                    usertranin = CustomUser.objects.all()
                    usertranout = usertranin.get(username=post.transfer_out)
                    for item in usertranin:
                        if item.username == post.transfer_in:
                            usertranall = usertranin.get(username=post.transfer_in)
                            if usertranout.balance > post.transfer_sum:
                                usertranout.balance -= post.transfer_sum
                                usertranall.balance += post.transfer_sum

                                # создаем транзакцию отправителя
                                Transaction.objects.create(transaction_name='Отправлен внутренний перевод № ' + str(n) + ', пользователю ' + str(post.transfer_in),
                                                           transaction_number=str(n),
                                                           transaction_user=post.transfer_out,
                                                           transaction_status='Выполнена',
                                                           date_end_change=timezone.now(),
                                                           transaction_sum='- ' + str(post.transfer_sum) + ' $',
                                                           transaction_sistemchange='Внутренний перевод')
                                # создаем транзакцию получателя
                                Transaction.objects.create(transaction_name='Получен внутренний перевод № ' + str(n) + ', от пользователя ' + str(post.transfer_out),
                                                           transaction_number=str(n),
                                                           transaction_user=post.transfer_in,
                                                           transaction_status='Выполнена',
                                                           date_end_change=timezone.now(),
                                                           transaction_sum='+ ' + str(post.transfer_sum) + ' $',
                                                           transaction_sistemchange='Внутренний перевод')
                                usertranout.save()
                                usertranall.save()
                                post.save()
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
            status_reque_in = False
            status_reque_out = False
            base_reque = RequestChange.objects.filter(request_user=request.user)
            base_reque_in = base_reque.filter(request_type='Заявка на пополнение')
            base_reque_out = base_reque.filter(request_type='Заявка на вывод')
            for i in base_reque:
                if i.request_type == 'Заявка на пополнение' and i.request_status != 'Выполнена':
                    status_reque_in = True
                if i.request_type == 'Заявка на вывод' and i.request_status != 'Выполнена':
                    status_reque_out = True
            context = {
                'status_reque_in': status_reque_in,
                'status_reque_out': status_reque_out,
                'base_reque_in': base_reque_in,
                'base_reque_out': base_reque_out,
            }
            return render(request, 'personalaccount/cabinet/requset/requsetwallet.html', context)
        else:
            raise Http404
    else:
        return redirect('account_login')


# /КОШЕЛЕК/ ПОДТВЕРЖДЕНИЕ ОПЛАТЫ КЛИЕНТОМ
def requsetwalletsuccess(request, pk):
    succ = RequestChange.objects.get(pk=pk)
    succ.request_status = 'Оплачена'
    succ.save()
    return redirect('requsetwallet')

# /КОШЕЛЕК/ УДАЛЕНИЕ ЗАЯВКИ
def requsetwalletdel(request, pk):
    succ = RequestChange.objects.get(pk=pk)
    if succ.request_user == request.user.username:
        succ.delete()
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
            data_message = None
            message_status = False
            if cache.get('info_message'):
                data_message = cache.get('info_message')
                message_status = True
            context = {
                'data_message': data_message,
                'message_status': message_status,
            }
            cache.delete('info_message')
            return render(request, 'personalaccount/cabinet/profile/profilewallet.html', context)
        else:
            raise Http404
    else:
        return redirect('account_login')


# /КОШЕЛЕК/ НАСТРОЙКИ
def settingwallet(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=1):
            data_user = CustomUser.objects.get(username=request.user)
            data_error = False
            if request.method == 'POST':
                form = ProfileForm(request.POST, request.FILES, instance=data_user)
                if form.is_valid():
                    flag_good = True
                    post = form.save(commit=False)
                    if not post.first_name:
                        flag_good = False
                    if not post.last_name:
                        flag_good = False
                    if not post.middle_name:
                        flag_good = False
                    if not post.phone_number:
                        flag_good = False
                    if not post.telegram_username:
                        flag_good = False

                    if flag_good == True:
                        if 'avatar-clear-cust' in request.POST:
                            post.avatar.delete()
                        post.save()
                        message_success()
                        return redirect('profilewallet')
                    else:
                        data_error = True
            context = {
                'form': ProfileForm(instance=data_user),
                'data_error': data_error,
            }
            return render(request, 'personalaccount/cabinet/setting/settingwallet.html', context)
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


# /ОБМЕННИК/ ИСПОЛНЕНИЕ ЗАЯВКИ НА ВЫВОД
def withdrawalexchangegood(request, pk):
    userchange = CustomUser.objects.get(username=request.user)
    requestchange = RequestChange.objects.get(pk=pk)
    transactions = Transaction.objects.get(transaction_number=requestchange.request_name)
    userchange.balance += requestchange.request_good_sum_change_valute
    requestchange.request_status = 'Выполнена'
    requestchange.date_end_change = timezone.now()
    transactions.transaction_status = 'Выполнена'
    transactions.date_end_change = timezone.now()


    # Создаем строку прибыли обменника
    print(requestchange.request_good_sum_change-(requestchange.request_good_sum*requestchange.request_curse))
    StaticDailyProfit.objects.create(dailyprofit_user=request.user.username,
                                     dailyprofit_value=requestchange.request_good_sum_change-(requestchange.request_good_sum*requestchange.request_curse)
                                     )

    # создаем транзакцию получателя
    Transaction.objects.create(transaction_name='Обработка заявки на вывод № ' + str(requestchange.request_name),
                                transaction_number=str(requestchange.request_name),
                                transaction_user=userchange.username,
                                transaction_status='Выполнена',
                                date_end_change=timezone.now(),
                                transaction_sum='+ ' + str(requestchange.request_good_sum_change_valute) + ' $',
                                transaction_sistemchange=str(requestchange.request_sistemchange))
    userchange.save()
    requestchange.save()
    transactions.save()
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


# /ОБМЕННИК/ ИСПОЛНЕНИЕ ЗАЯВКИ НА ПОПОЛНЕНИЕ
def depositexchangerequestupdate(request, pk):
    requestchange = RequestChange.objects.get(pk=pk)
    if request.user.username == requestchange.request_userchange:
        userwallet = CustomUser.objects.get(username=requestchange.request_user)
        userchange = CustomUser.objects.get(username=request.user)
        userchange.balance -= requestchange.request_good_sum_change
        userwallet.balance += requestchange.request_good_sum
        requestchange.date_end_change = timezone.now()
        requestchange.request_status = 'Выполнена'

        # Создаем строку прибыли обменника
        StaticDailyProfit.objects.create(dailyprofit_user=request.user.username,
                                         dailyprofit_value=((requestchange.request_sum / 100) * requestchange.request_commission_change) * requestchange.request_curse
                                         )

        #Создаем транзакцию для пользователя
        Transaction.objects.create(transaction_name='Заявка на пополнение № ' + str(requestchange.request_name),
                                   transaction_number=requestchange.request_name,
                                   transaction_user=requestchange.request_user,
                                   transaction_status=requestchange.request_status,
                                   transaction_sum='+ ' + str(float(requestchange.request_good_sum_valute)) + ' $',
                                   transaction_sistemchange=requestchange.request_sistemchange,
                                   date_end_change=timezone.now(),
                                   date_joined_change=requestchange.date_joined_change)

        #Создаем транзакцию для Обменника
        Transaction.objects.create(transaction_name='Обработка заявки на пополнение № ' + str(requestchange.request_name),
                                   transaction_number=requestchange.request_name,
                                   transaction_user=request.user.username,
                                   transaction_status=requestchange.request_status,
                                   transaction_sum='- ' + str(requestchange.request_good_sum_change_valute) + ' $',
                                   transaction_sistemchange=requestchange.request_sistemchange,
                                   date_end_change=timezone.now(),
                                   date_joined_change=requestchange.date_joined_change)
        requestchange.save()
        userwallet.save()
        userchange.save()
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

# /ОБМЕННИК/ РЕЗЕРВ ФОРМА
def reservchangeedit(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=2):
            rekvis = CustomUser.objects.get(username=request.user)
            context = {
                'rekvis': rekvis,
                'form': ReservChangeForm(instance=rekvis),
            }
            if request.method == "POST":
                form = ReservChangeForm(request.POST, instance=rekvis)
                if form.is_valid():
                    form.save()
                    return redirect('reservchange')
            return render(request, 'personalaccount/cabinet/reserv/reservchangeedit.html', context)
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
                    form.save()
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
            return render(request, 'personalaccount/cabinet/rekvisit/rekvisitchange.html', {'rekvis': rekvis})
        else:
            raise Http404
    else:
        return redirect('account_login')


def rekvisitchangeupdate(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=2):
            rekvis = CustomUser.objects.get(username=request.user)
            context = {
                'rekvis': rekvis,
                'form1': RequisitesForm(instance=rekvis),
            }
            if request.method == "POST":
                form = RequisitesForm(request.POST, instance=rekvis)
                if form.is_valid():
                    form.save()
                    return redirect('rekvisitchange')
            return render(request, 'personalaccount/cabinet/rekvisit/rekvisitchangeupdate.html', context)
        else:
            raise Http404
    else:
        return redirect('account_login')


# /ОБМЕННИК/ ПРОФИЛЬ
def profilechange(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=2):
            data_message = None
            message_status = False
            if cache.get('info_message'):
                data_message = cache.get('info_message')
                message_status = True
            context = {
                'data_message': data_message,
                'message_status': message_status,
            }
            cache.delete('info_message')
            return render(request, 'personalaccount/cabinet/profile/profilechange.html', context)
        else:
            raise Http404
    else:
        return redirect('account_login')


# /ОБМЕННИК/ НАСТРОЙКИ
def settingchange(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=2):
            data_user = CustomUser.objects.get(username=request.user)
            data_error = False
            if request.method == 'POST':
                form = ProfileForm(request.POST, request.FILES, instance=data_user)
                if form.is_valid():
                    flag_good = True
                    post = form.save(commit=False)
                    if not post.first_name:
                        flag_good = False
                    if not post.last_name:
                        flag_good = False
                    if not post.middle_name:
                        flag_good = False
                    if not post.phone_number:
                        flag_good = False
                    if not post.telegram_username:
                        flag_good = False

                    if flag_good == True:
                        if 'avatar-clear-cust' in request.POST:
                            post.avatar.delete()
                        post.save()
                        message_success()
                        return redirect('profilechange')
                    else:
                        data_error = True
            context = {
                'form': ProfileForm(instance=data_user),
                'data_error': data_error,
            }
            return render(request, 'personalaccount/cabinet/setting/settingchange.html', context)
        else:
            raise Http404
    else:
        return redirect('account_login')

# /ОБМЕННИК/ ЛИМИТЫ ДЛЯ ЗАЯВОК НА ПОПОЛНЕНИЕ
def rangechangedeposit(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=2):
            if RangeSumDeposit.objects.filter(deposit_range_username=request.user).exists():
                range_list = RangeSumDeposit.objects.get(deposit_range_username=request.user)
                return render(request, 'personalaccount/cabinet/range/rangechangedeposit.html', {'range_list': range_list})
            else:
                return redirect('rangechangedepositedit')
        else:
            raise Http404
    else:
        return redirect('account_login')


# /ОБМЕННИК/ ЛИМИТЫ ДЛЯ ЗАЯВОК НА ВЫВОД
def rangechangewidth(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=2):
            if RangeSumWidth.objects.filter(width_range_username=request.user).exists():
                range_list = RangeSumWidth.objects.get(width_range_username=request.user)
                return render(request, 'personalaccount/cabinet/range/rangechangewidth.html', {'range_list': range_list})
            else:
                return redirect('rangechangewidthedit')
        else:
            raise Http404
    else:
        return redirect('account_login')

# /ОБМЕННИК/ ИЗМЕНЕНИЕ ЛИМИТОВ НА ПОПОЛНЕНИЕ
def rangechangedepositedit(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=2):
            if RangeSumDeposit.objects.filter(deposit_range_username=request.user).exists():
                range_list = RangeSumDeposit.objects.get(deposit_range_username=request.user)
                if request.method == "POST":
                    form = RangeDepositForm(request.POST, instance=range_list)
                    if form.is_valid():
                        post = form.save(commit=False)
                        post.deposit_range_username = request.user
                        post.save()
                        return redirect('rangechangedeposit')
                else:
                    form = RangeDepositForm(instance=range_list)
                    return render(request, 'personalaccount/cabinet/range/editrangechangedeposit.html', {'form': form})
            else:
                if request.method == "POST":
                    form = RangeDepositForm(request.POST)
                    if form.is_valid():
                        post = form.save(commit=False)
                        post.deposit_range_username = request.user
                        post.save()
                        return redirect('rangechangedeposit')
                else:
                    form = RangeDepositForm()
                    return render(request, 'personalaccount/cabinet/range/editrangechangedeposit.html', {'form': form})
        else:
            raise Http404
    else:
        return redirect('account_login')


# /ОБМЕННИК/ ИЗМЕНЕНИЕ ЛИМИТОВ НА ВЫВОД
def rangechangewidthedit(request):
    if request.user.is_authenticated:
        if request.user.userid == CustomUserId.objects.get(pk=2):
            if RangeSumWidth.objects.filter(width_range_username=request.user).exists():
                range_list = RangeSumWidth.objects.get(width_range_username=request.user)
                if request.method == "POST":
                    form = RangeWidthForm(request.POST, instance=range_list)
                    if form.is_valid():
                        post = form.save(commit=False)
                        post.width_range_username = request.user
                        post.save()
                        return redirect('rangechangewidth')
                else:
                    form = RangeWidthForm(instance=range_list)
                    return render(request, 'personalaccount/cabinet/range/editrangechangewidth.html', {'form': form})
            else:
                if request.method == "POST":
                    form = RangeWidthForm(request.POST)
                    if form.is_valid():
                        post = form.save(commit=False)
                        post.width_range_username = request.user
                        post.save()
                        return redirect('rangechangewidth')
                else:
                    form = RangeWidthForm()
                    return render(request, 'personalaccount/cabinet/range/editrangechangewidth.html', {'form': form})
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
            form.save()
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
    currencyviewusd.base_currency = 1 / float(irub.rate)
    currencyviewusd.save()
    # обновляем курс EUR
    ieur = get_rates(section_id='Euro')
    currencyvieweur = CurrencyCBRF.objects.get(name_currency=ieur.name)
    currencyvieweur.base_currency = 1 / float(ieur.rate)
    currencyvieweur.save()

    # обновляем курсы криптовалют
    currencyjson = get_rates_crypto()
    currencycrypto = CurrencyCBRF.objects.all()
    iistcrypto = ['bitcoin', 'ethereum', 'ethereum-classic', 'monero', 'ripple', 'dash', 'bitcoin-cash', 'litecoin']
    for item in iistcrypto:
        for aut in currencyjson:
            if aut['id'] == item:
                currencyvieweur = currencycrypto.get(name_currency=aut['symbol'].upper())
                currencyvieweur.base_currency = aut['current_price']
                currencyvieweur.save()
    return redirect('personalaccount')
