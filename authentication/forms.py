from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)
        field_classes = {'email': forms.EmailField}