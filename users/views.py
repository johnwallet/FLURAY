import hashlib
import random
import uuid
from datetime import datetime

from django.contrib.auth import login, authenticate
from django.core.cache import cache
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils import timezone

from MyWallets.settings import EMAIL_HOST_USER
from personalaccount.message import message_email_succes
from personalaccount.metodviews import mail_send_metod
from users.forms import SignUpForm, AuthForm


# регистрация аккаунта
from users.models import Confirm_Email_Key, CustomUser, Line_Program


def account_signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()

                # Создаем запись партнера
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')

                userparth = CustomUser.objects.get(username=username)

                salt = uuid.uuid4().hex
                referal_code = str(salt[:16])
                domain = request.build_absolute_uri('/')
                domain_home = request.get_host()
                referal_link = domain + 'accounts/signup/r=' + referal_code
                Line_Program.objects.create(line_user=userparth, line_ref_code=referal_code,
                                            line_ref_link=referal_link)

                # отправляем письмо с подтверждением
                confirmation_key = hashlib.sha256((str(random.random()) + email).encode('utf-8')).hexdigest()[:40]
                Confirm_Email_Key.objects.create(confirm_username=username, confirm_key=confirmation_key)
                link_good_email = domain + 'accounts/email/confirm/' + confirmation_key

                mail_send_metod(email=email,
                                templates='users/account/email/signup_confirm.html',
                                context={'username': username, 'link_good_email': link_good_email},
                                subject=domain_home + ' | Успешная регистрация')

                return render(request, 'users/account/account_email_check.html', {'email_user': email})
        else:
            form = SignUpForm()
        return render(request, 'users/account/signup.html', {'form': form, 'link_status': False})
    else:
        return redirect('home')



def account_signup_ref(request, link):
    if not request.user.is_authenticated:
        code_upd = link.replace('r=', "")
        try:
            user_parent = Line_Program.objects.get(line_ref_code=code_upd)
            if request.method == 'POST':
                form = SignUpForm(request.POST)
                if form.is_valid():
                    form.save()

                    # Создаем запись партнера
                    username = form.cleaned_data.get('username')
                    email = form.cleaned_data.get('email')
                    userparth = CustomUser.objects.get(username=username)
                    userparent_email = CustomUser.objects.get(username=user_parent)

                    salt = uuid.uuid4().hex
                    referal_code = str(salt[:16])
                    domain = request.build_absolute_uri('/')
                    domain_home = request.get_host()
                    referal_link = domain + 'accounts/signup/r=' + referal_code
                    Line_Program.objects.create(parent=user_parent, line_user=userparth, line_ref_code=referal_code, line_ref_link=referal_link)

                    # отправляем письмо с подтверждением зарегистрированному пользователю и пригласителю
                    confirmation_key = hashlib.sha256((str(random.random()) + email).encode('utf-8')).hexdigest()[:40]
                    Confirm_Email_Key.objects.create(confirm_username=username, confirm_key=confirmation_key)
                    link_good_email = domain + 'accounts/email/confirm/' + confirmation_key

                    mail_send_metod(email=email,
                                    templates='users/account/email/signup_confirm.html',
                                    context={'username': username, 'link_good_email': link_good_email},
                                    subject=domain_home + ' | Успешная регистрация!')

                    mail_send_metod(email=userparent_email.email,
                                    templates='users/account/email/signup_new_ref.html',
                                    context={'username_ref': username},
                                    subject=domain_home + ' | У Вас новый партнер!')

                    return render(request, 'users/account/account_email_check.html', {'email_user': email, 'link_status': False})
            else:
                form = SignUpForm()
        except:
            user_parent = None
            form = SignUpForm()

        context = {
            'form': form,
            'user_parent': user_parent,
            'link_status': True,
        }
        return render(request, 'users/account/signup.html', context)
    else:
        return redirect('home')



# аутентификация и вход в аккаунт
def account_login(request):
    if not request.user.is_authenticated:
        data_message = None
        message_status = False
        if cache.get('info_message'):
            data_message = cache.get('info_message')
            message_status = True
        cache.delete('info_message')
        if request.method == 'POST':
            form = AuthForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('personalaccount')
            context = {
                'form': AuthForm(data=request.POST),
                'data_message': data_message,
                'message_status': message_status,
            }
        else:
            context = {
                'form': AuthForm(),
                'data_message': data_message,
                'message_status': message_status,
            }
        return render(request, 'users/account/login.html', context)
    else:
        return redirect('home')


# подтверждение почты аккаунта, если ключ устарел, отправляем новый
def account_email_confirm(request, confirm_key):
    try:
        key = Confirm_Email_Key.objects.get(confirm_key=confirm_key)
        user = CustomUser.objects.get(username=key.confirm_username)
        email_user = user.email
        domain_home = request.get_host()
        key_time = timezone.now() - key.confirm_date
        key_time_m = key_time.total_seconds() / 60
        if key_time_m < 60:
            user.is_active = True
            user.save()
            key.delete()
            message_email_succes()
            return redirect('account_login')
        else:
            confirmation_key = hashlib.sha256((str(random.random()) + email_user).encode('utf-8')).hexdigest()[:40]
            key.confirm_key = confirmation_key
            key.confirm_date = timezone.now()
            key.save()
            link_good_email = 'http://127.0.0.1:8000/accounts/email/confirm/' + confirmation_key

            mail_send_metod(email=email_user,
                            templates='users/account/email/signup_confirm.html',
                            context={'username': user.username, 'link_good_email': link_good_email},
                            subject=domain_home + ' | Подтверждение почты')

            return render(request, 'users/account/account_email_check_change.html', {'email_user': email_user})
    except:
        raise Http404


