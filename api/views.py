import random
from decimal import Decimal
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Merchant
from api.serializers import DepositRequestUpdateSerializers, DepositRequestCreateSerializers, \
    WidthRequestCreateSerializers, AllRequestCreateModelSerializers, ALLPSSerializers
from personalaccount.metodviews import active_deposit_ps_global, range_deposit_ps_global, min_and_max_sum_request, \
    depositsortchangeps, depositsortcritery, active_width_ps_global, range_width_ps_global, widthsortchangeps, \
    widthsortcritery
from personalaccount.models import CurrencyCBRF, RequestChange, Transaction
from users.models import CustomUser


class RequestPSStatusDepositView(APIView):
    """Получение списка для заявок на пополнение, с информацией о ПС (Название, Активность, Резерв, Минимальный лимит, Максимальный лимит)"""

    def get(self, request):
        if 'Key-Merchant' in request.headers:
            key = request.headers['Key-Merchant']
            if Merchant.objects.filter(merchant_secret_key=key).exists():
                currency = CurrencyCBRF.objects.all()
                active_ps = active_deposit_ps_global()
                range_ps = range_deposit_ps_global(list_active_user=active_ps['list_active_user'])
                merchant_ps = []
                list_name_ps = {
                    'sberbank_rub': 'СБЕРБАНК',
                    'psb_rub': 'ПСБ',
                    'tinkoff_rub': 'ТИНЬКОФФ',
                    'gazprombank_rub': 'ГАЗПРОМБАНК',
                    'alfabank_rub': 'АЛЬФА БАНК',
                    'russtandart_rub': 'РУССКИЙ СТАНДАРТ',
                    'vtb_rub': 'ВТБ',
                    'rosselhoz_rub': 'РОССЕЛЬХОЗБАНК',
                    'raifaizen_rub': 'РАЙФФАЙЗЕНБАНК',
                    'otkritie_rub': 'ОТКРЫТИЕ',
                    'pochtabank_rub': 'ПОЧТА БАНК',
                    'rnkb_rub': 'РНКБ',
                    'rosbank_rub': 'РОСБАНК',
                    'mtsbank_rub': 'МТС БАНК',
                    'qiwi_rub': 'QIWI RUB',
                    'qiwi_usd': 'QIWI USD',
                    'payeer_rub': 'PAYEER RUB',
                    'payeer_usd': 'PAYEER USD',
                    'payeer_eur': 'PAYEER EUR',
                    'webmoney_rub': 'WEBMONEY RUB',
                    'webmoney_usd': 'WEBMONEY USD',
                    'webmoney_eur': 'WEBMONEY EUR',
                    'pm_btc': 'PERFECT MONEY BTC',
                    'pm_usd': 'PERFECT MONEY USD',
                    'pm_eur': 'PERFECT MONEY EUR',
                    'skrill_eur': 'SKRILL EUR',
                    'skrill_usd': 'SKRILL USD',
                    'paypal_rub': 'PAYPAL RUB',
                    'paypal_usd': 'PAYPAL USD',
                    'paypal_eur': 'PAYPAL EUR',
                    'umoney_rub': 'UMONEY RUB',
                    'btc': 'BITCOIN',
                    'xrp': 'RIPPLE',
                    'ltc': 'LITECOIN',
                    'bch': 'BITCOIN CASH',
                    'xmr': 'MONERO',
                    'eth': 'ETHEREUM',
                    'etc': 'ETHEREUM CLASSIC',
                    'dash': 'DASH',
                }
                list_id_ps = {
                    'sberbank_rub': 11,
                    'psb_rub': 12,
                    'tinkoff_rub': 13,
                    'gazprombank_rub': 14,
                    'alfabank_rub': 15,
                    'russtandart_rub': 16,
                    'vtb_rub': 17,
                    'rosselhoz_rub': 18,
                    'raifaizen_rub': 19,
                    'otkritie_rub': 20,
                    'pochtabank_rub': 21,
                    'rnkb_rub': 22,
                    'rosbank_rub': 23,
                    'mtsbank_rub': 24,
                    'qiwi_rub': 25,
                    'qiwi_usd': 26,
                    'payeer_rub': 27,
                    'payeer_usd': 28,
                    'payeer_eur': 29,
                    'webmoney_rub': 30,
                    'webmoney_usd': 31,
                    'webmoney_eur': 32,
                    'pm_btc': 33,
                    'pm_usd': 34,
                    'pm_eur': 35,
                    'skrill_eur': 36,
                    'skrill_usd': 37,
                    'paypal_rub': 38,
                    'paypal_usd': 39,
                    'paypal_eur': 40,
                    'umoney_rub': 41,
                    'btc': 42,
                    'xrp': 43,
                    'ltc': 44,
                    'bch': 45,
                    'xmr': 46,
                    'eth': 47,
                    'etc': 48,
                    'dash': 49,
                }
                list_valute_ps = {
                    'sberbank_rub': 'RUB',
                    'psb_rub': 'RUB',
                    'tinkoff_rub': 'RUB',
                    'gazprombank_rub': 'RUB',
                    'alfabank_rub': 'RUB',
                    'russtandart_rub': 'RUB',
                    'vtb_rub': 'RUB',
                    'rosselhoz_rub': 'RUB',
                    'raifaizen_rub': 'RUB',
                    'otkritie_rub': 'RUB',
                    'pochtabank_rub': 'RUB',
                    'rnkb_rub': 'RUB',
                    'rosbank_rub': 'RUB',
                    'mtsbank_rub': 'RUB',
                    'qiwi_rub': 'RUB',
                    'qiwi_usd': 'USD',
                    'payeer_rub': 'RUB',
                    'payeer_usd': 'USD',
                    'payeer_eur': 'EUR',
                    'webmoney_rub': 'RUB',
                    'webmoney_usd': 'USD',
                    'webmoney_eur': 'EUR',
                    'pm_btc': 'BTC',
                    'pm_usd': 'USD',
                    'pm_eur': 'EUR',
                    'skrill_eur': 'EUR',
                    'skrill_usd': 'USD',
                    'paypal_rub': 'RUB',
                    'paypal_usd': 'USD',
                    'paypal_eur': 'EUR',
                    'umoney_rub': 'RUB',
                    'btc': 'BTC',
                    'xrp': 'XRP',
                    'ltc': 'LTC',
                    'bch': 'BCH',
                    'xmr': 'XMR',
                    'eth': 'ETH',
                    'etc': 'ETC',
                    'dash': 'DASH',
                }
                list_curse_valute = {
                    'sberbank_rub': currency.get(name_currency='RUB').base_currency,
                    'psb_rub': currency.get(name_currency='RUB').base_currency,
                    'tinkoff_rub': currency.get(name_currency='RUB').base_currency,
                    'gazprombank_rub': currency.get(name_currency='RUB').base_currency,
                    'alfabank_rub': currency.get(name_currency='RUB').base_currency,
                    'russtandart_rub': currency.get(name_currency='RUB').base_currency,
                    'vtb_rub': currency.get(name_currency='RUB').base_currency,
                    'rosselhoz_rub': currency.get(name_currency='RUB').base_currency,
                    'raifaizen_rub': currency.get(name_currency='RUB').base_currency,
                    'otkritie_rub': currency.get(name_currency='RUB').base_currency,
                    'pochtabank_rub': currency.get(name_currency='RUB').base_currency,
                    'rnkb_rub': currency.get(name_currency='RUB').base_currency,
                    'rosbank_rub': currency.get(name_currency='RUB').base_currency,
                    'mtsbank_rub': currency.get(name_currency='RUB').base_currency,
                    'qiwi_rub': currency.get(name_currency='RUB').base_currency,
                    'qiwi_usd': currency.get(name_currency='USD').base_currency,
                    'payeer_rub': currency.get(name_currency='RUB').base_currency,
                    'payeer_usd': currency.get(name_currency='USD').base_currency,
                    'payeer_eur': currency.get(name_currency='EUR').base_currency,
                    'webmoney_rub': currency.get(name_currency='RUB').base_currency,
                    'webmoney_usd': currency.get(name_currency='USD').base_currency,
                    'webmoney_eur': currency.get(name_currency='EUR').base_currency,
                    'pm_btc': currency.get(name_currency='BTC').base_currency,
                    'pm_usd': currency.get(name_currency='USD').base_currency,
                    'pm_eur': currency.get(name_currency='EUR').base_currency,
                    'skrill_eur': currency.get(name_currency='EUR').base_currency,
                    'skrill_usd': currency.get(name_currency='USD').base_currency,
                    'paypal_rub': currency.get(name_currency='RUB').base_currency,
                    'paypal_usd': currency.get(name_currency='USD').base_currency,
                    'paypal_eur': currency.get(name_currency='EUR').base_currency,
                    'umoney_rub': currency.get(name_currency='RUB').base_currency,
                    'btc': currency.get(name_currency='BTC').base_currency,
                    'xrp': currency.get(name_currency='XRP').base_currency,
                    'ltc': currency.get(name_currency='LTC').base_currency,
                    'bch': currency.get(name_currency='BCH').base_currency,
                    'xmr': currency.get(name_currency='XMR').base_currency,
                    'eth': currency.get(name_currency='ETH').base_currency,
                    'etc': currency.get(name_currency='ETC').base_currency,
                    'dash': currency.get(name_currency='DASH').base_currency,
                }

                for itemps_k, itemps_v in range_ps['active_list_ps'].items():
                    if itemps_v:
                        merchant_ps.append({
                            'id': list_id_ps[itemps_k],
                            'name': list_name_ps[itemps_k],
                            'valute': list_valute_ps[itemps_k],
                            'curse': list_curse_valute[itemps_k],
                            'reserve': active_ps['list_active_reserve_ps'][itemps_k],
                            'min_limit': range_ps['list_range_min_reserve_ps'][itemps_k],
                            'max_limit': range_ps['list_range_max_reserve_ps'][itemps_k],
                        })
                serializers_merch = ALLPSSerializers(data=merchant_ps, many=True)
                serializers_merch.is_valid()
                return Response(serializers_merch.data, status=status.HTTP_200_OK)
            else:
                return Response({"ERROR": "Secret key not found"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"ERROR": "Key 'Key-Merchant', not found"}, status=status.HTTP_403_FORBIDDEN)


class RequestPSStatusWidthdrawalView(APIView):
    """Получение списка для заявок на вывод, с информацией о ПС (Название, Активность, Резерв, Минимальный лимит, Максимальный лимит)"""

    def get(self, request):
        if 'Key-Merchant' in request.headers:
            key = request.headers['Key-Merchant']
            if Merchant.objects.filter(merchant_secret_key=key).exists():
                merchant_owner = Merchant.objects.get(merchant_secret_key=key)
                currency = CurrencyCBRF.objects.all()
                userwidth = CustomUser.objects.get(username=merchant_owner.merchant_user.username)
                active_ps = active_width_ps_global()
                range_ps = range_width_ps_global(list_active_user=active_ps['list_active_user'],
                                                 balance_user=userwidth.balance)
                merchant_ps = []
                list_name_ps = {
                    'sberbank_rub': 'СБЕРБАНК',
                    'psb_rub': 'ПСБ',
                    'tinkoff_rub': 'ТИНЬКОФФ',
                    'gazprombank_rub': 'ГАЗПРОМБАНК',
                    'alfabank_rub': 'АЛЬФА БАНК',
                    'russtandart_rub': 'РУССКИЙ СТАНДАРТ',
                    'vtb_rub': 'ВТБ',
                    'rosselhoz_rub': 'РОССЕЛЬХОЗБАНК',
                    'raifaizen_rub': 'РАЙФФАЙЗЕНБАНК',
                    'otkritie_rub': 'ОТКРЫТИЕ',
                    'pochtabank_rub': 'ПОЧТА БАНК',
                    'rnkb_rub': 'РНКБ',
                    'rosbank_rub': 'РОСБАНК',
                    'mtsbank_rub': 'МТС БАНК',
                    'qiwi_rub': 'QIWI RUB',
                    'qiwi_usd': 'QIWI USD',
                    'payeer_rub': 'PAYEER RUB',
                    'payeer_usd': 'PAYEER USD',
                    'payeer_eur': 'PAYEER EUR',
                    'webmoney_rub': 'WEBMONEY RUB',
                    'webmoney_usd': 'WEBMONEY USD',
                    'webmoney_eur': 'WEBMONEY EUR',
                    'pm_btc': 'PERFECT MONEY BTC',
                    'pm_usd': 'PERFECT MONEY USD',
                    'pm_eur': 'PERFECT MONEY EUR',
                    'skrill_eur': 'SKRILL EUR',
                    'skrill_usd': 'SKRILL USD',
                    'paypal_rub': 'PAYPAL RUB',
                    'paypal_usd': 'PAYPAL USD',
                    'paypal_eur': 'PAYPAL EUR',
                    'umoney_rub': 'UMONEY RUB',
                    'btc': 'BITCOIN',
                    'xrp': 'RIPPLE',
                    'ltc': 'LITECOIN',
                    'bch': 'BITCOIN CASH',
                    'xmr': 'MONERO',
                    'eth': 'ETHEREUM',
                    'etc': 'ETHEREUM CLASSIC',
                    'dash': 'DASH',
                }
                list_id_ps = {
                    'sberbank_rub': 11,
                    'psb_rub': 12,
                    'tinkoff_rub': 13,
                    'gazprombank_rub': 14,
                    'alfabank_rub': 15,
                    'russtandart_rub': 16,
                    'vtb_rub': 17,
                    'rosselhoz_rub': 18,
                    'raifaizen_rub': 19,
                    'otkritie_rub': 20,
                    'pochtabank_rub': 21,
                    'rnkb_rub': 22,
                    'rosbank_rub': 23,
                    'mtsbank_rub': 24,
                    'qiwi_rub': 25,
                    'qiwi_usd': 26,
                    'payeer_rub': 27,
                    'payeer_usd': 28,
                    'payeer_eur': 29,
                    'webmoney_rub': 30,
                    'webmoney_usd': 31,
                    'webmoney_eur': 32,
                    'pm_btc': 33,
                    'pm_usd': 34,
                    'pm_eur': 35,
                    'skrill_eur': 36,
                    'skrill_usd': 37,
                    'paypal_rub': 38,
                    'paypal_usd': 39,
                    'paypal_eur': 40,
                    'umoney_rub': 41,
                    'btc': 42,
                    'xrp': 43,
                    'ltc': 44,
                    'bch': 45,
                    'xmr': 46,
                    'eth': 47,
                    'etc': 48,
                    'dash': 49,
                }
                list_valute_ps = {
                    'sberbank_rub': 'RUB',
                    'psb_rub': 'RUB',
                    'tinkoff_rub': 'RUB',
                    'gazprombank_rub': 'RUB',
                    'alfabank_rub': 'RUB',
                    'russtandart_rub': 'RUB',
                    'vtb_rub': 'RUB',
                    'rosselhoz_rub': 'RUB',
                    'raifaizen_rub': 'RUB',
                    'otkritie_rub': 'RUB',
                    'pochtabank_rub': 'RUB',
                    'rnkb_rub': 'RUB',
                    'rosbank_rub': 'RUB',
                    'mtsbank_rub': 'RUB',
                    'qiwi_rub': 'RUB',
                    'qiwi_usd': 'USD',
                    'payeer_rub': 'RUB',
                    'payeer_usd': 'USD',
                    'payeer_eur': 'EUR',
                    'webmoney_rub': 'RUB',
                    'webmoney_usd': 'USD',
                    'webmoney_eur': 'EUR',
                    'pm_btc': 'BTC',
                    'pm_usd': 'USD',
                    'pm_eur': 'EUR',
                    'skrill_eur': 'EUR',
                    'skrill_usd': 'USD',
                    'paypal_rub': 'RUB',
                    'paypal_usd': 'USD',
                    'paypal_eur': 'EUR',
                    'umoney_rub': 'RUB',
                    'btc': 'BTC',
                    'xrp': 'XRP',
                    'ltc': 'LTC',
                    'bch': 'BCH',
                    'xmr': 'XMR',
                    'eth': 'ETH',
                    'etc': 'ETC',
                    'dash': 'DASH',
                }
                list_curse_valute = {
                    'sberbank_rub': currency.get(name_currency='RUB').base_currency,
                    'psb_rub': currency.get(name_currency='RUB').base_currency,
                    'tinkoff_rub': currency.get(name_currency='RUB').base_currency,
                    'gazprombank_rub': currency.get(name_currency='RUB').base_currency,
                    'alfabank_rub': currency.get(name_currency='RUB').base_currency,
                    'russtandart_rub': currency.get(name_currency='RUB').base_currency,
                    'vtb_rub': currency.get(name_currency='RUB').base_currency,
                    'rosselhoz_rub': currency.get(name_currency='RUB').base_currency,
                    'raifaizen_rub': currency.get(name_currency='RUB').base_currency,
                    'otkritie_rub': currency.get(name_currency='RUB').base_currency,
                    'pochtabank_rub': currency.get(name_currency='RUB').base_currency,
                    'rnkb_rub': currency.get(name_currency='RUB').base_currency,
                    'rosbank_rub': currency.get(name_currency='RUB').base_currency,
                    'mtsbank_rub': currency.get(name_currency='RUB').base_currency,
                    'qiwi_rub': currency.get(name_currency='RUB').base_currency,
                    'qiwi_usd': currency.get(name_currency='USD').base_currency,
                    'payeer_rub': currency.get(name_currency='RUB').base_currency,
                    'payeer_usd': currency.get(name_currency='USD').base_currency,
                    'payeer_eur': currency.get(name_currency='EUR').base_currency,
                    'webmoney_rub': currency.get(name_currency='RUB').base_currency,
                    'webmoney_usd': currency.get(name_currency='USD').base_currency,
                    'webmoney_eur': currency.get(name_currency='EUR').base_currency,
                    'pm_btc': currency.get(name_currency='BTC').base_currency,
                    'pm_usd': currency.get(name_currency='USD').base_currency,
                    'pm_eur': currency.get(name_currency='EUR').base_currency,
                    'skrill_eur': currency.get(name_currency='EUR').base_currency,
                    'skrill_usd': currency.get(name_currency='USD').base_currency,
                    'paypal_rub': currency.get(name_currency='RUB').base_currency,
                    'paypal_usd': currency.get(name_currency='USD').base_currency,
                    'paypal_eur': currency.get(name_currency='EUR').base_currency,
                    'umoney_rub': currency.get(name_currency='RUB').base_currency,
                    'btc': currency.get(name_currency='BTC').base_currency,
                    'xrp': currency.get(name_currency='XRP').base_currency,
                    'ltc': currency.get(name_currency='LTC').base_currency,
                    'bch': currency.get(name_currency='BCH').base_currency,
                    'xmr': currency.get(name_currency='XMR').base_currency,
                    'eth': currency.get(name_currency='ETH').base_currency,
                    'etc': currency.get(name_currency='ETC').base_currency,
                    'dash': currency.get(name_currency='DASH').base_currency,
                }

                for itemps_k, itemps_v in range_ps['active_list_ps'].items():
                    if itemps_v:
                        merchant_ps.append({
                            'id': list_id_ps[itemps_k],
                            'name': list_name_ps[itemps_k],
                            'valute': list_valute_ps[itemps_k],
                            'curse': list_curse_valute[itemps_k],
                            'reserve': active_ps['list_active_reserve_ps'][itemps_k],
                            'min_limit': range_ps['list_range_min_reserve_ps'][itemps_k],
                            'max_limit': range_ps['list_range_max_reserve_ps'][itemps_k],
                        })
                serializers_merch = ALLPSSerializers(data=merchant_ps, many=True)
                serializers_merch.is_valid()
                return Response(serializers_merch.data, status=status.HTTP_200_OK)
            else:
                return Response({"ERROR": "Secret key not found"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"ERROR": "Key 'Key-Merchant', not found"}, status=status.HTTP_403_FORBIDDEN)


class DepositRequestCreateView(APIView):
    """Создание заявки на пополнение"""

    def post(self, request):
        if 'Key-Merchant' in request.headers:
            key = request.headers['Key-Merchant']
            if Merchant.objects.filter(merchant_secret_key=key).exists():
                merchant_owner = Merchant.objects.get(merchant_secret_key=key)
                form = DepositRequestCreateSerializers(data=request.data)
                if form.is_valid():
                    critery_list = {1: 'БЫСТРАЯ ЗАЯВКА', 2: 'ВЫГОДНЫЙ КУРС'}
                    order_criterion = form.validated_data['order_criterion']
                    if order_criterion in critery_list:
                        payment_list = {
                            11: 'СБЕРБАНК',
                            12: 'ПСБ',
                            13: 'ТИНЬКОФФ',
                            14: 'ГАЗПРОМБАНК',
                            15: 'АЛЬФА БАНК',
                            16: 'РУССКИЙ СТАНДАРТ',
                            17: 'ВТБ',
                            18: 'РОССЕЛЬХОЗБАНК',
                            19: 'РАЙФФАЙЗЕНБАНК',
                            20: 'ОТКРЫТИЕ',
                            21: 'ПОЧТА БАНК',
                            22: 'РНКБ',
                            23: 'РОСБАНК',
                            24: 'МТС БАНК',
                            25: 'QIWI RUB',
                            26: 'QIWI USD',
                            27: 'PAYEER RUB',
                            28: 'PAYEER USD',
                            29: 'PAYEER EUR',
                            30: 'WEBMONEY RUB',
                            31: 'WEBMONEY USD',
                            32: 'WEBMONEY EUR',
                            33: 'PERFECT MONEY BTC',
                            34: 'PERFECT MONEY USD',
                            35: 'PERFECT MONEY EUR',
                            36: 'SKRILL EUR',
                            37: 'SKRILL USD',
                            38: 'PAYPAL RUB',
                            39: 'PAYPAL USD',
                            40: 'PAYPAL EUR',
                            41: 'UMONEY RUB',
                            42: 'BITCOIN',
                            43: 'RIPPLE',
                            44: 'LITECOIN',
                            45: 'BITCOIN CASH',
                            46: 'MONERO',
                            47: 'ETHEREUM',
                            48: 'ETHEREUM CLASSIC',
                            49: 'DASH',
                        }
                        order_pay = form.validated_data['order_pay']
                        if order_pay in payment_list:
                            active_ps = active_deposit_ps_global()
                            range_ps = range_deposit_ps_global(list_active_user=active_ps['list_active_user'])
                            n = random.randint(1000000, 9999999)
                            post = {}
                            post['request_sum'] = round(form.validated_data['order_amount'], 8)
                            post['request_sistemchange'] = payment_list[order_pay]
                            post['criteri'] = critery_list[order_criterion]
                            range_list = min_and_max_sum_request(ps_request=post['request_sistemchange'], range_ps=range_ps)
                            if range_list['min_sum'] <= post['request_sum'] <= range_list['max_sum']:
                                post['request_user'] = str(merchant_owner.merchant_user)
                                post['request_name'] = str(n)
                                post['request_type'] = "Мерчант пополнение"
                                post['request_status'] = "Ожидает оплаты"
                                changerequest = depositsortchangeps(nameps=post['request_sistemchange'], request_sum=post['request_sum'])
                                if len(changerequest['changeq']) > 0:
                                    request_good = CurrencyCBRF.objects.get(name_currency=changerequest['valute'])
                                    usernamepsch = depositsortcritery(userps=changerequest['changeq'], critery=post['criteri'],
                                                                      nameps=post['request_sistemchange'])

                                    usernamepschange = usernamepsch['usernameps']
                                    post['request_commission'] = round(usernamepsch['base_comis'] + Decimal(0.5), 2)
                                    post['request_commission_change'] = round(usernamepsch['base_comis'], 2)
                                    post['requisites'] = usernamepsch['rekvesites']
                                    post['request_userchange'] = usernamepschange.username

                                    request_summe = post['request_sum'] - ((post['request_sum'] / 100) * post['request_commission'])
                                    post['request_good_sum'] = round(request_summe * request_good.base_currency, 8)

                                    request_good_summe = post['request_sum'] - (
                                                (post['request_sum'] / 100) * post['request_commission_change'])
                                    post['request_good_sum_change'] = round(request_good_summe * request_good.base_currency, 8)

                                    post['request_company_profit'] = round(post['request_good_sum_change'] - post['request_good_sum'], 8)
                                    post['request_type_valute'] = changerequest['valute']
                                    post['request_sum_valute'] = round(post['request_sum'], 2)
                                    post['request_good_sum_valute'] = round(post['request_good_sum'], 2)
                                    post['request_good_sum_change_valute'] = round(post['request_good_sum_change'], 2)
                                    post['request_curse'] = round(request_good.base_currency, 4)
                                    post['date_joined_change'] = timezone.now()

                                    user_hold_update = CustomUser.objects.get(username=post['request_userchange'])
                                    user_hold_update.balance -= post['request_good_sum_change_valute']
                                    user_hold_update.hold += post['request_good_sum_change_valute']

                                    request_init = AllRequestCreateModelSerializers(data=post)
                                    try:
                                        request_init.is_valid()
                                        request_init.save()
                                        user_hold_update.save()
                                        order = {
                                            "number": request_init.data['request_name'],
                                            "date": request_init.data['date_joined_change'],
                                            "type": "Заявка на пополнение",
                                            "pay_id": order_pay,
                                            "pay_name": request_init.data['request_sistemchange'],
                                            "valute": request_init.data['request_type_valute'],
                                            "criterion": request_init.data['criteri'],
                                            "status": request_init.data['request_status'],
                                            "requisites": request_init.data['requisites'],
                                            "amount": request_init.data['request_sum'],
                                            "commission": request_init.data['request_commission'],
                                            "exchanger": request_init.data['request_userchange'],
                                            "total_amount": request_init.data['request_good_sum'],
                                            "curse": request_init.data['request_curse']
                                        }
                                        return Response(order, status=status.HTTP_201_CREATED)
                                    except:
                                        return Response({"ERROR": "Internal error"}, status=status.HTTP_400_BAD_REQUEST)

                                else:
                                    return Response({"ERROR": "No exchange offices found"}, status=status.HTTP_400_BAD_REQUEST)

                            else:
                                if range_list['min_sum'] > post['request_sum'] < range_list['max_sum']:
                                    return Response({"ERROR": "Requested amount, exceeds the minimum limit"}, status=status.HTTP_400_BAD_REQUEST)
                                elif range_list['min_sum'] < post['request_sum'] > range_list['max_sum']:
                                    return Response({"ERROR": "Requested amount, exceeds the maximum limit"}, status=status.HTTP_400_BAD_REQUEST)
                        else:
                            return Response({"ERROR": "The specified payment system does not exist, does not exist"}, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response({"ERROR": "The specified criterion does not exist"}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"ERROR": "The data is not valid"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"ERROR": "Secret key not found"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"ERROR": "Key 'Key-Merchant', not found"}, status=status.HTTP_403_FORBIDDEN)


class WidthRequestCreateView(APIView):
    """Создание заявки на вывод"""

    def post(self, request):
        if 'Key-Merchant' in request.headers:
            key = request.headers['Key-Merchant']
            if Merchant.objects.filter(merchant_secret_key=key).exists():
                merchant_owner = Merchant.objects.get(merchant_secret_key=key)
                form = WidthRequestCreateSerializers(data=request.data)
                if form.is_valid():
                    critery_list = {1: 'БЫСТРАЯ ЗАЯВКА', 2: 'ВЫГОДНЫЙ КУРС'}
                    order_criterion = form.validated_data['order_criterion']
                    if order_criterion in critery_list:
                        payment_list = {
                            11: 'СБЕРБАНК',
                            12: 'ПСБ',
                            13: 'ТИНЬКОФФ',
                            14: 'ГАЗПРОМБАНК',
                            15: 'АЛЬФА БАНК',
                            16: 'РУССКИЙ СТАНДАРТ',
                            17: 'ВТБ',
                            18: 'РОССЕЛЬХОЗБАНК',
                            19: 'РАЙФФАЙЗЕНБАНК',
                            20: 'ОТКРЫТИЕ',
                            21: 'ПОЧТА БАНК',
                            22: 'РНКБ',
                            23: 'РОСБАНК',
                            24: 'МТС БАНК',
                            25: 'QIWI RUB',
                            26: 'QIWI USD',
                            27: 'PAYEER RUB',
                            28: 'PAYEER USD',
                            29: 'PAYEER EUR',
                            30: 'WEBMONEY RUB',
                            31: 'WEBMONEY USD',
                            32: 'WEBMONEY EUR',
                            33: 'PERFECT MONEY BTC',
                            34: 'PERFECT MONEY USD',
                            35: 'PERFECT MONEY EUR',
                            36: 'SKRILL EUR',
                            37: 'SKRILL USD',
                            38: 'PAYPAL RUB',
                            39: 'PAYPAL USD',
                            40: 'PAYPAL EUR',
                            41: 'UMONEY RUB',
                            42: 'BITCOIN',
                            43: 'RIPPLE',
                            44: 'LITECOIN',
                            45: 'BITCOIN CASH',
                            46: 'MONERO',
                            47: 'ETHEREUM',
                            48: 'ETHEREUM CLASSIC',
                            49: 'DASH',
                        }
                        order_pay = form.validated_data['order_pay']
                        if order_pay in payment_list:
                            active_ps = active_width_ps_global()
                            userwidth = CustomUser.objects.get(username=merchant_owner.merchant_user.username)
                            range_ps = range_width_ps_global(list_active_user=active_ps['list_active_user'],
                                                             balance_user=userwidth.balance)
                            n = random.randint(1000000, 9999999)
                            post = {}
                            post['request_sum'] = round(form.validated_data['order_amount'], 8)
                            post['request_sistemchange'] = payment_list[order_pay]
                            post['criteri'] = critery_list[order_criterion]
                            post['requisites'] = form.validated_data['order_rekvisites']
                            range_list = min_and_max_sum_request(ps_request=post['request_sistemchange'], range_ps=range_ps)
                            if range_list['min_sum'] <= post['request_sum'] <= range_list['max_sum']:
                                post['request_user'] = str(merchant_owner.merchant_user)
                                post['request_name'] = str(n)
                                post['request_type'] = "Мерчант вывод"
                                post['request_status'] = "Ожидает оплаты"
                                changerequest = widthsortchangeps(nameps=post['request_sistemchange'], request_sum=post['request_sum'])
                                if len(changerequest['changeq']) > 0:
                                    request_good = CurrencyCBRF.objects.get(name_currency=changerequest['valute'])
                                    usernamepsch = widthsortcritery(userps=changerequest['changeq'],
                                                                    critery=post['criteri'],
                                                                    nameps=post['request_sistemchange'],
                                                                    valuteps=changerequest['valute'],
                                                                    balanceps=post['request_sum'])

                                    usernamepschange = usernamepsch['usernameps']
                                    userwidth.balance -= post['request_sum']
                                    post['request_commission'] = round(usernamepsch['base_comis'] + Decimal(0.5), 2)
                                    post['request_commission_change'] = round(usernamepsch['base_comis'], 2)
                                    post['request_userchange'] = usernamepschange.username

                                    request_summe = post['request_sum'] - ((post['request_sum'] / 100) * post['request_commission'])
                                    post['request_good_sum'] = round(request_summe / request_good.base_currency, 8)
                                    post['request_good_sum_change'] = round(post['request_sum'] - (post['request_sum'] / 200), 8)

                                    post['request_company_profit'] = round(post['request_sum'] - post['request_good_sum_change'], 8)
                                    post['request_type_valute'] = changerequest['valute']
                                    post['request_sum_valute'] = round(post['request_sum'], 2)
                                    post['request_good_sum_valute'] = round(post['request_good_sum'], 2)
                                    post['request_good_sum_change_valute'] = round(post['request_good_sum_change'], 2)
                                    post['request_curse'] = round(request_good.base_currency, 4)
                                    post['date_joined_change'] = timezone.now()

                                    # создаем транзакцию для получателя вывода
                                    Transaction.objects.create(
                                        transaction_name='Вывод через мерчант, заявка № ' + str(n),
                                        transaction_number=str(n),
                                        transaction_category='Вывод через мерчант',
                                        transaction_type='Вывод',
                                        transaction_user=userwidth.username,
                                        transaction_status='В обработке',
                                        transaction_sum=post['request_sum'],
                                        transaction_sistemchange=post['request_sistemchange'])

                                    user_hold_update = CustomUser.objects.get(username=post['request_userchange'])
                                    user_hold_update.hold += post['request_good_sum_change_valute']

                                    request_init = AllRequestCreateModelSerializers(data=post)
                                    try:
                                        request_init.is_valid()
                                        request_init.save()
                                        userwidth.save()
                                        user_hold_update.save()
                                        order = {
                                            "number": request_init.data['request_name'],
                                            "date": request_init.data['date_joined_change'],
                                            "type": "Заявка на вывод",
                                            "pay_id": order_pay,
                                            "pay_name": request_init.data['request_sistemchange'],
                                            "valute": request_init.data['request_type_valute'],
                                            "criterion": request_init.data['criteri'],
                                            "status": request_init.data['request_status'],
                                            "requisites": request_init.data['requisites'],
                                            "amount": request_init.data['request_sum'],
                                            "commission": request_init.data['request_commission'],
                                            "exchanger": request_init.data['request_userchange'],
                                            "total_amount": request_init.data['request_good_sum'],
                                            "curse": request_init.data['request_curse']
                                        }
                                        return Response(order, status=status.HTTP_201_CREATED)
                                    except:
                                        return Response({"ERROR": "Internal error"}, status=status.HTTP_400_BAD_REQUEST)

                                else:
                                    return Response({"ERROR": "No exchange offices found"}, status=status.HTTP_400_BAD_REQUEST)

                            else:
                                if range_list['min_sum'] > post['request_sum'] < range_list['max_sum']:
                                    return Response({"ERROR": "Requested amount, exceeds the minimum limit"}, status=status.HTTP_400_BAD_REQUEST)
                                elif range_list['min_sum'] < post['request_sum'] > range_list['max_sum']:
                                    return Response({"ERROR": "Requested amount, exceeds the maximum limit"}, status=status.HTTP_400_BAD_REQUEST)
                        else:
                            return Response({"ERROR": "The specified payment system does not exist, does not exist"}, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response({"ERROR": "The specified criterion does not exist"}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"ERROR": "The data is not valid"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"ERROR": "Secret key not found"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"ERROR": "Key 'Key-Merchant', not found"}, status=status.HTTP_403_FORBIDDEN)


class DepositRequestUpdateView(APIView):
    """Обновление статуса заявки на пополнение"""

    def post(self, request):
        if 'Key-Merchant' in request.headers:
            key = request.headers['Key-Merchant']
            if Merchant.objects.filter(merchant_secret_key=key).exists():
                form = DepositRequestUpdateSerializers(data=request.data)
                if form.is_valid():
                    if RequestChange.objects.filter(request_name=form.validated_data['order_number']).exists():
                        order_update = RequestChange.objects.get(request_name=form.validated_data['order_number'])
                        if order_update.request_status == 'Ожидает оплаты':
                            order_update.request_status = 'Оплачена'
                            order_update.date_change_request = timezone.now()
                            order_update.save()
                            order = {
                                "number": order_update.request_name,
                                "status": order_update.request_status
                            }
                            return Response(order, status=status.HTTP_202_ACCEPTED)
                        else:
                            return Response({"ERROR": "Application status - " + order_update.request_status}, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response({"ERROR": "Application not found"}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"ERROR": "The data is not valid"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"ERROR": "Secret key not found"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"ERROR": "Key 'Key-Merchant', not found"}, status=status.HTTP_403_FORBIDDEN)


class StatusOrderView(APIView):
    """Запрос статуса заявки"""

    def post(self, request):
        if 'Key-Merchant' in request.headers:
            key = request.headers['Key-Merchant']
            if Merchant.objects.filter(merchant_secret_key=key).exists():
                merchant_owner = Merchant.objects.get(merchant_secret_key=key)
                form = DepositRequestUpdateSerializers(data=request.data)
                if form.is_valid():
                    if RequestChange.objects.filter(request_name=form.validated_data['order_number']).exists():
                        order_check = RequestChange.objects.get(request_name=form.validated_data['order_number'])
                        if order_check.request_user == merchant_owner.merchant_user.username:
                            order = {
                                "number": order_check.request_name,
                                "status": order_check.request_status
                            }
                            return Response(order, status=status.HTTP_200_OK)
                        else:
                            return Response({"ERROR": "Application not found"}, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response({"ERROR": "Application not found"}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"ERROR": "The data is not valid"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"ERROR": "Secret key not found"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"ERROR": "Key 'Key-Merchant', not found"}, status=status.HTTP_403_FORBIDDEN)





