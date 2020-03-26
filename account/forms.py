from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import User, Contact


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'avatar')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'avatar')


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['email', 'title', 'text']


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    password2 = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def clean_password2():
        cleaned_data = super().clean()
        return cleaned_data