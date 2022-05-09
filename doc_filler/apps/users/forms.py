from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from doc_filler.apps.users.fields import UsernameFieldWithPlaceholder
from doc_filler.apps.users.models import User


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
    )
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}),
    )

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={
                'placeholder': 'Пароль',
                'class': 'form-control',
            }
        )
        self.fields['password1'].help_text = 'Пароль должен содержать хотя бы 8 символов'
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={
                'placeholder': 'Подтверждение пароля',
                'class': 'form-control',
            }
        )
        self.label_suffix = ''

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
        field_classes = {'username': UsernameFieldWithPlaceholder}


class UserAuthenticationForm(AuthenticationForm):

    def __init__(self, request=None, *args, **kwargs):
        super(UserAuthenticationForm, self).__init__(request=request, *args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={
            'autofocus': True,
            'placeholder': 'Имя пользователя',
        })
        self.fields['password'].widget = forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'placeholder': 'Пароль',
            }
        )
        self.label_suffix = ''
