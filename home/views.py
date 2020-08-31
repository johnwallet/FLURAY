from django.shortcuts import render

from users.models import CustomUser


def home(request):
    return render(request, 'home/index.html')


def formelement(request):
    return render(request, 'home/form-elements.html')
