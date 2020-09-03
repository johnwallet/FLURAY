from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from .managers import CustomUserManager


# кастомная модель юзера.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('почта', blank=False)
    username = models.CharField('логин пользователя', max_length=50, unique=True)
    date_joined = models.DateTimeField('дата регистрации', default=timezone.now)
    first_name = models.CharField('имя', max_length=100, blank=True)
    last_name = models.CharField('фамилия', max_length=100, blank=True)
    middle_name = models.CharField('отчество', max_length=100, blank=True)
    bio = models.CharField('биография', max_length=100, blank=True)
    balance = models.DecimalField('баланс', default=0, max_digits=10, decimal_places=8)
    is_staff = models.BooleanField('Модератор', default=False)
    is_active = models.BooleanField('Активный', default=True)
    is_superuser = models.BooleanField('Админ', default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
