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
    is_active_change = models.BooleanField('Статус активности обработчика', default=False)

# === АКТИВНОСТЬ ПС ПОПОЛНЕНИЕ ===
# БАНКИ
    active_in_sberbank_rub = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ СБЕРБАНК', default=False)
    active_in_psb_rub = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ ПСБ', default=False)
    active_in_tinkoff_rub = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ ТИНЬКОФФ', default=False)
    active_in_gazprombank_rub = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ ГАЗПРОМБАНК', default=False)
    active_in_alfabank_rub = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ АЛЬФАБАНК', default=False)
    active_in_russtandart_rub = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ РУССКИЙСТАНДАРТ', default=False)
    active_in_vtb_rub = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ ВТБ', default=False)
    active_in_rosselhoz_rub = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ РОССЕЛЬХОЗБАНК', default=False)
    active_in_raifaizen_rub = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ РАЙФАЙЗЕНБАНК', default=False)
    active_in_roketbank_rub = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ РОКЕТБАНК', default=False)
    active_in_otkritie_rub = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ ОТКРЫТИЕ', default=False)
    active_in_pochtabank_rub = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ ПОЧТАБАНК', default=False)
    active_in_rnkb_rub = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ РНКБ', default=False)
    active_in_rosbank_rub = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ РОСБАНК', default=False)
    active_in_mtsbank_rub = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ МТСБАНК', default=False)
# ПС
    active_in_qiwi_rub = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ КИВИРУБ', default=False)
    active_in_qiwi_usd = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ КИВИДОЛЛАР', default=False)
    active_in_payeer_rub = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ ПАЕЕРРУБ', default=False)
    active_in_payeer_usd = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ ПАЕЕРДОЛЛАР', default=False)
    active_in_payeer_eur = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ ПАЕЕРЕВРО', default=False)
    active_in_webmoney_rub = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ ВЕБМАНИРУБ', default=False)
    active_in_webmoney_usd = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ ВЕБМАНИДОЛЛАР', default=False)
    active_in_webmoney_eur = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ ВЕБМАНИЕВРО', default=False)
    active_in_pm_btc = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ ПМБИТКОИН', default=False)
    active_in_pm_usd = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ ПМДОЛЛАР', default=False)
    active_in_pm_eur = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ ПМЕВРО', default=False)
    active_in_skrill_eur = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ СКРИЛЛЕВРО', default=False)
    active_in_skrill_usd = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ СКРИЛДОЛЛАР', default=False)
    active_in_paypal_rub = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ ПАЙПАЛРУБ', default=False)
    active_in_paypal_usd = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ ПАЙПАЛДОЛЛАР', default=False)
    active_in_paypal_eur = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ ПАЙПАЛЕВРО', default=False)
    active_in_umoney_rub = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ ЮМАНИ', default=False)
# КРИПТА
    active_in_btc = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ БИТКОИН', default=False)
    active_in_xrp = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ РИПЛ', default=False)
    active_in_ltc = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ ЛАЙТКОИН', default=False)
    active_in_bch = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ БИТКОИНКЕШ', default=False)
    active_in_xmr = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ МОНЕРО', default=False)
    active_in_eth = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ ЭФИР', default=False)
    active_in_etc = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ ЭФИРКЛАССИК', default=False)
    active_in_dash = models.BooleanField('АКТИВНОСТЬ НА ПОПОЛНЕНИЕ ДАШ', default=False)

# === АКТИВНОСТЬ ПС ВЫВОД ===
# БАНКИ
    active_out_sberbank_rub = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД СБЕРБАНК', default=False)
    active_out_psb_rub = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД ПСБ', default=False)
    active_out_tinkoff_rub = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД ТИНЬКОФФ', default=False)
    active_out_gazprombank_rub = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД ГАЗПРОМБАНК', default=False)
    active_out_alfabank_rub = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД АЛЬФАБАНК', default=False)
    active_out_russtandart_rub = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД РУССКИЙСТАНДАРТ', default=False)
    active_out_vtb_rub = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД ВТБ', default=False)
    active_out_rosselhoz_rub = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД РОССЕЛЬХОЗБАНК', default=False)
    active_out_raifaizen_rub = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД РАЙФАЙЗЕНБАНК', default=False)
    active_out_roketbank_rub = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД РОКЕТБАНК', default=False)
    active_out_otkritie_rub = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД ОТКРЫТИЕ', default=False)
    active_out_pochtabank_rub = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД ПОЧТАБАНК', default=False)
    active_out_rnkb_rub = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД РНКБ', default=False)
    active_out_rosbank_rub = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД РОСБАНК', default=False)
    active_out_mtsbank_rub = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД МТСБАНК', default=False)
# ПС
    active_out_qiwi_rub = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД КИВИРУБ', default=False)
    active_out_qiwi_usd = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД КИВИДОЛЛАР', default=False)
    active_out_payeer_rub = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД ПАЕЕРРУБ', default=False)
    active_out_payeer_usd = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД ПАЕЕРДОЛЛАР', default=False)
    active_out_payeer_eur = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД ПАЕЕРЕВРО', default=False)
    active_out_webmoney_rub = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД ВЕБМАНИРУБ', default=False)
    active_out_webmoney_usd = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД ВЕБМАНИДОЛЛАР', default=False)
    active_out_webmoney_eur = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД ВЕБМАНИЕВРО', default=False)
    active_out_pm_btc = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД ПМБИТКОИН', default=False)
    active_out_pm_usd = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД ПМДОЛЛАР', default=False)
    active_out_pm_eur = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД ПМЕВРО', default=False)
    active_out_skrill_eur = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД СКРИЛЛЕВРО', default=False)
    active_out_skrill_usd = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД СКРИЛДОЛЛАР', default=False)
    active_out_paypal_rub = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД ПАЙПАЛРУБ', default=False)
    active_out_paypal_usd = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД ПАЙПАЛДОЛЛАР', default=False)
    active_out_paypal_eur = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД ПАЙПАЛЕВРО', default=False)
    active_out_umoney_rub = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД ЮМАНИ', default=False)
# КРИПТА
    active_out_btc = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД БИТКОИН', default=False)
    active_out_xrp = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД РИПЛ', default=False)
    active_out_ltc = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД ЛАЙТКОИН', default=False)
    active_out_bch = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД БИТКОИНКЕШ', default=False)
    active_out_xmr = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД МОНЕРО', default=False)
    active_out_eth = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД ЭФИР', default=False)
    active_out_etc = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД ЭФИРКЛАССИК', default=False)
    active_out_dash = models.BooleanField('АКТИВНОСТЬ НА ВЫВОД ДАШ', default=False)


# === КОММИСИИ на пополнение ===
# БАНКИ
    comis_in_sberbank_rub = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ СБЕРБАНК', max_digits=4, decimal_places=2, default=0)
    comis_in_psb_rub = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ ПСБ', max_digits=4, decimal_places=2, default=0)
    comis_in_tinkoff_rub = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ ТИНЬКОФФ', max_digits=4, decimal_places=2, default=0)
    comis_in_gazprombank_rub = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ ГАЗПРОМБАНК', max_digits=4, decimal_places=2, default=0)
    comis_in_alfabank_rub = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ АЛЬФАБАНК', max_digits=4, decimal_places=2, default=0)
    comis_in_russtandart_rub = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ РУССКИЙСТАНДАРТ', max_digits=4, decimal_places=2, default=0)
    comis_in_vtb_rub = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ ВТБ', max_length=50, max_digits=4, decimal_places=2, default=0)
    comis_in_rosselhoz_rub = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ РОССЕЛЬХОЗБАНК', max_digits=4, decimal_places=2, default=0)
    comis_in_raifaizen_rub = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ РАЙФАЙЗЕНБАНК', max_digits=4, decimal_places=2, default=0)
    comis_in_roketbank_rub = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ РОКЕТБАНК', max_digits=4, decimal_places=2, default=0)
    comis_in_otkritie_rub = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ ОТКРЫТИЕ', max_digits=4, decimal_places=2, default=0)
    comis_in_pochtabank_rub = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ ПОЧТАБАНК', max_digits=4, decimal_places=2, default=0)
    comis_in_rnkb_rub = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ РНКБ', max_digits=4, decimal_places=2, default=0)
    comis_in_rosbank_rub = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ РОСБАНК', max_digits=4, decimal_places=2, default=0)
    comis_in_mtsbank_rub = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ МТСБАНК', max_digits=4, decimal_places=2, default=0)
# ПС
    comis_in_qiwi_rub = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ КИВИРУБ', max_digits=4, decimal_places=2, default=0)
    comis_in_qiwi_usd = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ КИВИДОЛЛАР', max_digits=4, decimal_places=2, default=0)
    comis_in_payeer_rub = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ ПАЕЕРРУБ', max_digits=4, decimal_places=2, default=0)
    comis_in_payeer_usd = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ ПАЕЕРДОЛЛАР', max_digits=4, decimal_places=2, default=0)
    comis_in_payeer_eur = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ ПАЕЕРЕВРО', max_digits=4, decimal_places=2, default=0)
    comis_in_webmoney_rub = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ ВЕБМАНИРУБ', max_digits=4, decimal_places=2, default=0)
    comis_in_webmoney_usd = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ ВЕБМАНИДОЛЛАР', max_digits=4, decimal_places=2, default=0)
    comis_in_webmoney_eur = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ ВЕБМАНИЕВРО', max_digits=4, decimal_places=2, default=0)
    comis_in_pm_btc = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ ПМБИТКОИН', max_digits=4, decimal_places=2, default=0)
    comis_in_pm_usd = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ ПМДОЛЛАР', max_digits=4, decimal_places=2, default=0)
    comis_in_pm_eur = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ ПМЕВРО', max_digits=4, decimal_places=2, default=0)
    comis_in_skrill_eur = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ СКРИЛЛЕВРО', max_digits=4, decimal_places=2, default=0)
    comis_in_skrill_usd = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ СКРИЛДОЛЛАР', max_digits=4, decimal_places=2, default=0)
    comis_in_paypal_rub = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ ПАЙПАЛРУБ', max_digits=4, decimal_places=2, default=0)
    comis_in_paypal_usd = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ ПАЙПАЛДОЛЛАР', max_digits=4, decimal_places=2, default=0)
    comis_in_paypal_eur = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ ПАЙПАЛЕВРО', max_digits=4, decimal_places=2, default=0)
    comis_in_umoney_rub = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ ЮМАНИ', max_digits=4, decimal_places=2, default=0)
# КРИПТА
    comis_in_btc = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ БИТКОИН', max_digits=4, decimal_places=2, default=0)
    comis_in_xrp = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ РИПЛ', max_digits=4, decimal_places=2, default=0)
    comis_in_ltc = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ ЛАЙТКОИН', max_digits=4, decimal_places=2, default=0)
    comis_in_bch = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ БИТКОИНКЕШ', max_digits=4, decimal_places=2, default=0)
    comis_in_xmr = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ МОНЕРО', max_digits=4, decimal_places=2, default=0)
    comis_in_eth = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ ЭФИР', max_digits=4, decimal_places=2, default=0)
    comis_in_etc = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ ЭФИРКЛАССИК', max_digits=4, decimal_places=2, default=0)
    comis_in_dash = models.DecimalField('КОММИСИЯ НА ПОПОЛНЕНИЕ ДАШ', max_digits=4, decimal_places=2, default=0)

# === КОММИСИИ на вывод ===
# БАНКИ
    comis_out_sberbank_rub = models.DecimalField('КОММИСИЯ НА ВЫВОД СБЕРБАНК', max_digits=4, decimal_places=2, default=0)
    comis_out_psb_rub = models.DecimalField('КОММИСИЯ НА ВЫВОД ПСБ', max_digits=4, decimal_places=2, default=0)
    comis_out_tinkoff_rub = models.DecimalField('КОММИСИЯ НА ВЫВОД ТИНЬКОФФ', max_digits=4, decimal_places=2, default=0)
    comis_out_gazprombank_rub = models.DecimalField('КОММИСИЯ НА ВЫВОД ГАЗПРОМБАНК', max_digits=4, decimal_places=2, default=0)
    comis_out_alfabank_rub = models.DecimalField('КОММИСИЯ НА ВЫВОД АЛЬФАБАНК', max_digits=4, decimal_places=2, default=0)
    comis_out_russtandart_rub = models.DecimalField('КОММИСИЯ НА ВЫВОД РУССКИЙСТАНДАРТ', max_digits=4, decimal_places=2, default=0)
    comis_out_vtb_rub = models.DecimalField('КОММИСИЯ НА ВЫВОД ВТБ', max_digits=4, decimal_places=2, default=0)
    comis_out_rosselhoz_rub = models.DecimalField('КОММИСИЯ НА ВЫВОД РОССЕЛЬХОЗБАНК', max_digits=4, decimal_places=2, default=0)
    comis_out_raifaizen_rub = models.DecimalField('КОММИСИЯ НА ВЫВОД РАЙФАЙЗЕНБАНК', max_digits=4, decimal_places=2, default=0)
    comis_out_roketbank_rub = models.DecimalField('КОММИСИЯ НА ВЫВОД РОКЕТБАНК', max_digits=4, decimal_places=2, default=0)
    comis_out_otkritie_rub = models.DecimalField('КОММИСИЯ НА ВЫВОД ОТКРЫТИЕ', max_digits=4, decimal_places=2, default=0)
    comis_out_pochtabank_rub = models.DecimalField('КОММИСИЯ НА ВЫВОД ПОЧТАБАНК', max_digits=4, decimal_places=2, default=0)
    comis_out_rnkb_rub = models.DecimalField('КОММИСИЯ НА ВЫВОД РНКБ', max_digits=4, decimal_places=2, default=0)
    comis_out_rosbank_rub = models.DecimalField('КОММИСИЯ НА ВЫВОД РОСБАНК', max_digits=4, decimal_places=2, default=0)
    comis_out_mtsbank_rub = models.DecimalField('КОММИСИЯ НА ВЫВОД МТСБАНК', max_digits=4, decimal_places=2, default=0)
# ПС
    comis_out_qiwi_rub = models.DecimalField('КОММИСИЯ НА ВЫВОД КИВИРУБ', max_digits=4, decimal_places=2, default=0)
    comis_out_qiwi_usd = models.DecimalField('КОММИСИЯ НА ВЫВОД КИВИДОЛЛАР', max_digits=4, decimal_places=2, default=0)
    comis_out_payeer_rub = models.DecimalField('КОММИСИЯ НА ВЫВОД ПАЕЕРРУБ', max_digits=4, decimal_places=2, default=0)
    comis_out_payeer_usd = models.DecimalField('КОММИСИЯ НА ВЫВОД ПАЕЕРДОЛЛАР', max_digits=4, decimal_places=2, default=0)
    comis_out_payeer_eur = models.DecimalField('КОММИСИЯ НА ВЫВОД ПАЕЕРЕВРО', max_digits=4, decimal_places=2, default=0)
    comis_out_webmoney_rub = models.DecimalField('КОММИСИЯ НА ВЫВОД ВЕБМАНИРУБ', max_digits=4, decimal_places=2, default=0)
    comis_out_webmoney_usd = models.DecimalField('КОММИСИЯ НА ВЫВОД ВЕБМАНИДОЛЛАР', max_digits=4, decimal_places=2, default=0)
    comis_out_webmoney_eur = models.DecimalField('КОММИСИЯ НА ВЫВОД ВЕБМАНИЕВРО', max_digits=4, decimal_places=2, default=0)
    comis_out_pm_btc = models.DecimalField('КОММИСИЯ НА ВЫВОД ПМБИТКОИН', max_digits=4, decimal_places=2, default=0)
    comis_out_pm_usd = models.DecimalField('КОММИСИЯ НА ВЫВОД ПМДОЛЛАР', max_digits=4, decimal_places=2, default=0)
    comis_out_pm_eur = models.DecimalField('КОММИСИЯ НА ВЫВОД ПМЕВРО', max_digits=4, decimal_places=2, default=0)
    comis_out_skrill_eur = models.DecimalField('КОММИСИЯ НА ВЫВОД СКРИЛЛЕВРО', max_digits=4, decimal_places=2, default=0)
    comis_out_skrill_usd = models.DecimalField('КОММИСИЯ НА ВЫВОД СКРИЛДОЛЛАР', max_digits=4, decimal_places=2, default=0)
    comis_out_paypal_rub = models.DecimalField('КОММИСИЯ НА ВЫВОД ПАЙПАЛРУБ', max_digits=4, decimal_places=2, default=0)
    comis_out_paypal_usd = models.DecimalField('КОММИСИЯ НА ВЫВОД ПАЙПАЛДОЛЛАР', max_digits=4, decimal_places=2, default=0)
    comis_out_paypal_eur = models.DecimalField('КОММИСИЯ НА ВЫВОД ПАЙПАЛЕВРО', max_digits=4, decimal_places=2, default=0)
    comis_out_umoney_rub = models.DecimalField('КОММИСИЯ НА ВЫВОД ЮМАНИ', max_digits=4, decimal_places=2, default=0)
# КРИПТА
    comis_out_btc = models.DecimalField('КОММИСИЯ НА ВЫВОД БИТКОИН', max_digits=4, decimal_places=2, default=0)
    comis_out_xrp = models.DecimalField('КОММИСИЯ НА ВЫВОД РИПЛ', max_digits=4, decimal_places=2, default=0)
    comis_out_ltc = models.DecimalField('КОММИСИЯ НА ВЫВОД ЛАЙТКОИН', max_digits=4, decimal_places=2, default=0)
    comis_out_bch = models.DecimalField('КОММИСИЯ НА ВЫВОД БИТКОИНКЕШ', max_digits=4, decimal_places=2, default=0)
    comis_out_xmr = models.DecimalField('КОММИСИЯ НА ВЫВОД МОНЕРО', max_digits=4, decimal_places=2, default=0)
    comis_out_eth = models.DecimalField('КОММИСИЯ НА ВЫВОД ЭФИР', max_digits=4, decimal_places=2, default=0)
    comis_out_etc = models.DecimalField('КОММИСИЯ НА ВЫВОД ЭФИРКЛАССИК', max_digits=4, decimal_places=2, default=0)
    comis_out_dash = models.DecimalField('КОММИСИЯ НА ВЫВОД ДАШ', max_digits=4, decimal_places=2, default=0)

# === РЕКВИЗИТЫ для пополнения ===
# БАНКИ
    requsites_sberbank_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ СБЕРБАНК', max_length=50, blank=True)
    requsites_psb_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ ПСБ', max_length=50, blank=True)
    requsites_tinkoff_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ ТИНЬКОФФ', max_length=50, blank=True)
    requsites_gazprombank_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ ГАЗПРОМБАНК', max_length=50, blank=True)
    requsites_alfabank_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ АЛЬФАБАНК', max_length=50, blank=True)
    requsites_russtandart_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ РУССКИЙСТАНДАРТ', max_length=50, blank=True)
    requsites_vtb_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ ВТБ', max_length=50, blank=True)
    requsites_rosselhoz_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ РОССЕЛЬХОЗБАНК', max_length=50, blank=True)
    requsites_raifaizen_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ РАЙФАЙЗЕНБАНК', max_length=50, blank=True)
    requsites_roketbank_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ РОКЕТБАНК', max_length=50, blank=True)
    requsites_otkritie_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ ОТКРЫТИЕ', max_length=50, blank=True)
    requsites_pochtabank_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ ПОЧТАБАНК', max_length=50, blank=True)
    requsites_rnkb_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ РНКБ', max_length=50, blank=True)
    requsites_rosbank_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ РОСБАНК', max_length=50, blank=True)
    requsites_mtsbank_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ МТСБАНК', max_length=50, blank=True)
# ПС
    requsites_qiwi_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ КИВИРУБ', max_length=50, blank=True)
    requsites_qiwi_usd = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ КИВИДОЛЛАР', max_length=50, blank=True)
    requsites_payeer_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ ПАЕЕРРУБ', max_length=50, blank=True)
    requsites_payeer_usd = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ ПАЕЕРДОЛЛАР', max_length=50, blank=True)
    requsites_payeer_eur = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ ПАЕЕРЕВРО', max_length=50, blank=True)
    requsites_webmoney_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ ВЕБМАНИРУБ', max_length=50, blank=True)
    requsites_webmoney_usd = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ ВЕБМАНИДОЛЛАР', max_length=50, blank=True)
    requsites_webmoney_eur = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ ВЕБМАНИЕВРО', max_length=50, blank=True)
    requsites_pm_btc = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ ПМБИТКОИН', max_length=50, blank=True)
    requsites_pm_usd = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ ПМДОЛЛАР', max_length=50, blank=True)
    requsites_pm_eur = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ ПМЕВРО', max_length=50, blank=True)
    requsites_skrill_eur = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ СКРИЛЛЕВРО', max_length=50, blank=True)
    requsites_skrill_usd = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ СКРИЛДОЛЛАР', max_length=50, blank=True)
    requsites_paypal_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ ПАЙПАЛРУБ', max_length=50, blank=True)
    requsites_paypal_usd = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ ПАЙПАЛДОЛЛАР', max_length=50, blank=True)
    requsites_paypal_eur = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ ПАЙПАЛЕВРО', max_length=50, blank=True)
    requsites_umoney_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ ЮМАНИ', max_length=50, blank=True)
# КРИПТА
    requsites_btc = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ БИТКОИН', max_length=50, blank=True)
    requsites_xrp = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ РИПЛ', max_length=50, blank=True)
    requsites_ltc = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ ЛАЙТКОИН', max_length=50, blank=True)
    requsites_bch = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ БИТКОИНКЕШ', max_length=50, blank=True)
    requsites_xmr = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ МОНЕРО', max_length=50, blank=True)
    requsites_eth = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ ЭФИР', max_length=50, blank=True)
    requsites_etc = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ ЭФИРКЛАССИК', max_length=50, blank=True)
    requsites_dash = models.CharField('РЕКВИЗИТЫ ДЛЯ ПОПОЛНЕНИЯ ДАШ', max_length=50, blank=True)

# === РЕКВИЗИТЫ для вывода===
# БАНКИ
    requsites_width_sberbank_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА СБЕРБАНК', max_length=50, blank=True)
    requsites_width_psb_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА ПСБ', max_length=50, blank=True)
    requsites_width_tinkoff_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА ТИНЬКОФФ', max_length=50, blank=True)
    requsites_width_gazprombank_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА ГАЗПРОМБАНК', max_length=50, blank=True)
    requsites_width_alfabank_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА АЛЬФАБАНК', max_length=50, blank=True)
    requsites_width_russtandart_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА РУССКИЙСТАНДАРТ', max_length=50, blank=True)
    requsites_width_vtb_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА ВТБ', max_length=50, blank=True)
    requsites_width_rosselhoz_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА РОССЕЛЬХОЗБАНК', max_length=50, blank=True)
    requsites_width_raifaizen_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА РАЙФАЙЗЕНБАНК', max_length=50, blank=True)
    requsites_width_roketbank_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА РОКЕТБАНК', max_length=50, blank=True)
    requsites_width_otkritie_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА ОТКРЫТИЕ', max_length=50, blank=True)
    requsites_width_pochtabank_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА ПОЧТАБАНК', max_length=50, blank=True)
    requsites_width_rnkb_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА РНКБ', max_length=50, blank=True)
    requsites_width_rosbank_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА РОСБАНК', max_length=50, blank=True)
    requsites_width_mtsbank_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА МТСБАНК', max_length=50, blank=True)
# ПС
    requsites_width_qiwi_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА КИВИРУБ', max_length=50, blank=True)
    requsites_width_qiwi_usd = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА КИВИДОЛЛАР', max_length=50, blank=True)
    requsites_width_payeer_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА ПАЕЕРРУБ', max_length=50, blank=True)
    requsites_width_payeer_usd = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА ПАЕЕРДОЛЛАР', max_length=50, blank=True)
    requsites_width_payeer_eur = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА ПАЕЕРЕВРО', max_length=50, blank=True)
    requsites_width_webmoney_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА ВЕБМАНИРУБ', max_length=50, blank=True)
    requsites_width_webmoney_usd = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА ВЕБМАНИДОЛЛАР', max_length=50, blank=True)
    requsites_width_webmoney_eur = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА ВЕБМАНИЕВРО', max_length=50, blank=True)
    requsites_width_pm_btc = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА ПМБИТКОИН', max_length=50, blank=True)
    requsites_width_pm_usd = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА ПМДОЛЛАР', max_length=50, blank=True)
    requsites_width_pm_eur = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА ПМЕВРО', max_length=50, blank=True)
    requsites_width_skrill_eur = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА СКРИЛЛЕВРО', max_length=50, blank=True)
    requsites_width_skrill_usd = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА СКРИЛДОЛЛАР', max_length=50, blank=True)
    requsites_width_paypal_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА ПАЙПАЛРУБ', max_length=50, blank=True)
    requsites_width_paypal_usd = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА ПАЙПАЛДОЛЛАР', max_length=50, blank=True)
    requsites_width_paypal_eur = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА ПАЙПАЛЕВРО', max_length=50, blank=True)
    requsites_width_umoney_rub = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА ЮМАНИ', max_length=50, blank=True)
# КРИПТА
    requsites_width_btc = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА БИТКОИН', max_length=50, blank=True)
    requsites_width_xrp = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА РИПЛ', max_length=50, blank=True)
    requsites_width_ltc = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА ЛАЙТКОИН', max_length=50, blank=True)
    requsites_width_bch = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА БИТКОИНКЕШ', max_length=50, blank=True)
    requsites_width_xmr = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА МОНЕРО', max_length=50, blank=True)
    requsites_width_eth = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА ЭФИР', max_length=50, blank=True)
    requsites_width_etc = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА ЭФИРКЛАССИК', max_length=50, blank=True)
    requsites_width_dash = models.CharField('РЕКВИЗИТЫ ДЛЯ ВЫВОДА ДАШ', max_length=50, blank=True)

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


