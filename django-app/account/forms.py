from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60)

    class Meta:
        model = Account
        fields = ("email", "first_name", "last_name", "password1", "password2")

