from django import forms
from django.forms import Select, TextInput

from .models import RequestChange


class RequestForm(forms.ModelForm):

    class Meta:
        model = RequestChange
        fields = ('request_sistemchange', 'request_currency', 'request_sum')
        widgets = {
            'request_sistemchange': Select(attrs={'class': 'btn btn-outline-primary btn-block waves-effect waves-light'}),
            'request_currency': Select(attrs={'class': 'btn btn-outline-primary btn-block waves-effect waves-light'}),
            'request_sum': TextInput(attrs={'class': 'form-control'}),
        }
