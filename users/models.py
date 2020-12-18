from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from .managers import CustomUserManager


# кастомная модель юзера.
class CustomUser(AbstractBaseUser, PermissionsMixin):
# ОСНОВА
    avatar = models.ImageField('Аватар', upload_to='user/', blank=True)
    email = models.EmailField('Почта', blank=False)
    username = models.CharField('Логин пользователя', max_length=50, unique=True)
    date_joined = models.DateTimeField('Дата регистрации', default=timezone.now)
    kompan_name = models.CharField('Наименование компании', max_length=100, blank=True)
    first_name = models.CharField('Имя', max_length=100, blank=True)
    last_name = models.CharField('Фамилия', max_length=100, blank=True)
    middle_name = models.CharField('Отчество', max_length=100, blank=True)
    balance = models.DecimalField('Баланс $', default=0, max_digits=10, decimal_places=2)
    is_staff = models.BooleanField('Модератор', default=False)
    is_active = models.BooleanField('Активный', default=True)
    is_superuser = models.BooleanField('Админ', default=False)
    userid = models.ForeignKey('CustomUserId', on_delete=models.PROTECT, default=1, verbose_name='Роль')
# КОММИСИИ
    valute_usd = models.DecimalField('Коммисия на пополнение USD', max_digits=4, decimal_places=2, default=0)
    valute_rub = models.DecimalField('Коммисия на пополнение RUB', max_digits=4, decimal_places=2, default=0)
    valute_eur = models.DecimalField('Коммисия на пополнение EUR', max_digits=4, decimal_places=2, default=0)

    valute_with_usd = models.DecimalField('Коммисия на вывод USD', max_digits=4, decimal_places=2, default=0)
    valute_with_rub = models.DecimalField('Коммисия на вывод RUB', max_digits=4, decimal_places=2, default=0)
    valute_with_eur = models.DecimalField('Коммисия на вывод EUR', max_digits=4, decimal_places=2, default=0)

# === РЕКВИЗИТЫ для пополнения ===
# БАНКИ
    requsites_sberbank_rub = models.CharField('СБЕРБАНК', max_length=50, blank=True)
    requsites_psb_rub = models.CharField('ПСБ', max_length=50, blank=True)
    requsites_tinkoff_rub = models.CharField('ТИНЬКОФФ', max_length=50, blank=True)
    requsites_gazprombank_rub = models.CharField('ГАЗПРОМБАНК', max_length=50, blank=True)
    requsites_alfabank_rub = models.CharField('АЛЬФАБАНК', max_length=50, blank=True)
    requsites_russtandart_rub = models.CharField('РУССКИЙСТАНДАРТ', max_length=50, blank=True)
    requsites_vtb_rub = models.CharField('ВТБ', max_length=50, blank=True)
    requsites_rosselhoz_rub = models.CharField('РОССЕЛЬХОЗБАНК', max_length=50, blank=True)
    requsites_raifaizen_rub = models.CharField('РАЙФАЙЗЕНБАНК', max_length=50, blank=True)
    requsites_roketbank_rub = models.CharField('РОКЕТБАНК', max_length=50, blank=True)
    requsites_otkritie_rub = models.CharField('ОТКРЫТИЕ', max_length=50, blank=True)
    requsites_pochtabank_rub = models.CharField('ПОЧТАБАНК', max_length=50, blank=True)
    requsites_rnkb_rub = models.CharField('РНКБ', max_length=50, blank=True)
    requsites_rosbank_rub = models.CharField('РОСБАНК', max_length=50, blank=True)
    requsites_mtsbank_rub = models.CharField('МТСБАНК', max_length=50, blank=True)
# ПС
    requsites_qiwi_rub = models.CharField('КИВИРУБ', max_length=50, blank=True)
    requsites_qiwi_usd = models.CharField('КИВИДОЛЛАР', max_length=50, blank=True)
    requsites_payeer_rub = models.CharField('ПАЕЕРРУБ', max_length=50, blank=True)
    requsites_payeer_usd = models.CharField('ПАЕЕРДОЛЛАР', max_length=50, blank=True)
    requsites_payeer_eur = models.CharField('ПАЕЕРЕВРО', max_length=50, blank=True)
    requsites_webmoney_rub = models.CharField('ВЕБМАНИРУБ', max_length=50, blank=True)
    requsites_webmoney_usd = models.CharField('ВЕБМАНИДОЛЛАР', max_length=50, blank=True)
    requsites_webmoney_eur = models.CharField('ВЕБМАНИЕВРО', max_length=50, blank=True)
    requsites_pm_btc = models.CharField('ПМБИТКОИН', max_length=50, blank=True)
    requsites_pm_usd = models.CharField('ПМДОЛЛАР', max_length=50, blank=True)
    requsites_pm_eur = models.CharField('ПМЕВРО', max_length=50, blank=True)
    requsites_skrill_rub = models.CharField('СКРИЛЛРУБ', max_length=50, blank=True)
    requsites_skrill_usd = models.CharField('СКРИЛДОЛЛАР', max_length=50, blank=True)
    requsites_paypal_rub = models.CharField('ПАЙПАЛРУБ', max_length=50, blank=True)
    requsites_paypal_usd = models.CharField('ПАЙПАЛДОЛЛАР', max_length=50, blank=True)
    requsites_paypal_eur = models.CharField('ПАЙПАЛЕВРО', max_length=50, blank=True)
    requsites_umoney_rub = models.CharField('ЮМАНИ', max_length=50, blank=True)
# КРИПТА
    requsites_btc = models.CharField('БИТКОИН', max_length=50, blank=True)
    requsites_xrp = models.CharField('РИПЛ', max_length=50, blank=True)
    requsites_ltc = models.CharField('ЛАЙТКОИН', max_length=50, blank=True)
    requsites_bch = models.CharField('БИТКОИНКЕШ', max_length=50, blank=True)
    requsites_xmr = models.CharField('МОНЕРО', max_length=50, blank=True)
    requsites_eth = models.CharField('ЭФИР', max_length=50, blank=True)
    requsites_etc = models.CharField('ЭФИРКЛАССИК', max_length=50, blank=True)
    requsites_dash = models.CharField('ДАШ', max_length=50, blank=True)
# === РЕКВИЗИТЫ для вывода===
# БАНКИ
    requsites_width_sberbank_rub = models.CharField('СБЕРБАНК', max_length=50, blank=True)
    requsites_width_psb_rub = models.CharField('ПСБ', max_length=50, blank=True)
    requsites_width_tinkoff_rub = models.CharField('ТИНЬКОФФ', max_length=50, blank=True)
    requsites_width_gazprombank_rub = models.CharField('ГАЗПРОМБАНК', max_length=50, blank=True)
    requsites_width_alfabank_rub = models.CharField('АЛЬФАБАНК', max_length=50, blank=True)
    requsites_width_russtandart_rub = models.CharField('РУССКИЙСТАНДАРТ', max_length=50, blank=True)
    requsites_width_vtb_rub = models.CharField('ВТБ', max_length=50, blank=True)
    requsites_width_rosselhoz_rub = models.CharField('РОССЕЛЬХОЗБАНК', max_length=50, blank=True)
    requsites_width_raifaizen_rub = models.CharField('РАЙФАЙЗЕНБАНК', max_length=50, blank=True)
    requsites_width_roketbank_rub = models.CharField('РОКЕТБАНК', max_length=50, blank=True)
    requsites_width_otkritie_rub = models.CharField('ОТКРЫТИЕ', max_length=50, blank=True)
    requsites_width_pochtabank_rub = models.CharField('ПОЧТАБАНК', max_length=50, blank=True)
    requsites_width_rnkb_rub = models.CharField('РНКБ', max_length=50, blank=True)
    requsites_width_rosbank_rub = models.CharField('РОСБАНК', max_length=50, blank=True)
    requsites_width_mtsbank_rub = models.CharField('МТСБАНК', max_length=50, blank=True)
# ПС
    requsites_width_qiwi_rub = models.CharField('КИВИРУБ', max_length=50, blank=True)
    requsites_width_qiwi_usd = models.CharField('КИВИДОЛЛАР', max_length=50, blank=True)
    requsites_width_payeer_rub = models.CharField('ПАЕЕРРУБ', max_length=50, blank=True)
    requsites_width_payeer_usd = models.CharField('ПАЕЕРДОЛЛАР', max_length=50, blank=True)
    requsites_width_payeer_eur = models.CharField('ПАЕЕРЕВРО', max_length=50, blank=True)
    requsites_width_webmoney_rub = models.CharField('ВЕБМАНИРУБ', max_length=50, blank=True)
    requsites_width_webmoney_usd = models.CharField('ВЕБМАНИДОЛЛАР', max_length=50, blank=True)
    requsites_width_webmoney_eur = models.CharField('ВЕБМАНИЕВРО', max_length=50, blank=True)
    requsites_width_pm_btc = models.CharField('ПМБИТКОИН', max_length=50, blank=True)
    requsites_width_pm_usd = models.CharField('ПМДОЛЛАР', max_length=50, blank=True)
    requsites_width_pm_eur = models.CharField('ПМЕВРО', max_length=50, blank=True)
    requsites_width_skrill_rub = models.CharField('СКРИЛЛРУБ', max_length=50, blank=True)
    requsites_width_skrill_usd = models.CharField('СКРИЛДОЛЛАР', max_length=50, blank=True)
    requsites_width_paypal_rub = models.CharField('ПАЙПАЛРУБ', max_length=50, blank=True)
    requsites_width_paypal_usd = models.CharField('ПАЙПАЛДОЛЛАР', max_length=50, blank=True)
    requsites_width_paypal_eur = models.CharField('ПАЙПАЛЕВРО', max_length=50, blank=True)
    requsites_width_umoney_rub = models.CharField('ЮМАНИ', max_length=50, blank=True)
# КРИПТА
    requsites_width_btc = models.CharField('БИТКОИН', max_length=50, blank=True)
    requsites_width_xrp = models.CharField('РИПЛ', max_length=50, blank=True)
    requsites_width_ltc = models.CharField('ЛАЙТКОИН', max_length=50, blank=True)
    requsites_width_bch = models.CharField('БИТКОИНКЕШ', max_length=50, blank=True)
    requsites_width_xmr = models.CharField('МОНЕРО', max_length=50, blank=True)
    requsites_width_eth = models.CharField('ЭФИР', max_length=50, blank=True)
    requsites_width_etc = models.CharField('ЭФИРКЛАССИК', max_length=50, blank=True)
    requsites_width_dash = models.CharField('ДАШ', max_length=50, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'userid']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'


class CustomUserId(models.Model):
    custuserid = models.CharField('Роль', max_length=150, db_index=True)

    def __str__(self):
        return self.custuserid

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


