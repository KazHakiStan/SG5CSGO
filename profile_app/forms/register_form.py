from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label='Логин',
        help_text='Имя пользователя должно содержать не более 150 символов и не допускается спецсимволы',
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    password1 = forms.CharField(
        label='Пароль',
        help_text='Пароль должен содержать 1 большую букву, цифру и минимум 8 символов',
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'class': 'form-input'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')