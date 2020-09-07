from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, CustomUserId


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username',)


class SignUpId(forms.Form):
    userid = forms.ModelChoiceField(label='userid',queryset=CustomUserId.objects.all(), empty_label=None,
                                        widget=forms.Select(attrs={'class': 'btn btn-outline-primary btn-block waves-effect waves-light'}))

    def signup(self, request, user):
        user.userid = self.cleaned_data['userid']
        user.save()
