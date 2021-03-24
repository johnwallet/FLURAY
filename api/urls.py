from django.urls import path
from api.views import *


urlpatterns = (
    path('get/deposit/ps/', RequestPSStatusDepositView.as_view()),
    path('get/width/ps/', RequestPSStatusWidthdrawalView.as_view()),
    path('post/deposit/order/create/', DepositRequestCreateView.as_view()),
    path('post/width/order/create/', WidthRequestCreateView.as_view()),
    path('post/deposit/order/update/', DepositRequestUpdateView.as_view()),
    path('post/all/order/check/', StatusOrderView.as_view()),
)
