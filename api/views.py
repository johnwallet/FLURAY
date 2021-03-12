from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Merchant
from api.serializers import RequestPSStatusSerializers, DepositRequestCreateSerializers
from personalaccount.metodviews import active_deposit_ps_global, range_deposit_ps_global
from personalaccount.models import CurrencyCBRF
from users.models import CustomUser


class RequestPSStatusView(APIView):
    """Получение списка для заявок на пополнение, с информацией о ПС (Название, Активность, Резерв, Минимальный лимит, Максимальный лимит)"""

    def get(self, request, key):
        try:
            merchant_owner = Merchant.objects.get(merchant_secret_key=key)
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
                        'code': itemps_k,
                        'name': list_name_ps[itemps_k],
                        'valute': list_valute_ps[itemps_k],
                        'curse': list_curse_valute[itemps_k],
                        'reserve': active_ps['list_active_reserve_ps'][itemps_k],
                        'min_limit': range_ps['list_range_min_reserve_ps'][itemps_k],
                        'max_limit': range_ps['list_range_max_reserve_ps'][itemps_k],
                    })
            s_list = RequestPSStatusSerializers(merchant_ps, many=True)
            return Response(s_list.data)
        except:
            return Response({"ERROR": "Secret key not found"}, status=status.HTTP_400_BAD_REQUEST)


class DepositRequestCreateView(APIView):
    """Создание заявки на пополнение"""

    def post(self, request, key):
        try:
            merchant_owner = Merchant.objects.get(merchant_secret_key=key)
            form = DepositRequestCreateSerializers(data=request.data)
            if form.is_valid():
                return Response(form.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"ERROR": "The data is not valid"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"ERROR": "Secret key not found"}, status=status.HTTP_400_BAD_REQUEST)



