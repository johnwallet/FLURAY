from django.urls import path
from home.views import *


urlpatterns = (
    path('', home, name='home'),
    path('support/', support, name='support'),
    path('news/', news, name='news'),
    path('news/<int:pk>/', newsview, name='newsview'),
    path('api/', api, name='api'),
)
