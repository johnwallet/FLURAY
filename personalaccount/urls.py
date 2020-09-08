from django.urls import path
from personalaccount import views


urlpatterns = [
    path('', views.personalaccount.as_view(), name='personalaccount'),
    path('depositwallet/', views.depositwallet, name='depositwallet'),
    path('withdrawalwallet/', views.withdrawalwallet, name='withdrawalwallet'),
    path('transferwallet/', views.transferwallet, name='transferwallet'),
    path('transactionwallet/', views.transactionwallet, name='transactionwallet'),
]
