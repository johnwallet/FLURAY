from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField, \
    PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import TextInput, EmailInput, PasswordInput
from django.utils.translation import gettext, gettext_lazy as _

from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)

from .models import CustomUser, CustomUserId


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username',)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Это поле обязательно', widget=forms.EmailInput(
                                      attrs={'class': 'form-control'}))
    userid = forms.ModelChoiceField(queryset=CustomUserId.objects.all(), empty_label=None,
                                  widget=forms.Select(
                                      attrs={'class': 'custom-select'}))

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control password-views'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control password-views'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'userid')
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs['autofocus'] = False


class AuthForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': False, 'class': 'form-control'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control password-views'}),
    )

    error_messages = {
        'invalid_login': "Пользователя не существует",
        'inactive': "Активируйте аккаунт, перейдя по ссылке из письма",
        'invalid_pass': 'Неверный пароль',
    }

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                try:
                    user_login = CustomUser.objects.get(username=username)
                    user_pass = False
                except:
                    user_login = None
                    user_pass = False

                if user_login is not None:
                    self.confirm_login_allowed(user_login)
                    if not user_pass:
                        raise forms.ValidationError(
                            self.error_messages['invalid_pass'],
                            code='invalid_pass',
                        )
                else:
                    raise forms.ValidationError(
                        self.error_messages['invalid_login'],
                        code='invalid_login',
                    )
        return self.cleaned_data


class PassReset(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-control'})
    )


class PassResetConfirm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control password-views'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control password-views'}),
    )


class PassChange(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': False, 'class': 'form-control password-views'}),
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control password-views'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control password-views'}),
    )



