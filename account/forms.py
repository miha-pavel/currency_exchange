import io
import datetime

from django.core.files import File
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import Form
from django import forms

from .models import User, Contact


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')


class ContactForm(Form):
    email = forms.EmailField()
    title = forms.CharField(required=False)
    text = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 20}))

    def save(self):
        data = self.cleaned_data
        email = data['email']
        title = data['title']
        text = data['text']
        file_name = f'{datetime.datetime.now()}.txt'
        in_memory_file = io.StringIO(str(data))
        message_file = File(in_memory_file, name=file_name)
        Contact.objects.create(
            email=email,
            title=title,
            text=text,
            message_file=message_file
            )
