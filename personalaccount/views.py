from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from users.models import CustomUserId


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


def rekvisitwallet(request):
    return render(request, 'personalaccount/cabinet/rekvisit/rekvisitwallet.html')


def profilewallet(request):
    return render(request, 'personalaccount/cabinet/profile/profilewallet.html')


def settingwallet(request):
    return render(request, 'personalaccount/cabinet/setting/settingwallet.html')


def withdrawalexchange(request):
    return render(request, 'personalaccount/cabinet/withdrawal/withdrawalexchange.html')


def depositexchange(request):
    return render(request, 'personalaccount/cabinet/deposit/depositexchange.html')


def depositreservchange(request):
    return render(request, 'personalaccount/cabinet/deposit/depositreservchange.html')


def withdrawalreservchange(request):
    return render(request, 'personalaccount/cabinet/withdrawal/withdrawalreservchange.html')


def transactionchange(request):
    return render(request, 'personalaccount/cabinet/transaction/transactionchange.html')


def coursechange(request):
    return render(request, 'personalaccount/cabinet/course/coursechange.html')


def rekvisitchange(request):
    return render(request, 'personalaccount/cabinet/rekvisit/rekvisitchange.html')


def profilechange(request):
    return render(request, 'personalaccount/cabinet/profile/profilechange.html')


def settingchange(request):
    return render(request, 'personalaccount/cabinet/setting/settingchange.html')
