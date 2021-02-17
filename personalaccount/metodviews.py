import random

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from MyWallets import settings
from personalaccount.models import CurrencyCBRF, RequestChange, StaticDailyProfit
from users.models import CustomUser, RangeSumDeposit, RangeSumWidth

from datetime import timedelta, datetime, date


# активность обменника и направлений для пополнения
def depositsortchangeps(nameps):
    itemchange = CustomUser.objects.filter(userid__custuserid='Владелец Обменника', is_active_change=1)
    changeq = []
    if nameps == 'СБЕРБАНК':
        for item in itemchange:
            if item.active_in_sberbank_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'ТИНЬКОФФ':
        for item in itemchange:
            if item.active_in_tinkoff_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'АЛЬФА БАНК':
        for item in itemchange:
            if item.active_in_alfabank_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'ВТБ':
        for item in itemchange:
            if item.active_in_vtb_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'РАЙФФАЙЗЕНБАНК':
        for item in itemchange:
            if item.active_in_raifaizen_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'ОТКРЫТИЕ':
        for item in itemchange:
            if item.active_in_otkritie_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'ПСБ':
        for item in itemchange:
            if item.active_in_psb_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'ГАЗПРОМБАНК':
        for item in itemchange:
            if item.active_in_gazprombank_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'РУССКИЙ СТАНДАРТ':
        for item in itemchange:
            if item.active_in_russtandart_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'РОССЕЛЬХОЗБАНК':
        for item in itemchange:
            if item.active_in_rosselhoz_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'ПОЧТА БАНК':
        for item in itemchange:
            if item.active_in_pochtabank_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'РОСБАНК':
        for item in itemchange:
            if item.active_in_rosbank_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'РНКБ':
        for item in itemchange:
            if item.active_in_rnkb_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'МТС БАНК':
        for item in itemchange:
            if item.active_in_mtsbank_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'QIWI RUB':
        for item in itemchange:
            if item.active_in_qiwi_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'QIWI USD':
        for item in itemchange:
            if item.active_in_qiwi_usd == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'USD'}
    elif nameps == 'PAYEER RUB':
        for item in itemchange:
            if item.active_in_payeer_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'PAYEER EUR':
        for item in itemchange:
            if item.active_in_payeer_eur == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'EUR'}
    elif nameps == 'PAYEER USD':
        for item in itemchange:
            if item.active_in_payeer_usd == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'USD'}
    elif nameps == 'WEBMONEY RUB':
        for item in itemchange:
            if item.active_in_webmoney_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'WEBMONEY EUR':
        for item in itemchange:
            if item.active_in_webmoney_eur == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'EUR'}
    elif nameps == 'WEBMONEY USD':
        for item in itemchange:
            if item.active_in_webmoney_usd == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'USD'}
    elif nameps == 'PERFECT MONEY BTC':
        for item in itemchange:
            if item.active_in_pm_btc == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'BTC'}
    elif nameps == 'PERFECT MONEY EUR':
        for item in itemchange:
            if item.active_in_pm_eur == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'EUR'}
    elif nameps == 'PERFECT MONEY USD':
        for item in itemchange:
            if item.active_in_pm_usd == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'USD'}
    elif nameps == 'PAYPAL RUB':
        for item in itemchange:
            if item.active_in_paypal_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'PAYPAL EUR':
        for item in itemchange:
            if item.active_in_paypal_eur == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'EUR'}
    elif nameps == 'PAYPAL USD':
        for item in itemchange:
            if item.active_in_paypal_usd == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'USD'}
    elif nameps == 'SKRILL EUR':
        for item in itemchange:
            if item.active_in_skrill_eur == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'EUR'}
    elif nameps == 'SKRILL USD':
        for item in itemchange:
            if item.active_in_skrill_usd == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'USD'}
    elif nameps == 'UMONEY RUB':
        for item in itemchange:
            if item.active_in_umoney_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'BITCOIN':
        for item in itemchange:
            if item.active_in_btc == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'BTC'}
    elif nameps == 'LITECOIN':
        for item in itemchange:
            if item.active_in_ltc == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'LTC'}
    elif nameps == 'MONERO':
        for item in itemchange:
            if item.active_in_xmr == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'XMR'}
    elif nameps == 'ETHEREUM CLASSIC':
        for item in itemchange:
            if item.active_in_etc == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'ETC'}
    elif nameps == 'DASH':
        for item in itemchange:
            if item.active_in_dash == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'DASH'}
    elif nameps == 'RIPPLE':
        for item in itemchange:
            if item.active_in_xrp == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'XRP'}
    elif nameps == 'BITCOIN CASH':
        for item in itemchange:
            if item.active_in_bch == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'BCH'}
    elif nameps == 'ETHEREUM':
        for item in itemchange:
            if item.active_in_eth == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'ETH'}


# активность обменника и направлений для вывода
def widthsortchangeps(nameps):
    itemchange = CustomUser.objects.filter(userid__custuserid='Владелец Обменника', is_active_change=1)
    changeq = []
    if nameps == 'СБЕРБАНК':
        for item in itemchange:
            if item.active_out_sberbank_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'ТИНЬКОФФ':
        for item in itemchange:
            if item.active_out_tinkoff_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'АЛЬФА БАНК':
        for item in itemchange:
            if item.active_out_alfabank_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'ВТБ':
        for item in itemchange:
            if item.active_out_vtb_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'РАЙФФАЙЗЕНБАНК':
        for item in itemchange:
            if item.active_out_raifaizen_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'ОТКРЫТИЕ':
        for item in itemchange:
            if item.active_out_otkritie_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'ПСБ':
        for item in itemchange:
            if item.active_out_psb_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'ГАЗПРОМБАНК':
        for item in itemchange:
            if item.active_out_gazprombank_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'РУССКИЙ СТАНДАРТ':
        for item in itemchange:
            if item.active_out_russtandart_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'РОССЕЛЬХОЗБАНК':
        for item in itemchange:
            if item.active_out_rosselhoz_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'ПОЧТА БАНК':
        for item in itemchange:
            if item.active_out_pochtabank_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'РОСБАНК':
        for item in itemchange:
            if item.active_out_rosbank_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'РНКБ':
        for item in itemchange:
            if item.active_out_rnkb_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'МТС БАНК':
        for item in itemchange:
            if item.active_out_mtsbank_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'QIWI RUB':
        for item in itemchange:
            if item.active_out_qiwi_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'QIWI USD':
        for item in itemchange:
            if item.active_out_qiwi_usd == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'USD'}
    elif nameps == 'PAYEER RUB':
        for item in itemchange:
            if item.active_out_payeer_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'PAYEER EUR':
        for item in itemchange:
            if item.active_out_payeer_eur == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'EUR'}
    elif nameps == 'PAYEER USD':
        for item in itemchange:
            if item.active_out_payeer_usd == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'USD'}
    elif nameps == 'WEBMONEY RUB':
        for item in itemchange:
            if item.active_out_webmoney_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'WEBMONEY EUR':
        for item in itemchange:
            if item.active_out_webmoney_eur == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'EUR'}
    elif nameps == 'WEBMONEY USD':
        for item in itemchange:
            if item.active_out_webmoney_usd == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'USD'}
    elif nameps == 'PERFECT MONEY BTC':
        for item in itemchange:
            if item.active_out_pm_btc == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'BTC'}
    elif nameps == 'PERFECT MONEY EUR':
        for item in itemchange:
            if item.active_out_pm_eur == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'EUR'}
    elif nameps == 'PERFECT MONEY USD':
        for item in itemchange:
            if item.active_out_pm_usd == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'USD'}
    elif nameps == 'PAYPAL RUB':
        for item in itemchange:
            if item.active_out_paypal_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'PAYPAL EUR':
        for item in itemchange:
            if item.active_out_paypal_eur == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'EUR'}
    elif nameps == 'PAYPAL USD':
        for item in itemchange:
            if item.active_out_paypal_usd == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'USD'}
    elif nameps == 'SKRILL EUR':
        for item in itemchange:
            if item.active_out_skrill_eur == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'EUR'}
    elif nameps == 'SKRILL USD':
        for item in itemchange:
            if item.active_out_skrill_usd == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'USD'}
    elif nameps == 'UMONEY RUB':
        for item in itemchange:
            if item.active_out_umoney_rub == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'RUB'}
    elif nameps == 'BITCOIN':
        for item in itemchange:
            if item.active_out_btc == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'BTC'}
    elif nameps == 'LITECOIN':
        for item in itemchange:
            if item.active_out_ltc == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'LTC'}
    elif nameps == 'MONERO':
        for item in itemchange:
            if item.active_out_xmr == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'XMR'}
    elif nameps == 'ETHEREUM CLASSIC':
        for item in itemchange:
            if item.active_out_etc == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'ETC'}
    elif nameps == 'DASH':
        for item in itemchange:
            if item.active_out_dash == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'DASH'}
    elif nameps == 'RIPPLE':
        for item in itemchange:
            if item.active_out_xrp == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'XRP'}
    elif nameps == 'BITCOIN CASH':
        for item in itemchange:
            if item.active_out_bch == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'BCH'}
    elif nameps == 'ETHEREUM':
        for item in itemchange:
            if item.active_out_eth == 1:
                changeq.append(item)
        return {'changeq': changeq, 'valute': 'ETH'}


# проверка баланса для пополнений
def depositsortbalanceps(userps, balanceps, valuteps):
    userlist = []
    currencysort = CurrencyCBRF.objects.get(name_currency=valuteps)
    if valuteps == 'USD':
        for userchange in userps:
            if balanceps < userchange.balance:
                userlist.append(userchange)
    else:
        for userchange in userps:
            if balanceps * currencysort.base_currency < userchange.balance:
                userlist.append(userchange)

    return userlist


# проверка баланса для вывода
def widthsortbalanceps(userps, balanceps, nameps, valuteps):
    userlist = []
    currencysort = CurrencyCBRF.objects.get(name_currency=valuteps)
    if nameps == 'СБЕРБАНК':
        for userchange in userps:
            if userchange.reserv_sberbank_rub * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'ТИНЬКОФФ':
        for userchange in userps:
            if userchange.reserv_tinkoff_rub * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'АЛЬФА БАНК':
        for userchange in userps:
            if userchange.reserv_alfabank_rub * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'ВТБ':
        for userchange in userps:
            if userchange.reserv_vtb_rub * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'РАЙФФАЙЗЕНБАНК':
        for userchange in userps:
            if userchange.reserv_raifaizen_rub * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'ОТКРЫТИЕ':
        for userchange in userps:
            if userchange.reserv_otkritie_rub * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'ПСБ':
        for userchange in userps:
            if userchange.reserv_psb_rub * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'ГАЗПРОМБАНК':
        for userchange in userps:
            if userchange.reserv_gazprombank_rub * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'РУССКИЙ СТАНДАРТ':
        for userchange in userps:
            if userchange.reserv_russtandart_rub * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'РОССЕЛЬХОЗБАНК':
        for userchange in userps:
            if userchange.reserv_rosselhoz_rub * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'ПОЧТА БАНК':
        for userchange in userps:
            if userchange.reserv_pochtabank_rub * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'РОСБАНК':
        for userchange in userps:
            if userchange.reserv_rosbank_rub * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'РНКБ':
        for userchange in userps:
            if userchange.reserv_rnkb_rub * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'МТС БАНК':
        for userchange in userps:
            if userchange.reserv_mtsbank_rub * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'QIWI RUB':
        for userchange in userps:
            if userchange.reserv_qiwi_rub * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'QIWI USD':
        for userchange in userps:
            if userchange.reserv_qiwi_usd * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'PAYEER RUB':
        for userchange in userps:
            if userchange.reserv_payeer_rub * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'PAYEER EUR':
        for userchange in userps:
            if userchange.reserv_payeer_eur * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'PAYEER USD':
        for userchange in userps:
            if userchange.reserv_payeer_usd * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'WEBMONEY RUB':
        for userchange in userps:
            if userchange.reserv_webmoney_rub * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'WEBMONEY EUR':
        for userchange in userps:
            if userchange.reserv_webmoney_eur * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'WEBMONEY USD':
        for userchange in userps:
            if userchange.reserv_webmoney_usd * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'PERFECT MONEY BTC':
        for userchange in userps:
            if userchange.reserv_pm_btc * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'PERFECT MONEY EUR':
        for userchange in userps:
            if userchange.reserv_pm_eur * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'PERFECT MONEY USD':
        for userchange in userps:
            if userchange.reserv_pm_usd * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'PAYPAL RUB':
        for userchange in userps:
            if userchange.reserv_paypal_rub * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'PAYPAL EUR':
        for userchange in userps:
            if userchange.reserv_paypal_eur * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'PAYPAL USD':
        for userchange in userps:
            if userchange.reserv_paypal_usd * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'SKRILL EUR':
        for userchange in userps:
            if userchange.reserv_skrill_eur * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'SKRILL USD':
        for userchange in userps:
            if userchange.reserv_skrill_usd * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'UMONEY RUB':
        for userchange in userps:
            if userchange.reserv_umoney_rub * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'BITCOIN':
        for userchange in userps:
            if userchange.reserv_btc * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'LITECOIN':
        for userchange in userps:
            if userchange.reserv_ltc * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'MONERO':
        for userchange in userps:
            if userchange.reserv_xmr * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'ETHEREUM CLASSIC':
        for userchange in userps:
            if userchange.reserv_etc * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'DASH':
        for userchange in userps:
            if userchange.reserv_dash * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'RIPPLE':
        for userchange in userps:
            if userchange.reserv_xrp * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'BITCOIN CASH':
        for userchange in userps:
            if userchange.reserv_bch * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    elif nameps == 'ETHEREUM':
        for userchange in userps:
            if userchange.reserv_eth * currencysort.base_currency > balanceps < userchange.balance:
                userlist.append(userchange)
    return userlist


# выбор победителя для пополнений
def depositsortcritery(userps, critery, nameps):
    rekvesites = ''
    usernameps = []
    userrandom = []
    base_comis = 99
    base_time = 1000
    if critery == 'БЫСТРАЯ ЗАЯВКА':
        for item in userps:
            requestps = RequestChange.objects.filter(request_userchange=item.username)
            if requestps:
                chartime = []
                for time in requestps:
                    if time.date_end_change and time.request_type == 'Заявка на пополнение':
                        timelimit = time.date_end_change - time.date_joined_change
                        timebase = timelimit.seconds / 60
                        chartime.append(timebase)
                if len(chartime) >= 1:
                    itemchar = float(0)
                    for ichar in chartime:
                        itemchar = itemchar + ichar
                    timedef = itemchar / float(len(chartime))
                    if timedef < base_time:
                        usernameps = item
                        base_time = timedef
                else:
                    userrandom.append(item)
            else:
                userrandom.append(item)

        if not usernameps:
            ranuser = random.randint(1, len(userrandom))
            ran = 1
            for r in userrandom:
                if ran == ranuser:
                    usernameps = r
                    break
                else:
                    ran += 1

        if nameps == 'СБЕРБАНК':
            base_comis = usernameps.comis_in_sberbank_rub
            rekvesites = usernameps.requsites_sberbank_rub
        elif nameps == 'ТИНЬКОФФ':
            base_comis = usernameps.comis_in_tinkoff_rub
            rekvesites = usernameps.requsites_tinkoff_rub
        elif nameps == 'АЛЬФА БАНК':
            base_comis = usernameps.comis_in_alfabank_rub
            rekvesites = usernameps.requsites_alfabank_rub
        elif nameps == 'ВТБ':
            base_comis = usernameps.comis_in_vtb_rub
            rekvesites = usernameps.requsites_vtb_rub
        elif nameps == 'РАЙФФАЙЗЕНБАНК':
            base_comis = usernameps.comis_in_raifaizen_rub
            rekvesites = usernameps.requsites_raifaizen_rub
        elif nameps == 'ОТКРЫТИЕ':
            base_comis = usernameps.comis_in_otkritie_rub
            rekvesites = usernameps.requsites_otkritie_rub
        elif nameps == 'ПСБ':
            base_comis = usernameps.comis_in_psb_rub
            rekvesites = usernameps.requsites_psb_rub
        elif nameps == 'ГАЗПРОМБАНК':
            base_comis = usernameps.comis_in_gazprombank_rub
            rekvesites = usernameps.requsites_gazprombank_rub
        elif nameps == 'РУССКИЙ СТАНДАРТ':
            base_comis = usernameps.comis_in_russtandart_rub
            rekvesites = usernameps.requsites_russtandart_rub
        elif nameps == 'РОССЕЛЬХОЗБАНК':
            base_comis = usernameps.comis_in_rosselhoz_rub
            rekvesites = usernameps.requsites_rosselhoz_rub
        elif nameps == 'ПОЧТА БАНК':
            base_comis = usernameps.comis_in_pochtabank_rub
            rekvesites = usernameps.requsites_pochtabank_rub
        elif nameps == 'РОСБАНК':
            base_comis = usernameps.comis_in_rosbank_rub
            rekvesites = usernameps.requsites_rosbank_rub
        elif nameps == 'РНКБ':
            base_comis = usernameps.comis_in_rnkb_rub
            rekvesites = usernameps.requsites_rnkb_rub
        elif nameps == 'МТС БАНК':
            base_comis = usernameps.comis_in_mtsbank_rub
            rekvesites = usernameps.requsites_mtsbank_rub
        elif nameps == 'QIWI RUB':
            base_comis = usernameps.comis_in_qiwi_rub
            rekvesites = usernameps.requsites_qiwi_rub
        elif nameps == 'QIWI USD':
            base_comis = usernameps.comis_in_qiwi_usd
            rekvesites = usernameps.requsites_qiwi_usd
        elif nameps == 'PAYEER RUB':
            base_comis = usernameps.comis_in_payeer_rub
            rekvesites = usernameps.requsites_payeer_rub
        elif nameps == 'PAYEER EUR':
            base_comis = usernameps.comis_in_payeer_eur
            rekvesites = usernameps.requsites_payeer_eur
        elif nameps == 'PAYEER USD':
            base_comis = usernameps.comis_in_payeer_usd
            rekvesites = usernameps.requsites_payeer_usd
        elif nameps == 'WEBMONEY RUB':
            base_comis = usernameps.comis_in_webmoney_rub
            rekvesites = usernameps.requsites_webmoney_rub
        elif nameps == 'WEBMONEY EUR':
            base_comis = usernameps.comis_in_webmoney_eur
            rekvesites = usernameps.requsites_webmoney_eur
        elif nameps == 'WEBMONEY USD':
            base_comis = usernameps.comis_in_webmoney_usd
            rekvesites = usernameps.requsites_webmoney_usd
        elif nameps == 'PERFECT MONEY BTC':
            base_comis = usernameps.comis_in_pm_btc
            rekvesites = usernameps.requsites_pm_btc
        elif nameps == 'PERFECT MONEY EUR':
            base_comis = usernameps.comis_in_pm_eur
            rekvesites = usernameps.requsites_pm_eur
        elif nameps == 'PERFECT MONEY USD':
            base_comis = usernameps.comis_in_pm_usd
            rekvesites = usernameps.requsites_pm_usd
        elif nameps == 'PAYPAL RUB':
            base_comis = usernameps.comis_in_paypal_rub
            rekvesites = usernameps.requsites_paypal_rub
        elif nameps == 'PAYPAL EUR':
            base_comis = usernameps.comis_in_paypal_eur
            rekvesites = usernameps.requsites_paypal_eur
        elif nameps == 'PAYPAL USD':
            base_comis = usernameps.comis_in_paypal_usd
            rekvesites = usernameps.requsites_paypal_usd
        elif nameps == 'SKRILL EUR':
            base_comis = usernameps.comis_in_skrill_eur
            rekvesites = usernameps.requsites_skrill_eur
        elif nameps == 'SKRILL USD':
            base_comis = usernameps.comis_in_skrill_usd
            rekvesites = usernameps.requsites_skrill_usd
        elif nameps == 'UMONEY RUB':
            base_comis = usernameps.comis_in_umoney_rub
            rekvesites = usernameps.requsites_umoney_rub
        elif nameps == 'BITCOIN':
            base_comis = usernameps.comis_in_btc
            rekvesites = usernameps.requsites_btc
        elif nameps == 'LITECOIN':
            base_comis = usernameps.comis_in_ltc
            rekvesites = usernameps.requsites_ltc
        elif nameps == 'MONERO':
            base_comis = usernameps.comis_in_xmr
            rekvesites = usernameps.requsites_xmr
        elif nameps == 'ETHEREUM CLASSIC':
            base_comis = usernameps.comis_in_etc
            rekvesites = usernameps.requsites_etc
        elif nameps == 'DASH':
            base_comis = usernameps.comis_in_dash
            rekvesites = usernameps.requsites_dash
        elif nameps == 'RIPPLE':
            base_comis = usernameps.comis_in_xrp
            rekvesites = usernameps.requsites_xrp
        elif nameps == 'BITCOIN CASH':
            base_comis = usernameps.comis_in_bch
            rekvesites = usernameps.requsites_bch
        elif nameps == 'ETHEREUM':
            base_comis = usernameps.comis_in_eth
            rekvesites = usernameps.requsites_eth

    elif critery == 'ВЫГОДНЫЙ КУРС':
        if nameps == 'СБЕРБАНК':
            for item in userps:
                if item.comis_in_sberbank_rub < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_sberbank_rub
                    base_comis = item.comis_in_sberbank_rub
        elif nameps == 'ТИНЬКОФФ':
            for item in userps:
                if item.comis_in_tinkoff_rub < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_tinkoff_rub
                    base_comis = item.comis_in_tinkoff_rub
        elif nameps == 'АЛЬФА БАНК':
            for item in userps:
                if item.comis_in_alfabank_rub < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_alfabank_rub
                    base_comis = item.comis_in_alfabank_rub
        elif nameps == 'ВТБ':
            for item in userps:
                if item.comis_in_vtb_rub < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_vtb_rub
                    base_comis = item.comis_in_vtb_rub
        elif nameps == 'РАЙФФАЙЗЕНБАНК':
            for item in userps:
                if item.comis_in_raifaizen_rub < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_raifaizen_rub
                    base_comis = item.comis_in_raifaizen_rub
        elif nameps == 'ОТКРЫТИЕ':
            for item in userps:
                if item.comis_in_otkritie_rub < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_otkritie_rub
                    base_comis = item.comis_in_otkritie_rub
        elif nameps == 'ПСБ':
            for item in userps:
                if item.comis_in_psb_rub < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_psb_rub
                    base_comis = item.comis_in_psb_rub
        elif nameps == 'ГАЗПРОМБАНК':
            for item in userps:
                if item.comis_in_gazprombank_rub < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_gazprombank_rub
                    base_comis = item.comis_in_gazprombank_rub
        elif nameps == 'РУССКИЙ СТАНДАРТ':
            for item in userps:
                if item.comis_in_russtandart_rub < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_russtandart_rub
                    base_comis = item.comis_in_russtandart_rub
        elif nameps == 'РОССЕЛЬХОЗБАНК':
            for item in userps:
                if item.comis_in_rosselhoz_rub < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_rosselhoz_rub
                    base_comis = item.comis_in_rosselhoz_rub
        elif nameps == 'ПОЧТА БАНК':
            for item in userps:
                if item.comis_in_pochtabank_rub < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_pochtabank_rub
                    base_comis = item.comis_in_pochtabank_rub
        elif nameps == 'РОСБАНК':
            for item in userps:
                if item.comis_in_rosbank_rub < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_rosbank_rub
                    base_comis = item.comis_in_rosbank_rub
        elif nameps == 'РНКБ':
            for item in userps:
                if item.comis_in_rnkb_rub < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_rnkb_rub
                    base_comis = item.comis_in_rnkb_rub
        elif nameps == 'МТС БАНК':
            for item in userps:
                if item.comis_in_mtsbank_rub < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_mtsbank_rub
                    base_comis = item.comis_in_mtsbank_rub
        elif nameps == 'QIWI RUB':
            for item in userps:
                if item.comis_in_qiwi_rub < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_qiwi_rub
                    base_comis = item.comis_in_qiwi_rub
        elif nameps == 'QIWI USD':
            for item in userps:
                if item.comis_in_qiwi_usd < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_qiwi_usd
                    base_comis = item.comis_in_qiwi_usd
        elif nameps == 'PAYEER RUB':
            for item in userps:
                if item.comis_in_payeer_rub < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_payeer_rub
                    base_comis = item.comis_in_payeer_rub
        elif nameps == 'PAYEER EUR':
            for item in userps:
                if item.comis_in_payeer_eur < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_payeer_eur
                    base_comis = item.comis_in_payeer_eur
        elif nameps == 'PAYEER USD':
            for item in userps:
                if item.comis_in_payeer_usd < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_payeer_usd
                    base_comis = item.comis_in_payeer_usd
        elif nameps == 'WEBMONEY RUB':
            for item in userps:
                if item.comis_in_webmoney_rub < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_webmoney_rub
                    base_comis = item.comis_in_webmoney_rub
        elif nameps == 'WEBMONEY EUR':
            for item in userps:
                if item.comis_in_webmoney_eur < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_webmoney_eur
                    base_comis = item.comis_in_webmoney_eur
        elif nameps == 'WEBMONEY USD':
            for item in userps:
                if item.comis_in_webmoney_usd < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_webmoney_usd
                    base_comis = item.comis_in_webmoney_usd
        elif nameps == 'PERFECT MONEY BTC':
            for item in userps:
                if item.comis_in_pm_btc < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_pm_btc
                    base_comis = item.comis_in_pm_btc
        elif nameps == 'PERFECT MONEY EUR':
            for item in userps:
                if item.comis_in_pm_eur < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_pm_eur
                    base_comis = item.comis_in_pm_eur
        elif nameps == 'PERFECT MONEY USD':
            for item in userps:
                if item.comis_in_pm_usd < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_pm_usd
                    base_comis = item.comis_in_pm_usd
        elif nameps == 'PAYPAL RUB':
            for item in userps:
                if item.comis_in_paypal_rub < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_paypal_rub
                    base_comis = item.comis_in_paypal_rub
        elif nameps == 'PAYPAL EUR':
            for item in userps:
                if item.comis_in_paypal_eur < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_paypal_eur
                    base_comis = item.comis_in_paypal_eur
        elif nameps == 'PAYPAL USD':
            for item in userps:
                if item.comis_in_paypal_usd < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_paypal_usd
                    base_comis = item.comis_in_paypal_usd
        elif nameps == 'SKRILL EUR':
            for item in userps:
                if item.comis_in_skrill_eur < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_skrill_eur
                    base_comis = item.comis_in_skrill_eur
        elif nameps == 'SKRILL USD':
            for item in userps:
                if item.comis_in_skrill_usd < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_skrill_usd
                    base_comis = item.comis_in_skrill_usd
        elif nameps == 'UMONEY RUB':
            for item in userps:
                if item.comis_in_umoney_rub < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_umoney_rub
                    base_comis = item.comis_in_umoney_rub
        elif nameps == 'BITCOIN':
            for item in userps:
                if item.comis_in_btc < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_btc
                    base_comis = item.comis_in_btc
        elif nameps == 'LITECOIN':
            for item in userps:
                if item.comis_in_ltc < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_ltc
                    base_comis = item.comis_in_ltc
        elif nameps == 'MONERO':
            for item in userps:
                if item.comis_in_xmr < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_xmr
                    base_comis = item.comis_in_xmr
        elif nameps == 'ETHEREUM CLASSIC':
            for item in userps:
                if item.comis_in_etc < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_etc
                    base_comis = item.comis_in_etc
        elif nameps == 'DASH':
            for item in userps:
                if item.comis_in_dash < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_dash
                    base_comis = item.comis_in_dash
        elif nameps == 'RIPPLE':
            for item in userps:
                if item.comis_in_xrp < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_xrp
                    base_comis = item.comis_in_xrp
        elif nameps == 'BITCOIN CASH':
            for item in userps:
                if item.comis_in_bch < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_bch
                    base_comis = item.comis_in_bch
        elif nameps == 'ETHEREUM':
            for item in userps:
                if item.comis_in_eth < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_eth
                    base_comis = item.comis_in_eth
    return {'usernameps': usernameps, 'base_comis': base_comis, 'rekvesites': rekvesites}


# выбор победителя для вывода
def widthsortcritery(userps, critery, nameps, valuteps, balanceps):
    usernameps = []
    userrandom = []
    base_comis = 99
    base_time = 1000
    currencysort = CurrencyCBRF.objects.get(name_currency=valuteps)
    if critery == 'БЫСТРАЯ ЗАЯВКА':
        for item in userps:
            requestps = RequestChange.objects.filter(request_userchange=item.username)
            if requestps:
                chartime = []
                for time in requestps:
                    if time.date_end_change and time.request_type == 'Заявка на вывод':
                        timelimit = time.date_end_change - time.date_joined_change
                        timebase = timelimit.seconds / 60
                        chartime.append(timebase)
                if len(chartime) >= 1:
                    itemchar = float(0)
                    for ichar in chartime:
                        itemchar = itemchar + ichar
                    timedef = itemchar / float(len(chartime))
                    if timedef < base_time:
                        usernameps = item
                        base_time = timedef
                else:
                    userrandom.append(item)
            else:
                userrandom.append(item)

        if not usernameps:
            ranuser = random.randint(1, len(userrandom))
            ran = 1
            for r in userrandom:
                if ran == ranuser:
                    usernameps = r
                    break
                else:
                    ran += 1

        if nameps == 'СБЕРБАНК':
            usernameps.reserv_sberbank_rub -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_sberbank_rub
        elif nameps == 'ТИНЬКОФФ':
            usernameps.reserv_tinkoff_rub -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_tinkoff_rub
        elif nameps == 'АЛЬФА БАНК':
            usernameps.reserv_alfabank_rub -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_alfabank_rub
        elif nameps == 'ВТБ':
            usernameps.reserv_vtb_rub -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_vtb_rub
        elif nameps == 'РАЙФФАЙЗЕНБАНК':
            usernameps.reserv_raifaizen_rub -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_raifaizen_rub
        elif nameps == 'ОТКРЫТИЕ':
            usernameps.reserv_otkritie_rub -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_otkritie_rub
        elif nameps == 'ПСБ':
            usernameps.reserv_psb_rub -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_psb_rub
        elif nameps == 'ГАЗПРОМБАНК':
            usernameps.reserv_gazprombank_rub -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_gazprombank_rub
        elif nameps == 'РУССКИЙ СТАНДАРТ':
            usernameps.reserv_russtandart_rub -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_russtandart_rub
        elif nameps == 'РОССЕЛЬХОЗБАНК':
            usernameps.reserv_rosselhoz_rub -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_rosselhoz_rub
        elif nameps == 'ПОЧТА БАНК':
            usernameps.reserv_pochtabank_rub -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_pochtabank_rub
        elif nameps == 'РОСБАНК':
            usernameps.reserv_rosbank_rub -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_rosbank_rub
        elif nameps == 'РНКБ':
            usernameps.reserv_rnkb_rub -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_rnkb_rub
        elif nameps == 'МТС БАНК':
            usernameps.reserv_mtsbank_rub -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_mtsbank_rub
        elif nameps == 'QIWI RUB':
            usernameps.reserv_qiwi_rub -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_qiwi_rub
        elif nameps == 'QIWI USD':
            usernameps.reserv_qiwi_usd -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_qiwi_usd
        elif nameps == 'PAYEER RUB':
            usernameps.reserv_payeer_rub -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_payeer_rub
        elif nameps == 'PAYEER EUR':
            usernameps.reserv_payeer_eur -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_payeer_eur
        elif nameps == 'PAYEER USD':
            usernameps.reserv_payeer_usd -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_payeer_usd
        elif nameps == 'WEBMONEY RUB':
            usernameps.reserv_webmoney_rub -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_webmoney_rub
        elif nameps == 'WEBMONEY EUR':
            usernameps.reserv_webmoney_eur -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_webmoney_eur
        elif nameps == 'WEBMONEY USD':
            usernameps.reserv_webmoney_usd -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_webmoney_usd
        elif nameps == 'PERFECT MONEY BTC':
            usernameps.reserv_pm_btc -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_pm_btc
        elif nameps == 'PERFECT MONEY EUR':
            usernameps.reserv_pm_eur -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_pm_eur
        elif nameps == 'PERFECT MONEY USD':
            usernameps.reserv_pm_usd -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_pm_usd
        elif nameps == 'PAYPAL RUB':
            usernameps.reserv_paypal_rub -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_paypal_rub
        elif nameps == 'PAYPAL EUR':
            usernameps.reserv_paypal_eur -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_paypal_eur
        elif nameps == 'PAYPAL USD':
            usernameps.reserv_paypal_usd -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_paypal_usd
        elif nameps == 'SKRILL EUR':
            usernameps.reserv_skrill_eur -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_skrill_eur
        elif nameps == 'SKRILL USD':
            usernameps.reserv_skrill_usd -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_skrill_usd
        elif nameps == 'UMONEY RUB':
            usernameps.reserv_umoney_rub -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_umoney_rub
        elif nameps == 'BITCOIN':
            usernameps.reserv_btc -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_btc
        elif nameps == 'LITECOIN':
            usernameps.reserv_ltc -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_ltc
        elif nameps == 'MONERO':
            usernameps.reserv_xmr -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_xmr
        elif nameps == 'ETHEREUM CLASSIC':
            usernameps.reserv_etc -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_etc
        elif nameps == 'DASH':
            usernameps.reserv_dash -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_dash
        elif nameps == 'RIPPLE':
            usernameps.reserv_xrp -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_xrp
        elif nameps == 'BITCOIN CASH':
            usernameps.reserv_bch -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_bch
        elif nameps == 'ETHEREUM':
            usernameps.reserv_eth -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_eth
        usernameps.save()

    elif critery == 'ВЫГОДНЫЙ КУРС':
        if nameps == 'СБЕРБАНК':
            for item in userps:
                if item.comis_out_sberbank_rub < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_sberbank_rub
            usernameps.reserv_sberbank_rub -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'ТИНЬКОФФ':
            for item in userps:
                if item.comis_out_tinkoff_rub < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_tinkoff_rub
            usernameps.reserv_tinkoff_rub -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'АЛЬФА БАНК':
            for item in userps:
                if item.comis_out_alfabank_rub < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_alfabank_rub
            usernameps.reserv_alfabank_rub -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'ВТБ':
            for item in userps:
                if item.comis_out_vtb_rub < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_vtb_rub
            usernameps.reserv_vtb_rub -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'РАЙФФАЙЗЕНБАНК':
            for item in userps:
                if item.comis_out_raifaizen_rub < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_raifaizen_rub
            usernameps.reserv_raifaizen_rub -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'ОТКРЫТИЕ':
            for item in userps:
                if item.comis_out_otkritie_rub < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_otkritie_rub
            usernameps.reserv_otkritie_rub -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'ПСБ':
            for item in userps:
                if item.comis_out_psb_rub < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_psb_rub
            usernameps.reserv_psb_rub -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'ГАЗПРОМБАНК':
            for item in userps:
                if item.comis_out_gazprombank_rub < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_gazprombank_rub
            usernameps.reserv_gazprombank_rub -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'РУССКИЙ СТАНДАРТ':
            for item in userps:
                if item.comis_out_russtandart_rub < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_russtandart_rub
            usernameps.reserv_russtandart_rub -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'РОССЕЛЬХОЗБАНК':
            for item in userps:
                if item.comis_out_rosselhoz_rub < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_rosselhoz_rub
            usernameps.reserv_rosselhoz_rub -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'ПОЧТА БАНК':
            for item in userps:
                if item.comis_out_pochtabank_rub < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_pochtabank_rub
            usernameps.reserv_pochtabank_rub -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'РОСБАНК':
            for item in userps:
                if item.comis_out_rosbank_rub < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_rosbank_rub
            usernameps.reserv_rosbank_rub -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'РНКБ':
            for item in userps:
                if item.comis_out_rnkb_rub < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_rnkb_rub
            usernameps.reserv_rnkb_rub -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'МТС БАНК':
            for item in userps:
                if item.comis_out_mtsbank_rub < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_mtsbank_rub
            usernameps.reserv_mtsbank_rub -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'QIWI RUB':
            for item in userps:
                if item.comis_out_qiwi_rub < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_qiwi_rub
            usernameps.reserv_qiwi_rub -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'QIWI USD':
            for item in userps:
                if item.comis_out_qiwi_usd < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_qiwi_usd
            usernameps.reserv_qiwi_usd -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'PAYEER RUB':
            for item in userps:
                if item.comis_out_payeer_rub < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_payeer_rub
            usernameps.reserv_payeer_rub -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'PAYEER EUR':
            for item in userps:
                if item.comis_out_payeer_eur < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_payeer_eur
            usernameps.reserv_payeer_eur -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'PAYEER USD':
            for item in userps:
                if item.comis_out_payeer_usd < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_payeer_usd
            usernameps.reserv_payeer_usd -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'WEBMONEY RUB':
            for item in userps:
                if item.comis_out_webmoney_rub < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_webmoney_rub
            usernameps.reserv_webmoney_rub -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'WEBMONEY EUR':
            for item in userps:
                if item.comis_out_webmoney_eur < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_webmoney_eur
            usernameps.reserv_webmoney_eur -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'WEBMONEY USD':
            for item in userps:
                if item.comis_out_webmoney_usd < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_webmoney_usd
            usernameps.reserv_webmoney_usd -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'PERFECT MONEY BTC':
            for item in userps:
                if item.comis_out_pm_btc < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_pm_btc
            usernameps.reserv_pm_btc -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'PERFECT MONEY EUR':
            for item in userps:
                if item.comis_out_pm_eur < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_pm_eur
            usernameps.reserv_pm_eur -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'PERFECT MONEY USD':
            for item in userps:
                if item.comis_out_pm_usd < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_pm_usd
            usernameps.reserv_pm_usd -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'PAYPAL RUB':
            for item in userps:
                if item.comis_out_paypal_rub < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_paypal_rub
            usernameps.reserv_paypal_rub -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'PAYPAL EUR':
            for item in userps:
                if item.comis_out_paypal_eur < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_paypal_eur
            usernameps.reserv_paypal_eur -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'PAYPAL USD':
            for item in userps:
                if item.comis_out_paypal_usd < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_paypal_usd
            usernameps.reserv_paypal_usd -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'SKRILL EUR':
            for item in userps:
                if item.comis_out_skrill_eur < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_skrill_eur
            usernameps.reserv_skrill_eur -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'SKRILL USD':
            for item in userps:
                if item.comis_out_skrill_usd < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_skrill_usd
            usernameps.reserv_skrill_usd -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'UMONEY RUB':
            for item in userps:
                if item.comis_out_umoney_rub < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_umoney_rub
            usernameps.reserv_umoney_rub -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'BITCOIN':
            for item in userps:
                if item.comis_out_btc < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_btc
            usernameps.reserv_btc -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'LITECOIN':
            for item in userps:
                if item.comis_out_ltc < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_ltc
            usernameps.reserv_ltc -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'MONERO':
            for item in userps:
                if item.comis_out_xmr < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_xmr
            usernameps.reserv_xmr -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'ETHEREUM CLASSIC':
            for item in userps:
                if item.comis_out_etc < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_etc
            usernameps.reserv_etc -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'DASH':
            for item in userps:
                if item.comis_out_dash < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_dash
            usernameps.reserv_dash -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'RIPPLE':
            for item in userps:
                if item.comis_out_xrp < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_xrp
            usernameps.reserv_xrp -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'BITCOIN CASH':
            for item in userps:
                if item.comis_out_bch < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_bch
            usernameps.reserv_bch -= balanceps / currencysort.base_currency
            usernameps.save()
        elif nameps == 'ETHEREUM':
            for item in userps:
                if item.comis_out_eth < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_eth
            usernameps.reserv_eth -= balanceps / currencysort.base_currency
            usernameps.save()
    return {'usernameps': usernameps, 'base_comis': base_comis}


# вывод активности пс. Количество
def activepsuser(usernameactiveps):
    userps = CustomUser.objects.get(username=usernameactiveps)
    activepsin = 0
    noactivepsin = 0
    activepsout = 0
    noactivepsout = 0
    if userps.active_in_sberbank_rub == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_psb_rub == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_tinkoff_rub == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_gazprombank_rub == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_alfabank_rub == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_russtandart_rub == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_vtb_rub == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_rosselhoz_rub == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_raifaizen_rub == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_otkritie_rub == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_pochtabank_rub == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_rnkb_rub == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_rosbank_rub == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_mtsbank_rub == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_qiwi_rub == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_qiwi_usd == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_payeer_rub == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_payeer_usd == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_payeer_eur == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_webmoney_rub == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_webmoney_usd == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_webmoney_eur == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_pm_btc == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_pm_usd == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_pm_eur == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_skrill_eur == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_skrill_usd == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_paypal_rub == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_paypal_usd == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_paypal_eur == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_umoney_rub == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_btc == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_xrp == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_ltc == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_bch == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_xmr == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_eth == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_etc == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_in_dash == 1:
        activepsin += 1
    else:
        noactivepsin += 1
    if userps.active_out_sberbank_rub == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_psb_rub == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_tinkoff_rub == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_gazprombank_rub == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_alfabank_rub == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_russtandart_rub == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_vtb_rub == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_rosselhoz_rub == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_raifaizen_rub == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_otkritie_rub == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_pochtabank_rub == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_rnkb_rub == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_rosbank_rub == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_mtsbank_rub == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_qiwi_rub == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_qiwi_usd == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_payeer_rub == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_payeer_usd == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_payeer_eur == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_webmoney_rub == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_webmoney_usd == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_webmoney_eur == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_pm_btc == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_pm_usd == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_pm_eur == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_skrill_eur == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_skrill_usd == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_paypal_rub == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_paypal_usd == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_paypal_eur == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_umoney_rub == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_btc == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_xrp == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_ltc == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_bch == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_xmr == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_eth == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_etc == 1:
        activepsout += 1
    else:
        noactivepsout += 1
    if userps.active_out_dash == 1:
        activepsout += 1
    else:
        noactivepsout += 1

    return {'activepsin': activepsin, 'activepsout': activepsout, 'noactivepsin': noactivepsin, 'noactivepsout': noactivepsout}


# вывод активных заявок обработчика
def requestchangeon(usernamereq):
    requesttargetin = 0
    requesttargetout = 0
    change = RequestChange.objects.filter(request_userchange=usernamereq)
    for i in change:
        if i.request_type == 'Заявка на пополнение' and i.request_status == 'Оплачена':
            requesttargetin += 1
        elif i.request_type == 'Заявка на вывод' and i.request_status == 'Ожидает оплаты':
            requesttargetout += 1
    requesttotal = requesttargetin + requesttargetout
    return {'requesttargetin': requesttargetin, 'requesttargetout': requesttargetout, 'requesttotal': requesttotal}


# вывод активных заявок кошелька
def walrequestchangeon(usernamereq):
    requesttargetin = 0
    requesttargetout = 0
    change = RequestChange.objects.filter(request_user=usernamereq)
    for i in change:
        if i.request_type == 'Заявка на пополнение' and (i.request_status == 'Ожидает оплаты' or i.request_status == 'Оплачена'):
            requesttargetin += 1
        elif i.request_type == 'Заявка на вывод' and i.request_status == 'Ожидает оплаты':
            requesttargetout += 1
    requesttotal = requesttargetin + requesttargetout
    return {'requesttargetin': requesttargetin, 'requesttargetout': requesttargetout, 'requesttotal': requesttotal}


# данные по дням прибыль обменника для графика
def dailyprofitcount(usernamedailyprofit):
    staticdailypriftlist = StaticDailyProfit.objects.filter(dailyprofit_user=usernamedailyprofit.username)
    staticlist = staticdailypriftlist.order_by('dailyprofit_date')
    staticdata = []
    staticvalue = []
    staticvaluereset = float(0)
    valuedate = None
    valuedatereset = None
    datenow = date.today()
    lenstaticlistreset = 1
    if len(staticlist) > 1:
        for staticone in staticlist:
            if not valuedate:
                valuedate = staticone.dailyprofit_date
                valuedatereset = staticone.dailyprofit_date + timedelta(1)
                staticvaluereset += float(staticone.dailyprofit_value)
                lenstaticlistreset += 1
            else:
                if staticone.dailyprofit_date == valuedate:
                    if lenstaticlistreset < len(staticlist):
                        staticvaluereset += float(staticone.dailyprofit_value)
                        lenstaticlistreset += 1
                    else:
                        staticvaluereset += float(staticone.dailyprofit_value)
                        staticdata.append(str(valuedate))
                        staticvalue.append(round(staticvaluereset, 2))
                        valuedatereset = staticone.dailyprofit_date + timedelta(1)
                else:
                    if staticone.dailyprofit_date == valuedatereset:
                        staticdata.append(str(valuedate))
                        staticvalue.append(round(staticvaluereset, 2))
                        if lenstaticlistreset < len(staticlist):
                            staticvaluereset = float(staticone.dailyprofit_value)
                            valuedate = staticone.dailyprofit_date
                            valuedatereset = staticone.dailyprofit_date + timedelta(1)
                            lenstaticlistreset += 1
                        else:
                            staticdata.append(str(staticone.dailyprofit_date))
                            staticvalue.append(float(round(staticone.dailyprofit_value, 2)))
                            valuedatereset = staticone.dailyprofit_date + timedelta(1)
                    elif staticone.dailyprofit_date > valuedatereset:
                        staticdata.append(str(valuedate))
                        staticvalue.append(round(staticvaluereset, 2))
                        while staticone.dailyprofit_date != valuedatereset:
                            staticdata.append(str(valuedatereset))
                            staticvalue.append(float(0))
                            valuedatereset += timedelta(1)
                        if lenstaticlistreset < len(staticlist):
                            staticvaluereset = float(staticone.dailyprofit_value)
                            valuedate = staticone.dailyprofit_date
                            valuedatereset = staticone.dailyprofit_date + timedelta(1)
                            lenstaticlistreset += 1
                        else:
                            staticdata.append(str(staticone.dailyprofit_date))
                            staticvalue.append(float(round(staticone.dailyprofit_value, 2)))
                            valuedatereset = staticone.dailyprofit_date + timedelta(1)
        if valuedatereset <= datenow:
            while valuedatereset <= datenow:
                staticdata.append(str(valuedatereset))
                staticvalue.append(float(0))
                valuedatereset += timedelta(1)
    if len(staticlist) == 1:
        for staticone in staticlist:
            staticdata.append(str(staticone.dailyprofit_date))
            staticvalue.append(float(staticone.dailyprofit_value))
            valuedatereset = staticone.dailyprofit_date + timedelta(1)
        if valuedatereset <= datenow:
            while valuedatereset <= datenow:
                staticdata.append(str(valuedatereset))
                staticvalue.append(float(0))
                valuedatereset += timedelta(1)
    return {'staticdata': staticdata, 'staticvalue': staticvalue}


# вывод статистики прибыли, ежедневно, общая
def totalprofitstatic(usernametotalstatic):
    totalprofitstaticlist = StaticDailyProfit.objects.filter(dailyprofit_user=usernametotalstatic.username)
    inrequestl = totalprofitstaticlist.filter(dailyprofit_date=date.today())
    dailyprofit = 0
    totalprofit = 0
    if inrequestl:
        for iteml in inrequestl:
            dailyprofit += iteml.dailyprofit_value
    if totalprofitstaticlist:
        for item in totalprofitstaticlist:
            totalprofit += item.dailyprofit_value
    return {'dailyprofit': float(round(dailyprofit, 2)), 'totalprofit': float(round(totalprofit, 2))}


# вывод исполненых заявок
def requesttotal(usernamerequesttotal):
    requestuserlist = RequestChange.objects.filter(request_userchange=usernamerequesttotal.username)
    inrequestl = requestuserlist.filter(date_end_change__date=date.today())
    inrequest = 0
    inrequesttotal = 0
    widthrequest = 0
    widthrequesttotal = 0
    if inrequestl:
        for iteml in inrequestl:
            if iteml.request_type == 'Заявка на пополнение':
                inrequest += 1
            if iteml.request_type == 'Заявка на вывод':
                widthrequest += 1
    if requestuserlist:
        for item in requestuserlist:
            if item.request_type == 'Заявка на пополнение' and item.date_end_change:
                inrequesttotal += 1
            if item.request_type == 'Заявка на вывод' and item.date_end_change:
                widthrequesttotal += 1
    return {'inrequest': inrequest, 'inrequesttotal': inrequesttotal, 'widthrequest': widthrequest, 'widthrequesttotal': widthrequesttotal}


# активные пс на пополнение и резерв(запас -3%) у обменников
def active_deposit_ps_global():
    list_change = CustomUser.objects.filter(userid__custuserid='Владелец Обменника', is_active_change=1)
    currency = CurrencyCBRF.objects.all()
    list_active_change_ps = {
        'sberbank_rub': False, 'psb_rub': False, 'tinkoff_rub': False, 'gazprombank_rub': False, 'alfabank_rub': False,
        'russtandart_rub': False, 'vtb_rub': False, 'rosselhoz_rub': False, 'raifaizen_rub': False,
        'otkritie_rub': False, 'pochtabank_rub': False, 'rnkb_rub': False, 'rosbank_rub': False, 'mtsbank_rub': False,
        'qiwi_rub': False, 'qiwi_usd': False, 'payeer_rub': False, 'payeer_usd': False, 'payeer_eur': False,
        'webmoney_rub': False, 'webmoney_usd': False, 'webmoney_eur': False, 'pm_btc': False, 'pm_usd': False,
        'pm_eur': False, 'skrill_eur': False, 'skrill_usd': False, 'paypal_rub': False, 'paypal_usd': False,
        'paypal_eur': False, 'umoney_rub': False, 'btc': False, 'xrp': False, 'ltc': False, 'bch': False,
        'xmr': False, 'eth': False, 'etc': False, 'dash': False
    }
    list_active_reserve_ps = {
        'sberbank_rub': 0, 'psb_rub': 0, 'tinkoff_rub': 0, 'gazprombank_rub': 0, 'alfabank_rub': 0, 'russtandart_rub': 0,
        'vtb_rub': 0, 'rosselhoz_rub': 0, 'raifaizen_rub': 0, 'otkritie_rub': 0, 'pochtabank_rub': 0, 'rnkb_rub': 0,
        'rosbank_rub': 0, 'mtsbank_rub': 0, 'qiwi_rub': 0, 'qiwi_usd': 0, 'payeer_rub': 0, 'payeer_usd': 0,
        'payeer_eur': 0, 'webmoney_rub': 0, 'webmoney_usd': 0, 'webmoney_eur': 0, 'pm_btc': 0, 'pm_usd': 0,
        'pm_eur': 0, 'skrill_eur': 0, 'skrill_usd': 0, 'paypal_rub': 0, 'paypal_usd': 0, 'paypal_eur': 0, 'umoney_rub': 0,
        'btc': 0, 'xrp': 0, 'ltc': 0, 'bch': 0, 'xmr': 0, 'eth': 0, 'etc': 0, 'dash': 0
    }
    for change in list_change:
        if RangeSumDeposit.objects.filter(deposit_range_username=change).exists():
            if change.active_in_sberbank_rub == 1:
                currencyget = currency.get(name_currency='RUB').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['sberbank_rub']:
                    list_active_reserve_ps['sberbank_rub'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['sberbank_rub'] = True
            if change.active_in_psb_rub == 1:
                currencyget = currency.get(name_currency='RUB').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['psb_rub']:
                    list_active_reserve_ps['psb_rub'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['psb_rub'] = True
            if change.active_in_tinkoff_rub == 1:
                currencyget = currency.get(name_currency='RUB').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['tinkoff_rub']:
                    list_active_reserve_ps['tinkoff_rub'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['tinkoff_rub'] = True
            if change.active_in_gazprombank_rub == 1:
                currencyget = currency.get(name_currency='RUB').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['gazprombank_rub']:
                    list_active_reserve_ps['gazprombank_rub'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['gazprombank_rub'] = True
            if change.active_in_alfabank_rub == 1:
                currencyget = currency.get(name_currency='RUB').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['alfabank_rub']:
                    list_active_reserve_ps['alfabank_rub'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['alfabank_rub'] = True
            if change.active_in_russtandart_rub == 1:
                currencyget = currency.get(name_currency='RUB').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['russtandart_rub']:
                    list_active_reserve_ps['russtandart_rub'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['russtandart_rub'] = True
            if change.active_in_vtb_rub == 1:
                currencyget = currency.get(name_currency='RUB').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['vtb_rub']:
                    list_active_reserve_ps['vtb_rub'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['vtb_rub'] = True
            if change.active_in_rosselhoz_rub == 1:
                currencyget = currency.get(name_currency='RUB').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['rosselhoz_rub']:
                    list_active_reserve_ps['rosselhoz_rub'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['rosselhoz_rub'] = True
            if change.active_in_raifaizen_rub == 1:
                currencyget = currency.get(name_currency='RUB').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['raifaizen_rub']:
                    list_active_reserve_ps['raifaizen_rub'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['raifaizen_rub'] = True
            if change.active_in_otkritie_rub == 1:
                currencyget = currency.get(name_currency='RUB').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['otkritie_rub']:
                    list_active_reserve_ps['otkritie_rub'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['otkritie_rub'] = True
            if change.active_in_pochtabank_rub == 1:
                currencyget = currency.get(name_currency='RUB').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['pochtabank_rub']:
                    list_active_reserve_ps['pochtabank_rub'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['pochtabank_rub'] = True
            if change.active_in_rnkb_rub == 1:
                currencyget = currency.get(name_currency='RUB').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['rnkb_rub']:
                    list_active_reserve_ps['rnkb_rub'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['rnkb_rub'] = True
            if change.active_in_rosbank_rub == 1:
                currencyget = currency.get(name_currency='RUB').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['rosbank_rub']:
                    list_active_reserve_ps['rosbank_rub'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['rosbank_rub'] = True
            if change.active_in_mtsbank_rub == 1:
                currencyget = currency.get(name_currency='RUB').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['mtsbank_rub']:
                    list_active_reserve_ps['mtsbank_rub'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['mtsbank_rub'] = True
            if change.active_in_qiwi_rub == 1:
                currencyget = currency.get(name_currency='RUB').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['qiwi_rub']:
                    list_active_reserve_ps['qiwi_rub'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['qiwi_rub'] = True
            if change.active_in_qiwi_usd == 1:
                currencyget = currency.get(name_currency='USD').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['qiwi_usd']:
                    list_active_reserve_ps['qiwi_usd'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['qiwi_usd'] = True
            if change.active_in_payeer_rub == 1:
                currencyget = currency.get(name_currency='RUB').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['payeer_rub']:
                    list_active_reserve_ps['payeer_rub'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['payeer_rub'] = True
            if change.active_in_payeer_usd == 1:
                currencyget = currency.get(name_currency='USD').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['payeer_usd']:
                    list_active_reserve_ps['payeer_usd'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['payeer_usd'] = True
            if change.active_in_payeer_eur == 1:
                currencyget = currency.get(name_currency='EUR').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['payeer_eur']:
                    list_active_reserve_ps['payeer_eur'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['payeer_eur'] = True
            if change.active_in_webmoney_rub == 1:
                currencyget = currency.get(name_currency='RUB').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['webmoney_rub']:
                    list_active_reserve_ps['webmoney_rub'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['webmoney_rub'] = True
            if change.active_in_webmoney_usd == 1:
                currencyget = currency.get(name_currency='USD').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['webmoney_usd']:
                    list_active_reserve_ps['webmoney_usd'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['webmoney_usd'] = True
            if change.active_in_webmoney_eur == 1:
                currencyget = currency.get(name_currency='EUR').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['webmoney_eur']:
                    list_active_reserve_ps['webmoney_eur'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['webmoney_eur'] = True
            if change.active_in_pm_btc == 1:
                currencyget = currency.get(name_currency='BTC').base_currency
                if round(change.balance/currencyget, 8) > list_active_reserve_ps['pm_btc']:
                    list_active_reserve_ps['pm_btc'] = round((change.balance/currencyget)-(((change.balance/currencyget)/100)*3), 8)
                    list_active_change_ps['pm_btc'] = True
            if change.active_in_pm_usd == 1:
                currencyget = currency.get(name_currency='USD').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['pm_usd']:
                    list_active_reserve_ps['pm_usd'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['pm_usd'] = True
            if change.active_in_pm_eur == 1:
                currencyget = currency.get(name_currency='EUR').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['pm_eur']:
                    list_active_reserve_ps['pm_eur'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['pm_eur'] = True
            if change.active_in_skrill_eur == 1:
                currencyget = currency.get(name_currency='EUR').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['skrill_eur']:
                    list_active_reserve_ps['skrill_eur'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['skrill_eur'] = True
            if change.active_in_skrill_usd == 1:
                currencyget = currency.get(name_currency='USD').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['skrill_usd']:
                    list_active_reserve_ps['skrill_usd'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['skrill_usd'] = True
            if change.active_in_paypal_rub == 1:
                currencyget = currency.get(name_currency='RUB').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['paypal_rub']:
                    list_active_reserve_ps['paypal_rub'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['paypal_rub'] = True
            if change.active_in_paypal_usd == 1:
                currencyget = currency.get(name_currency='USD').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['paypal_usd']:
                    list_active_reserve_ps['paypal_usd'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['paypal_usd'] = True
            if change.active_in_paypal_eur == 1:
                currencyget = currency.get(name_currency='EUR').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['paypal_eur']:
                    list_active_reserve_ps['paypal_eur'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['paypal_eur'] = True
            if change.active_in_umoney_rub == 1:
                currencyget = currency.get(name_currency='RUB').base_currency
                if int(change.balance/currencyget) > list_active_reserve_ps['umoney_rub']:
                    list_active_reserve_ps['umoney_rub'] = int((change.balance/currencyget)-(((change.balance/currencyget)/100)*3))
                    list_active_change_ps['umoney_rub'] = True
            if change.active_in_btc == 1:
                currencyget = currency.get(name_currency='BTC').base_currency
                if round(change.balance/currencyget, 8) > list_active_reserve_ps['btc']:
                    list_active_reserve_ps['btc'] = round((change.balance/currencyget)-(((change.balance/currencyget)/100)*3), 8)
                    list_active_change_ps['btc'] = True
            if change.active_in_xrp == 1:
                currencyget = currency.get(name_currency='XRP').base_currency
                if round(change.balance/currencyget, 8) > list_active_reserve_ps['xrp']:
                    list_active_reserve_ps['xrp'] = round((change.balance/currencyget)-(((change.balance/currencyget)/100)*3), 8)
                    list_active_change_ps['xrp'] = True
            if change.active_in_ltc == 1:
                currencyget = currency.get(name_currency='LTC').base_currency
                if round(change.balance/currencyget, 8) > list_active_reserve_ps['ltc']:
                    list_active_reserve_ps['ltc'] = round((change.balance/currencyget)-(((change.balance/currencyget)/100)*3), 8)
                    list_active_change_ps['ltc'] = True
            if change.active_in_bch == 1:
                currencyget = currency.get(name_currency='BCH').base_currency
                if round(change.balance/currencyget, 8) > list_active_reserve_ps['bch']:
                    list_active_reserve_ps['bch'] = round((change.balance/currencyget)-(((change.balance/currencyget)/100)*3), 8)
                    list_active_change_ps['bch'] = True
            if change.active_in_xmr == 1:
                currencyget = currency.get(name_currency='XMR').base_currency
                if round(change.balance/currencyget, 8) > list_active_reserve_ps['xmr']:
                    list_active_reserve_ps['xmr'] = round((change.balance/currencyget)-(((change.balance/currencyget)/100)*3), 8)
                    list_active_change_ps['xmr'] = True
            if change.active_in_eth == 1:
                currencyget = currency.get(name_currency='ETH').base_currency
                if round(change.balance/currencyget, 8) > list_active_reserve_ps['eth']:
                    list_active_reserve_ps['eth'] = round((change.balance/currencyget)-(((change.balance/currencyget)/100)*3), 8)
                    list_active_change_ps['eth'] = True
            if change.active_in_etc == 1:
                currencyget = currency.get(name_currency='ETC').base_currency
                if round(change.balance/currencyget, 8) > list_active_reserve_ps['etc']:
                    list_active_reserve_ps['etc'] = round((change.balance/currencyget)-(((change.balance/currencyget)/100)*3), 8)
                    list_active_change_ps['etc'] = True
            if change.active_in_dash == 1:
                currencyget = currency.get(name_currency='DASH').base_currency
                if round(change.balance/currencyget, 8) > list_active_reserve_ps['dash']:
                    list_active_reserve_ps['dash'] = round((change.balance/currencyget)-(((change.balance/currencyget)/100)*3), 8)
                    list_active_change_ps['dash'] = True
    return {'list_active_change_ps': list_active_change_ps, 'list_active_reserve_ps': list_active_reserve_ps}


# активные пс на вывод у всех обменников
def active_width_ps_global():
    list_change = CustomUser.objects.filter(userid__custuserid='Владелец Обменника', is_active_change=1)
    currency = CurrencyCBRF.objects.all()
    list_range_list = RangeSumWidth.objects.all()
    currencyget_rub = currency.get(name_currency='RUB').base_currency
    currencyget_usd = currency.get(name_currency='USD').base_currency
    currencyget_eur = currency.get(name_currency='EUR').base_currency
    currencyget_btc = currency.get(name_currency='BTC').base_currency
    currencyget_xrp = currency.get(name_currency='XRP').base_currency
    currencyget_ltc = currency.get(name_currency='LTC').base_currency
    currencyget_bch = currency.get(name_currency='BCH').base_currency
    currencyget_xmr = currency.get(name_currency='XMR').base_currency
    currencyget_eth = currency.get(name_currency='ETH').base_currency
    currencyget_etc = currency.get(name_currency='ETC').base_currency
    currencyget_dash = currency.get(name_currency='DASH').base_currency
    list_active_change_ps = {
        'sberbank_rub': False, 'psb_rub': False, 'tinkoff_rub': False, 'gazprombank_rub': False, 'alfabank_rub': False,
        'russtandart_rub': False, 'vtb_rub': False, 'rosselhoz_rub': False, 'raifaizen_rub': False,
        'otkritie_rub': False, 'pochtabank_rub': False, 'rnkb_rub': False, 'rosbank_rub': False, 'mtsbank_rub': False,
        'qiwi_rub': False, 'qiwi_usd': False, 'payeer_rub': False, 'payeer_usd': False, 'payeer_eur': False,
        'webmoney_rub': False, 'webmoney_usd': False, 'webmoney_eur': False, 'pm_btc': False, 'pm_usd': False,
        'pm_eur': False, 'skrill_eur': False, 'skrill_usd': False, 'paypal_rub': False, 'paypal_usd': False,
        'paypal_eur': False, 'umoney_rub': False, 'btc': False, 'xrp': False, 'ltc': False, 'bch': False,
        'xmr': False, 'eth': False, 'etc': False, 'dash': False
    }
    list_active_reserve_ps = {
        'sberbank_rub': 0, 'psb_rub': 0, 'tinkoff_rub': 0, 'gazprombank_rub': 0, 'alfabank_rub': 0, 'russtandart_rub': 0,
        'vtb_rub': 0, 'rosselhoz_rub': 0, 'raifaizen_rub': 0, 'otkritie_rub': 0, 'pochtabank_rub': 0, 'rnkb_rub': 0,
        'rosbank_rub': 0, 'mtsbank_rub': 0, 'qiwi_rub': 0, 'qiwi_usd': 0, 'payeer_rub': 0, 'payeer_usd': 0,
        'payeer_eur': 0, 'webmoney_rub': 0, 'webmoney_usd': 0, 'webmoney_eur': 0, 'pm_btc': 0, 'pm_usd': 0,
        'pm_eur': 0, 'skrill_eur': 0, 'skrill_usd': 0, 'paypal_rub': 0, 'paypal_usd': 0, 'paypal_eur': 0, 'umoney_rub': 0,
        'btc': 0, 'xrp': 0, 'ltc': 0, 'bch': 0, 'xmr': 0, 'eth': 0, 'etc': 0, 'dash': 0
    }
    for change in list_change:
        if RangeSumWidth.objects.filter(width_range_username=change).exists():
            list_range = list_range_list.get(width_range_username=change)
            if change.active_out_sberbank_rub == 1:
                if change.balance > list_active_reserve_ps['sberbank_rub']:
                    if change.balance < change.reserv_sberbank_rub*currencyget_rub:
                        list_active_reserve_ps['sberbank_rub'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['sberbank_rub'] = int((change.reserv_sberbank_rub*currencyget_rub)-(((change.reserv_sberbank_rub*currencyget_rub)/100)*3))
                    list_active_change_ps['sberbank_rub'] = True
            if change.active_out_psb_rub == 1:
                if change.balance > list_active_reserve_ps['psb_rub']:
                    if change.balance < change.reserv_psb_rub*currencyget_rub:
                        list_active_reserve_ps['psb_rub'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['psb_rub'] = int((change.reserv_psb_rub*currencyget_rub)-(((change.reserv_psb_rub*currencyget_rub)/100)*3))
                    list_active_change_ps['psb_rub'] = True
            if change.active_out_tinkoff_rub == 1:
                if change.balance > list_active_reserve_ps['tinkoff_rub']:
                    if change.balance < change.reserv_tinkoff_rub*currencyget_rub:
                        list_active_reserve_ps['tinkoff_rub'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['tinkoff_rub'] = int((change.reserv_tinkoff_rub*currencyget_rub)-(((change.reserv_tinkoff_rub*currencyget_rub)/100)*3))
                    list_active_change_ps['tinkoff_rub'] = True
            if change.active_out_gazprombank_rub == 1:
                if change.balance > list_active_reserve_ps['gazprombank_rub']:
                    if change.balance < change.reserv_gazprombank_rub*currencyget_rub:
                        list_active_reserve_ps['gazprombank_rub'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['gazprombank_rub'] = int((change.reserv_gazprombank_rub*currencyget_rub)-(((change.reserv_gazprombank_rub*currencyget_rub)/100)*3))
                    list_active_change_ps['gazprombank_rub'] = True
            if change.active_out_alfabank_rub == 1:
                if change.balance > list_active_reserve_ps['alfabank_rub']:
                    if change.balance < change.reserv_alfabank_rub*currencyget_rub:
                        list_active_reserve_ps['alfabank_rub'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['alfabank_rub'] = int((change.reserv_alfabank_rub*currencyget_rub)-(((change.reserv_alfabank_rub*currencyget_rub)/100)*3))
                    list_active_change_ps['alfabank_rub'] = True
            if change.active_out_russtandart_rub == 1:
                if change.balance > list_active_reserve_ps['russtandart_rub']:
                    if change.balance < change.reserv_russtandart_rub*currencyget_rub:
                        list_active_reserve_ps['russtandart_rub'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['russtandart_rub'] = int((change.reserv_russtandart_rub*currencyget_rub)-(((change.reserv_russtandart_rub*currencyget_rub)/100)*3))
                    list_active_change_ps['russtandart_rub'] = True
            if change.active_out_vtb_rub == 1:
                if change.balance > list_active_reserve_ps['vtb_rub']:
                    if change.balance < change.reserv_vtb_rub*currencyget_rub:
                        list_active_reserve_ps['vtb_rub'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['vtb_rub'] = int((change.reserv_vtb_rub*currencyget_rub)-(((change.reserv_vtb_rub*currencyget_rub)/100)*3))
                    list_active_change_ps['vtb_rub'] = True
            if change.active_out_rosselhoz_rub == 1:
                if change.balance > list_active_reserve_ps['rosselhoz_rub']:
                    if change.balance < change.reserv_rosselhoz_rub*currencyget_rub:
                        list_active_reserve_ps['rosselhoz_rub'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['rosselhoz_rub'] = int((change.reserv_rosselhoz_rub*currencyget_rub)-(((change.reserv_rosselhoz_rub*currencyget_rub)/100)*3))
                    list_active_change_ps['rosselhoz_rub'] = True
            if change.active_out_raifaizen_rub == 1:
                if change.balance > list_active_reserve_ps['raifaizen_rub']:
                    if change.balance < change.reserv_raifaizen_rub*currencyget_rub:
                        list_active_reserve_ps['raifaizen_rub'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['raifaizen_rub'] = int((change.reserv_raifaizen_rub*currencyget_rub)-(((change.reserv_raifaizen_rub*currencyget_rub)/100)*3))
                    list_active_change_ps['raifaizen_rub'] = True
            if change.active_out_otkritie_rub == 1:
                if change.balance > list_active_reserve_ps['otkritie_rub']:
                    if change.balance < change.reserv_otkritie_rub*currencyget_rub:
                        list_active_reserve_ps['otkritie_rub'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['otkritie_rub'] = int((change.reserv_otkritie_rub*currencyget_rub)-(((change.reserv_otkritie_rub*currencyget_rub)/100)*3))
                    list_active_change_ps['otkritie_rub'] = True
            if change.active_out_pochtabank_rub == 1:
                if change.balance > list_active_reserve_ps['pochtabank_rub']:
                    if change.balance < change.reserv_pochtabank_rub*currencyget_rub:
                        list_active_reserve_ps['pochtabank_rub'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['pochtabank_rub'] = int((change.reserv_pochtabank_rub*currencyget_rub)-(((change.reserv_pochtabank_rub*currencyget_rub)/100)*3))
                    list_active_change_ps['pochtabank_rub'] = True
            if change.active_out_rnkb_rub == 1:
                if change.balance > list_active_reserve_ps['rnkb_rub']:
                    if change.balance < change.reserv_rnkb_rub*currencyget_rub:
                        list_active_reserve_ps['rnkb_rub'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['rnkb_rub'] = int((change.reserv_rnkb_rub*currencyget_rub)-(((change.reserv_rnkb_rub*currencyget_rub)/100)*3))
                    list_active_change_ps['rnkb_rub'] = True
            if change.active_out_rosbank_rub == 1:
                if change.balance > list_active_reserve_ps['rosbank_rub']:
                    if change.balance < change.reserv_rosbank_rub*currencyget_rub:
                        list_active_reserve_ps['rosbank_rub'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['rosbank_rub'] = int((change.reserv_rosbank_rub*currencyget_rub)-(((change.reserv_rosbank_rub*currencyget_rub)/100)*3))
                    list_active_change_ps['rosbank_rub'] = True
            if change.active_out_mtsbank_rub == 1:
                if change.balance > list_active_reserve_ps['mtsbank_rub']:
                    if change.balance < change.reserv_mtsbank_rub*currencyget_rub:
                        list_active_reserve_ps['mtsbank_rub'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['mtsbank_rub'] = int((change.reserv_mtsbank_rub*currencyget_rub)-(((change.reserv_mtsbank_rub*currencyget_rub)/100)*3))
                    list_active_change_ps['mtsbank_rub'] = True
            if change.active_out_qiwi_rub == 1:
                if change.balance > list_active_reserve_ps['qiwi_rub']:
                    if change.balance < change.reserv_qiwi_rub*currencyget_rub:
                        list_active_reserve_ps['qiwi_rub'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['qiwi_rub'] = int((change.reserv_qiwi_rub*currencyget_rub)-(((change.reserv_qiwi_rub*currencyget_rub)/100)*3))
                    list_active_change_ps['qiwi_rub'] = True
            if change.active_out_qiwi_usd == 1:
                if change.balance > list_active_reserve_ps['qiwi_usd']:
                    if change.balance < change.reserv_qiwi_usd*currencyget_usd:
                        list_active_reserve_ps['qiwi_usd'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['qiwi_usd'] = int((change.reserv_qiwi_usd*currencyget_usd)-(((change.reserv_qiwi_usd*currencyget_usd)/100)*3))
                    list_active_change_ps['qiwi_usd'] = True
            if change.active_out_payeer_rub == 1:
                if change.balance > list_active_reserve_ps['payeer_rub']:
                    if change.balance < change.reserv_payeer_rub*currencyget_rub:
                        list_active_reserve_ps['payeer_rub'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['payeer_rub'] = int((change.reserv_payeer_rub*currencyget_rub)-(((change.reserv_payeer_rub*currencyget_rub)/100)*3))
                    list_active_change_ps['payeer_rub'] = True
            if change.active_out_payeer_usd == 1:
                if change.balance > list_active_reserve_ps['payeer_usd']:
                    if change.balance < change.reserv_payeer_usd*currencyget_usd:
                        list_active_reserve_ps['payeer_usd'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['payeer_usd'] = int((change.reserv_payeer_usd*currencyget_usd)-(((change.reserv_payeer_usd*currencyget_usd)/100)*3))
                    list_active_change_ps['payeer_usd'] = True
            if change.active_out_payeer_eur == 1:
                if change.balance > list_active_reserve_ps['payeer_eur']:
                    if change.balance < change.reserv_payeer_eur*currencyget_usd:
                        list_active_reserve_ps['payeer_eur'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['payeer_eur'] = int((change.reserv_payeer_eur*currencyget_usd)-(((change.reserv_payeer_eur*currencyget_usd)/100)*3))
                    list_active_change_ps['payeer_eur'] = True
            if change.active_out_webmoney_rub == 1:
                if change.balance > list_active_reserve_ps['webmoney_rub']:
                    if change.balance < change.reserv_webmoney_rub*currencyget_rub:
                        list_active_reserve_ps['webmoney_rub'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['webmoney_rub'] = int((change.reserv_webmoney_rub*currencyget_rub)-(((change.reserv_webmoney_rub*currencyget_rub)/100)*3))
                    list_active_change_ps['webmoney_rub'] = True
            if change.active_out_webmoney_usd == 1:
                if change.balance > list_active_reserve_ps['webmoney_usd']:
                    if change.balance < change.reserv_webmoney_usd*currencyget_usd:
                        list_active_reserve_ps['webmoney_usd'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['webmoney_usd'] = int((change.reserv_webmoney_usd*currencyget_usd)-(((change.reserv_webmoney_usd*currencyget_usd)/100)*3))
                    list_active_change_ps['webmoney_usd'] = True
            if change.active_out_webmoney_eur == 1:
                if change.balance > list_active_reserve_ps['webmoney_eur']:
                    if change.balance < change.reserv_webmoney_eur*currencyget_eur:
                        list_active_reserve_ps['webmoney_eur'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['webmoney_eur'] = int((change.reserv_webmoney_eur*currencyget_eur)-(((change.reserv_webmoney_eur*currencyget_eur)/100)*3))
                    list_active_change_ps['webmoney_eur'] = True
            if change.active_out_pm_btc == 1:
                if change.balance > list_active_reserve_ps['pm_btc']:
                    if change.balance < change.reserv_pm_btc*currencyget_btc:
                        list_active_reserve_ps['pm_btc'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['pm_btc'] = int((change.reserv_pm_btc*currencyget_btc)-(((change.reserv_pm_btc*currencyget_btc)/100)*3))
                    list_active_change_ps['pm_btc'] = True
            if change.active_out_pm_usd == 1:
                if change.balance > list_active_reserve_ps['pm_usd']:
                    if change.balance < change.reserv_pm_usd*currencyget_usd:
                        list_active_reserve_ps['pm_usd'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['pm_usd'] = int((change.reserv_pm_usd*currencyget_usd)-(((change.reserv_pm_usd*currencyget_usd)/100)*3))
                    list_active_change_ps['pm_usd'] = True
            if change.active_out_pm_eur == 1:
                if change.balance > list_active_reserve_ps['pm_eur']:
                    if change.balance < change.reserv_pm_eur*currencyget_eur:
                        list_active_reserve_ps['pm_eur'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['pm_eur'] = int((change.reserv_pm_eur*currencyget_eur)-(((change.reserv_pm_eur*currencyget_eur)/100)*3))
                    list_active_change_ps['pm_eur'] = True
            if change.active_out_skrill_eur == 1:
                if change.balance > list_active_reserve_ps['skrill_eur']:
                    if change.balance < change.reserv_skrill_eur*currencyget_eur:
                        list_active_reserve_ps['skrill_eur'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['skrill_eur'] = int((change.reserv_skrill_eur*currencyget_eur)-(((change.reserv_skrill_eur*currencyget_eur)/100)*3))
                    list_active_change_ps['skrill_eur'] = True
            if change.active_out_skrill_usd == 1:
                if change.balance > list_active_reserve_ps['skrill_usd']:
                    if change.balance < change.reserv_skrill_usd*currencyget_usd:
                        list_active_reserve_ps['skrill_usd'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['skrill_usd'] = int((change.reserv_skrill_usd*currencyget_usd)-(((change.reserv_skrill_usd*currencyget_usd)/100)*3))
                    list_active_change_ps['skrill_usd'] = True
            if change.active_out_paypal_rub == 1:
                if change.balance > list_active_reserve_ps['paypal_rub']:
                    if change.balance < change.reserv_paypal_rub*currencyget_rub:
                        list_active_reserve_ps['paypal_rub'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['paypal_rub'] = int((change.reserv_paypal_rub*currencyget_rub)-(((change.reserv_paypal_rub*currencyget_rub)/100)*3))
                    list_active_change_ps['paypal_rub'] = True
            if change.active_out_paypal_usd == 1:
                if change.balance > list_active_reserve_ps['paypal_usd']:
                    if change.balance < change.reserv_paypal_usd*currencyget_usd:
                        list_active_reserve_ps['paypal_usd'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['paypal_usd'] = int((change.reserv_paypal_usd*currencyget_usd)-(((change.reserv_paypal_usd*currencyget_usd)/100)*3))
                    list_active_change_ps['paypal_usd'] = True
            if change.active_out_paypal_eur == 1:
                if change.balance > list_active_reserve_ps['paypal_eur']:
                    if change.balance < change.reserv_paypal_eur*currencyget_eur:
                        list_active_reserve_ps['paypal_eur'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['paypal_eur'] = int((change.reserv_paypal_eur*currencyget_eur)-(((change.reserv_paypal_eur*currencyget_eur)/100)*3))
                    list_active_change_ps['paypal_eur'] = True
            if change.active_out_umoney_rub == 1:
                if change.balance > list_active_reserve_ps['umoney_rub']:
                    if change.balance < change.reserv_umoney_rub*currencyget_rub:
                        list_active_reserve_ps['umoney_rub'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['umoney_rub'] = int((change.reserv_umoney_rub*currencyget_rub)-(((change.reserv_umoney_rub*currencyget_rub)/100)*3))
                    list_active_change_ps['umoney_rub'] = True
            if change.active_out_btc == 1:
                if change.balance > list_active_reserve_ps['btc']:
                    if change.balance < change.reserv_btc*currencyget_btc:
                        list_active_reserve_ps['btc'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['btc'] = int((change.reserv_btc*currencyget_btc)-(((change.reserv_btc*currencyget_btc)/100)*3))
                    list_active_change_ps['btc'] = True
            if change.active_out_xrp == 1:
                if change.balance > list_active_reserve_ps['xrp']:
                    if change.balance < change.reserv_xrp*currencyget_xrp:
                        list_active_reserve_ps['xrp'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['xrp'] = int((change.reserv_xrp*currencyget_xrp)-(((change.reserv_xrp*currencyget_xrp)/100)*3))
                    list_active_change_ps['xrp'] = True
            if change.active_out_ltc == 1:
                if change.balance > list_active_reserve_ps['ltc']:
                    if change.balance < change.reserv_ltc*currencyget_ltc:
                        list_active_reserve_ps['ltc'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['ltc'] = int((change.reserv_ltc*currencyget_ltc)-(((change.reserv_ltc*currencyget_ltc)/100)*3))
                    list_active_change_ps['ltc'] = True
            if change.active_out_bch == 1:
                if change.balance > list_active_reserve_ps['bch']:
                    if change.balance < change.reserv_bch*currencyget_bch:
                        list_active_reserve_ps['bch'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['bch'] = int((change.reserv_bch*currencyget_bch)-(((change.reserv_bch*currencyget_bch)/100)*3))
                    list_active_change_ps['bch'] = True
            if change.active_out_xmr == 1:
                if change.balance > list_active_reserve_ps['xmr']:
                    if change.balance < change.reserv_xmr*currencyget_xmr:
                        list_active_reserve_ps['xmr'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['xmr'] = int((change.reserv_xmr*currencyget_xmr)-(((change.reserv_xmr*currencyget_xmr)/100)*3))
                    list_active_change_ps['xmr'] = True
            if change.active_out_eth == 1:
                if change.balance > list_active_reserve_ps['eth']:
                    if change.balance < change.reserv_eth*currencyget_eth:
                        list_active_reserve_ps['eth'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['eth'] = int((change.reserv_eth*currencyget_eth)-(((change.reserv_eth*currencyget_eth)/100)*3))
                    list_active_change_ps['eth'] = True
            if change.active_out_etc == 1:
                if change.balance > list_active_reserve_ps['etc']:
                    if change.balance < change.reserv_etc*currencyget_etc:
                        list_active_reserve_ps['etc'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['etc'] = int((change.reserv_etc*currencyget_etc)-(((change.reserv_etc*currencyget_etc)/100)*3))
                    list_active_change_ps['etc'] = True
            if change.active_out_dash == 1:
                if change.balance > list_active_reserve_ps['dash']:
                    if change.balance < change.reserv_dash*currencyget_dash:
                        list_active_reserve_ps['dash'] = int(change.balance-((change.balance/100)*3))
                    else:
                        list_active_reserve_ps['dash'] = int((change.reserv_dash*currencyget_dash)-(((change.reserv_dash*currencyget_dash)/100)*3))
                    list_active_change_ps['dash'] = True
    return {'list_active_change_ps': list_active_change_ps, 'list_active_reserve_ps': list_active_reserve_ps}


# метод для range_..._ps_global
def ps_metod_width(ps, name, list_range_min_reserve_ps, list_active, list_range_max_reserve_ps, active_list_ps, balance):
    # мимимальный лимит
    list_range_min_reserve_ps = list_range_min_reserve_ps
    # Резерв
    list_active = list_active
    # максимальный лимит
    list_range_max_reserve_ps = list_range_max_reserve_ps
    # активность пс
    active_list_ps = active_list_ps
    if ps > list_range_max_reserve_ps[name]:
        if ps < list_active[name]:
            if ps > list_range_min_reserve_ps[name] < balance:
                if ps <= balance:
                    list_range_max_reserve_ps[name] = float(ps)
                else:
                    list_range_max_reserve_ps[name] = float(balance)
            else:
                active_list_ps[name] = False
        else:
            if list_active[name] > list_range_min_reserve_ps[name] < balance:
                if list_active[name] <= balance:
                    list_range_max_reserve_ps[name] = float(list_active[name])
                else:
                    list_range_max_reserve_ps[name] = float(balance)
            else:
                active_list_ps[name] = False
    return {'list_range_min_reserve_ps': list_range_min_reserve_ps, 'list_active': list_active, 'list_range_max_reserve_ps': list_range_max_reserve_ps, 'active_list_ps': active_list_ps}


# метод для range_..._ps_global
def ps_metod(ps, name, list_range_min_reserve_ps, list_active, list_range_max_reserve_ps, active_list_ps):
    # мимимальный лимит
    list_range_min_reserve_ps = list_range_min_reserve_ps
    # Резерв
    list_active = list_active
    # максимальный лимит
    list_range_max_reserve_ps = list_range_max_reserve_ps
    # активность пс
    active_list_ps = active_list_ps
    if ps > list_range_max_reserve_ps[name]:
        if ps < list_active[name]:
            if ps > list_range_min_reserve_ps[name]:
                list_range_max_reserve_ps[name] = float(ps)
            else:
                active_list_ps[name] = False
        else:
            if list_active[name] > list_range_min_reserve_ps[name]:
                list_range_max_reserve_ps[name] = float(list_active[name])
            else:
                active_list_ps[name] = False
    return {'list_range_min_reserve_ps': list_range_min_reserve_ps, 'list_active': list_active, 'list_range_max_reserve_ps': list_range_max_reserve_ps, 'active_list_ps': active_list_ps}


# лимиты для заявок на пополнение
def range_deposit_ps_global(list_active, active_list_ps):
    list_change = CustomUser.objects.filter(userid__custuserid='Владелец Обменника', is_active_change=1)
    active_list_ps = active_list_ps
    list_range_min_reserve_ps = {
        'sberbank_rub': 100000, 'psb_rub': 100000, 'tinkoff_rub': 100000, 'gazprombank_rub': 100000, 'alfabank_rub': 100000, 'russtandart_rub': 100000,
        'vtb_rub': 100000, 'rosselhoz_rub': 100000, 'raifaizen_rub': 100000, 'otkritie_rub': 100000, 'pochtabank_rub': 100000, 'rnkb_rub': 100000,
        'rosbank_rub': 100000, 'mtsbank_rub': 100000, 'qiwi_rub': 100000, 'qiwi_usd': 100000, 'payeer_rub': 100000, 'payeer_usd': 100000,
        'payeer_eur': 100000, 'webmoney_rub': 100000, 'webmoney_usd': 100000, 'webmoney_eur': 100000, 'pm_btc': 100000, 'pm_usd': 100000,
        'pm_eur': 100000, 'skrill_eur': 100000, 'skrill_usd': 100000, 'paypal_rub': 100000, 'paypal_usd': 100000, 'paypal_eur': 100000, 'umoney_rub': 100000,
        'btc': 100000, 'xrp': 100000, 'ltc': 100000, 'bch': 100000, 'xmr': 100000, 'eth': 100000, 'etc': 100000, 'dash': 100000
    }
    list_range_max_reserve_ps = {
        'sberbank_rub': 0, 'psb_rub': 0, 'tinkoff_rub': 0, 'gazprombank_rub': 0, 'alfabank_rub': 0, 'russtandart_rub': 0,
        'vtb_rub': 0, 'rosselhoz_rub': 0, 'raifaizen_rub': 0, 'otkritie_rub': 0, 'pochtabank_rub': 0, 'rnkb_rub': 0,
        'rosbank_rub': 0, 'mtsbank_rub': 0, 'qiwi_rub': 0, 'qiwi_usd': 0, 'payeer_rub': 0, 'payeer_usd': 0,
        'payeer_eur': 0, 'webmoney_rub': 0, 'webmoney_usd': 0, 'webmoney_eur': 0, 'pm_btc': 0, 'pm_usd': 0,
        'pm_eur': 0, 'skrill_eur': 0, 'skrill_usd': 0, 'paypal_rub': 0, 'paypal_usd': 0, 'paypal_eur': 0, 'umoney_rub': 0,
        'btc': 0, 'xrp': 0, 'ltc': 0, 'bch': 0, 'xmr': 0, 'eth': 0, 'etc': 0, 'dash': 0
    }
    for userrange in list_change:
        if RangeSumDeposit.objects.filter(deposit_range_username=userrange).exists():
            list_range = RangeSumDeposit.objects.get(deposit_range_username=userrange)
            if list_range.deposit_min_sberbank_rub < list_range_min_reserve_ps['sberbank_rub']:
                list_range_min_reserve_ps['sberbank_rub'] = list_range.deposit_min_sberbank_rub
            if list_range.deposit_min_psb_rub < list_range_min_reserve_ps['psb_rub']:
                list_range_min_reserve_ps['psb_rub'] = list_range.deposit_min_psb_rub
            if list_range.deposit_min_tinkoff_rub < list_range_min_reserve_ps['tinkoff_rub']:
                list_range_min_reserve_ps['tinkoff_rub'] = list_range.deposit_min_tinkoff_rub
            if list_range.deposit_min_gazprombank_rub < list_range_min_reserve_ps['gazprombank_rub']:
                list_range_min_reserve_ps['gazprombank_rub'] = list_range.deposit_min_gazprombank_rub
            if list_range.deposit_min_alfabank_rub < list_range_min_reserve_ps['alfabank_rub']:
                list_range_min_reserve_ps['alfabank_rub'] = list_range.deposit_min_alfabank_rub
            if list_range.deposit_min_russtandart_rub < list_range_min_reserve_ps['russtandart_rub']:
                list_range_min_reserve_ps['russtandart_rub'] = list_range.deposit_min_russtandart_rub
            if list_range.deposit_min_vtb_rub < list_range_min_reserve_ps['vtb_rub']:
                list_range_min_reserve_ps['vtb_rub'] = list_range.deposit_min_vtb_rub
            if list_range.deposit_min_rosselhoz_rub < list_range_min_reserve_ps['rosselhoz_rub']:
                list_range_min_reserve_ps['rosselhoz_rub'] = list_range.deposit_min_rosselhoz_rub
            if list_range.deposit_min_raifaizen_rub < list_range_min_reserve_ps['raifaizen_rub']:
                list_range_min_reserve_ps['raifaizen_rub'] = list_range.deposit_min_raifaizen_rub
            if list_range.deposit_min_otkritie_rub < list_range_min_reserve_ps['otkritie_rub']:
                list_range_min_reserve_ps['otkritie_rub'] = list_range.deposit_min_otkritie_rub
            if list_range.deposit_min_pochtabank_rub < list_range_min_reserve_ps['pochtabank_rub']:
                list_range_min_reserve_ps['pochtabank_rub'] = list_range.deposit_min_pochtabank_rub
            if list_range.deposit_min_rnkb_rub < list_range_min_reserve_ps['rnkb_rub']:
                list_range_min_reserve_ps['rnkb_rub'] = list_range.deposit_min_rnkb_rub
            if list_range.deposit_min_rosbank_rub < list_range_min_reserve_ps['rosbank_rub']:
                list_range_min_reserve_ps['rosbank_rub'] = list_range.deposit_min_rosbank_rub
            if list_range.deposit_min_mtsbank_rub < list_range_min_reserve_ps['mtsbank_rub']:
                list_range_min_reserve_ps['mtsbank_rub'] = list_range.deposit_min_mtsbank_rub
            if list_range.deposit_min_qiwi_rub < list_range_min_reserve_ps['qiwi_rub']:
                list_range_min_reserve_ps['qiwi_rub'] = list_range.deposit_min_qiwi_rub
            if list_range.deposit_min_qiwi_usd < list_range_min_reserve_ps['qiwi_usd']:
                list_range_min_reserve_ps['qiwi_usd'] = list_range.deposit_min_qiwi_usd
            if list_range.deposit_min_payeer_rub < list_range_min_reserve_ps['payeer_rub']:
                list_range_min_reserve_ps['payeer_rub'] = list_range.deposit_min_payeer_rub
            if list_range.deposit_min_payeer_usd < list_range_min_reserve_ps['payeer_usd']:
                list_range_min_reserve_ps['payeer_usd'] = list_range.deposit_min_payeer_usd
            if list_range.deposit_min_payeer_eur < list_range_min_reserve_ps['payeer_eur']:
                list_range_min_reserve_ps['payeer_eur'] = list_range.deposit_min_payeer_eur
            if list_range.deposit_min_webmoney_rub < list_range_min_reserve_ps['webmoney_rub']:
                list_range_min_reserve_ps['webmoney_rub'] = list_range.deposit_min_webmoney_rub
            if list_range.deposit_min_webmoney_usd < list_range_min_reserve_ps['webmoney_usd']:
                list_range_min_reserve_ps['webmoney_usd'] = list_range.deposit_min_webmoney_usd
            if list_range.deposit_min_webmoney_eur < list_range_min_reserve_ps['webmoney_eur']:
                list_range_min_reserve_ps['webmoney_eur'] = list_range.deposit_min_webmoney_eur
            if list_range.deposit_min_pm_btc < list_range_min_reserve_ps['pm_btc']:
                list_range_min_reserve_ps['pm_btc'] = list_range.deposit_min_pm_btc
            if list_range.deposit_min_pm_usd < list_range_min_reserve_ps['pm_usd']:
                list_range_min_reserve_ps['pm_usd'] = list_range.deposit_min_pm_usd
            if list_range.deposit_min_pm_eur < list_range_min_reserve_ps['pm_eur']:
                list_range_min_reserve_ps['pm_eur'] = list_range.deposit_min_pm_eur
            if list_range.deposit_min_skrill_eur < list_range_min_reserve_ps['skrill_eur']:
                list_range_min_reserve_ps['skrill_eur'] = list_range.deposit_min_skrill_eur
            if list_range.deposit_min_skrill_usd < list_range_min_reserve_ps['skrill_usd']:
                list_range_min_reserve_ps['skrill_usd'] = list_range.deposit_min_skrill_usd
            if list_range.deposit_min_paypal_rub < list_range_min_reserve_ps['paypal_rub']:
                list_range_min_reserve_ps['paypal_rub'] = list_range.deposit_min_paypal_rub
            if list_range.deposit_min_paypal_usd < list_range_min_reserve_ps['paypal_usd']:
                list_range_min_reserve_ps['paypal_usd'] = list_range.deposit_min_paypal_usd
            if list_range.deposit_min_paypal_eur < list_range_min_reserve_ps['paypal_eur']:
                list_range_min_reserve_ps['paypal_eur'] = list_range.deposit_min_paypal_eur
            if list_range.deposit_min_umoney_rub < list_range_min_reserve_ps['umoney_rub']:
                list_range_min_reserve_ps['umoney_rub'] = list_range.deposit_min_umoney_rub
            if list_range.deposit_min_btc < list_range_min_reserve_ps['btc']:
                list_range_min_reserve_ps['btc'] = list_range.deposit_min_btc
            if list_range.deposit_min_xrp < list_range_min_reserve_ps['xrp']:
                list_range_min_reserve_ps['xrp'] = list_range.deposit_min_xrp
            if list_range.deposit_min_ltc < list_range_min_reserve_ps['ltc']:
                list_range_min_reserve_ps['ltc'] = list_range.deposit_min_ltc
            if list_range.deposit_min_bch < list_range_min_reserve_ps['bch']:
                list_range_min_reserve_ps['bch'] = list_range.deposit_min_bch
            if list_range.deposit_min_xmr < list_range_min_reserve_ps['xmr']:
                list_range_min_reserve_ps['xmr'] = list_range.deposit_min_xmr
            if list_range.deposit_min_eth < list_range_min_reserve_ps['eth']:
                list_range_min_reserve_ps['eth'] = list_range.deposit_min_eth
            if list_range.deposit_min_etc < list_range_min_reserve_ps['etc']:
                list_range_min_reserve_ps['etc'] = list_range.deposit_min_etc
            if list_range.deposit_min_dash < list_range_min_reserve_ps['dash']:
                list_range_min_reserve_ps['dash'] = list_range.deposit_min_dash

            keys_list = {
                'sberbank_rub': list_range.deposit_max_sberbank_rub,
                'psb_rub': list_range.deposit_max_psb_rub,
                'tinkoff_rub': list_range.deposit_max_tinkoff_rub,
                'gazprombank_rub': list_range.deposit_max_gazprombank_rub,
                'alfabank_rub': list_range.deposit_max_alfabank_rub,
                'russtandart_rub': list_range.deposit_max_russtandart_rub,
                'vtb_rub': list_range.deposit_max_vtb_rub,
                'rosselhoz_rub': list_range.deposit_max_rosselhoz_rub,
                'raifaizen_rub': list_range.deposit_max_raifaizen_rub,
                'otkritie_rub': list_range.deposit_max_otkritie_rub,
                'pochtabank_rub': list_range.deposit_max_pochtabank_rub,
                'rnkb_rub': list_range.deposit_max_rnkb_rub,
                'rosbank_rub': list_range.deposit_max_rosbank_rub,
                'mtsbank_rub': list_range.deposit_max_mtsbank_rub,
                'qiwi_rub': list_range.deposit_max_qiwi_rub,
                'qiwi_usd': list_range.deposit_max_qiwi_usd,
                'payeer_rub': list_range.deposit_max_payeer_rub,
                'payeer_usd': list_range.deposit_max_payeer_usd,
                'payeer_eur': list_range.deposit_max_payeer_eur,
                'webmoney_rub': list_range.deposit_max_webmoney_rub,
                'webmoney_usd': list_range.deposit_max_webmoney_usd,
                'webmoney_eur': list_range.deposit_max_webmoney_eur,
                'pm_btc': list_range.deposit_max_pm_btc,
                'pm_usd': list_range.deposit_max_pm_usd,
                'pm_eur': list_range.deposit_max_pm_eur,
                'skrill_eur': list_range.deposit_max_skrill_eur,
                'skrill_usd': list_range.deposit_max_skrill_usd,
                'paypal_rub': list_range.deposit_max_paypal_rub,
                'paypal_usd': list_range.deposit_max_paypal_usd,
                'paypal_eur': list_range.deposit_max_paypal_eur,
                'umoney_rub': list_range.deposit_max_umoney_rub,
                'btc': list_range.deposit_max_btc,
                'xrp': list_range.deposit_max_xrp,
                'ltc': list_range.deposit_max_ltc,
                'bch': list_range.deposit_max_bch,
                'xmr': list_range.deposit_max_xmr,
                'eth': list_range.deposit_max_eth,
                'etc': list_range.deposit_max_etc,
                'dash': list_range.deposit_max_etc,
            }

            for item in keys_list:
                ps = keys_list.get(item)
                name = item
                listed = ps_metod(ps=ps, name=name, list_range_min_reserve_ps=list_range_min_reserve_ps,
                                  list_active=list_active, list_range_max_reserve_ps=list_range_max_reserve_ps,
                                  active_list_ps=active_list_ps)
                list_range_min_reserve_ps = listed['list_range_min_reserve_ps']
                list_range_max_reserve_ps = listed['list_range_max_reserve_ps']
                list_active = listed['list_active']
                active_list_ps = listed['active_list_ps']

    return {'list_range_min_reserve_ps': list_range_min_reserve_ps,
            'list_range_max_reserve_ps': list_range_max_reserve_ps,
            'active_list_ps': active_list_ps
            }


# лимиты для заявок на вывод
def range_width_ps_global(list_active, active_list_ps, balance):
    list_change = CustomUser.objects.filter(userid__custuserid='Владелец Обменника', is_active_change=1)
    currency = CurrencyCBRF.objects.all()
    list_range_list = RangeSumWidth.objects.all()
    active_list_ps = active_list_ps
    list_range_min_reserve_ps = {
        'sberbank_rub': 100000, 'psb_rub': 100000, 'tinkoff_rub': 100000, 'gazprombank_rub': 100000, 'alfabank_rub': 100000, 'russtandart_rub': 100000,
        'vtb_rub': 100000, 'rosselhoz_rub': 100000, 'raifaizen_rub': 100000, 'otkritie_rub': 100000, 'pochtabank_rub': 100000, 'rnkb_rub': 100000,
        'rosbank_rub': 100000, 'mtsbank_rub': 100000, 'qiwi_rub': 100000, 'qiwi_usd': 100000, 'payeer_rub': 100000, 'payeer_usd': 100000,
        'payeer_eur': 100000, 'webmoney_rub': 100000, 'webmoney_usd': 100000, 'webmoney_eur': 100000, 'pm_btc': 100000, 'pm_usd': 100000,
        'pm_eur': 100000, 'skrill_eur': 100000, 'skrill_usd': 100000, 'paypal_rub': 100000, 'paypal_usd': 100000, 'paypal_eur': 100000, 'umoney_rub': 100000,
        'btc': 100000, 'xrp': 100000, 'ltc': 100000, 'bch': 100000, 'xmr': 100000, 'eth': 100000, 'etc': 100000, 'dash': 100000
    }
    list_range_max_reserve_ps = {
        'sberbank_rub': 0, 'psb_rub': 0, 'tinkoff_rub': 0, 'gazprombank_rub': 0, 'alfabank_rub': 0, 'russtandart_rub': 0,
        'vtb_rub': 0, 'rosselhoz_rub': 0, 'raifaizen_rub': 0, 'otkritie_rub': 0, 'pochtabank_rub': 0, 'rnkb_rub': 0,
        'rosbank_rub': 0, 'mtsbank_rub': 0, 'qiwi_rub': 0, 'qiwi_usd': 0, 'payeer_rub': 0, 'payeer_usd': 0,
        'payeer_eur': 0, 'webmoney_rub': 0, 'webmoney_usd': 0, 'webmoney_eur': 0, 'pm_btc': 0, 'pm_usd': 0,
        'pm_eur': 0, 'skrill_eur': 0, 'skrill_usd': 0, 'paypal_rub': 0, 'paypal_usd': 0, 'paypal_eur': 0, 'umoney_rub': 0,
        'btc': 0, 'xrp': 0, 'ltc': 0, 'bch': 0, 'xmr': 0, 'eth': 0, 'etc': 0, 'dash': 0
    }
    currencyget_rub = currency.get(name_currency='RUB').base_currency
    currencyget_usd = currency.get(name_currency='USD').base_currency
    currencyget_eur = currency.get(name_currency='EUR').base_currency
    currencyget_btc = currency.get(name_currency='BTC').base_currency
    currencyget_xrp = currency.get(name_currency='XRP').base_currency
    currencyget_ltc = currency.get(name_currency='LTC').base_currency
    currencyget_bch = currency.get(name_currency='BCH').base_currency
    currencyget_xmr = currency.get(name_currency='XMR').base_currency
    currencyget_eth = currency.get(name_currency='ETH').base_currency
    currencyget_etc = currency.get(name_currency='ETC').base_currency
    currencyget_dash = currency.get(name_currency='DASH').base_currency
    for userrange in list_change:
        if RangeSumWidth.objects.filter(width_range_username=userrange).exists():
            list_range = list_range_list.get(width_range_username=userrange)
            if list_range.width_min_sberbank_rub*currencyget_rub < list_range_min_reserve_ps['sberbank_rub']:
                list_range_min_reserve_ps['sberbank_rub'] = float(round(list_range.width_min_sberbank_rub*currencyget_rub, 2))
            if list_range.width_min_psb_rub*currencyget_rub < list_range_min_reserve_ps['psb_rub']:
                list_range_min_reserve_ps['psb_rub'] = float(round(list_range.width_min_psb_rub*currencyget_rub, 2))
            if list_range.width_min_tinkoff_rub*currencyget_rub < list_range_min_reserve_ps['tinkoff_rub']:
                list_range_min_reserve_ps['tinkoff_rub'] = float(round(list_range.width_min_tinkoff_rub*currencyget_rub, 2))
            if list_range.width_min_gazprombank_rub*currencyget_rub < list_range_min_reserve_ps['gazprombank_rub']:
                list_range_min_reserve_ps['gazprombank_rub'] = float(round(list_range.width_min_gazprombank_rub*currencyget_rub, 2))
            if list_range.width_min_alfabank_rub*currencyget_rub < list_range_min_reserve_ps['alfabank_rub']:
                list_range_min_reserve_ps['alfabank_rub'] = float(round(list_range.width_min_alfabank_rub*currencyget_rub, 2))
            if list_range.width_min_russtandart_rub*currencyget_rub < list_range_min_reserve_ps['russtandart_rub']:
                list_range_min_reserve_ps['russtandart_rub'] = float(round(list_range.width_min_russtandart_rub*currencyget_rub, 2))
            if list_range.width_min_vtb_rub*currencyget_rub < list_range_min_reserve_ps['vtb_rub']:
                list_range_min_reserve_ps['vtb_rub'] = float(round(list_range.width_min_vtb_rub*currencyget_rub, 2))
            if list_range.width_min_rosselhoz_rub*currencyget_rub < list_range_min_reserve_ps['rosselhoz_rub']:
                list_range_min_reserve_ps['rosselhoz_rub'] = float(round(list_range.width_min_rosselhoz_rub*currencyget_rub, 2))
            if list_range.width_min_raifaizen_rub*currencyget_rub < list_range_min_reserve_ps['raifaizen_rub']:
                list_range_min_reserve_ps['raifaizen_rub'] = float(round(list_range.width_min_raifaizen_rub*currencyget_rub, 2))
            if list_range.width_min_otkritie_rub*currencyget_rub < list_range_min_reserve_ps['otkritie_rub']:
                list_range_min_reserve_ps['otkritie_rub'] = float(round(list_range.width_min_otkritie_rub*currencyget_rub, 2))
            if list_range.width_min_pochtabank_rub*currencyget_rub < list_range_min_reserve_ps['pochtabank_rub']:
                list_range_min_reserve_ps['pochtabank_rub'] = float(round(list_range.width_min_pochtabank_rub*currencyget_rub, 2))
            if list_range.width_min_rnkb_rub*currencyget_rub < list_range_min_reserve_ps['rnkb_rub']:
                list_range_min_reserve_ps['rnkb_rub'] = float(round(list_range.width_min_rnkb_rub*currencyget_rub, 2))
            if list_range.width_min_rosbank_rub*currencyget_rub < list_range_min_reserve_ps['rosbank_rub']:
                list_range_min_reserve_ps['rosbank_rub'] = float(round(list_range.width_min_rosbank_rub*currencyget_rub, 2))
            if list_range.width_min_mtsbank_rub*currencyget_rub < list_range_min_reserve_ps['mtsbank_rub']:
                list_range_min_reserve_ps['mtsbank_rub'] = float(round(list_range.width_min_mtsbank_rub*currencyget_rub, 2))
            if list_range.width_min_qiwi_rub*currencyget_rub < list_range_min_reserve_ps['qiwi_rub']:
                list_range_min_reserve_ps['qiwi_rub'] = float(round(list_range.width_min_qiwi_rub*currencyget_rub, 2))
            if list_range.width_min_qiwi_usd*currencyget_usd < list_range_min_reserve_ps['qiwi_usd']:
                list_range_min_reserve_ps['qiwi_usd'] = float(round(list_range.width_min_qiwi_usd*currencyget_usd, 2))
            if list_range.width_min_payeer_rub*currencyget_rub < list_range_min_reserve_ps['payeer_rub']:
                list_range_min_reserve_ps['payeer_rub'] = float(round(list_range.width_min_payeer_rub*currencyget_rub, 2))
            if list_range.width_min_payeer_usd*currencyget_usd < list_range_min_reserve_ps['payeer_usd']:
                list_range_min_reserve_ps['payeer_usd'] = float(round(list_range.width_min_payeer_usd*currencyget_usd, 2))
            if list_range.width_min_payeer_eur*currencyget_eur < list_range_min_reserve_ps['payeer_eur']:
                list_range_min_reserve_ps['payeer_eur'] = float(round(list_range.width_min_payeer_eur*currencyget_eur, 2))
            if list_range.width_min_webmoney_rub*currencyget_rub < list_range_min_reserve_ps['webmoney_rub']:
                list_range_min_reserve_ps['webmoney_rub'] = float(round(list_range.width_min_webmoney_rub*currencyget_rub, 2))
            if list_range.width_min_webmoney_usd*currencyget_usd < list_range_min_reserve_ps['webmoney_usd']:
                list_range_min_reserve_ps['webmoney_usd'] = float(round(list_range.width_min_webmoney_usd*currencyget_usd, 2))
            if list_range.width_min_webmoney_eur*currencyget_eur < list_range_min_reserve_ps['webmoney_eur']:
                list_range_min_reserve_ps['webmoney_eur'] = float(round(list_range.width_min_webmoney_eur*currencyget_eur, 2))
            if list_range.width_min_pm_btc*currencyget_btc < list_range_min_reserve_ps['pm_btc']:
                list_range_min_reserve_ps['pm_btc'] = float(round(list_range.width_min_pm_btc*currencyget_btc, 2))
            if list_range.width_min_pm_usd*currencyget_usd < list_range_min_reserve_ps['pm_usd']:
                list_range_min_reserve_ps['pm_usd'] = float(round(list_range.width_min_pm_usd*currencyget_usd, 2))
            if list_range.width_min_pm_eur*currencyget_eur < list_range_min_reserve_ps['pm_eur']:
                list_range_min_reserve_ps['pm_eur'] = float(round(list_range.width_min_pm_eur*currencyget_eur, 2))
            if list_range.width_min_skrill_eur*currencyget_eur < list_range_min_reserve_ps['skrill_eur']:
                list_range_min_reserve_ps['skrill_eur'] = float(round(list_range.width_min_skrill_eur*currencyget_eur, 2))
            if list_range.width_min_skrill_usd*currencyget_usd < list_range_min_reserve_ps['skrill_usd']:
                list_range_min_reserve_ps['skrill_usd'] = float(round(list_range.width_min_skrill_usd*currencyget_usd, 2))
            if list_range.width_min_paypal_rub*currencyget_rub < list_range_min_reserve_ps['paypal_rub']:
                list_range_min_reserve_ps['paypal_rub'] = float(round(list_range.width_min_paypal_rub*currencyget_rub, 2))
            if list_range.width_min_paypal_usd*currencyget_usd < list_range_min_reserve_ps['paypal_usd']:
                list_range_min_reserve_ps['paypal_usd'] = float(round(list_range.width_min_paypal_usd*currencyget_usd, 2))
            if list_range.width_min_paypal_eur*currencyget_eur < list_range_min_reserve_ps['paypal_eur']:
                list_range_min_reserve_ps['paypal_eur'] = float(round(list_range.width_min_paypal_eur*currencyget_eur, 2))
            if list_range.width_min_umoney_rub*currencyget_rub < list_range_min_reserve_ps['umoney_rub']:
                list_range_min_reserve_ps['umoney_rub'] = float(round(list_range.width_min_umoney_rub*currencyget_rub, 2))
            if list_range.width_min_btc*currencyget_btc < list_range_min_reserve_ps['btc']:
                list_range_min_reserve_ps['btc'] = float(round(list_range.width_min_btc*currencyget_btc, 2))
            if list_range.width_min_xrp*currencyget_xrp < list_range_min_reserve_ps['xrp']:
                list_range_min_reserve_ps['xrp'] = float(round(list_range.width_min_xrp*currencyget_xrp, 2))
            if list_range.width_min_ltc*currencyget_ltc < list_range_min_reserve_ps['ltc']:
                list_range_min_reserve_ps['ltc'] = float(round(list_range.width_min_ltc*currencyget_ltc, 2))
            if list_range.width_min_bch*currencyget_bch < list_range_min_reserve_ps['bch']:
                list_range_min_reserve_ps['bch'] = float(round(list_range.width_min_bch*currencyget_bch, 2))
            if list_range.width_min_xmr*currencyget_xmr < list_range_min_reserve_ps['xmr']:
                list_range_min_reserve_ps['xmr'] = float(round(list_range.width_min_xmr*currencyget_xmr, 2))
            if list_range.width_min_eth*currencyget_eth < list_range_min_reserve_ps['eth']:
                list_range_min_reserve_ps['eth'] = float(round(list_range.width_min_eth*currencyget_eth, 2))
            if list_range.width_min_etc*currencyget_etc < list_range_min_reserve_ps['etc']:
                list_range_min_reserve_ps['etc'] = float(round(list_range.width_min_etc*currencyget_etc, 2))
            if list_range.width_min_dash*currencyget_dash < list_range_min_reserve_ps['dash']:
                list_range_min_reserve_ps['dash'] = float(round(list_range.width_min_dash*currencyget_dash, 2))

            keys_list = {
                'sberbank_rub': float(round(list_range.width_max_sberbank_rub*currencyget_rub, 2)),
                'psb_rub': float(round(list_range.width_max_psb_rub*currencyget_rub, 2)),
                'tinkoff_rub': float(round(list_range.width_max_tinkoff_rub*currencyget_rub, 2)),
                'gazprombank_rub': float(round(list_range.width_max_gazprombank_rub*currencyget_rub, 2)),
                'alfabank_rub': float(round(list_range.width_max_alfabank_rub*currencyget_rub, 2)),
                'russtandart_rub': float(round(list_range.width_max_russtandart_rub*currencyget_rub, 2)),
                'vtb_rub': float(round(list_range.width_max_vtb_rub*currencyget_rub, 2)),
                'rosselhoz_rub': float(round(list_range.width_max_rosselhoz_rub*currencyget_rub, 2)),
                'raifaizen_rub': float(round(list_range.width_max_raifaizen_rub*currencyget_rub, 2)),
                'otkritie_rub': float(round(list_range.width_max_otkritie_rub*currencyget_rub, 2)),
                'pochtabank_rub': float(round(list_range.width_max_pochtabank_rub*currencyget_rub, 2)),
                'rnkb_rub': float(round(list_range.width_max_rnkb_rub*currencyget_rub, 2)),
                'rosbank_rub': float(round(list_range.width_max_rosbank_rub*currencyget_rub, 2)),
                'mtsbank_rub': float(round(list_range.width_max_mtsbank_rub*currencyget_rub, 2)),
                'qiwi_rub': float(round(list_range.width_max_qiwi_rub*currencyget_rub, 2)),
                'qiwi_usd': float(round(list_range.width_max_qiwi_usd*currencyget_usd, 2)),
                'payeer_rub': float(round(list_range.width_max_payeer_rub*currencyget_rub, 2)),
                'payeer_usd': float(round(list_range.width_max_payeer_usd*currencyget_usd, 2)),
                'payeer_eur': float(round(list_range.width_max_payeer_eur*currencyget_eur, 2)),
                'webmoney_rub': float(round(list_range.width_max_webmoney_rub*currencyget_rub, 2)),
                'webmoney_usd': float(round(list_range.width_max_webmoney_usd*currencyget_usd, 2)),
                'webmoney_eur': float(round(list_range.width_max_webmoney_eur*currencyget_eur, 2)),
                'pm_btc': float(round(list_range.width_max_pm_btc*currencyget_btc, 2)),
                'pm_usd': float(round(list_range.width_max_pm_usd*currencyget_usd, 2)),
                'pm_eur': float(round(list_range.width_max_pm_eur*currencyget_eur, 2)),
                'skrill_eur': float(round(list_range.width_max_skrill_eur*currencyget_eur, 2)),
                'skrill_usd': float(round(list_range.width_max_skrill_usd*currencyget_usd, 2)),
                'paypal_rub': float(round(list_range.width_max_paypal_rub*currencyget_rub, 2)),
                'paypal_usd': float(round(list_range.width_max_paypal_usd*currencyget_usd, 2)),
                'paypal_eur': float(round(list_range.width_max_paypal_eur*currencyget_eur, 2)),
                'umoney_rub': float(round(list_range.width_max_umoney_rub*currencyget_rub, 2)),
                'btc': float(round(list_range.width_max_btc*currencyget_btc, 2)),
                'xrp': float(round(list_range.width_max_xrp*currencyget_xrp, 2)),
                'ltc': float(round(list_range.width_max_ltc*currencyget_ltc, 2)),
                'bch': float(round(list_range.width_max_bch*currencyget_bch, 2)),
                'xmr': float(round(list_range.width_max_xmr*currencyget_xmr, 2)),
                'eth': float(round(list_range.width_max_eth*currencyget_eth, 2)),
                'etc': float(round(list_range.width_max_etc*currencyget_etc, 2)),
                'dash': float(round(list_range.width_max_etc*currencyget_dash, 2)),
            }

            for item in keys_list:
                ps = keys_list.get(item)
                name = item
                listed = ps_metod_width(ps=ps, name=name, list_range_min_reserve_ps=list_range_min_reserve_ps,
                                  list_active=list_active, list_range_max_reserve_ps=list_range_max_reserve_ps,
                                  active_list_ps=active_list_ps, balance=balance)
                list_range_min_reserve_ps = listed['list_range_min_reserve_ps']
                list_range_max_reserve_ps = listed['list_range_max_reserve_ps']
                list_active = listed['list_active']
                active_list_ps = listed['active_list_ps']

    return {'list_range_min_reserve_ps': list_range_min_reserve_ps,
            'list_range_max_reserve_ps': list_range_max_reserve_ps,
            'active_list_ps': active_list_ps
            }


# получаем минимальную и максимальную сумму заявки
def min_and_max_sum_request(ps_request, range_ps):
    range_min_list = range_ps['list_range_min_reserve_ps']
    range_max_list = range_ps['list_range_max_reserve_ps']
    min_sum = 0
    max_sum = 0
    if ps_request == 'СБЕРБАНК':
        min_sum = range_min_list['sberbank_rub']
        max_sum = range_max_list['sberbank_rub']
    elif ps_request == 'ТИНЬКОФФ':
        min_sum = range_min_list['tinkoff_rub']
        max_sum = range_max_list['tinkoff_rub']
    elif ps_request == 'АЛЬФА БАНК':
        min_sum = range_min_list['alfabank_rub']
        max_sum = range_max_list['alfabank_rub']
    elif ps_request == 'ВТБ':
        min_sum = range_min_list['vtb_rub']
        max_sum = range_max_list['vtb_rub']
    elif ps_request == 'РАЙФФАЙЗЕНБАНК':
        min_sum = range_min_list['raifaizen_rub']
        max_sum = range_max_list['raifaizen_rub']
    elif ps_request == 'ОТКРЫТИЕ':
        min_sum = range_min_list['otkritie_rub']
        max_sum = range_max_list['otkritie_rub']
    elif ps_request == 'ПСБ':
        min_sum = range_min_list['psb_rub']
        max_sum = range_max_list['psb_rub']
    elif ps_request == 'ГАЗПРОМБАНК':
        min_sum = range_min_list['gazprombank_rub']
        max_sum = range_max_list['gazprombank_rub']
    elif ps_request == 'РУССКИЙ СТАНДАРТ':
        min_sum = range_min_list['russtandart_rub']
        max_sum = range_max_list['russtandart_rub']
    elif ps_request == 'РОССЕЛЬХОЗБАНК':
        min_sum = range_min_list['rosselhoz_rub']
        max_sum = range_max_list['rosselhoz_rub']
    elif ps_request == 'ПОЧТА БАНК':
        min_sum = range_min_list['pochtabank_rub']
        max_sum = range_max_list['pochtabank_rub']
    elif ps_request == 'РОСБАНК':
        min_sum = range_min_list['rosbank_rub']
        max_sum = range_max_list['rosbank_rub']
    elif ps_request == 'РНКБ':
        min_sum = range_min_list['rnkb_rub']
        max_sum = range_max_list['rnkb_rub']
    elif ps_request == 'МТС БАНК':
        min_sum = range_min_list['mtsbank_rub']
        max_sum = range_max_list['mtsbank_rub']
    elif ps_request == 'QIWI RUB':
        min_sum = range_min_list['qiwi_rub']
        max_sum = range_max_list['qiwi_rub']
    elif ps_request == 'QIWI USD':
        min_sum = range_min_list['qiwi_usd']
        max_sum = range_max_list['qiwi_usd']
    elif ps_request == 'PAYEER RUB':
        min_sum = range_min_list['payeer_rub']
        max_sum = range_max_list['payeer_rub']
    elif ps_request == 'PAYEER EUR':
        min_sum = range_min_list['payeer_eur']
        max_sum = range_max_list['payeer_eur']
    elif ps_request == 'PAYEER USD':
        min_sum = range_min_list['payeer_usd']
        max_sum = range_max_list['payeer_usd']
    elif ps_request == 'WEBMONEY RUB':
        min_sum = range_min_list['webmoney_rub']
        max_sum = range_max_list['webmoney_rub']
    elif ps_request == 'WEBMONEY EUR':
        min_sum = range_min_list['webmoney_eur']
        max_sum = range_max_list['webmoney_eur']
    elif ps_request == 'WEBMONEY USD':
        min_sum = range_min_list['webmoney_usd']
        max_sum = range_max_list['webmoney_usd']
    elif ps_request == 'PERFECT MONEY BTC':
        min_sum = range_min_list['pm_btc']
        max_sum = range_max_list['pm_btc']
    elif ps_request == 'PERFECT MONEY EUR':
        min_sum = range_min_list['pm_eur']
        max_sum = range_max_list['pm_eur']
    elif ps_request == 'PERFECT MONEY USD':
        min_sum = range_min_list['pm_usd']
        max_sum = range_max_list['pm_usd']
    elif ps_request == 'PAYPAL RUB':
        min_sum = range_min_list['paypal_rub']
        max_sum = range_max_list['paypal_rub']
    elif ps_request == 'PAYPAL EUR':
        min_sum = range_min_list['paypal_eur']
        max_sum = range_max_list['paypal_eur']
    elif ps_request == 'PAYPAL USD':
        min_sum = range_min_list['paypal_usd']
        max_sum = range_max_list['paypal_usd']
    elif ps_request == 'SKRILL EUR':
        min_sum = range_min_list['skrill_eur']
        max_sum = range_max_list['skrill_eur']
    elif ps_request == 'SKRILL USD':
        min_sum = range_min_list['skrill_usd']
        max_sum = range_max_list['skrill_usd']
    elif ps_request == 'UMONEY RUB':
        min_sum = range_min_list['umoney_rub']
        max_sum = range_max_list['umoney_rub']
    elif ps_request == 'BITCOIN':
        min_sum = range_min_list['btc']
        max_sum = range_max_list['btc']
    elif ps_request == 'LITECOIN':
        min_sum = range_min_list['ltc']
        max_sum = range_max_list['ltc']
    elif ps_request == 'MONERO':
        min_sum = range_min_list['xmr']
        max_sum = range_max_list['xmr']
    elif ps_request == 'ETHEREUM CLASSIC':
        min_sum = range_min_list['etc']
        max_sum = range_max_list['etc']
    elif ps_request == 'DASH':
        min_sum = range_min_list['dash']
        max_sum = range_max_list['dash']
    elif ps_request == 'RIPPLE':
        min_sum = range_min_list['xrp']
        max_sum = range_max_list['xrp']
    elif ps_request == 'BITCOIN CASH':
        min_sum = range_min_list['bch']
        max_sum = range_max_list['bch']
    elif ps_request == 'ETHEREUM':
        min_sum = range_min_list['eth']
        max_sum = range_max_list['eth']
    return {'min_sum': min_sum, 'max_sum': max_sum}


# отправка сообщения на почту
def mail_send_metod(email, templates, context, subject):
    html_body = render_to_string(templates, context)
    msg = EmailMultiAlternatives(subject=subject, from_email=settings.EMAIL_HOST_USER, to=[email])
    msg.attach_alternative(html_body, 'text/html')
    msg.send()









