import random

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from FLURAY import settings
from personalaccount.models import CurrencyCBRF, RequestChange, StaticDailyProfit
from users.models import CustomUser, RangeSumDeposit, RangeSumWidth

from datetime import timedelta, datetime, date


# активность обменника и направлений для пополнения
def depositsortchangeps(nameps, request_sum):
    itemchange = CustomUser.objects.filter(userid__custuserid='Владелец Обменника', is_active_change=1)
    changeq = []
    currencysort_list = CurrencyCBRF.objects.all()
    itemrange_list = RangeSumDeposit.objects.all()

    name_ps_list = {
        'СБЕРБАНК': 'RUB',
        'ТИНЬКОФФ': 'RUB',
        'АЛЬФА БАНК': 'RUB',
        'ВТБ': 'RUB',
        'РАЙФФАЙЗЕНБАНК': 'RUB',
        'ОТКРЫТИЕ': 'RUB',
        'ПСБ': 'RUB',
        'ГАЗПРОМБАНК': 'RUB',
        'РУССКИЙ СТАНДАРТ': 'RUB',
        'РОССЕЛЬХОЗБАНК': 'RUB',
        'ПОЧТА БАНК': 'RUB',
        'РОСБАНК': 'RUB',
        'РНКБ': 'RUB',
        'МТС БАНК': 'RUB',
        'QIWI RUB': 'RUB',
        'QIWI USD': 'USD',
        'PAYEER RUB': 'RUB',
        'PAYEER EUR': 'EUR',
        'PAYEER USD': 'USD',
        'WEBMONEY RUB': 'RUB',
        'WEBMONEY EUR': 'EUR',
        'WEBMONEY USD': 'USD',
        'PERFECT MONEY BTC': 'BTC',
        'PERFECT MONEY EUR': 'EUR',
        'PERFECT MONEY USD': 'USD',
        'PAYPAL RUB': 'RUB',
        'PAYPAL EUR': 'EUR',
        'PAYPAL USD': 'USD',
        'SKRILL EUR': 'EUR',
        'SKRILL USD': 'USD',
        'UMONEY RUB': 'RUB',
        'BITCOIN': 'BTC',
        'LITECOIN': 'LTC',
        'MONERO': 'XMR',
        'ETHEREUM CLASSIC': 'ETC',
        'DASH': 'DASH',
        'RIPPLE': 'XRP',
        'BITCOIN CASH': 'BCH',
        'ETHEREUM': 'ETH',
    }

    name_ps_get = nameps
    valute_ps_get = name_ps_list[nameps]
    currencysort = currencysort_list.get(name_currency=valute_ps_get)

    for item in itemchange:
        itemrange = itemrange_list.get(deposit_range_username=item)
        list_active_in = {
            'СБЕРБАНК': item.active_in_sberbank_rub,
            'ПСБ': item.active_in_psb_rub,
            'ТИНЬКОФФ': item.active_in_tinkoff_rub,
            'ГАЗПРОМБАНК': item.active_in_gazprombank_rub,
            'АЛЬФА БАНК': item.active_in_alfabank_rub,
            'РУССКИЙ СТАНДАРТ': item.active_in_russtandart_rub,
            'ВТБ': item.active_in_vtb_rub,
            'РОССЕЛЬХОЗБАНК': item.active_in_rosselhoz_rub,
            'РАЙФФАЙЗЕНБАНК': item.active_in_raifaizen_rub,
            'ОТКРЫТИЕ': item.active_in_otkritie_rub,
            'ПОЧТА БАНК': item.active_in_pochtabank_rub,
            'РНКБ': item.active_in_rnkb_rub,
            'РОСБАНК': item.active_in_rosbank_rub,
            'МТС БАНК': item.active_in_mtsbank_rub,
            'QIWI RUB': item.active_in_qiwi_rub,
            'QIWI USD': item.active_in_qiwi_usd,
            'PAYEER RUB': item.active_in_payeer_rub,
            'PAYEER USD': item.active_in_payeer_usd,
            'PAYEER EUR': item.active_in_payeer_eur,
            'WEBMONEY RUB': item.active_in_webmoney_rub,
            'WEBMONEY USD': item.active_in_webmoney_usd,
            'WEBMONEY EUR': item.active_in_webmoney_eur,
            'PERFECT MONEY BTC': item.active_in_pm_btc,
            'PERFECT MONEY USD': item.active_in_pm_usd,
            'PERFECT MONEY EUR': item.active_in_pm_eur,
            'SKRILL EUR': item.active_in_skrill_eur,
            'SKRILL USD': item.active_in_skrill_usd,
            'PAYPAL RUB': item.active_in_paypal_rub,
            'PAYPAL USD': item.active_in_paypal_usd,
            'PAYPAL EUR': item.active_in_paypal_eur,
            'UMONEY RUB': item.active_in_umoney_rub,
            'BITCOIN': item.active_in_btc,
            'RIPPLE': item.active_in_xrp,
            'LITECOIN': item.active_in_ltc,
            'BITCOIN CASH': item.active_in_bch,
            'MONERO': item.active_in_xmr,
            'ETHEREUM': item.active_in_eth,
            'ETHEREUM CLASSIC': item.active_in_etc,
            'DASH': item.active_in_dash,
        }
        list_deposit_max = {
            'СБЕРБАНК': itemrange.deposit_max_sberbank_rub,
            'ПСБ': itemrange.deposit_max_psb_rub,
            'ТИНЬКОФФ': itemrange.deposit_max_tinkoff_rub,
            'ГАЗПРОМБАНК': itemrange.deposit_max_gazprombank_rub,
            'АЛЬФА БАНК': itemrange.deposit_max_alfabank_rub,
            'РУССКИЙ СТАНДАРТ': itemrange.deposit_max_russtandart_rub,
            'ВТБ': itemrange.deposit_max_vtb_rub,
            'РОССЕЛЬХОЗБАНК': itemrange.deposit_max_rosselhoz_rub,
            'РАЙФФАЙЗЕНБАНК': itemrange.deposit_max_raifaizen_rub,
            'ОТКРЫТИЕ': itemrange.deposit_max_otkritie_rub,
            'ПОЧТА БАНК': itemrange.deposit_max_pochtabank_rub,
            'РНКБ': itemrange.deposit_max_rnkb_rub,
            'РОСБАНК': itemrange.deposit_max_rosbank_rub,
            'МТС БАНК': itemrange.deposit_max_mtsbank_rub,
            'QIWI RUB': itemrange.deposit_max_qiwi_rub,
            'QIWI USD': itemrange.deposit_max_qiwi_usd,
            'PAYEER RUB': itemrange.deposit_max_payeer_rub,
            'PAYEER USD': itemrange.deposit_max_payeer_usd,
            'PAYEER EUR': itemrange.deposit_max_payeer_eur,
            'WEBMONEY RUB': itemrange.deposit_max_webmoney_rub,
            'WEBMONEY USD': itemrange.deposit_max_webmoney_usd,
            'WEBMONEY EUR': itemrange.deposit_max_webmoney_eur,
            'PERFECT MONEY BTC': itemrange.deposit_max_pm_btc,
            'PERFECT MONEY USD': itemrange.deposit_max_pm_usd,
            'PERFECT MONEY EUR': itemrange.deposit_max_pm_eur,
            'SKRILL EUR': itemrange.deposit_max_skrill_eur,
            'SKRILL USD': itemrange.deposit_max_skrill_usd,
            'PAYPAL RUB': itemrange.deposit_max_paypal_rub,
            'PAYPAL USD': itemrange.deposit_max_paypal_usd,
            'PAYPAL EUR': itemrange.deposit_max_paypal_eur,
            'UMONEY RUB': itemrange.deposit_max_umoney_rub,
            'BITCOIN': itemrange.deposit_max_btc,
            'RIPPLE': itemrange.deposit_max_xrp,
            'LITECOIN': itemrange.deposit_max_ltc,
            'BITCOIN CASH': itemrange.deposit_max_bch,
            'MONERO': itemrange.deposit_max_xmr,
            'ETHEREUM': itemrange.deposit_max_eth,
            'ETHEREUM CLASSIC': itemrange.deposit_max_etc,
            'DASH': itemrange.deposit_max_dash,
        }
        if list_active_in[name_ps_get] == 1:
            if request_sum <= list_deposit_max[name_ps_get] and (request_sum * currencysort.base_currency) < item.balance:
                changeq.append(item)
    return {'changeq': changeq, 'valute': valute_ps_get}


# активность обменника и направлений для вывода
def widthsortchangeps(nameps, request_sum):
    itemchange = CustomUser.objects.filter(userid__custuserid='Владелец Обменника', is_active_change=1)
    changeq = []
    currencysort_list = CurrencyCBRF.objects.all()
    itemrange_list = RangeSumWidth.objects.all()

    name_ps_list = {
        'СБЕРБАНК': 'RUB',
        'ТИНЬКОФФ': 'RUB',
        'АЛЬФА БАНК': 'RUB',
        'ВТБ': 'RUB',
        'РАЙФФАЙЗЕНБАНК': 'RUB',
        'ОТКРЫТИЕ': 'RUB',
        'ПСБ': 'RUB',
        'ГАЗПРОМБАНК': 'RUB',
        'РУССКИЙ СТАНДАРТ': 'RUB',
        'РОССЕЛЬХОЗБАНК': 'RUB',
        'ПОЧТА БАНК': 'RUB',
        'РОСБАНК': 'RUB',
        'РНКБ': 'RUB',
        'МТС БАНК': 'RUB',
        'QIWI RUB': 'RUB',
        'QIWI USD': 'USD',
        'PAYEER RUB': 'RUB',
        'PAYEER EUR': 'EUR',
        'PAYEER USD': 'USD',
        'WEBMONEY RUB': 'RUB',
        'WEBMONEY EUR': 'EUR',
        'WEBMONEY USD': 'USD',
        'PERFECT MONEY BTC': 'BTC',
        'PERFECT MONEY EUR': 'EUR',
        'PERFECT MONEY USD': 'USD',
        'PAYPAL RUB': 'RUB',
        'PAYPAL EUR': 'EUR',
        'PAYPAL USD': 'USD',
        'SKRILL EUR': 'EUR',
        'SKRILL USD': 'USD',
        'UMONEY RUB': 'RUB',
        'BITCOIN': 'BTC',
        'LITECOIN': 'LTC',
        'MONERO': 'XMR',
        'ETHEREUM CLASSIC': 'ETC',
        'DASH': 'DASH',
        'RIPPLE': 'XRP',
        'BITCOIN CASH': 'BCH',
        'ETHEREUM': 'ETH',
    }

    name_ps_get = nameps
    valute_ps_get = name_ps_list[nameps]
    currencysort = currencysort_list.get(name_currency=valute_ps_get)

    for item in itemchange:
        itemrange = itemrange_list.get(width_range_username=item)
        list_active_out = {
            'СБЕРБАНК': item.active_out_sberbank_rub,
            'ПСБ': item.active_out_psb_rub,
            'ТИНЬКОФФ': item.active_out_tinkoff_rub,
            'ГАЗПРОМБАНК': item.active_out_gazprombank_rub,
            'АЛЬФА БАНК': item.active_out_alfabank_rub,
            'РУССКИЙ СТАНДАРТ': item.active_out_russtandart_rub,
            'ВТБ': item.active_out_vtb_rub,
            'РОССЕЛЬХОЗБАНК': item.active_out_rosselhoz_rub,
            'РАЙФФАЙЗЕНБАНК': item.active_out_raifaizen_rub,
            'ОТКРЫТИЕ': item.active_out_otkritie_rub,
            'ПОЧТА БАНК': item.active_out_pochtabank_rub,
            'РНКБ': item.active_out_rnkb_rub,
            'РОСБАНК': item.active_out_rosbank_rub,
            'МТС БАНК': item.active_out_mtsbank_rub,
            'QIWI RUB': item.active_out_qiwi_rub,
            'QIWI USD': item.active_out_qiwi_usd,
            'PAYEER RUB': item.active_out_payeer_rub,
            'PAYEER USD': item.active_out_payeer_usd,
            'PAYEER EUR': item.active_out_payeer_eur,
            'WEBMONEY RUB': item.active_out_webmoney_rub,
            'WEBMONEY USD': item.active_out_webmoney_usd,
            'WEBMONEY EUR': item.active_out_webmoney_eur,
            'PERFECT MONEY BTC': item.active_out_pm_btc,
            'PERFECT MONEY USD': item.active_out_pm_usd,
            'PERFECT MONEY EUR': item.active_out_pm_eur,
            'SKRILL EUR': item.active_out_skrill_eur,
            'SKRILL USD': item.active_out_skrill_usd,
            'PAYPAL RUB': item.active_out_paypal_rub,
            'PAYPAL USD': item.active_out_paypal_usd,
            'PAYPAL EUR': item.active_out_paypal_eur,
            'UMONEY RUB': item.active_out_umoney_rub,
            'BITCOIN': item.active_out_btc,
            'RIPPLE': item.active_out_xrp,
            'LITECOIN': item.active_out_ltc,
            'BITCOIN CASH': item.active_out_bch,
            'MONERO': item.active_out_xmr,
            'ETHEREUM': item.active_out_eth,
            'ETHEREUM CLASSIC': item.active_out_etc,
            'DASH': item.active_out_dash,
        }
        list_width_max = {
            'СБЕРБАНК': itemrange.width_max_sberbank_rub,
            'ПСБ': itemrange.width_max_psb_rub,
            'ТИНЬКОФФ': itemrange.width_max_tinkoff_rub,
            'ГАЗПРОМБАНК': itemrange.width_max_gazprombank_rub,
            'АЛЬФА БАНК': itemrange.width_max_alfabank_rub,
            'РУССКИЙ СТАНДАРТ': itemrange.width_max_russtandart_rub,
            'ВТБ': itemrange.width_max_vtb_rub,
            'РОССЕЛЬХОЗБАНК': itemrange.width_max_rosselhoz_rub,
            'РАЙФФАЙЗЕНБАНК': itemrange.width_max_raifaizen_rub,
            'ОТКРЫТИЕ': itemrange.width_max_otkritie_rub,
            'ПОЧТА БАНК': itemrange.width_max_pochtabank_rub,
            'РНКБ': itemrange.width_max_rnkb_rub,
            'РОСБАНК': itemrange.width_max_rosbank_rub,
            'МТС БАНК': itemrange.width_max_mtsbank_rub,
            'QIWI RUB': itemrange.width_max_qiwi_rub,
            'QIWI USD': itemrange.width_max_qiwi_usd,
            'PAYEER RUB': itemrange.width_max_payeer_rub,
            'PAYEER USD': itemrange.width_max_payeer_usd,
            'PAYEER EUR': itemrange.width_max_payeer_eur,
            'WEBMONEY RUB': itemrange.width_max_webmoney_rub,
            'WEBMONEY USD': itemrange.width_max_webmoney_usd,
            'WEBMONEY EUR': itemrange.width_max_webmoney_eur,
            'PERFECT MONEY BTC': itemrange.width_max_pm_btc,
            'PERFECT MONEY USD': itemrange.width_max_pm_usd,
            'PERFECT MONEY EUR': itemrange.width_max_pm_eur,
            'SKRILL EUR': itemrange.width_max_skrill_eur,
            'SKRILL USD': itemrange.width_max_skrill_usd,
            'PAYPAL RUB': itemrange.width_max_paypal_rub,
            'PAYPAL USD': itemrange.width_max_paypal_usd,
            'PAYPAL EUR': itemrange.width_max_paypal_eur,
            'UMONEY RUB': itemrange.width_max_umoney_rub,
            'BITCOIN': itemrange.width_max_btc,
            'RIPPLE': itemrange.width_max_xrp,
            'LITECOIN': itemrange.width_max_ltc,
            'BITCOIN CASH': itemrange.width_max_bch,
            'MONERO': itemrange.width_max_xmr,
            'ETHEREUM': itemrange.width_max_eth,
            'ETHEREUM CLASSIC': itemrange.width_max_etc,
            'DASH': itemrange.width_max_dash,
        }
        list_reserv = {
            'СБЕРБАНК': item.reserv_sberbank_rub,
            'ПСБ': item.reserv_psb_rub,
            'ТИНЬКОФФ': item.reserv_tinkoff_rub,
            'ГАЗПРОМБАНК': item.reserv_gazprombank_rub,
            'АЛЬФА БАНК': item.reserv_alfabank_rub,
            'РУССКИЙ СТАНДАРТ': item.reserv_russtandart_rub,
            'ВТБ': item.reserv_vtb_rub,
            'РОССЕЛЬХОЗБАНК': item.reserv_rosselhoz_rub,
            'РАЙФФАЙЗЕНБАНК': item.reserv_raifaizen_rub,
            'ОТКРЫТИЕ': item.reserv_otkritie_rub,
            'ПОЧТА БАНК': item.reserv_pochtabank_rub,
            'РНКБ': item.reserv_rnkb_rub,
            'РОСБАНК': item.reserv_rosbank_rub,
            'МТС БАНК': item.reserv_mtsbank_rub,
            'QIWI RUB': item.reserv_qiwi_rub,
            'QIWI USD': item.reserv_qiwi_usd,
            'PAYEER RUB': item.reserv_payeer_rub,
            'PAYEER USD': item.reserv_payeer_usd,
            'PAYEER EUR': item.reserv_payeer_eur,
            'WEBMONEY RUB': item.reserv_webmoney_rub,
            'WEBMONEY USD': item.reserv_webmoney_usd,
            'WEBMONEY EUR': item.reserv_webmoney_eur,
            'PERFECT MONEY BTC': item.reserv_pm_btc,
            'PERFECT MONEY USD': item.reserv_pm_usd,
            'PERFECT MONEY EUR': item.reserv_pm_eur,
            'SKRILL EUR': item.reserv_skrill_eur,
            'SKRILL USD': item.reserv_skrill_usd,
            'PAYPAL RUB': item.reserv_paypal_rub,
            'PAYPAL USD': item.reserv_paypal_usd,
            'PAYPAL EUR': item.reserv_paypal_eur,
            'UMONEY RUB': item.reserv_umoney_rub,
            'BITCOIN': item.reserv_btc,
            'RIPPLE': item.reserv_xrp,
            'LITECOIN': item.reserv_ltc,
            'BITCOIN CASH': item.reserv_bch,
            'MONERO': item.reserv_xmr,
            'ETHEREUM': item.reserv_eth,
            'ETHEREUM CLASSIC': item.reserv_etc,
            'DASH': item.reserv_dash,
        }
        if list_active_out[name_ps_get] == 1:
            if request_sum <= list_width_max[name_ps_get] * currencysort.base_currency and list_reserv[name_ps_get] * currencysort.base_currency > request_sum:
                changeq.append(item)
    return {'changeq': changeq, 'valute': valute_ps_get}


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
                    if time.date_end_change and time.date_change_request and time.request_type == 'Заявка на пополнение':
                        timelimit = time.date_end_change - time.date_change_request
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

        if userrandom:
            usernameps = random.choice(userrandom)

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

        if userrandom:
            usernameps = random.choice(userrandom)

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
        elif i.request_type == 'Мерчант пополнение' and i.request_status == 'Оплачена':
            requesttargetin += 1
        elif i.request_type == 'Мерчант вывод' and i.request_status == 'Ожидает оплаты':
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
            if iteml.request_type == 'Заявка на пополнение' or iteml.request_type == 'Мерчант пополнение':
                inrequest += 1
            if iteml.request_type == 'Заявка на вывод' or iteml.request_type == 'Мерчант вывод':
                widthrequest += 1
    if requestuserlist:
        for item in requestuserlist:
            if item.request_type == 'Заявка на пополнение' or item.request_type == 'Мерчант пополнение' and item.date_end_change:
                inrequesttotal += 1
            if item.request_type == 'Заявка на вывод' or item.request_type == 'Мерчант вывод' and item.date_end_change:
                widthrequesttotal += 1
    return {'inrequest': inrequest, 'inrequesttotal': inrequesttotal, 'widthrequest': widthrequest, 'widthrequesttotal': widthrequesttotal}


# получение общего резерва обменников на пополнение
def active_deposit_ps_global():
    list_change = CustomUser.objects.filter(userid__custuserid='Владелец Обменника', is_active_change=1)
    currency = CurrencyCBRF.objects.all()
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
    list_active_reserve_ps = {
        'sberbank_rub': 0, 'psb_rub': 0, 'tinkoff_rub': 0, 'gazprombank_rub': 0, 'alfabank_rub': 0, 'russtandart_rub': 0,
        'vtb_rub': 0, 'rosselhoz_rub': 0, 'raifaizen_rub': 0, 'otkritie_rub': 0, 'pochtabank_rub': 0, 'rnkb_rub': 0,
        'rosbank_rub': 0, 'mtsbank_rub': 0, 'qiwi_rub': 0, 'qiwi_usd': 0, 'payeer_rub': 0, 'payeer_usd': 0,
        'payeer_eur': 0, 'webmoney_rub': 0, 'webmoney_usd': 0, 'webmoney_eur': 0, 'pm_btc': 0, 'pm_usd': 0,
        'pm_eur': 0, 'skrill_eur': 0, 'skrill_usd': 0, 'paypal_rub': 0, 'paypal_usd': 0, 'paypal_eur': 0, 'umoney_rub': 0,
        'btc': 0, 'xrp': 0, 'ltc': 0, 'bch': 0, 'xmr': 0, 'eth': 0, 'etc': 0, 'dash': 0
    }
    list_get_valute = {
        'sberbank_rub': 0, 'psb_rub': 0, 'tinkoff_rub': 0, 'gazprombank_rub': 0, 'alfabank_rub': 0, 'russtandart_rub': 0,
        'vtb_rub': 0, 'rosselhoz_rub': 0, 'raifaizen_rub': 0, 'otkritie_rub': 0, 'pochtabank_rub': 0, 'rnkb_rub': 0,
        'rosbank_rub': 0, 'mtsbank_rub': 0, 'qiwi_rub': 0, 'qiwi_usd': 0, 'payeer_rub': 0, 'payeer_usd': 0,
        'payeer_eur': 0, 'webmoney_rub': 0, 'webmoney_usd': 0, 'webmoney_eur': 0, 'pm_usd': 0,
        'pm_eur': 0, 'skrill_eur': 0, 'skrill_usd': 0, 'paypal_rub': 0, 'paypal_usd': 0, 'paypal_eur': 0, 'umoney_rub': 0
    }
    list_get_crypto = {
        'pm_btc': 0, 'btc': 0, 'xrp': 0, 'ltc': 0, 'bch': 0, 'xmr': 0, 'eth': 0, 'etc': 0, 'dash': 0
    }

    list_active_user = []
    for change in list_change:
        if RangeSumDeposit.objects.filter(deposit_range_username=change).exists():
            list_active_in = {
                'sberbank_rub': change.active_in_sberbank_rub,
                'psb_rub': change.active_in_psb_rub,
                'tinkoff_rub': change.active_in_tinkoff_rub,
                'gazprombank_rub': change.active_in_gazprombank_rub,
                'alfabank_rub': change.active_in_alfabank_rub,
                'russtandart_rub': change.active_in_russtandart_rub,
                'vtb_rub': change.active_in_vtb_rub,
                'rosselhoz_rub': change.active_in_rosselhoz_rub,
                'raifaizen_rub': change.active_in_raifaizen_rub,
                'otkritie_rub': change.active_in_otkritie_rub,
                'pochtabank_rub': change.active_in_pochtabank_rub,
                'rnkb_rub': change.active_in_rnkb_rub,
                'rosbank_rub': change.active_in_rosbank_rub,
                'mtsbank_rub': change.active_in_mtsbank_rub,
                'qiwi_rub': change.active_in_qiwi_rub,
                'qiwi_usd': change.active_in_qiwi_usd,
                'payeer_rub': change.active_in_payeer_rub,
                'payeer_usd': change.active_in_payeer_usd,
                'payeer_eur': change.active_in_payeer_eur,
                'webmoney_rub': change.active_in_webmoney_rub,
                'webmoney_usd': change.active_in_webmoney_usd,
                'webmoney_eur': change.active_in_webmoney_eur,
                'pm_btc': change.active_in_pm_btc,
                'pm_usd': change.active_in_pm_usd,
                'pm_eur': change.active_in_pm_eur,
                'skrill_eur': change.active_in_skrill_eur,
                'skrill_usd': change.active_in_skrill_usd,
                'paypal_rub': change.active_in_paypal_rub,
                'paypal_usd': change.active_in_paypal_usd,
                'paypal_eur': change.active_in_paypal_eur,
                'umoney_rub': change.active_in_umoney_rub,
                'btc': change.active_in_btc,
                'xrp': change.active_in_xrp,
                'ltc': change.active_in_ltc,
                'bch': change.active_in_bch,
                'xmr': change.active_in_xmr,
                'eth': change.active_in_eth,
                'etc': change.active_in_etc,
                'dash': change.active_in_dash,
            }
            list_balance = {
                'sberbank_rub': change.balance/currencyget_rub,
                'psb_rub': change.balance/currencyget_rub,
                'tinkoff_rub': change.balance/currencyget_rub,
                'gazprombank_rub': change.balance/currencyget_rub,
                'alfabank_rub': change.balance/currencyget_rub,
                'russtandart_rub': change.balance/currencyget_rub,
                'vtb_rub': change.balance/currencyget_rub,
                'rosselhoz_rub': change.balance/currencyget_rub,
                'raifaizen_rub': change.balance/currencyget_rub,
                'otkritie_rub': change.balance/currencyget_rub,
                'pochtabank_rub': change.balance/currencyget_rub,
                'rnkb_rub': change.balance/currencyget_rub,
                'rosbank_rub': change.balance/currencyget_rub,
                'mtsbank_rub': change.balance/currencyget_rub,
                'qiwi_rub': change.balance/currencyget_rub,
                'qiwi_usd': change.balance/currencyget_usd,
                'payeer_rub': change.balance/currencyget_rub,
                'payeer_usd': change.balance/currencyget_usd,
                'payeer_eur': change.balance/currencyget_eur,
                'webmoney_rub': change.balance/currencyget_rub,
                'webmoney_usd': change.balance/currencyget_usd,
                'webmoney_eur': change.balance/currencyget_eur,
                'pm_btc': change.balance/currencyget_btc,
                'pm_usd': change.balance/currencyget_usd,
                'pm_eur': change.balance/currencyget_eur,
                'skrill_eur': change.balance/currencyget_eur,
                'skrill_usd': change.balance/currencyget_usd,
                'paypal_rub': change.balance/currencyget_rub,
                'paypal_usd': change.balance/currencyget_eur,
                'paypal_eur': change.balance/currencyget_eur,
                'umoney_rub': change.balance/currencyget_rub,
                'btc': change.balance/currencyget_btc,
                'xrp': change.balance/currencyget_xrp,
                'ltc': change.balance/currencyget_ltc,
                'bch': change.balance/currencyget_bch,
                'xmr': change.balance/currencyget_xmr,
                'eth': change.balance/currencyget_eth,
                'etc': change.balance/currencyget_etc,
                'dash': change.balance/currencyget_dash,
            }

            for k, v in list_active_in.items():
                if v == 1:
                    if list_get_valute.get(k) is not None:
                        list_active_reserve_ps[k] = round(list_active_reserve_ps[k] + list_balance[k], 2)
                    elif list_get_crypto.get(k) is not None:
                        list_active_reserve_ps[k] = round(list_active_reserve_ps[k] + list_balance[k], 8)
                    if list_active_user.count(change) < 1:
                        list_active_user.append(change)
    return {'list_active_reserve_ps': list_active_reserve_ps, 'list_active_user': list_active_user}


# общий резерв всех обменников на вывод
def active_width_ps_global():
    list_change = CustomUser.objects.filter(userid__custuserid='Владелец Обменника', is_active_change=1)
    currency = CurrencyCBRF.objects.all()
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
    list_active_reserve_ps = {
        'sberbank_rub': 0, 'psb_rub': 0, 'tinkoff_rub': 0, 'gazprombank_rub': 0, 'alfabank_rub': 0, 'russtandart_rub': 0,
        'vtb_rub': 0, 'rosselhoz_rub': 0, 'raifaizen_rub': 0, 'otkritie_rub': 0, 'pochtabank_rub': 0, 'rnkb_rub': 0,
        'rosbank_rub': 0, 'mtsbank_rub': 0, 'qiwi_rub': 0, 'qiwi_usd': 0, 'payeer_rub': 0, 'payeer_usd': 0,
        'payeer_eur': 0, 'webmoney_rub': 0, 'webmoney_usd': 0, 'webmoney_eur': 0, 'pm_btc': 0, 'pm_usd': 0,
        'pm_eur': 0, 'skrill_eur': 0, 'skrill_usd': 0, 'paypal_rub': 0, 'paypal_usd': 0, 'paypal_eur': 0, 'umoney_rub': 0,
        'btc': 0, 'xrp': 0, 'ltc': 0, 'bch': 0, 'xmr': 0, 'eth': 0, 'etc': 0, 'dash': 0
    }
    list_active_user = []
    for change in list_change:
        if RangeSumWidth.objects.filter(width_range_username=change).exists():
            list_active_out = {
                'sberbank_rub': change.active_out_sberbank_rub,
                'psb_rub': change.active_out_psb_rub,
                'tinkoff_rub': change.active_out_tinkoff_rub,
                'gazprombank_rub': change.active_out_gazprombank_rub,
                'alfabank_rub': change.active_out_alfabank_rub,
                'russtandart_rub': change.active_out_russtandart_rub,
                'vtb_rub': change.active_out_vtb_rub,
                'rosselhoz_rub': change.active_out_rosselhoz_rub,
                'raifaizen_rub': change.active_out_raifaizen_rub,
                'otkritie_rub': change.active_out_otkritie_rub,
                'pochtabank_rub': change.active_out_pochtabank_rub,
                'rnkb_rub': change.active_out_rnkb_rub,
                'rosbank_rub': change.active_out_rosbank_rub,
                'mtsbank_rub': change.active_out_mtsbank_rub,
                'qiwi_rub': change.active_out_qiwi_rub,
                'qiwi_usd': change.active_out_qiwi_usd,
                'payeer_rub': change.active_out_payeer_rub,
                'payeer_usd': change.active_out_payeer_usd,
                'payeer_eur': change.active_out_payeer_eur,
                'webmoney_rub': change.active_out_webmoney_rub,
                'webmoney_usd': change.active_out_webmoney_usd,
                'webmoney_eur': change.active_out_webmoney_eur,
                'pm_btc': change.active_out_pm_btc,
                'pm_usd': change.active_out_pm_usd,
                'pm_eur': change.active_out_pm_eur,
                'skrill_eur': change.active_out_skrill_eur,
                'skrill_usd': change.active_out_skrill_usd,
                'paypal_rub': change.active_out_paypal_rub,
                'paypal_usd': change.active_out_paypal_usd,
                'paypal_eur': change.active_out_paypal_eur,
                'umoney_rub': change.active_out_umoney_rub,
                'btc': change.active_out_btc,
                'xrp': change.active_out_xrp,
                'ltc': change.active_out_ltc,
                'bch': change.active_out_bch,
                'xmr': change.active_out_xmr,
                'eth': change.active_out_eth,
                'etc': change.active_out_etc,
                'dash': change.active_out_dash,
            }
            list_reserve = {
                'sberbank_rub': change.reserv_sberbank_rub*currencyget_rub,
                'psb_rub': change.reserv_psb_rub*currencyget_rub,
                'tinkoff_rub': change.reserv_tinkoff_rub*currencyget_rub,
                'gazprombank_rub': change.reserv_gazprombank_rub*currencyget_rub,
                'alfabank_rub': change.reserv_alfabank_rub*currencyget_rub,
                'russtandart_rub': change.reserv_russtandart_rub*currencyget_rub,
                'vtb_rub': change.reserv_vtb_rub*currencyget_rub,
                'rosselhoz_rub': change.reserv_rosselhoz_rub*currencyget_rub,
                'raifaizen_rub': change.reserv_raifaizen_rub*currencyget_rub,
                'otkritie_rub': change.reserv_otkritie_rub*currencyget_rub,
                'pochtabank_rub': change.reserv_pochtabank_rub*currencyget_rub,
                'rnkb_rub': change.reserv_rnkb_rub*currencyget_rub,
                'rosbank_rub': change.reserv_rosbank_rub*currencyget_rub,
                'mtsbank_rub': change.reserv_mtsbank_rub*currencyget_rub,
                'qiwi_rub': change.reserv_qiwi_rub*currencyget_rub,
                'qiwi_usd': change.reserv_qiwi_usd*currencyget_usd,
                'payeer_rub': change.reserv_payeer_rub*currencyget_rub,
                'payeer_usd': change.reserv_payeer_usd*currencyget_usd,
                'payeer_eur': change.reserv_payeer_eur*currencyget_eur,
                'webmoney_rub': change.reserv_webmoney_rub*currencyget_rub,
                'webmoney_usd': change.reserv_webmoney_usd*currencyget_usd,
                'webmoney_eur': change.reserv_webmoney_eur*currencyget_eur,
                'pm_btc': change.reserv_pm_btc*currencyget_btc,
                'pm_usd': change.reserv_pm_usd*currencyget_usd,
                'pm_eur': change.reserv_pm_eur*currencyget_eur,
                'skrill_eur': change.reserv_skrill_eur*currencyget_eur,
                'skrill_usd': change.reserv_skrill_usd*currencyget_usd,
                'paypal_rub': change.reserv_paypal_rub*currencyget_rub,
                'paypal_usd': change.reserv_paypal_usd*currencyget_usd,
                'paypal_eur': change.reserv_paypal_eur*currencyget_eur,
                'umoney_rub': change.reserv_umoney_rub*currencyget_rub,
                'btc': change.reserv_btc*currencyget_btc,
                'xrp': change.reserv_xrp*currencyget_xrp,
                'ltc': change.reserv_ltc*currencyget_ltc,
                'bch': change.reserv_bch*currencyget_bch,
                'xmr': change.reserv_xmr*currencyget_xmr,
                'eth': change.reserv_eth*currencyget_eth,
                'etc': change.reserv_etc*currencyget_etc,
                'dash': change.reserv_dash*currencyget_dash,
            }

            for k, v in list_active_out.items():
                if v == 1:
                    list_active_reserve_ps[k] = int(list_active_reserve_ps[k] + list_reserve[k])
                    if list_active_user.count(change) < 1:
                        list_active_user.append(change)
    return {'list_active_reserve_ps': list_active_reserve_ps, 'list_active_user': list_active_user}


# лимиты для заявок на пополнение
def range_deposit_ps_global(list_active_user):
    currency = CurrencyCBRF.objects.all()
    list_range_user = RangeSumDeposit.objects.all()
    active_list_ps = {
        'sberbank_rub': False, 'psb_rub': False, 'tinkoff_rub': False, 'gazprombank_rub': False, 'alfabank_rub': False,
        'russtandart_rub': False, 'vtb_rub': False, 'rosselhoz_rub': False, 'raifaizen_rub': False,
        'otkritie_rub': False, 'pochtabank_rub': False, 'rnkb_rub': False, 'rosbank_rub': False, 'mtsbank_rub': False,
        'qiwi_rub': False, 'qiwi_usd': False, 'payeer_rub': False, 'payeer_usd': False, 'payeer_eur': False,
        'webmoney_rub': False, 'webmoney_usd': False, 'webmoney_eur': False, 'pm_btc': False, 'pm_usd': False,
        'pm_eur': False, 'skrill_eur': False, 'skrill_usd': False, 'paypal_rub': False, 'paypal_usd': False,
        'paypal_eur': False, 'umoney_rub': False, 'btc': False, 'xrp': False, 'ltc': False, 'bch': False,
        'xmr': False, 'eth': False, 'etc': False, 'dash': False
    }
    list_range_min_reserve_ps = {
        'sberbank_rub': 0, 'psb_rub': 0, 'tinkoff_rub': 0, 'gazprombank_rub': 0, 'alfabank_rub': 0, 'russtandart_rub': 0,
        'vtb_rub': 0, 'rosselhoz_rub': 0, 'raifaizen_rub': 0, 'otkritie_rub': 0, 'pochtabank_rub': 0, 'rnkb_rub': 0,
        'rosbank_rub': 0, 'mtsbank_rub': 0, 'qiwi_rub': 0, 'qiwi_usd': 0, 'payeer_rub': 0, 'payeer_usd': 0,
        'payeer_eur': 0, 'webmoney_rub': 0, 'webmoney_usd': 0, 'webmoney_eur': 0, 'pm_btc': 0, 'pm_usd': 0,
        'pm_eur': 0, 'skrill_eur': 0, 'skrill_usd': 0, 'paypal_rub': 0, 'paypal_usd': 0, 'paypal_eur': 0, 'umoney_rub': 0,
        'btc': 0, 'xrp': 0, 'ltc': 0, 'bch': 0, 'xmr': 0, 'eth': 0, 'etc': 0, 'dash': 0
    }
    list_range_max_reserve_ps = {
        'sberbank_rub': 0, 'psb_rub': 0, 'tinkoff_rub': 0, 'gazprombank_rub': 0, 'alfabank_rub': 0, 'russtandart_rub': 0,
        'vtb_rub': 0, 'rosselhoz_rub': 0, 'raifaizen_rub': 0, 'otkritie_rub': 0, 'pochtabank_rub': 0, 'rnkb_rub': 0,
        'rosbank_rub': 0, 'mtsbank_rub': 0, 'qiwi_rub': 0, 'qiwi_usd': 0, 'payeer_rub': 0, 'payeer_usd': 0,
        'payeer_eur': 0, 'webmoney_rub': 0, 'webmoney_usd': 0, 'webmoney_eur': 0, 'pm_btc': 0, 'pm_usd': 0,
        'pm_eur': 0, 'skrill_eur': 0, 'skrill_usd': 0, 'paypal_rub': 0, 'paypal_usd': 0, 'paypal_eur': 0, 'umoney_rub': 0,
        'btc': 0, 'xrp': 0, 'ltc': 0, 'bch': 0, 'xmr': 0, 'eth': 0, 'etc': 0, 'dash': 0
    }
    list_get_valute = {
        'sberbank_rub': 0, 'psb_rub': 0, 'tinkoff_rub': 0, 'gazprombank_rub': 0, 'alfabank_rub': 0, 'russtandart_rub': 0,
        'vtb_rub': 0, 'rosselhoz_rub': 0, 'raifaizen_rub': 0, 'otkritie_rub': 0, 'pochtabank_rub': 0, 'rnkb_rub': 0,
        'rosbank_rub': 0, 'mtsbank_rub': 0, 'qiwi_rub': 0, 'qiwi_usd': 0, 'payeer_rub': 0, 'payeer_usd': 0,
        'payeer_eur': 0, 'webmoney_rub': 0, 'webmoney_usd': 0, 'webmoney_eur': 0, 'pm_usd': 0,
        'pm_eur': 0, 'skrill_eur': 0, 'skrill_usd': 0, 'paypal_rub': 0, 'paypal_usd': 0, 'paypal_eur': 0, 'umoney_rub': 0
    }
    list_get_crypto = {
        'pm_btc': 0, 'btc': 0, 'xrp': 0, 'ltc': 0, 'bch': 0, 'xmr': 0, 'eth': 0, 'etc': 0, 'dash': 0
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

    for userrange in list_active_user:
        try:
            list_range = list_range_user.get(deposit_range_username=userrange)
            list_min_range = {
                'sberbank_rub': list_range.deposit_min_sberbank_rub,
                'psb_rub': list_range.deposit_min_psb_rub,
                'tinkoff_rub': list_range.deposit_min_tinkoff_rub,
                'gazprombank_rub': list_range.deposit_min_gazprombank_rub,
                'alfabank_rub': list_range.deposit_min_alfabank_rub,
                'russtandart_rub': list_range.deposit_min_russtandart_rub,
                'vtb_rub': list_range.deposit_min_vtb_rub,
                'rosselhoz_rub': list_range.deposit_min_rosselhoz_rub,
                'raifaizen_rub': list_range.deposit_min_raifaizen_rub,
                'otkritie_rub': list_range.deposit_min_otkritie_rub,
                'pochtabank_rub': list_range.deposit_min_pochtabank_rub,
                'rnkb_rub': list_range.deposit_min_rnkb_rub,
                'rosbank_rub': list_range.deposit_min_rosbank_rub,
                'mtsbank_rub': list_range.deposit_min_mtsbank_rub,
                'qiwi_rub': list_range.deposit_min_qiwi_rub,
                'qiwi_usd': list_range.deposit_min_qiwi_usd,
                'payeer_rub': list_range.deposit_min_payeer_rub,
                'payeer_usd': list_range.deposit_min_payeer_usd,
                'payeer_eur': list_range.deposit_min_payeer_eur,
                'webmoney_rub': list_range.deposit_min_webmoney_rub,
                'webmoney_usd': list_range.deposit_min_webmoney_usd,
                'webmoney_eur': list_range.deposit_min_webmoney_eur,
                'pm_btc': list_range.deposit_min_pm_btc,
                'pm_usd': list_range.deposit_min_pm_usd,
                'pm_eur': list_range.deposit_min_pm_eur,
                'skrill_eur': list_range.deposit_min_skrill_eur,
                'skrill_usd': list_range.deposit_min_skrill_usd,
                'paypal_rub': list_range.deposit_min_paypal_rub,
                'paypal_usd': list_range.deposit_min_paypal_usd,
                'paypal_eur': list_range.deposit_min_paypal_eur,
                'umoney_rub': list_range.deposit_min_umoney_rub,
                'btc': list_range.deposit_min_btc,
                'xrp': list_range.deposit_min_xrp,
                'ltc': list_range.deposit_min_ltc,
                'bch': list_range.deposit_min_bch,
                'xmr': list_range.deposit_min_xmr,
                'eth': list_range.deposit_min_eth,
                'etc': list_range.deposit_min_etc,
                'dash': list_range.deposit_min_dash,
            }
            # Получаем минимальный лимит
            for min_range_k, min_range_v in list_min_range.items():
                if min_range_v > 0:
                    if list_range_min_reserve_ps[min_range_k] != 0:
                        if min_range_v < list_range_min_reserve_ps[min_range_k]:
                            if list_get_valute.get(min_range_k) is not None:
                                list_range_min_reserve_ps[min_range_k] = round(min_range_v, 2)
                            elif list_get_crypto.get(min_range_k) is not None:
                                list_range_min_reserve_ps[min_range_k] = round(min_range_v, 8)
                    else:
                        if list_get_valute.get(min_range_k) is not None:
                            list_range_min_reserve_ps[min_range_k] = round(min_range_v, 2)
                        elif list_get_crypto.get(min_range_k) is not None:
                            list_range_min_reserve_ps[min_range_k] = round(min_range_v, 8)

            # Получаем максимальный лимит
            list_max_range = {
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
                'dash': list_range.deposit_max_dash,
            }
            list_balance_change = {
                'sberbank_rub': userrange.balance/currencyget_rub,
                'psb_rub': userrange.balance/currencyget_rub,
                'tinkoff_rub': userrange.balance/currencyget_rub,
                'gazprombank_rub': userrange.balance/currencyget_rub,
                'alfabank_rub': userrange.balance/currencyget_rub,
                'russtandart_rub': userrange.balance/currencyget_rub,
                'vtb_rub': userrange.balance/currencyget_rub,
                'rosselhoz_rub': userrange.balance/currencyget_rub,
                'raifaizen_rub': userrange.balance/currencyget_rub,
                'otkritie_rub': userrange.balance/currencyget_rub,
                'pochtabank_rub': userrange.balance/currencyget_rub,
                'rnkb_rub': userrange.balance/currencyget_rub,
                'rosbank_rub': userrange.balance/currencyget_rub,
                'mtsbank_rub': userrange.balance/currencyget_rub,
                'qiwi_rub': userrange.balance/currencyget_rub,
                'qiwi_usd': userrange.balance/currencyget_usd,
                'payeer_rub': userrange.balance/currencyget_rub,
                'payeer_usd': userrange.balance/currencyget_usd,
                'payeer_eur': userrange.balance/currencyget_eur,
                'webmoney_rub': userrange.balance/currencyget_rub,
                'webmoney_usd': userrange.balance/currencyget_usd,
                'webmoney_eur': userrange.balance/currencyget_eur,
                'pm_btc': userrange.balance/currencyget_btc,
                'pm_usd': userrange.balance/currencyget_usd,
                'pm_eur': userrange.balance/currencyget_eur,
                'skrill_eur': userrange.balance/currencyget_eur,
                'skrill_usd': userrange.balance/currencyget_usd,
                'paypal_rub': userrange.balance/currencyget_rub,
                'paypal_usd': userrange.balance/currencyget_usd,
                'paypal_eur': userrange.balance/currencyget_eur,
                'umoney_rub': userrange.balance/currencyget_rub,
                'btc': userrange.balance/currencyget_btc,
                'xrp': userrange.balance/currencyget_xrp,
                'ltc': userrange.balance/currencyget_ltc,
                'bch': userrange.balance/currencyget_bch,
                'xmr': userrange.balance/currencyget_xmr,
                'eth': userrange.balance/currencyget_eth,
                'etc': userrange.balance/currencyget_etc,
                'dash': userrange.balance/currencyget_dash,
            }
            for max_range_k, max_range_v in list_max_range.items():
                if list_range_min_reserve_ps[max_range_k] < max_range_v and list_range_min_reserve_ps[max_range_k] > 0 and list_balance_change[max_range_k] > list_range_min_reserve_ps[max_range_k]:
                    min_max_range = min([max_range_v, list_balance_change[max_range_k]])
                    if min_max_range > list_range_max_reserve_ps[max_range_k]:
                        if list_get_valute.get(max_range_k) is not None:
                            list_range_max_reserve_ps[max_range_k] = round(min_max_range-(min_max_range/100), 2)
                        elif list_get_crypto.get(max_range_k) is not None:
                            list_range_max_reserve_ps[max_range_k] = round(min_max_range-(min_max_range/100), 8)
                        active_list_ps[max_range_k] = True
        except:
            pass

    return {'list_range_min_reserve_ps': list_range_min_reserve_ps,
            'list_range_max_reserve_ps': list_range_max_reserve_ps,
            'active_list_ps': active_list_ps}


# лимиты для заявок на вывод
def range_width_ps_global(list_active_user, balance_user):
    currency = CurrencyCBRF.objects.all()
    list_range_user = RangeSumWidth.objects.all()
    active_list_ps = {
        'sberbank_rub': False, 'psb_rub': False, 'tinkoff_rub': False, 'gazprombank_rub': False, 'alfabank_rub': False,
        'russtandart_rub': False, 'vtb_rub': False, 'rosselhoz_rub': False, 'raifaizen_rub': False,
        'otkritie_rub': False, 'pochtabank_rub': False, 'rnkb_rub': False, 'rosbank_rub': False, 'mtsbank_rub': False,
        'qiwi_rub': False, 'qiwi_usd': False, 'payeer_rub': False, 'payeer_usd': False, 'payeer_eur': False,
        'webmoney_rub': False, 'webmoney_usd': False, 'webmoney_eur': False, 'pm_btc': False, 'pm_usd': False,
        'pm_eur': False, 'skrill_eur': False, 'skrill_usd': False, 'paypal_rub': False, 'paypal_usd': False,
        'paypal_eur': False, 'umoney_rub': False, 'btc': False, 'xrp': False, 'ltc': False, 'bch': False,
        'xmr': False, 'eth': False, 'etc': False, 'dash': False
    }
    list_range_min_reserve_ps = {
        'sberbank_rub': 0, 'psb_rub': 0, 'tinkoff_rub': 0, 'gazprombank_rub': 0, 'alfabank_rub': 0, 'russtandart_rub': 0,
        'vtb_rub': 0, 'rosselhoz_rub': 0, 'raifaizen_rub': 0, 'otkritie_rub': 0, 'pochtabank_rub': 0, 'rnkb_rub': 0,
        'rosbank_rub': 0, 'mtsbank_rub': 0, 'qiwi_rub': 0, 'qiwi_usd': 0, 'payeer_rub': 0, 'payeer_usd': 0,
        'payeer_eur': 0, 'webmoney_rub': 0, 'webmoney_usd': 0, 'webmoney_eur': 0, 'pm_btc': 0, 'pm_usd': 0,
        'pm_eur': 0, 'skrill_eur': 0, 'skrill_usd': 0, 'paypal_rub': 0, 'paypal_usd': 0, 'paypal_eur': 0, 'umoney_rub': 0,
        'btc': 0, 'xrp': 0, 'ltc': 0, 'bch': 0, 'xmr': 0, 'eth': 0, 'etc': 0, 'dash': 0
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

    for userrange in list_active_user:
        try:
            list_range = list_range_user.get(width_range_username=userrange)
            list_min_range = {
                'sberbank_rub': list_range.width_min_sberbank_rub*currencyget_rub,
                'psb_rub': list_range.width_min_psb_rub*currencyget_rub,
                'tinkoff_rub': list_range.width_min_tinkoff_rub*currencyget_rub,
                'gazprombank_rub': list_range.width_min_gazprombank_rub*currencyget_rub,
                'alfabank_rub': list_range.width_min_alfabank_rub*currencyget_rub,
                'russtandart_rub': list_range.width_min_russtandart_rub*currencyget_rub,
                'vtb_rub': list_range.width_min_vtb_rub*currencyget_rub,
                'rosselhoz_rub': list_range.width_min_rosselhoz_rub*currencyget_rub,
                'raifaizen_rub': list_range.width_min_raifaizen_rub*currencyget_rub,
                'otkritie_rub': list_range.width_min_otkritie_rub*currencyget_rub,
                'pochtabank_rub': list_range.width_min_pochtabank_rub*currencyget_rub,
                'rnkb_rub': list_range.width_min_rnkb_rub*currencyget_rub,
                'rosbank_rub': list_range.width_min_rosbank_rub*currencyget_rub,
                'mtsbank_rub': list_range.width_min_mtsbank_rub*currencyget_rub,
                'qiwi_rub': list_range.width_min_qiwi_rub*currencyget_rub,
                'qiwi_usd': list_range.width_min_qiwi_usd*currencyget_usd,
                'payeer_rub': list_range.width_min_payeer_rub*currencyget_rub,
                'payeer_usd': list_range.width_min_payeer_usd*currencyget_usd,
                'payeer_eur': list_range.width_min_payeer_eur*currencyget_eur,
                'webmoney_rub': list_range.width_min_webmoney_rub*currencyget_rub,
                'webmoney_usd': list_range.width_min_webmoney_usd*currencyget_usd,
                'webmoney_eur': list_range.width_min_webmoney_eur*currencyget_eur,
                'pm_btc': list_range.width_min_pm_btc*currencyget_btc,
                'pm_usd': list_range.width_min_pm_usd*currencyget_usd,
                'pm_eur': list_range.width_min_pm_eur*currencyget_eur,
                'skrill_eur': list_range.width_min_skrill_eur*currencyget_eur,
                'skrill_usd': list_range.width_min_skrill_usd*currencyget_usd,
                'paypal_rub': list_range.width_min_paypal_rub*currencyget_rub,
                'paypal_usd': list_range.width_min_paypal_usd*currencyget_usd,
                'paypal_eur': list_range.width_min_paypal_eur*currencyget_eur,
                'umoney_rub': list_range.width_min_umoney_rub*currencyget_rub,
                'btc': list_range.width_min_btc*currencyget_btc,
                'xrp': list_range.width_min_xrp*currencyget_xrp,
                'ltc': list_range.width_min_ltc*currencyget_ltc,
                'bch': list_range.width_min_bch*currencyget_bch,
                'xmr': list_range.width_min_xmr*currencyget_xmr,
                'eth': list_range.width_min_eth*currencyget_eth,
                'etc': list_range.width_min_etc*currencyget_etc,
                'dash': list_range.width_min_dash*currencyget_dash,
            }
            list_reserve = {
                'sberbank_rub': userrange.reserv_sberbank_rub*currencyget_rub,
                'psb_rub': userrange.reserv_psb_rub*currencyget_rub,
                'tinkoff_rub': userrange.reserv_tinkoff_rub*currencyget_rub,
                'gazprombank_rub': userrange.reserv_gazprombank_rub*currencyget_rub,
                'alfabank_rub': userrange.reserv_alfabank_rub*currencyget_rub,
                'russtandart_rub': userrange.reserv_russtandart_rub*currencyget_rub,
                'vtb_rub': userrange.reserv_vtb_rub*currencyget_rub,
                'rosselhoz_rub': userrange.reserv_rosselhoz_rub*currencyget_rub,
                'raifaizen_rub': userrange.reserv_raifaizen_rub*currencyget_rub,
                'otkritie_rub': userrange.reserv_otkritie_rub*currencyget_rub,
                'pochtabank_rub': userrange.reserv_pochtabank_rub*currencyget_rub,
                'rnkb_rub': userrange.reserv_rnkb_rub*currencyget_rub,
                'rosbank_rub': userrange.reserv_rosbank_rub*currencyget_rub,
                'mtsbank_rub': userrange.reserv_mtsbank_rub*currencyget_rub,
                'qiwi_rub': userrange.reserv_qiwi_rub*currencyget_rub,
                'qiwi_usd': userrange.reserv_qiwi_usd*currencyget_usd,
                'payeer_rub': userrange.reserv_payeer_rub*currencyget_rub,
                'payeer_usd': userrange.reserv_payeer_usd*currencyget_usd,
                'payeer_eur': userrange.reserv_payeer_eur*currencyget_eur,
                'webmoney_rub': userrange.reserv_webmoney_rub*currencyget_rub,
                'webmoney_usd': userrange.reserv_webmoney_usd*currencyget_usd,
                'webmoney_eur': userrange.reserv_webmoney_eur*currencyget_eur,
                'pm_btc': userrange.reserv_pm_btc*currencyget_btc,
                'pm_usd': userrange.reserv_pm_usd*currencyget_usd,
                'pm_eur': userrange.reserv_pm_eur*currencyget_eur,
                'skrill_eur': userrange.reserv_skrill_eur*currencyget_eur,
                'skrill_usd': userrange.reserv_skrill_usd*currencyget_usd,
                'paypal_rub': userrange.reserv_paypal_rub*currencyget_rub,
                'paypal_usd': userrange.reserv_paypal_usd*currencyget_usd,
                'paypal_eur': userrange.reserv_paypal_eur*currencyget_eur,
                'umoney_rub': userrange.reserv_umoney_rub*currencyget_rub,
                'btc': userrange.reserv_btc*currencyget_btc,
                'xrp': userrange.reserv_xrp*currencyget_xrp,
                'ltc': userrange.reserv_ltc*currencyget_ltc,
                'bch': userrange.reserv_bch*currencyget_bch,
                'xmr': userrange.reserv_xmr*currencyget_xmr,
                'eth': userrange.reserv_eth*currencyget_eth,
                'etc': userrange.reserv_etc*currencyget_etc,
                'dash': userrange.reserv_dash*currencyget_dash,
            }
            # Получаем минимальный лимит
            for min_range_k, min_range_v in list_min_range.items():
                if list_reserve[min_range_k] > min_range_v > 0:
                    if list_range_min_reserve_ps[min_range_k] != 0:
                        if min_range_v < list_range_min_reserve_ps[min_range_k]:
                            list_range_min_reserve_ps[min_range_k] = round(min_range_v, 2)
                    else:
                        list_range_min_reserve_ps[min_range_k] = round(min_range_v, 2)

            # Получаем максимальный лимит
            list_max_range = {
                'sberbank_rub': list_range.width_max_sberbank_rub*currencyget_rub,
                'psb_rub': list_range.width_max_psb_rub*currencyget_rub,
                'tinkoff_rub': list_range.width_max_tinkoff_rub*currencyget_rub,
                'gazprombank_rub': list_range.width_max_gazprombank_rub*currencyget_rub,
                'alfabank_rub': list_range.width_max_alfabank_rub*currencyget_rub,
                'russtandart_rub': list_range.width_max_russtandart_rub*currencyget_rub,
                'vtb_rub': list_range.width_max_vtb_rub*currencyget_rub,
                'rosselhoz_rub': list_range.width_max_rosselhoz_rub*currencyget_rub,
                'raifaizen_rub': list_range.width_max_raifaizen_rub*currencyget_rub,
                'otkritie_rub': list_range.width_max_otkritie_rub*currencyget_rub,
                'pochtabank_rub': list_range.width_max_pochtabank_rub*currencyget_rub,
                'rnkb_rub': list_range.width_max_rnkb_rub*currencyget_rub,
                'rosbank_rub': list_range.width_max_rosbank_rub*currencyget_rub,
                'mtsbank_rub': list_range.width_max_mtsbank_rub*currencyget_rub,
                'qiwi_rub': list_range.width_max_qiwi_rub*currencyget_rub,
                'qiwi_usd': list_range.width_max_qiwi_usd*currencyget_usd,
                'payeer_rub': list_range.width_max_payeer_rub*currencyget_rub,
                'payeer_usd': list_range.width_max_payeer_usd*currencyget_usd,
                'payeer_eur': list_range.width_max_payeer_eur*currencyget_eur,
                'webmoney_rub': list_range.width_max_webmoney_rub*currencyget_rub,
                'webmoney_usd': list_range.width_max_webmoney_usd*currencyget_usd,
                'webmoney_eur': list_range.width_max_webmoney_eur*currencyget_eur,
                'pm_btc': list_range.width_max_pm_btc*currencyget_btc,
                'pm_usd': list_range.width_max_pm_usd*currencyget_usd,
                'pm_eur': list_range.width_max_pm_eur*currencyget_eur,
                'skrill_eur': list_range.width_max_skrill_eur*currencyget_eur,
                'skrill_usd': list_range.width_max_skrill_usd*currencyget_usd,
                'paypal_rub': list_range.width_max_paypal_rub*currencyget_rub,
                'paypal_usd': list_range.width_max_paypal_usd*currencyget_usd,
                'paypal_eur': list_range.width_max_paypal_eur*currencyget_eur,
                'umoney_rub': list_range.width_max_umoney_rub*currencyget_rub,
                'btc': list_range.width_max_btc*currencyget_btc,
                'xrp': list_range.width_max_xrp*currencyget_xrp,
                'ltc': list_range.width_max_ltc*currencyget_ltc,
                'bch': list_range.width_max_bch*currencyget_bch,
                'xmr': list_range.width_max_xmr*currencyget_xmr,
                'eth': list_range.width_max_eth*currencyget_eth,
                'etc': list_range.width_max_etc*currencyget_etc,
                'dash': list_range.width_max_dash*currencyget_dash,
            }
            balance_user = balance_user
            balance_change = userrange.balance
            for max_range_k, max_range_v in list_max_range.items():
                if list_reserve[max_range_k] > list_range_min_reserve_ps[max_range_k] < max_range_v and list_range_min_reserve_ps[max_range_k] > 0 and balance_change > list_range_min_reserve_ps[max_range_k] < balance_user:
                    min_max_range = min([max_range_v, list_reserve[max_range_k], balance_change, balance_user])
                    if min_max_range > list_range_max_reserve_ps[max_range_k]:
                        list_range_max_reserve_ps[max_range_k] = round(min_max_range-(min_max_range/100), 2)
                        active_list_ps[max_range_k] = True
        except:
            pass

    return {'list_range_min_reserve_ps': list_range_min_reserve_ps,
            'list_range_max_reserve_ps': list_range_max_reserve_ps,
            'active_list_ps': active_list_ps}


# получаем минимальную и максимальную сумму заявки
def min_and_max_sum_request(ps_request, range_ps):
    range_min_list = range_ps['list_range_min_reserve_ps']
    range_max_list = range_ps['list_range_max_reserve_ps']
    min_sum = 0
    max_sum = 0
    if ps_request == 'СБЕРБАНК':
        min_sum = range_min_list['sberbank_rub']
        max_sum = range_max_list['sberbank_rub'] + (range_max_list['sberbank_rub']/200)
    elif ps_request == 'ТИНЬКОФФ':
        min_sum = range_min_list['tinkoff_rub']
        max_sum = range_max_list['tinkoff_rub'] + (range_max_list['tinkoff_rub']/200)
    elif ps_request == 'АЛЬФА БАНК':
        min_sum = range_min_list['alfabank_rub']
        max_sum = range_max_list['alfabank_rub'] + (range_max_list['alfabank_rub']/200)
    elif ps_request == 'ВТБ':
        min_sum = range_min_list['vtb_rub']
        max_sum = range_max_list['vtb_rub'] + (range_max_list['vtb_rub']/200)
    elif ps_request == 'РАЙФФАЙЗЕНБАНК':
        min_sum = range_min_list['raifaizen_rub']
        max_sum = range_max_list['raifaizen_rub'] + (range_max_list['raifaizen_rub']/200)
    elif ps_request == 'ОТКРЫТИЕ':
        min_sum = range_min_list['otkritie_rub']
        max_sum = range_max_list['otkritie_rub'] + (range_max_list['otkritie_rub']/200)
    elif ps_request == 'ПСБ':
        min_sum = range_min_list['psb_rub']
        max_sum = range_max_list['psb_rub'] + (range_max_list['psb_rub']/200)
    elif ps_request == 'ГАЗПРОМБАНК':
        min_sum = range_min_list['gazprombank_rub']
        max_sum = range_max_list['gazprombank_rub'] + (range_max_list['gazprombank_rub']/200)
    elif ps_request == 'РУССКИЙ СТАНДАРТ':
        min_sum = range_min_list['russtandart_rub']
        max_sum = range_max_list['russtandart_rub'] + (range_max_list['russtandart_rub']/200)
    elif ps_request == 'РОССЕЛЬХОЗБАНК':
        min_sum = range_min_list['rosselhoz_rub']
        max_sum = range_max_list['rosselhoz_rub'] + (range_max_list['rosselhoz_rub']/200)
    elif ps_request == 'ПОЧТА БАНК':
        min_sum = range_min_list['pochtabank_rub']
        max_sum = range_max_list['pochtabank_rub'] + (range_max_list['pochtabank_rub']/200)
    elif ps_request == 'РОСБАНК':
        min_sum = range_min_list['rosbank_rub']
        max_sum = range_max_list['rosbank_rub'] + (range_max_list['rosbank_rub']/200)
    elif ps_request == 'РНКБ':
        min_sum = range_min_list['rnkb_rub']
        max_sum = range_max_list['rnkb_rub'] + (range_max_list['rnkb_rub']/200)
    elif ps_request == 'МТС БАНК':
        min_sum = range_min_list['mtsbank_rub']
        max_sum = range_max_list['mtsbank_rub'] + (range_max_list['mtsbank_rub']/200)
    elif ps_request == 'QIWI RUB':
        min_sum = range_min_list['qiwi_rub']
        max_sum = range_max_list['qiwi_rub'] + (range_max_list['qiwi_rub']/200)
    elif ps_request == 'QIWI USD':
        min_sum = range_min_list['qiwi_usd']
        max_sum = range_max_list['qiwi_usd'] + (range_max_list['qiwi_usd']/200)
    elif ps_request == 'PAYEER RUB':
        min_sum = range_min_list['payeer_rub']
        max_sum = range_max_list['payeer_rub'] + (range_max_list['payeer_rub']/200)
    elif ps_request == 'PAYEER EUR':
        min_sum = range_min_list['payeer_eur']
        max_sum = range_max_list['payeer_eur'] + (range_max_list['payeer_eur']/200)
    elif ps_request == 'PAYEER USD':
        min_sum = range_min_list['payeer_usd']
        max_sum = range_max_list['payeer_usd'] + (range_max_list['payeer_usd']/200)
    elif ps_request == 'WEBMONEY RUB':
        min_sum = range_min_list['webmoney_rub']
        max_sum = range_max_list['webmoney_rub'] + (range_max_list['webmoney_rub']/200)
    elif ps_request == 'WEBMONEY EUR':
        min_sum = range_min_list['webmoney_eur']
        max_sum = range_max_list['webmoney_eur'] + (range_max_list['webmoney_eur']/200)
    elif ps_request == 'WEBMONEY USD':
        min_sum = range_min_list['webmoney_usd']
        max_sum = range_max_list['webmoney_usd'] + (range_max_list['webmoney_usd']/200)
    elif ps_request == 'PERFECT MONEY BTC':
        min_sum = range_min_list['pm_btc']
        max_sum = range_max_list['pm_btc'] + (range_max_list['pm_btc']/200)
    elif ps_request == 'PERFECT MONEY EUR':
        min_sum = range_min_list['pm_eur']
        max_sum = range_max_list['pm_eur'] + (range_max_list['pm_eur']/200)
    elif ps_request == 'PERFECT MONEY USD':
        min_sum = range_min_list['pm_usd']
        max_sum = range_max_list['pm_usd'] + (range_max_list['pm_usd']/200)
    elif ps_request == 'PAYPAL RUB':
        min_sum = range_min_list['paypal_rub']
        max_sum = range_max_list['paypal_rub'] + (range_max_list['paypal_rub']/200)
    elif ps_request == 'PAYPAL EUR':
        min_sum = range_min_list['paypal_eur']
        max_sum = range_max_list['paypal_eur'] + (range_max_list['paypal_eur']/200)
    elif ps_request == 'PAYPAL USD':
        min_sum = range_min_list['paypal_usd']
        max_sum = range_max_list['paypal_usd'] + (range_max_list['paypal_usd']/200)
    elif ps_request == 'SKRILL EUR':
        min_sum = range_min_list['skrill_eur']
        max_sum = range_max_list['skrill_eur'] + (range_max_list['skrill_eur']/200)
    elif ps_request == 'SKRILL USD':
        min_sum = range_min_list['skrill_usd']
        max_sum = range_max_list['skrill_usd'] + (range_max_list['skrill_usd']/200)
    elif ps_request == 'UMONEY RUB':
        min_sum = range_min_list['umoney_rub']
        max_sum = range_max_list['umoney_rub'] + (range_max_list['umoney_rub']/200)
    elif ps_request == 'BITCOIN':
        min_sum = range_min_list['btc']
        max_sum = range_max_list['btc'] + (range_max_list['btc']/200)
    elif ps_request == 'LITECOIN':
        min_sum = range_min_list['ltc']
        max_sum = range_max_list['ltc'] + (range_max_list['ltc']/200)
    elif ps_request == 'MONERO':
        min_sum = range_min_list['xmr']
        max_sum = range_max_list['xmr'] + (range_max_list['xmr']/200)
    elif ps_request == 'ETHEREUM CLASSIC':
        min_sum = range_min_list['etc']
        max_sum = range_max_list['etc'] + (range_max_list['etc']/200)
    elif ps_request == 'DASH':
        min_sum = range_min_list['dash']
        max_sum = range_max_list['dash'] + (range_max_list['dash']/200)
    elif ps_request == 'RIPPLE':
        min_sum = range_min_list['xrp']
        max_sum = range_max_list['xrp'] + (range_max_list['xrp']/200)
    elif ps_request == 'BITCOIN CASH':
        min_sum = range_min_list['bch']
        max_sum = range_max_list['bch'] + (range_max_list['bch']/200)
    elif ps_request == 'ETHEREUM':
        min_sum = range_min_list['eth']
        max_sum = range_max_list['eth'] + (range_max_list['eth']/200)
    return {'min_sum': min_sum, 'max_sum': max_sum}


# отправка сообщения на почту
def mail_send_metod(email, templates, context, subject):
    html_body = render_to_string(templates, context)
    msg = EmailMultiAlternatives(subject=subject, from_email=settings.EMAIL_HOST_USER, to=[email])
    msg.attach_alternative(html_body, 'text/html')
    msg.send()








