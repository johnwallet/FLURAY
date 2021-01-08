import random

import requests

from personalaccount.models import CurrencyCBRF, RequestChange
from users.models import CustomUser



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
    elif nameps == 'РОКЕТБАНК':
        for item in itemchange:
            if item.active_in_roketbank_rub == 1:
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
    elif nameps == 'РОКЕТБАНК':
        for item in itemchange:
            if item.active_out_roketbank_rub == 1:
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
    elif nameps == 'РОКЕТБАНК':
        for userchange in userps:
            if userchange.reserv_roketbank_rub * currencysort.base_currency > balanceps < userchange.balance:
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
        elif nameps == 'РОКЕТБАНК':
            base_comis = usernameps.comis_in_roketbank_rub
            rekvesites = usernameps.requsites_roketbank_rub
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
        elif nameps == 'РОКЕТБАНК':
            for item in userps:
                if item.comis_in_roketbank_rub < base_comis:
                    usernameps = item
                    rekvesites = item.requsites_roketbank_rub
                    base_comis = item.comis_in_roketbank_rub
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
            usernameps.reserv_gazprombank_rub-= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_gazprombank_rub
        elif nameps == 'РУССКИЙ СТАНДАРТ':
            usernameps.reserv_russtandart_rub -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_russtandart_rub
        elif nameps == 'РОССЕЛЬХОЗБАНК':
            usernameps.reserv_rosselhoz_rub -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_rosselhoz_rub
        elif nameps == 'РОКЕТБАНК':
            usernameps.reserv_roketbank_rub -= balanceps / currencysort.base_currency
            base_comis = usernameps.comis_out_roketbank_rub
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
        elif nameps == 'РОКЕТБАНК':
            for item in userps:
                if item.comis_out_roketbank_rub < base_comis:
                    usernameps = item
                    base_comis = item.comis_out_roketbank_rub
            usernameps.reserv_roketbank_rub -= balanceps / currencysort.base_currency
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




