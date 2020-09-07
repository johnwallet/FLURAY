from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from users.models import CustomUserId, CustomUser


# проверяем, если пользователь залогинен и владелец кошелька или обменника, выдаем нужный шаблон
class personalaccount(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.userid == CustomUserId.objects.get(pk=1):
                return render(request, 'personalaccount/cabinet/dashboard/dashboard.html')
            elif request.user.userid == CustomUserId.objects.get(pk=2):
                return render(request, 'personalaccount/cabinet/dashboard/dashboard2.html')
        else:
            return redirect('account_login')


def password_reset(request):
    return render(request, 'users/account/password_reset.html')
