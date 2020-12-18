from django import forms
from django.forms import Select, TextInput, RadioSelect, ClearableFileInput

from users.models import CustomUser
from .models import RequestChange, Transfer


# // КОШЕЛЕК // ФОРМА ДЛЯ ПОПОЛНЕНИЯ КОШЕЛЬКА
class RequestForm(forms.ModelForm):
    class Meta:
        model = RequestChange
        fields = ('request_sistemchange', 'request_currency', 'request_sum', 'criteri')
        widgets = {
            'request_sistemchange': RadioSelect(),
            'request_currency': RadioSelect(),
            'request_sum': TextInput(attrs={'class': 'form-control'}),
            'criteri': RadioSelect(),

        }


# // ОБМЕННИК // ФОРМА ДЛЯ ИЗМЕНЕНИЯ ПРИБЫЛИ
class CommissionForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('valute_usd', 'valute_rub', 'valute_eur', 'valute_with_usd', 'valute_with_rub', 'valute_with_eur')
        widgets = {
            'valute_usd': TextInput(attrs={'class': 'form-control'}),
            'valute_rub': TextInput(attrs={'class': 'form-control'}),
            'valute_eur': TextInput(attrs={'class': 'form-control'}),
            'valute_with_usd': TextInput(attrs={'class': 'form-control'}),
            'valute_with_rub': TextInput(attrs={'class': 'form-control'}),
            'valute_with_eur': TextInput(attrs={'class': 'form-control'}),
        }


# // ОБЩАЯ // ФОРМА ДЛЯ РЕКВИЗИТОВ
class RequisitesForm1(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'requsites_sberbank_rub', 'requsites_psb_rub', 'requsites_tinkoff_rub', 'requsites_gazprombank_rub',
            'requsites_alfabank_rub', 'requsites_russtandart_rub', 'requsites_vtb_rub', 'requsites_rosselhoz_rub', 'requsites_raifaizen_rub',
            'requsites_roketbank_rub', 'requsites_otkritie_rub', 'requsites_pochtabank_rub', 'requsites_rnkb_rub', 'requsites_rosbank_rub',
            'requsites_mtsbank_rub', 'requsites_qiwi_rub', 'requsites_qiwi_usd', 'requsites_payeer_rub', 'requsites_payeer_usd', 'requsites_payeer_eur',
            'requsites_webmoney_rub', 'requsites_webmoney_usd', 'requsites_webmoney_eur', 'requsites_pm_btc', 'requsites_pm_usd', 'requsites_pm_eur',
            'requsites_skrill_rub', 'requsites_skrill_usd', 'requsites_paypal_rub', 'requsites_paypal_usd', 'requsites_paypal_eur', 'requsites_umoney_rub',
            'requsites_btc', 'requsites_xrp', 'requsites_ltc', 'requsites_bch', 'requsites_xmr', 'requsites_eth', 'requsites_etc', 'requsites_dash')
        widgets = {

        }

class RequisitesForm2(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'requsites_width_sberbank_rub', 'requsites_width_psb_rub', 'requsites_width_tinkoff_rub', 'requsites_width_gazprombank_rub',
            'requsites_width_alfabank_rub', 'requsites_width_russtandart_rub', 'requsites_width_vtb_rub', 'requsites_width_rosselhoz_rub',
            'requsites_width_raifaizen_rub', 'requsites_width_roketbank_rub', 'requsites_width_otkritie_rub', 'requsites_width_pochtabank_rub', 'requsites_width_rnkb_rub',
            'requsites_width_rosbank_rub', 'requsites_width_mtsbank_rub', 'requsites_width_qiwi_rub', 'requsites_width_qiwi_usd', 'requsites_width_payeer_rub',
            'requsites_width_payeer_usd', 'requsites_width_payeer_eur', 'requsites_width_webmoney_rub', 'requsites_width_webmoney_usd', 'requsites_width_webmoney_eur', 'requsites_width_pm_btc',
            'requsites_width_pm_usd', 'requsites_width_pm_eur', 'requsites_width_skrill_rub', 'requsites_width_skrill_usd', 'requsites_width_paypal_rub', 'requsites_width_paypal_usd',
            'requsites_width_paypal_eur', 'requsites_width_umoney_rub', 'requsites_width_btc', 'requsites_width_xrp', 'requsites_width_ltc', 'requsites_width_bch', 'requsites_width_xmr', 'requsites_width_eth', 'requsites_width_etc', 'requsites_width_dash')




# // КОШЕЛЕК // ФОРМА ДЛЯ ВЫВОДА ИЗ КОШЕЛЬКА
class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = RequestChange
        fields = ('request_sistemchange', 'request_currency', 'request_sum', 'requisites', 'criteri')
        widgets = {
            'request_sistemchange': Select(
                attrs={'class': 'btn btn-outline-primary btn-block waves-effect waves-light'}),
            'request_currency': Select(attrs={'class': 'btn btn-outline-primary btn-block waves-effect waves-light'}),
            'request_sum': TextInput(attrs={'class': 'form-control'}),
            'requisites': TextInput(attrs={'class': 'form-control'}),
            'criteri': Select(
                attrs={'class': 'btn btn-outline-primary btn-block waves-effect waves-light'}),
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
