from django import forms
from django.forms import Select, TextInput

from users.models import CustomUser
from .models import RequestChange, Transfer


# // КОШЕЛЕК // ФОРМА ДЛЯ ПОПОЛНЕНИЯ КОШЕЛЬКА
class RequestForm(forms.ModelForm):
    class Meta:
        model = RequestChange
        fields = ('request_sistemchange', 'request_currency', 'request_sum', 'criteri')
        widgets = {
            'request_sistemchange': Select(
                attrs={'class': 'btn btn-outline-primary btn-block waves-effect waves-light'}),
            'request_currency': Select(attrs={'class': 'btn btn-outline-primary btn-block waves-effect waves-light'}),
            'request_sum': TextInput(attrs={'class': 'form-control'}),
            'criteri': Select(
                attrs={'class': 'btn btn-outline-primary btn-block waves-effect waves-light'}),

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
class RequisitesForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('requsites_sberbank', 'requsites_qiwi')
        widgets = {
            'requsites_sberbank': TextInput(attrs={'class': 'form-control'}),
            'requsites_qiwi': TextInput(attrs={'class': 'form-control'}),
        }


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
