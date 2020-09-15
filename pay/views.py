from django.shortcuts import render, redirect
import random

from pay.forms import RequestForm
from pay.models import Transaction
from users.models import CustomUser


def depositwalletform(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        #получаем номер завки
        n = random.randint(1000000, 9999999)
        if form.is_valid():
            post = form.save(commit=False)
            post.request_user = request.user
            post.request_name = str(n)

            # получаем обработчика заявки
            itemchange = CustomUser.objects.filter(userid__custuserid='Владелец Обменника')
            itemchangeset = []
            for i in itemchange:
                if str(post.request_currency) == "USD":
                    if i.balanceusd > post.request_sum:
                        itemchangeset += [i.username]
                if str(post.request_currency) == "RUB":
                    if i.balancerub > post.request_sum:
                        itemchangeset += [i.username]
                if str(post.request_currency) == "EUR":
                    if i.balanceeur > post.request_sum:
                        itemchangeset += [i.username]

            print(itemchangeset)



            Transaction.objects.create(transaction_name=str(n),
                                       transaction_user=post.request_user,
                                       #transaction_userchange=,
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
