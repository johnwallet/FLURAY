from django.urls import path, include
from pay import views


urlpatterns = [
    path('', views.depositwalletform, name='depositwalletform'),
    path('update/', views.coursechangecommission, name='coursechangecommission'),
]
