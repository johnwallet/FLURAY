from django.urls import path, include
from personalaccount import views

urlpatterns = [
    path('', views.personalaccount.as_view(), name='personalaccount'),
    path('depositwallet/', include('pay.urls')),
    path('withdrawalwallet/', views.withdrawalwallet, name='withdrawalwallet'),
    path('transferwallet/', views.transferwallet, name='transferwallet'),
    path('transactionwallet/', views.transactionwallet, name='transactionwallet'),
    path('rekvisitwallet/', views.rekvisitwallet, name='rekvisitwallet'),
    path('profilewallet/', views.profilewallet, name='profilewallet'),
    path('settingwallet/', views.settingwallet, name='settingwallet'),
    path('requsetwallet/', views.requsetwallet.as_view(), name='requsetwallet'),

    path('withdrawalexchange/', views.withdrawalexchange, name='withdrawalexchange')
    ,
    path('depositexchange/', views.depositexchange.as_view(), name='depositexchange'),
    path('depositexchange/<int:pk>/', views.depositexchangerequest.as_view(), name='depositexchangerequest'),
    path('depositexchange/update/<int:pk>/', views.depositexchangerequestupdate, name='depositexchangerequestupdate'),
    path('depositexchange/updateno/<int:pk>/', views.depositexchangerequestupdateno,
         name='depositexchangerequestupdateno'),

    path('depositreservchange/', views.depositreservchange, name='depositreservchange'),
    path('withdrawalreservchange/', views.withdrawalreservchange, name='withdrawalreservchange'),
    path('transactionchange/', views.transactionchange, name='transactionchange'),

    path('coursechange/', views.coursechange, name='coursechange'),
    path('coursechange/update/', views.coursechangeupdate, name='coursechangeupdate'),
    path('coursechange/commission/', include('pay.urls')),


    path('rekvisitchange/', views.rekvisitchange, name='rekvisitchange'),
    path('profilechange/', views.profilechange, name='profilechange'),
    path('settingchange/', views.settingchange, name='settingchange'),
]
