from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.dispatch import receiver
from django.utils import timezone

from MyWallets import settings
from .managers import CustomUserManager
from django.db.models.signals import pre_save
import os


# кастомная модель юзера.
class CustomUser(AbstractBaseUser, PermissionsMixin):
# ОСНОВА
    avatar = models.ImageField('Аватар', upload_to='user/', blank=True)
    email = models.EmailField('Почта', blank=False)
    username = models.CharField('Логин пользователя', max_length=50, unique=True, db_index=True)
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
    is_active_change = models.BooleanField('Статус активности обработчика', default=False)
    phone_number = models.CharField('Номер телефона', max_length=100, blank=True)
    telegram_username = models.CharField('Имя пользователя телеграм', max_length=100, blank=True)
    verifications_level_one = models.BooleanField('Верификация уровень 1', default=False)

# === АКТИВНОСТЬ ПС ПОПОЛНЕНИЕ ===
# БАНКИ
    active_in_sberbank_rub = models.BooleanField('СБЕРБАНК', default=False)
    active_in_psb_rub = models.BooleanField('ПСБ', default=False)
    active_in_tinkoff_rub = models.BooleanField('ТИНЬКОФФ', default=False)
    active_in_gazprombank_rub = models.BooleanField('ГАЗПРОМБАНК', default=False)
    active_in_alfabank_rub = models.BooleanField('АЛЬФАБАНК', default=False)
    active_in_russtandart_rub = models.BooleanField('РУССКИЙСТАНДАРТ', default=False)
    active_in_vtb_rub = models.BooleanField('ВТБ', default=False)
    active_in_rosselhoz_rub = models.BooleanField('РОССЕЛЬХОЗБАНК', default=False)
    active_in_raifaizen_rub = models.BooleanField('РАЙФАЙЗЕНБАНК', default=False)
    active_in_otkritie_rub = models.BooleanField('ОТКРЫТИЕ', default=False)
    active_in_pochtabank_rub = models.BooleanField('ПОЧТАБАНК', default=False)
    active_in_rnkb_rub = models.BooleanField('РНКБ', default=False)
    active_in_rosbank_rub = models.BooleanField('РОСБАНК', default=False)
    active_in_mtsbank_rub = models.BooleanField('МТСБАНК', default=False)
# ПС
    active_in_qiwi_rub = models.BooleanField('КИВИРУБ', default=False)
    active_in_qiwi_usd = models.BooleanField('КИВИДОЛЛАР', default=False)
    active_in_payeer_rub = models.BooleanField('ПАЕЕРРУБ', default=False)
    active_in_payeer_usd = models.BooleanField('ПАЕЕРДОЛЛАР', default=False)
    active_in_payeer_eur = models.BooleanField('ПАЕЕРЕВРО', default=False)
    active_in_webmoney_rub = models.BooleanField('ВЕБМАНИРУБ', default=False)
    active_in_webmoney_usd = models.BooleanField('ВЕБМАНИДОЛЛАР', default=False)
    active_in_webmoney_eur = models.BooleanField('ВЕБМАНИЕВРО', default=False)
    active_in_pm_btc = models.BooleanField('ПМБИТКОИН', default=False)
    active_in_pm_usd = models.BooleanField('ПМДОЛЛАР', default=False)
    active_in_pm_eur = models.BooleanField('ПМЕВРО', default=False)
    active_in_skrill_eur = models.BooleanField('СКРИЛЛЕВРО', default=False)
    active_in_skrill_usd = models.BooleanField('СКРИЛДОЛЛАР', default=False)
    active_in_paypal_rub = models.BooleanField('ПАЙПАЛРУБ', default=False)
    active_in_paypal_usd = models.BooleanField('ПАЙПАЛДОЛЛАР', default=False)
    active_in_paypal_eur = models.BooleanField('ПАЙПАЛЕВРО', default=False)
    active_in_umoney_rub = models.BooleanField('ЮМАНИ', default=False)
# КРИПТА
    active_in_btc = models.BooleanField('БИТКОИН', default=False)
    active_in_xrp = models.BooleanField('РИПЛ', default=False)
    active_in_ltc = models.BooleanField('ЛАЙТКОИН', default=False)
    active_in_bch = models.BooleanField('БИТКОИНКЕШ', default=False)
    active_in_xmr = models.BooleanField('МОНЕРО', default=False)
    active_in_eth = models.BooleanField('ЭФИР', default=False)
    active_in_etc = models.BooleanField('ЭФИРКЛАССИК', default=False)
    active_in_dash = models.BooleanField('ДАШ', default=False)

# === АКТИВНОСТЬ ПС ВЫВОД ===
# БАНКИ
    active_out_sberbank_rub = models.BooleanField('СБЕРБАНК', default=False)
    active_out_psb_rub = models.BooleanField('ПСБ', default=False)
    active_out_tinkoff_rub = models.BooleanField('ТИНЬКОФФ', default=False)
    active_out_gazprombank_rub = models.BooleanField('ГАЗПРОМБАНК', default=False)
    active_out_alfabank_rub = models.BooleanField('АЛЬФАБАНК', default=False)
    active_out_russtandart_rub = models.BooleanField('РУССКИЙСТАНДАРТ', default=False)
    active_out_vtb_rub = models.BooleanField('ВТБ', default=False)
    active_out_rosselhoz_rub = models.BooleanField('РОССЕЛЬХОЗБАНК', default=False)
    active_out_raifaizen_rub = models.BooleanField('РАЙФАЙЗЕНБАНК', default=False)
    active_out_otkritie_rub = models.BooleanField('ОТКРЫТИЕ', default=False)
    active_out_pochtabank_rub = models.BooleanField('ПОЧТАБАНК', default=False)
    active_out_rnkb_rub = models.BooleanField('РНКБ', default=False)
    active_out_rosbank_rub = models.BooleanField('РОСБАНК', default=False)
    active_out_mtsbank_rub = models.BooleanField('МТСБАНК', default=False)
# ПС
    active_out_qiwi_rub = models.BooleanField('КИВИРУБ', default=False)
    active_out_qiwi_usd = models.BooleanField('КИВИДОЛЛАР', default=False)
    active_out_payeer_rub = models.BooleanField('ПАЕЕРРУБ', default=False)
    active_out_payeer_usd = models.BooleanField('ПАЕЕРДОЛЛАР', default=False)
    active_out_payeer_eur = models.BooleanField('ПАЕЕРЕВРО', default=False)
    active_out_webmoney_rub = models.BooleanField('ВЕБМАНИРУБ', default=False)
    active_out_webmoney_usd = models.BooleanField('ВЕБМАНИДОЛЛАР', default=False)
    active_out_webmoney_eur = models.BooleanField('ВЕБМАНИЕВРО', default=False)
    active_out_pm_btc = models.BooleanField('ПМБИТКОИН', default=False)
    active_out_pm_usd = models.BooleanField('ПМДОЛЛАР', default=False)
    active_out_pm_eur = models.BooleanField('ПМЕВРО', default=False)
    active_out_skrill_eur = models.BooleanField('СКРИЛЛЕВРО', default=False)
    active_out_skrill_usd = models.BooleanField('СКРИЛДОЛЛАР', default=False)
    active_out_paypal_rub = models.BooleanField('ПАЙПАЛРУБ', default=False)
    active_out_paypal_usd = models.BooleanField('ПАЙПАЛДОЛЛАР', default=False)
    active_out_paypal_eur = models.BooleanField('ПАЙПАЛЕВРО', default=False)
    active_out_umoney_rub = models.BooleanField('ЮМАНИ', default=False)
# КРИПТА
    active_out_btc = models.BooleanField('БИТКОИН', default=False)
    active_out_xrp = models.BooleanField('РИПЛ', default=False)
    active_out_ltc = models.BooleanField('ЛАЙТКОИН', default=False)
    active_out_bch = models.BooleanField('БИТКОИНКЕШ', default=False)
    active_out_xmr = models.BooleanField('МОНЕРО', default=False)
    active_out_eth = models.BooleanField('ЭФИР', default=False)
    active_out_etc = models.BooleanField('ЭФИРКЛАССИК', default=False)
    active_out_dash = models.BooleanField('ДАШ', default=False)

# === РЕЗЕРВ ОБМЕННИКА ===
# БАНКИ
    reserv_sberbank_rub = models.DecimalField('СБЕРБАНК', max_digits=10, decimal_places=2, default=0)
    reserv_psb_rub = models.DecimalField('ПСБ', max_digits=10, decimal_places=2, default=0)
    reserv_tinkoff_rub = models.DecimalField('ТИНЬКОФФ', max_digits=10, decimal_places=2, default=0)
    reserv_gazprombank_rub = models.DecimalField('ГАЗПРОМБАНК', max_digits=10, decimal_places=2, default=0)
    reserv_alfabank_rub = models.DecimalField('АЛЬФАБАНК', max_digits=10, decimal_places=2, default=0)
    reserv_russtandart_rub = models.DecimalField('РУССКИЙСТАНДАРТ', max_digits=10, decimal_places=2, default=0)
    reserv_vtb_rub = models.DecimalField('ВТБ', max_digits=10, decimal_places=2, default=0)
    reserv_rosselhoz_rub = models.DecimalField('РОССЕЛЬХОЗБАНК', max_digits=10, decimal_places=2, default=0)
    reserv_raifaizen_rub = models.DecimalField('РАЙФАЙЗЕНБАНК', max_digits=10, decimal_places=2, default=0)
    reserv_otkritie_rub = models.DecimalField('ОТКРЫТИЕ', max_digits=10, decimal_places=2, default=0)
    reserv_pochtabank_rub = models.DecimalField('ПОЧТАБАНК', max_digits=10, decimal_places=2, default=0)
    reserv_rnkb_rub = models.DecimalField('РНКБ', max_digits=10, decimal_places=2, default=0)
    reserv_rosbank_rub = models.DecimalField('РОСБАНК', max_digits=10, decimal_places=2, default=0)
    reserv_mtsbank_rub = models.DecimalField('МТСБАНК', max_digits=10, decimal_places=2, default=0)
# ПС
    reserv_qiwi_rub = models.DecimalField('КИВИРУБ', max_digits=10, decimal_places=2, default=0)
    reserv_qiwi_usd = models.DecimalField('КИВИДОЛЛАР', max_digits=10, decimal_places=2, default=0)
    reserv_payeer_rub = models.DecimalField('ПАЕЕРРУБ', max_digits=10, decimal_places=2, default=0)
    reserv_payeer_usd = models.DecimalField('ПАЕЕРДОЛЛАР', max_digits=10, decimal_places=2, default=0)
    reserv_payeer_eur = models.DecimalField('ПАЕЕРЕВРО', max_digits=10, decimal_places=2, default=0)
    reserv_webmoney_rub = models.DecimalField('ВЕБМАНИРУБ', max_digits=10, decimal_places=2, default=0)
    reserv_webmoney_usd = models.DecimalField('ВЕБМАНИДОЛЛАР', max_digits=10, decimal_places=2, default=0)
    reserv_webmoney_eur = models.DecimalField('ВЕБМАНИЕВРО', max_digits=10, decimal_places=2, default=0)
    reserv_pm_btc = models.DecimalField('ПМБИТКОИН', max_digits=16, decimal_places=8, default=0)
    reserv_pm_usd = models.DecimalField('ПМДОЛЛАР', max_digits=10, decimal_places=2, default=0)
    reserv_pm_eur = models.DecimalField('ПМЕВРО', max_digits=10, decimal_places=2, default=0)
    reserv_skrill_eur = models.DecimalField('СКРИЛЛЕВРО', max_digits=10, decimal_places=2, default=0)
    reserv_skrill_usd = models.DecimalField('СКРИЛДОЛЛАР', max_digits=10, decimal_places=2, default=0)
    reserv_paypal_rub = models.DecimalField('ПАЙПАЛРУБ', max_digits=10, decimal_places=2, default=0)
    reserv_paypal_usd = models.DecimalField('ПАЙПАЛДОЛЛАР', max_digits=10, decimal_places=2, default=0)
    reserv_paypal_eur = models.DecimalField('ПАЙПАЛЕВРО', max_digits=10, decimal_places=2, default=0)
    reserv_umoney_rub = models.DecimalField('ЮМАНИ', max_digits=10, decimal_places=2, default=0)
# КРИПТА
    reserv_btc = models.DecimalField('БИТКОИН', max_digits=16, decimal_places=8, default=0)
    reserv_xrp = models.DecimalField('РИПЛ', max_digits=16, decimal_places=8, default=0)
    reserv_ltc = models.DecimalField('ЛАЙТКОИН', max_digits=16, decimal_places=8, default=0)
    reserv_bch = models.DecimalField('БИТКОИНКЕШ', max_digits=16, decimal_places=8, default=0)
    reserv_xmr = models.DecimalField('МОНЕРО', max_digits=16, decimal_places=8, default=0)
    reserv_eth = models.DecimalField('ЭФИР', max_digits=16, decimal_places=8, default=0)
    reserv_etc = models.DecimalField('ЭФИРКЛАССИК', max_digits=16, decimal_places=8, default=0)
    reserv_dash = models.DecimalField('ДАШ', max_digits=16, decimal_places=8, default=0)

# === КОММИСИИ на пополнение ===
# БАНКИ
    comis_in_sberbank_rub = models.DecimalField('СБЕРБАНК', max_digits=4, decimal_places=2, default=0)
    comis_in_psb_rub = models.DecimalField('ПСБ', max_digits=10, decimal_places=2, default=0)
    comis_in_tinkoff_rub = models.DecimalField('ТИНЬКОФФ', max_digits=4, decimal_places=2, default=0)
    comis_in_gazprombank_rub = models.DecimalField('ГАЗПРОМБАНК', max_digits=4, decimal_places=2, default=0)
    comis_in_alfabank_rub = models.DecimalField('АЛЬФАБАНК', max_digits=4, decimal_places=2, default=0)
    comis_in_russtandart_rub = models.DecimalField('РУССКИЙСТАНДАРТ', max_digits=4, decimal_places=2, default=0)
    comis_in_vtb_rub = models.DecimalField('ВТБ', max_length=50, max_digits=4, decimal_places=2, default=0)
    comis_in_rosselhoz_rub = models.DecimalField('РОССЕЛЬХОЗБАНК', max_digits=4, decimal_places=2, default=0)
    comis_in_raifaizen_rub = models.DecimalField('РАЙФАЙЗЕНБАНК', max_digits=4, decimal_places=2, default=0)
    comis_in_otkritie_rub = models.DecimalField('ОТКРЫТИЕ', max_digits=4, decimal_places=2, default=0)
    comis_in_pochtabank_rub = models.DecimalField('ПОЧТАБАНК', max_digits=4, decimal_places=2, default=0)
    comis_in_rnkb_rub = models.DecimalField('РНКБ', max_digits=4, decimal_places=2, default=0)
    comis_in_rosbank_rub = models.DecimalField('РОСБАНК', max_digits=4, decimal_places=2, default=0)
    comis_in_mtsbank_rub = models.DecimalField('МТСБАНК', max_digits=4, decimal_places=2, default=0)
# ПС
    comis_in_qiwi_rub = models.DecimalField('КИВИРУБ', max_digits=4, decimal_places=2, default=0)
    comis_in_qiwi_usd = models.DecimalField('КИВИДОЛЛАР', max_digits=4, decimal_places=2, default=0)
    comis_in_payeer_rub = models.DecimalField('ПАЕЕРРУБ', max_digits=4, decimal_places=2, default=0)
    comis_in_payeer_usd = models.DecimalField('ПАЕЕРДОЛЛАР', max_digits=4, decimal_places=2, default=0)
    comis_in_payeer_eur = models.DecimalField('ПАЕЕРЕВРО', max_digits=4, decimal_places=2, default=0)
    comis_in_webmoney_rub = models.DecimalField('ВЕБМАНИРУБ', max_digits=4, decimal_places=2, default=0)
    comis_in_webmoney_usd = models.DecimalField('ВЕБМАНИДОЛЛАР', max_digits=4, decimal_places=2, default=0)
    comis_in_webmoney_eur = models.DecimalField('ВЕБМАНИЕВРО', max_digits=4, decimal_places=2, default=0)
    comis_in_pm_btc = models.DecimalField('ПМБИТКОИН', max_digits=4, decimal_places=2, default=0)
    comis_in_pm_usd = models.DecimalField('ПМДОЛЛАР', max_digits=4, decimal_places=2, default=0)
    comis_in_pm_eur = models.DecimalField('ПМЕВРО', max_digits=4, decimal_places=2, default=0)
    comis_in_skrill_eur = models.DecimalField('СКРИЛЛЕВРО', max_digits=4, decimal_places=2, default=0)
    comis_in_skrill_usd = models.DecimalField('СКРИЛДОЛЛАР', max_digits=4, decimal_places=2, default=0)
    comis_in_paypal_rub = models.DecimalField('ПАЙПАЛРУБ', max_digits=4, decimal_places=2, default=0)
    comis_in_paypal_usd = models.DecimalField('ПАЙПАЛДОЛЛАР', max_digits=4, decimal_places=2, default=0)
    comis_in_paypal_eur = models.DecimalField('ПАЙПАЛЕВРО', max_digits=4, decimal_places=2, default=0)
    comis_in_umoney_rub = models.DecimalField('ЮМАНИ', max_digits=4, decimal_places=2, default=0)
# КРИПТА
    comis_in_btc = models.DecimalField('БИТКОИН', max_digits=4, decimal_places=2, default=0)
    comis_in_xrp = models.DecimalField('РИПЛ', max_digits=4, decimal_places=2, default=0)
    comis_in_ltc = models.DecimalField('ЛАЙТКОИН', max_digits=4, decimal_places=2, default=0)
    comis_in_bch = models.DecimalField('БИТКОИНКЕШ', max_digits=4, decimal_places=2, default=0)
    comis_in_xmr = models.DecimalField('МОНЕРО', max_digits=4, decimal_places=2, default=0)
    comis_in_eth = models.DecimalField('ЭФИР', max_digits=4, decimal_places=2, default=0)
    comis_in_etc = models.DecimalField('ЭФИРКЛАССИК', max_digits=4, decimal_places=2, default=0)
    comis_in_dash = models.DecimalField('ДАШ', max_digits=4, decimal_places=2, default=0)

# === КОММИСИИ на вывод ===
# БАНКИ
    comis_out_sberbank_rub = models.DecimalField('СБЕРБАНК', max_digits=4, decimal_places=2, default=0)
    comis_out_psb_rub = models.DecimalField('ПСБ', max_digits=4, decimal_places=2, default=0)
    comis_out_tinkoff_rub = models.DecimalField('ТИНЬКОФФ', max_digits=4, decimal_places=2, default=0)
    comis_out_gazprombank_rub = models.DecimalField('ГАЗПРОМБАНК', max_digits=4, decimal_places=2, default=0)
    comis_out_alfabank_rub = models.DecimalField('АЛЬФАБАНК', max_digits=4, decimal_places=2, default=0)
    comis_out_russtandart_rub = models.DecimalField('РУССКИЙСТАНДАРТ', max_digits=4, decimal_places=2, default=0)
    comis_out_vtb_rub = models.DecimalField('ВТБ', max_digits=4, decimal_places=2, default=0)
    comis_out_rosselhoz_rub = models.DecimalField('РОССЕЛЬХОЗБАНК', max_digits=4, decimal_places=2, default=0)
    comis_out_raifaizen_rub = models.DecimalField('РАЙФАЙЗЕНБАНК', max_digits=4, decimal_places=2, default=0)
    comis_out_otkritie_rub = models.DecimalField('ОТКРЫТИЕ', max_digits=4, decimal_places=2, default=0)
    comis_out_pochtabank_rub = models.DecimalField('ПОЧТАБАНК', max_digits=4, decimal_places=2, default=0)
    comis_out_rnkb_rub = models.DecimalField('РНКБ', max_digits=4, decimal_places=2, default=0)
    comis_out_rosbank_rub = models.DecimalField('РОСБАНК', max_digits=4, decimal_places=2, default=0)
    comis_out_mtsbank_rub = models.DecimalField('МТСБАНК', max_digits=4, decimal_places=2, default=0)
# ПС
    comis_out_qiwi_rub = models.DecimalField('КИВИРУБ', max_digits=4, decimal_places=2, default=0)
    comis_out_qiwi_usd = models.DecimalField('КИВИДОЛЛАР', max_digits=4, decimal_places=2, default=0)
    comis_out_payeer_rub = models.DecimalField('ПАЕЕРРУБ', max_digits=4, decimal_places=2, default=0)
    comis_out_payeer_usd = models.DecimalField('ПАЕЕРДОЛЛАР', max_digits=4, decimal_places=2, default=0)
    comis_out_payeer_eur = models.DecimalField('ПАЕЕРЕВРО', max_digits=4, decimal_places=2, default=0)
    comis_out_webmoney_rub = models.DecimalField('ВЕБМАНИРУБ', max_digits=4, decimal_places=2, default=0)
    comis_out_webmoney_usd = models.DecimalField('ВЕБМАНИДОЛЛАР', max_digits=4, decimal_places=2, default=0)
    comis_out_webmoney_eur = models.DecimalField('ВЕБМАНИЕВРО', max_digits=4, decimal_places=2, default=0)
    comis_out_pm_btc = models.DecimalField('ПМБИТКОИН', max_digits=4, decimal_places=2, default=0)
    comis_out_pm_usd = models.DecimalField('ПМДОЛЛАР', max_digits=4, decimal_places=2, default=0)
    comis_out_pm_eur = models.DecimalField('ПМЕВРО', max_digits=4, decimal_places=2, default=0)
    comis_out_skrill_eur = models.DecimalField('СКРИЛЛЕВРО', max_digits=4, decimal_places=2, default=0)
    comis_out_skrill_usd = models.DecimalField('СКРИЛДОЛЛАР', max_digits=4, decimal_places=2, default=0)
    comis_out_paypal_rub = models.DecimalField('ПАЙПАЛРУБ', max_digits=4, decimal_places=2, default=0)
    comis_out_paypal_usd = models.DecimalField('ПАЙПАЛДОЛЛАР', max_digits=4, decimal_places=2, default=0)
    comis_out_paypal_eur = models.DecimalField('ПАЙПАЛЕВРО', max_digits=4, decimal_places=2, default=0)
    comis_out_umoney_rub = models.DecimalField('ЮМАНИ', max_digits=4, decimal_places=2, default=0)
# КРИПТА
    comis_out_btc = models.DecimalField('БИТКОИН', max_digits=4, decimal_places=2, default=0)
    comis_out_xrp = models.DecimalField('РИПЛ', max_digits=4, decimal_places=2, default=0)
    comis_out_ltc = models.DecimalField('ЛАЙТКОИН', max_digits=4, decimal_places=2, default=0)
    comis_out_bch = models.DecimalField('БИТКОИНКЕШ', max_digits=4, decimal_places=2, default=0)
    comis_out_xmr = models.DecimalField('МОНЕРО', max_digits=4, decimal_places=2, default=0)
    comis_out_eth = models.DecimalField('ЭФИР', max_digits=4, decimal_places=2, default=0)
    comis_out_etc = models.DecimalField('ЭФИРКЛАССИК', max_digits=4, decimal_places=2, default=0)
    comis_out_dash = models.DecimalField('ДАШ', max_digits=4, decimal_places=2, default=0)

# === РЕКВИЗИТЫ ===
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
    requsites_skrill_eur = models.CharField('СКРИЛЛЕВРО', max_length=50, blank=True)
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

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'userid']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'


@receiver(pre_save, sender=CustomUser)
def delete_old_file(sender, instance, **kwargs):
    if instance._state.adding and not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).avatar
    except sender.DoesNotExist:
        return False

    file = instance.avatar
    if old_file and not old_file == file:
        print(os.path.isfile(old_file.path))
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


class CustomUserId(models.Model):
    custuserid = models.CharField('Роль', max_length=150, db_index=True)

    def __str__(self):
        return self.custuserid

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


# === ДИАПАЗОН СУММЫ ДЛЯ ПОПОЛНЕНИЯ ===
class RangeSumDeposit(models.Model):
    deposit_range_username = models.ForeignKey('CustomUser', on_delete=models.CASCADE, verbose_name='Пользователь')
    # БАНКИ
    deposit_min_sberbank_rub = models.IntegerField('СБЕРБАНК')
    deposit_min_psb_rub = models.IntegerField('ПСБ')
    deposit_min_tinkoff_rub = models.IntegerField('ТИНЬКОФФ')
    deposit_min_gazprombank_rub = models.IntegerField('ГАЗПРОМБАНК')
    deposit_min_alfabank_rub = models.IntegerField('АЛЬФАБАНК')
    deposit_min_russtandart_rub = models.IntegerField('РУССКИЙСТАНДАРТ')
    deposit_min_vtb_rub = models.IntegerField('ВТБ')
    deposit_min_rosselhoz_rub = models.IntegerField('РОССЕЛЬХОЗБАНК')
    deposit_min_raifaizen_rub = models.IntegerField('РАЙФАЙЗЕНБАНК')
    deposit_min_otkritie_rub = models.IntegerField('ОТКРЫТИЕ')
    deposit_min_pochtabank_rub = models.IntegerField('ПОЧТАБАНК')
    deposit_min_rnkb_rub = models.IntegerField('РНКБ')
    deposit_min_rosbank_rub = models.IntegerField('РОСБАНК')
    deposit_min_mtsbank_rub = models.IntegerField('МТСБАНК')
    # ПС
    deposit_min_qiwi_rub = models.IntegerField('КИВИРУБ')
    deposit_min_qiwi_usd = models.IntegerField('КИВИДОЛЛАР')
    deposit_min_payeer_rub = models.IntegerField('ПАЕЕРРУБ')
    deposit_min_payeer_usd = models.IntegerField('ПАЕЕРДОЛЛАР')
    deposit_min_payeer_eur = models.IntegerField('ПАЕЕРЕВРО')
    deposit_min_webmoney_rub = models.IntegerField('ВЕБМАНИРУБ')
    deposit_min_webmoney_usd = models.IntegerField('ВЕБМАНИДОЛЛАР')
    deposit_min_webmoney_eur = models.IntegerField('ВЕБМАНИЕВРО')
    deposit_min_pm_btc = models.DecimalField('ПМБИТКОИН', max_digits=16, decimal_places=8, default=0)
    deposit_min_pm_usd = models.IntegerField('ПМДОЛЛАР')
    deposit_min_pm_eur = models.IntegerField('ПМЕВРО')
    deposit_min_skrill_eur = models.IntegerField('СКРИЛЛЕВРО')
    deposit_min_skrill_usd = models.IntegerField('СКРИЛДОЛЛАР')
    deposit_min_paypal_rub = models.IntegerField('ПАЙПАЛРУБ')
    deposit_min_paypal_usd = models.IntegerField('ПАЙПАЛДОЛЛАР')
    deposit_min_paypal_eur = models.IntegerField('ПАЙПАЛЕВРО')
    deposit_min_umoney_rub = models.IntegerField('ЮМАНИ')
    # КРИПТА
    deposit_min_btc = models.DecimalField('БИТКОИН', max_digits=16, decimal_places=8, default=0)
    deposit_min_xrp = models.DecimalField('РИПЛ', max_digits=16, decimal_places=8, default=0)
    deposit_min_ltc = models.DecimalField('ЛАЙТКОИН', max_digits=16, decimal_places=8, default=0)
    deposit_min_bch = models.DecimalField('БИТКОИНКЕШ', max_digits=16, decimal_places=8, default=0)
    deposit_min_xmr = models.DecimalField('МОНЕРО', max_digits=16, decimal_places=8, default=0)
    deposit_min_eth = models.DecimalField('ЭФИР', max_digits=16, decimal_places=8, default=0)
    deposit_min_etc = models.DecimalField('ЭФИРКЛАССИК', max_digits=16, decimal_places=8, default=0)
    deposit_min_dash = models.DecimalField('ДАШ', max_digits=16, decimal_places=8, default=0)
    # БАНКИ
    deposit_max_sberbank_rub = models.IntegerField('СБЕРБАНК')
    deposit_max_psb_rub = models.IntegerField('ПСБ')
    deposit_max_tinkoff_rub = models.IntegerField('ТИНЬКОФФ')
    deposit_max_gazprombank_rub = models.IntegerField('ГАЗПРОМБАНК')
    deposit_max_alfabank_rub = models.IntegerField('АЛЬФАБАНК')
    deposit_max_russtandart_rub = models.IntegerField('РУССКИЙСТАНДАРТ')
    deposit_max_vtb_rub = models.IntegerField('ВТБ')
    deposit_max_rosselhoz_rub = models.IntegerField('РОССЕЛЬХОЗБАНК')
    deposit_max_raifaizen_rub = models.IntegerField('РАЙФАЙЗЕНБАНК')
    deposit_max_otkritie_rub = models.IntegerField('ОТКРЫТИЕ')
    deposit_max_pochtabank_rub = models.IntegerField('ПОЧТАБАНК')
    deposit_max_rnkb_rub = models.IntegerField('РНКБ')
    deposit_max_rosbank_rub = models.IntegerField('РОСБАНК')
    deposit_max_mtsbank_rub = models.IntegerField('МТСБАНК')
    # ПС
    deposit_max_qiwi_rub = models.IntegerField('КИВИРУБ')
    deposit_max_qiwi_usd = models.IntegerField('КИВИДОЛЛАР')
    deposit_max_payeer_rub = models.IntegerField('ПАЕЕРРУБ')
    deposit_max_payeer_usd = models.IntegerField('ПАЕЕРДОЛЛАР')
    deposit_max_payeer_eur = models.IntegerField('ПАЕЕРЕВРО')
    deposit_max_webmoney_rub = models.IntegerField('ВЕБМАНИРУБ')
    deposit_max_webmoney_usd = models.IntegerField('ВЕБМАНИДОЛЛАР')
    deposit_max_webmoney_eur = models.IntegerField('ВЕБМАНИЕВРО')
    deposit_max_pm_btc = models.DecimalField('ПМБИТКОИН', max_digits=16, decimal_places=8, default=0)
    deposit_max_pm_usd = models.IntegerField('ПМДОЛЛАР')
    deposit_max_pm_eur = models.IntegerField('ПМЕВРО')
    deposit_max_skrill_eur = models.IntegerField('СКРИЛЛЕВРО')
    deposit_max_skrill_usd = models.IntegerField('СКРИЛДОЛЛАР')
    deposit_max_paypal_rub = models.IntegerField('ПАЙПАЛРУБ')
    deposit_max_paypal_usd = models.IntegerField('ПАЙПАЛДОЛЛАР')
    deposit_max_paypal_eur = models.IntegerField('ПАЙПАЛЕВРО')
    deposit_max_umoney_rub = models.IntegerField('ЮМАНИ')
    # КРИПТА
    deposit_max_btc = models.DecimalField('БИТКОИН', max_digits=16, decimal_places=8, default=0)
    deposit_max_xrp = models.DecimalField('РИПЛ', max_digits=16, decimal_places=8, default=0)
    deposit_max_ltc = models.DecimalField('ЛАЙТКОИН', max_digits=16, decimal_places=8, default=0)
    deposit_max_bch = models.DecimalField('БИТКОИНКЕШ', max_digits=16, decimal_places=8, default=0)
    deposit_max_xmr = models.DecimalField('МОНЕРО', max_digits=16, decimal_places=8, default=0)
    deposit_max_eth = models.DecimalField('ЭФИР', max_digits=16, decimal_places=8, default=0)
    deposit_max_etc = models.DecimalField('ЭФИРКЛАССИК', max_digits=16, decimal_places=8, default=0)
    deposit_max_dash = models.DecimalField('ДАШ', max_digits=16, decimal_places=8, default=0)

    def __str__(self):
        return self.deposit_range_username.username

    class Meta:
        verbose_name = 'Диапазон для пополнений'
        verbose_name_plural = 'Диапазон для пополнений'


# === ДИАПАЗОН СУММЫ ДЛЯ ВЫВОДА ===
class RangeSumWidth(models.Model):
    width_range_username = models.ForeignKey('CustomUser', on_delete=models.CASCADE, verbose_name='Пользователь')
    # БАНКИ
    width_min_sberbank_rub = models.IntegerField('СБЕРБАНК')
    width_min_psb_rub = models.IntegerField('ПСБ')
    width_min_tinkoff_rub = models.IntegerField('ТИНЬКОФФ')
    width_min_gazprombank_rub = models.IntegerField('ГАЗПРОМБАНК')
    width_min_alfabank_rub = models.IntegerField('АЛЬФАБАНК')
    width_min_russtandart_rub = models.IntegerField('РУССКИЙСТАНДАРТ')
    width_min_vtb_rub = models.IntegerField('ВТБ')
    width_min_rosselhoz_rub = models.IntegerField('РОССЕЛЬХОЗБАНК')
    width_min_raifaizen_rub = models.IntegerField('РАЙФАЙЗЕНБАНК')
    width_min_otkritie_rub = models.IntegerField('ОТКРЫТИЕ')
    width_min_pochtabank_rub = models.IntegerField('ПОЧТАБАНК')
    width_min_rnkb_rub = models.IntegerField('РНКБ')
    width_min_rosbank_rub = models.IntegerField('РОСБАНК')
    width_min_mtsbank_rub = models.IntegerField('МТСБАНК')
    # ПС
    width_min_qiwi_rub = models.IntegerField('КИВИРУБ')
    width_min_qiwi_usd = models.IntegerField('КИВИДОЛЛАР')
    width_min_payeer_rub = models.IntegerField('ПАЕЕРРУБ')
    width_min_payeer_usd = models.IntegerField('ПАЕЕРДОЛЛАР')
    width_min_payeer_eur = models.IntegerField('ПАЕЕРЕВРО')
    width_min_webmoney_rub = models.IntegerField('ВЕБМАНИРУБ')
    width_min_webmoney_usd = models.IntegerField('ВЕБМАНИДОЛЛАР')
    width_min_webmoney_eur = models.IntegerField('ВЕБМАНИЕВРО')
    width_min_pm_btc = models.DecimalField('ПМБИТКОИН', max_digits=16, decimal_places=8, default=0)
    width_min_pm_usd = models.IntegerField('ПМДОЛЛАР')
    width_min_pm_eur = models.IntegerField('ПМЕВРО')
    width_min_skrill_eur = models.IntegerField('СКРИЛЛЕВРО')
    width_min_skrill_usd = models.IntegerField('СКРИЛДОЛЛАР')
    width_min_paypal_rub = models.IntegerField('ПАЙПАЛРУБ')
    width_min_paypal_usd = models.IntegerField('ПАЙПАЛДОЛЛАР')
    width_min_paypal_eur = models.IntegerField('ПАЙПАЛЕВРО')
    width_min_umoney_rub = models.IntegerField('ЮМАНИ')
    # КРИПТА
    width_min_btc = models.DecimalField('БИТКОИН', max_digits=16, decimal_places=8, default=0)
    width_min_xrp = models.DecimalField('РИПЛ', max_digits=16, decimal_places=8, default=0)
    width_min_ltc = models.DecimalField('ЛАЙТКОИН', max_digits=16, decimal_places=8, default=0)
    width_min_bch = models.DecimalField('БИТКОИНКЕШ', max_digits=16, decimal_places=8, default=0)
    width_min_xmr = models.DecimalField('МОНЕРО', max_digits=16, decimal_places=8, default=0)
    width_min_eth = models.DecimalField('ЭФИР', max_digits=16, decimal_places=8, default=0)
    width_min_etc = models.DecimalField('ЭФИРКЛАССИК', max_digits=16, decimal_places=8, default=0)
    width_min_dash = models.DecimalField('ДАШ', max_digits=16, decimal_places=8, default=0)
    # БАНКИ
    width_max_sberbank_rub = models.IntegerField('СБЕРБАНК')
    width_max_psb_rub = models.IntegerField('ПСБ')
    width_max_tinkoff_rub = models.IntegerField('ТИНЬКОФФ')
    width_max_gazprombank_rub = models.IntegerField('ГАЗПРОМБАНК')
    width_max_alfabank_rub = models.IntegerField('АЛЬФАБАНК')
    width_max_russtandart_rub = models.IntegerField('РУССКИЙСТАНДАРТ')
    width_max_vtb_rub = models.IntegerField('ВТБ')
    width_max_rosselhoz_rub = models.IntegerField('РОССЕЛЬХОЗБАНК')
    width_max_raifaizen_rub = models.IntegerField('РАЙФАЙЗЕНБАНК')
    width_max_otkritie_rub = models.IntegerField('ОТКРЫТИЕ')
    width_max_pochtabank_rub = models.IntegerField('ПОЧТАБАНК')
    width_max_rnkb_rub = models.IntegerField('РНКБ')
    width_max_rosbank_rub = models.IntegerField('РОСБАНК')
    width_max_mtsbank_rub = models.IntegerField('МТСБАНК')
    # ПС
    width_max_qiwi_rub = models.IntegerField('КИВИРУБ')
    width_max_qiwi_usd = models.IntegerField('КИВИДОЛЛАР')
    width_max_payeer_rub = models.IntegerField('ПАЕЕРРУБ')
    width_max_payeer_usd = models.IntegerField('ПАЕЕРДОЛЛАР')
    width_max_payeer_eur = models.IntegerField('ПАЕЕРЕВРО')
    width_max_webmoney_rub = models.IntegerField('ВЕБМАНИРУБ')
    width_max_webmoney_usd = models.IntegerField('ВЕБМАНИДОЛЛАР')
    width_max_webmoney_eur = models.IntegerField('ВЕБМАНИЕВРО')
    width_max_pm_btc = models.DecimalField('ПМБИТКОИН', max_digits=16, decimal_places=8, default=0)
    width_max_pm_usd = models.IntegerField('ПМДОЛЛАР')
    width_max_pm_eur = models.IntegerField('ПМЕВРО')
    width_max_skrill_eur = models.IntegerField('СКРИЛЛЕВРО')
    width_max_skrill_usd = models.IntegerField('СКРИЛДОЛЛАР')
    width_max_paypal_rub = models.IntegerField('ПАЙПАЛРУБ')
    width_max_paypal_usd = models.IntegerField('ПАЙПАЛДОЛЛАР')
    width_max_paypal_eur = models.IntegerField('ПАЙПАЛЕВРО')
    width_max_umoney_rub = models.IntegerField('ЮМАНИ')
    # КРИПТА
    width_max_btc = models.DecimalField('БИТКОИН', max_digits=16, decimal_places=8, default=0)
    width_max_xrp = models.DecimalField('РИПЛ', max_digits=16, decimal_places=8, default=0)
    width_max_ltc = models.DecimalField('ЛАЙТКОИН', max_digits=16, decimal_places=8, default=0)
    width_max_bch = models.DecimalField('БИТКОИНКЕШ', max_digits=16, decimal_places=8, default=0)
    width_max_xmr = models.DecimalField('МОНЕРО', max_digits=16, decimal_places=8, default=0)
    width_max_eth = models.DecimalField('ЭФИР', max_digits=16, decimal_places=8, default=0)
    width_max_etc = models.DecimalField('ЭФИРКЛАССИК', max_digits=16, decimal_places=8, default=0)
    width_max_dash = models.DecimalField('ДАШ', max_digits=16, decimal_places=8, default=0)

    def __str__(self):
        return self.width_range_username.username

    class Meta:
        verbose_name = 'Диапазон для вывода'
        verbose_name_plural = 'Диапазон для вывода'
