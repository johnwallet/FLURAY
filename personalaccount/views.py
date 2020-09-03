from django.shortcuts import render


def personalaccount(request):
    return render(request, 'personalaccount/index.html')

def password_reset(request):
    return render(request, 'users/account/password_reset.html')
