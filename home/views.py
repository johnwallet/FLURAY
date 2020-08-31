from django.shortcuts import render

from users.models import CustomUser


def home(request):
    return render(request, 'index.html')