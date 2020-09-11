from django.shortcuts import render, redirect
import random

from pay.forms import RequestForm
from pay.models import Transaction


def depositwalletform(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        n = random.randint(1000000, 9999999)
        if form.is_valid():
            post = form.save(commit=False)
            post.request_user = request.user
            post.request_name = 'Заявка № ' + str(n)
            formtran = Transaction.objects.create(transaction_name='Заявка на пополнение № ' + str(n),
                                                  transaction_user=post.request_user,
                                                  transaction_type='пополнение',
                                                  transaction_status=post.request_status,
                                                  transaction_currency=post.request_currency,
                                                  transaction_sum=post.request_sum,
                                                  transaction_sistemchange=post.request_sistemchange)
            formtran.save()
            post.save()
            return redirect('depositwalletform')
    else:
        form = RequestForm()
    return render(request, 'personalaccount/cabinet/deposit/depositwallet.html', {'form': form})
