from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-12'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-12'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control col-md-12'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

# class UserLoginForm(forms.ModelForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-md-12'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control col-md-12'}))
#
#     class Meta:
#         model = User
#         fields = ['username', 'password']
