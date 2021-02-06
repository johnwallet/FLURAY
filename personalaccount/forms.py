from django import forms
from django.forms import Select, TextInput, RadioSelect, ClearableFileInput, FileInput

from users.models import CustomUser, RangeSumDeposit, RangeSumWidth
from .models import RequestChange, Transfer


# // КОШЕЛЕК // ФОРМА ДЛЯ ПОПОЛНЕНИЯ КОШЕЛЬКА
class RequestForm(forms.ModelForm):
    class Meta:
        model = RequestChange
        fields = ('request_sistemchange', 'request_sum', 'criteri')
        widgets = {
            'request_sistemchange': TextInput(attrs={'class': 'input-final', 'id': 'name-fin-request-deposit', 'value': '-', 'readonly': ''}),
            'request_sum': TextInput(attrs={'class': 'input-final', 'id': 'sum-fin-request-deposit', 'value': '0.00', 'readonly': '', 'type': 'number'}),
            'criteri': TextInput(attrs={'class': 'input-final', 'id': 'kriteri-fin-request-deposit', 'value': 'БЫСТРАЯ ЗАЯВКА', 'readonly': ''}),
        }

# // КОШЕЛЕК // ДАННЫЕ ПРОФИЛЯ
class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('avatar', 'first_name', 'last_name', 'middle_name', 'phone_number', 'telegram_username')
        widgets = {
            'avatar': FileInput(),
            'first_name': TextInput(attrs={'spellcheck': 'false'}),
            'last_name': TextInput(attrs={'spellcheck': 'false'}),
            'middle_name': TextInput(attrs={'spellcheck': 'false'}),
            'phone_number': TextInput(attrs={'spellcheck': 'false'}),
            'telegram_username': TextInput(attrs={'spellcheck': 'false'})
        }


# // ОБМЕННИК // ФОРМА ДЛЯ ИЗМЕНЕНИЯ ПРИБЫЛИ
class CommissionForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'comis_in_sberbank_rub', 'comis_in_psb_rub', 'comis_in_tinkoff_rub', 'comis_in_gazprombank_rub',
            'comis_in_alfabank_rub', 'comis_in_russtandart_rub', 'comis_in_vtb_rub', 'comis_in_rosselhoz_rub',
            'comis_in_raifaizen_rub', 'comis_in_otkritie_rub', 'comis_in_pochtabank_rub',
            'comis_in_rnkb_rub', 'comis_in_rosbank_rub', 'comis_in_mtsbank_rub', 'comis_in_qiwi_rub',
            'comis_in_qiwi_usd', 'comis_in_payeer_rub', 'comis_in_payeer_usd', 'comis_in_payeer_eur',
            'comis_in_webmoney_rub', 'comis_in_webmoney_usd', 'comis_in_webmoney_eur', 'comis_in_pm_btc',
            'comis_in_pm_usd', 'comis_in_pm_eur', 'comis_in_skrill_eur', 'comis_in_skrill_usd', 'comis_in_paypal_rub',
            'comis_in_paypal_usd', 'comis_in_paypal_eur', 'comis_in_umoney_rub', 'comis_in_btc', 'comis_in_xrp',
            'comis_in_ltc', 'comis_in_bch', 'comis_in_xmr', 'comis_in_eth', 'comis_in_etc', 'comis_in_dash',

            'comis_out_sberbank_rub', 'comis_out_psb_rub', 'comis_out_tinkoff_rub', 'comis_out_gazprombank_rub',
            'comis_out_alfabank_rub', 'comis_out_russtandart_rub', 'comis_out_vtb_rub', 'comis_out_rosselhoz_rub',
            'comis_out_raifaizen_rub', 'comis_out_otkritie_rub', 'comis_out_pochtabank_rub',
            'comis_out_rnkb_rub', 'comis_out_rosbank_rub', 'comis_out_mtsbank_rub', 'comis_out_qiwi_rub',
            'comis_out_qiwi_usd', 'comis_out_payeer_rub', 'comis_out_payeer_usd', 'comis_out_payeer_eur',
            'comis_out_webmoney_rub', 'comis_out_webmoney_usd', 'comis_out_webmoney_eur', 'comis_out_pm_btc',
            'comis_out_pm_usd', 'comis_out_pm_eur', 'comis_out_skrill_eur', 'comis_out_skrill_usd', 'comis_out_paypal_rub',
            'comis_out_paypal_usd', 'comis_out_paypal_eur', 'comis_out_umoney_rub', 'comis_out_btc', 'comis_out_xrp',
            'comis_out_ltc', 'comis_out_bch', 'comis_out_xmr', 'comis_out_eth', 'comis_out_etc', 'comis_out_dash'
        )
        widgets = {

        }


# // ОБЩАЯ // ФОРМА ДЛЯ РЕКВИЗИТОВ
class RequisitesForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'requsites_sberbank_rub', 'requsites_psb_rub', 'requsites_tinkoff_rub', 'requsites_gazprombank_rub',
            'requsites_alfabank_rub', 'requsites_russtandart_rub', 'requsites_vtb_rub', 'requsites_rosselhoz_rub', 'requsites_raifaizen_rub',
            'requsites_otkritie_rub', 'requsites_pochtabank_rub', 'requsites_rnkb_rub', 'requsites_rosbank_rub',
            'requsites_mtsbank_rub', 'requsites_qiwi_rub', 'requsites_qiwi_usd', 'requsites_payeer_rub', 'requsites_payeer_usd', 'requsites_payeer_eur',
            'requsites_webmoney_rub', 'requsites_webmoney_usd', 'requsites_webmoney_eur', 'requsites_pm_btc', 'requsites_pm_usd', 'requsites_pm_eur',
            'requsites_skrill_eur', 'requsites_skrill_usd', 'requsites_paypal_rub', 'requsites_paypal_usd', 'requsites_paypal_eur', 'requsites_umoney_rub',
            'requsites_btc', 'requsites_xrp', 'requsites_ltc', 'requsites_bch', 'requsites_xmr', 'requsites_eth', 'requsites_etc', 'requsites_dash')


# // ОБМЕННИК // ФОРМА РЕЗЕРВА
class ReservChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'reserv_sberbank_rub', 'reserv_psb_rub', 'reserv_tinkoff_rub', 'reserv_gazprombank_rub',
            'reserv_alfabank_rub', 'reserv_russtandart_rub', 'reserv_vtb_rub', 'reserv_rosselhoz_rub',
            'reserv_raifaizen_rub', 'reserv_otkritie_rub', 'reserv_pochtabank_rub', 'reserv_rnkb_rub',
            'reserv_rosbank_rub', 'reserv_mtsbank_rub', 'reserv_qiwi_rub', 'reserv_qiwi_usd', 'reserv_payeer_rub',
            'reserv_payeer_usd', 'reserv_payeer_eur', 'reserv_webmoney_rub', 'reserv_webmoney_usd', 'reserv_webmoney_eur', 'reserv_pm_btc',
            'reserv_pm_usd', 'reserv_pm_eur', 'reserv_skrill_eur', 'reserv_skrill_usd', 'reserv_paypal_rub', 'reserv_paypal_usd',
            'reserv_paypal_eur', 'reserv_umoney_rub', 'reserv_btc', 'reserv_xrp', 'reserv_ltc', 'reserv_bch', 'reserv_xmr',
            'reserv_eth', 'reserv_etc', 'reserv_dash')


# // КОШЕЛЕК // ФОРМА ДЛЯ ВЫВОДА ИЗ КОШЕЛЬКА
class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = RequestChange
        fields = ('request_sistemchange', 'request_sum', 'criteri', 'requisites')
        widgets = {
            'request_sistemchange': TextInput(attrs={'class': 'input-final', 'id': 'name-fin-request-deposit', 'value': '-', 'readonly': ''}),
            'request_sum': TextInput(attrs={'class': 'input-final', 'id': 'sum-fin-request-deposit', 'value': '0.00', 'readonly': '', 'type': 'number'}),
            'criteri': TextInput(attrs={'class': 'input-final', 'id': 'kriteri-fin-request-deposit', 'value': 'БЫСТРАЯ ЗАЯВКА', 'readonly': ''}),
            'requisites': TextInput(attrs={'class': 'input-final', 'id': 'requisites-fin-request-deposit', 'value': '-', 'readonly': ''}),
        }


# // ОБЩАЯ // ФОРМА ПЕРЕВОДА
class TransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = ('transfer_in', 'transfer_sum')
        widgets = {
            'transfer_in': TextInput(attrs={'class': 'form-control'}),
            'transfer_sum': TextInput(attrs={'class': 'form-control'}),
        }

# // ОБМЕННИК // ФОРМА АКТИВНОСТИ ПС
class ActivePSForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('active_in_sberbank_rub', 'active_in_psb_rub', 'active_in_tinkoff_rub', 'active_in_gazprombank_rub',
                  'active_in_alfabank_rub', 'active_in_russtandart_rub', 'active_in_vtb_rub', 'active_in_rosselhoz_rub',
                  'active_in_raifaizen_rub', 'active_in_otkritie_rub', 'active_in_pochtabank_rub',
                  'active_in_rnkb_rub', 'active_in_rosbank_rub', 'active_in_mtsbank_rub', 'active_in_qiwi_rub', 'active_in_qiwi_usd',
                  'active_in_payeer_rub', 'active_in_payeer_usd', 'active_in_payeer_eur', 'active_in_webmoney_rub', 'active_in_webmoney_usd',
                  'active_in_webmoney_eur', 'active_in_pm_btc', 'active_in_pm_usd', 'active_in_pm_eur', 'active_in_skrill_eur',
                  'active_in_skrill_usd', 'active_in_paypal_rub', 'active_in_paypal_usd', 'active_in_paypal_eur', 'active_in_umoney_rub',
                  'active_in_btc', 'active_in_xrp', 'active_in_ltc', 'active_in_bch', 'active_in_xmr', 'active_in_eth', 'active_in_etc',
                  'active_in_dash', 'active_out_sberbank_rub', 'active_out_psb_rub', 'active_out_tinkoff_rub', 'active_out_gazprombank_rub',
                  'active_out_alfabank_rub', 'active_out_russtandart_rub', 'active_out_vtb_rub', 'active_out_rosselhoz_rub',
                  'active_out_raifaizen_rub', 'active_out_otkritie_rub', 'active_out_pochtabank_rub',
                  'active_out_rnkb_rub', 'active_out_rosbank_rub', 'active_out_mtsbank_rub', 'active_out_qiwi_rub', 'active_out_qiwi_usd',
                  'active_out_payeer_rub', 'active_out_payeer_usd', 'active_out_payeer_eur', 'active_out_webmoney_rub',
                  'active_out_webmoney_usd', 'active_out_webmoney_eur', 'active_out_pm_btc', 'active_out_pm_usd', 'active_out_pm_eur',
                  'active_out_skrill_eur', 'active_out_skrill_usd', 'active_out_paypal_rub', 'active_out_paypal_usd',
                  'active_out_paypal_eur', 'active_out_umoney_rub', 'active_out_btc', 'active_out_xrp', 'active_out_ltc',
                  'active_out_bch', 'active_out_xmr', 'active_out_eth', 'active_out_etc', 'active_out_dash')


# // ФОРМА ДИАПАЗОНА СУММ ОБМЕННИКА
class RangeDepositForm(forms.ModelForm):
    class Meta:
        model = RangeSumDeposit
        exclude = ['deposit_range_username']


# // ФОРМА ДИАПАЗОНА СУММ ОБМЕННИКА
class RangeWidthForm(forms.ModelForm):
    class Meta:
        model = RangeSumWidth
        exclude = ['width_range_username']
