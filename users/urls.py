"""FLURAY URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path, include, reverse_lazy
from users import views
from django.contrib.auth import views as auth_views

from users.forms import PassReset, PassResetConfirm, PassChange

urlpatterns = [
    path('login/', views.account_login, name='account_login'),
    path('signup/', views.account_signup, name='account_signup'),
    path('signup/<str:link>', views.account_signup_ref, name='account_signup_ref'),
    path('logout/', auth_views.LogoutView.as_view(), name='account_logout'),

    path('email/confirm/<str:confirm_key>', views.account_email_confirm, name='account_email_confirm'),

    path('password-reset/', PasswordResetView.as_view(
        email_template_name='registration/password_reset_email.html',
        form_class=PassReset,
        html_email_template_name='users/account/email/pass_reset.html',
        template_name='users/account/password_reset.html',
    ), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(
        template_name='users/account/password_reset_done.html'
    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        form_class=PassResetConfirm,
        post_reset_login=True,
        success_url=reverse_lazy('personalaccount'),
        template_name='users/account/password_reset_confirm.html',
    ), name='password_reset_confirm'),
    path('password_change/', PasswordChangeView.as_view(
        form_class=PassChange,
        success_url=reverse_lazy('personalaccount'),
        template_name='users/account/password_change.html',
    ), name='password_change'),
]
