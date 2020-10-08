from django.urls import path
from home import views


urlpatterns = (
    path('', views.home, name='home'),
    path('api/request/', views.RequestList.as_view())
)
