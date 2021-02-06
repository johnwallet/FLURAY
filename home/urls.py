from django.urls import path
from home import views


urlpatterns = (
    path('', views.home, name='home'),
    path('support/', views.support, name='support'),
    path('news/', views.news, name='news'),
    path('news/<int:pk>/', views.newsview, name='newsview'),
    path('api/request/', views.RequestList.as_view())
)
