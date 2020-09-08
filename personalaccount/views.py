from django.shortcuts import render, redirect
from django.views.generic import TemplateView

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


def transactionwallet(request):
    return render(request, 'personalaccount/cabinet/transaction/transactionwallet.html')
