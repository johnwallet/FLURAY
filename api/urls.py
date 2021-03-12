from django.urls import path
from api.views import *


urlpatterns = (
    path('get/ps/status/<str:key>/', RequestPSStatusView.as_view()),
    path('get/deposit/request/<str:key>/', DepositRequestCreateView.as_view()),
)
