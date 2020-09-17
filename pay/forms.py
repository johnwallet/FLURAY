from django import forms
from django.forms import Select, TextInput

from users.models import CustomUser
from .models import RequestChange


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


class CommissionForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('valute_usd', 'valute_rub', 'valute_eur')
        widgets = {
            'valute_usd': TextInput(attrs={'class': 'form-control'}),
            'valute_rub': TextInput(attrs={'class': 'form-control'}),
            'valute_eur': TextInput(attrs={'class': 'form-control'}),
        }
