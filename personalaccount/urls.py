from django.urls import path
from personalaccount import views

urlpatterns = [
    path('', views.personalaccount, name='personalaccount'),
    path('depositwallet/', views.depositwalletform, name='depositwallet'),
    path('withdrawalwallet/', views.withdrawalwallet, name='withdrawalwallet'),
    path('transferwallet/', views.transferwallet, name='transferwallet'),
    path('transactionwallet/', views.transactionwallet, name='transactionwallet'),

    path('profilewallet/', views.profilewallet, name='profilewallet'),
    path('settingwallet/', views.settingwallet, name='settingwallet'),

    path('requsetwallet/', views.requsetwallet, name='requsetwallet'),
    path('requsetwallet/<int:pk>/', views.requsetwalletsuccess, name='requsetwalletsuccess'),
    path('requsetwallet/<int:pk>/del/', views.requsetwalletdel, name='requsetwalletdel'),

    path('withdrawalexchange/', views.withdrawalexchange, name='withdrawalexchange'),
    path('withdrawalexchange/<int:pk>/good/', views.withdrawalexchangegood, name='withdrawalexchangegood'),

    path('depositexchange/', views.depositexchange, name='depositexchange'),
    path('depositexchange/<int:pk>/', views.depositexchangerequest, name='depositexchangerequest'),
    path('depositexchange/<int:pk>/good/', views.depositexchangerequestupdate, name='depositexchangerequestupdate'),

    path('depositreservchange/', views.depositreservchange, name='depositreservchange'),
    path('withdrawalreservchange/', views.withdrawalreservchange, name='withdrawalreservchange'),
    path('transactionchange/', views.transactionchange, name='transactionchange'),

    path('activechange/', views.activechange, name='activechange'),
    path('activechange/statuschange/', views.activechangestch, name='activechangestch'),
    path('activechange/statuschange/toggle', views.activechangestchtoggle, name='activechangestchtoggle'),
    path('activechange/statusps/', views.activechangestps, name='activechangestps'),


    path('reservchange/', views.reservchange, name='reservchange'),
    path('reservchangeedit/', views.reservchangeedit, name='reservchangeedit'),
    path('coursechange/', views.coursechange, name='coursechange'),
    path('coursechange/update/', views.coursechangeupdate, name='coursechangeupdate'),
    path('coursechange/commission/', views.coursechangecommission, name='coursechangecommission'),
    path('rekvisitchange/', views.rekvisitchange, name='rekvisitchange'),
    path('rekvisitchange/update/', views.rekvisitchangeupdate, name='rekvisitchangeupdate'),

    path('profilechange/', views.profilechange, name='profilechange'),
    path('settingchange/', views.settingchange, name='settingchange'),
]
