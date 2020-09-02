from django.shortcuts import render


def personalaccount(request):
    return render(request, 'personalaccount/index.html')
