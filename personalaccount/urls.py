from django.urls import path
from personalaccount import views


urlpatterns = [
    path('', views.personalaccount.as_view(), name='personalaccount'),
    path('depositwallet/', views.depositwallet, name='depositwallet'),
    path('withdrawalwallet/', views.withdrawalwallet, name='withdrawalwallet'),
    path('transferwallet/', views.transferwallet, name='transferwallet'),
    path('transactionwallet/', views.transactionwallet, name='transactionwallet'),
    path('rekvisitwallet/', views.rekvisitwallet, name='rekvisitwallet'),
    path('profilewallet/', views.profilewallet, name='profilewallet'),
    path('settingwallet/', views.settingwallet, name='settingwallet'),

    path('withdrawalexchange/', views.withdrawalexchange, name='withdrawalexchange'),
    path('depositexchange/', views.depositexchange, name='depositexchange'),
    path('depositreservchange/', views.depositreservchange, name='depositreservchange'),
    path('withdrawalreservchange/', views.withdrawalreservchange, name='withdrawalreservchange'),
    path('transactionchange/', views.transactionchange, name='transactionchange'),
    path('coursechange/', views.coursechange, name='coursechange'),
    path('rekvisitchange/', views.rekvisitchange, name='rekvisitchange'),
    path('profilechange/', views.profilechange, name='profilechange'),
    path('settingchange/', views.settingchange, name='settingchange'),
]
