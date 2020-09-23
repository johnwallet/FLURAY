from django.urls import path
from personalaccount import views

urlpatterns = [
    path('', views.personalaccount.as_view(), name='personalaccount'),
    path('depositwallet/', views.depositwalletform, name='depositwallet'),
    path('withdrawalwallet/', views.withdrawalwallet, name='withdrawalwallet'),
    path('transferwallet/', views.transferwallet, name='transferwallet'),
    path('transactionwallet/', views.transactionwallet, name='transactionwallet'),
    path('rekvisitwallet/', views.rekvisitwallet, name='rekvisitwallet'),
    path('profilewallet/', views.profilewallet, name='profilewallet'),
    path('settingwallet/', views.settingwallet, name='settingwallet'),

    path('requsetwallet/', views.requsetwallet.as_view(), name='requsetwallet'),
    path('requsetwallet/<int:pk>/', views.requsetwalletsuccess, name='requsetwalletsuccess'),

    path('withdrawalexchange/', views.withdrawalexchange.as_view(), name='withdrawalexchange'),
    path('withdrawalexchange/<int:pk>/', views.withdrawalexchangerequest.as_view(), name='withdrawalexchangerequest'),
    path('withdrawalexchange/<int:pk>/good/', views.withdrawalexchangerequestupdate, name='withdrawalexchangerequestupdate'),

    path('depositexchange/', views.depositexchange.as_view(), name='depositexchange'),
    path('depositexchange/<int:pk>/', views.depositexchangerequest.as_view(), name='depositexchangerequest'),
    path('depositexchange/<int:pk>/good/', views.depositexchangerequestupdate, name='depositexchangerequestupdate'),
    path('depositexchange/<int:pk>/no/', views.depositexchangerequestupdateno,
         name='depositexchangerequestupdateno'),

    path('depositreservchange/', views.depositreservchange, name='depositreservchange'),
    path('withdrawalreservchange/', views.withdrawalreservchange, name='withdrawalreservchange'),
    path('transactionchange/', views.transactionchange, name='transactionchange'),

    path('coursechange/', views.coursechange, name='coursechange'),
    path('coursechange/update/', views.coursechangeupdate, name='coursechangeupdate'),
    path('coursechange/commission/', views.coursechangecommission, name='coursechangecommission'),


    path('rekvisitchange/', views.rekvisitchange, name='rekvisitchange'),
    path('profilechange/', views.profilechange, name='profilechange'),
    path('settingchange/', views.settingchange, name='settingchange'),
]
