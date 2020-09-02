from django.urls import path
from personalaccount import views


urlpatterns = [
    path('', views.personalaccount, name='personalaccount'),
]
