from django import forms
from django.core import validators
from . import models

class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='نام',widget=forms.TextInput(attrs={'placeholder': 'First Name'}),
                                 validators=[validators.MaxLengthValidator(100)])
    last_name = forms.CharField(label='نام خانوادگی',widget=forms.TextInput(attrs={'placeholder': 'Last Name'}),
                                validators=[validators.MaxLengthValidator(100)])
    username = forms.CharField(label='نام کاربری',widget=forms.TextInput(attrs={'placeholder': 'Username'}),
                               validators=[validators.MaxLengthValidator(100)])
    email = forms.EmailField(label='ایمیل',widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
                             validators=[validators.MaxLengthValidator(100), validators.EmailValidator])
    phone = forms.CharField(label='تلفن',
        widget=forms.TextInput(attrs={'placeholder': 'Enter phone number'}),max_length=15)
    password = forms.CharField(label=' کلمه عبور',widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                               validators=[validators.MaxLengthValidator(100)])
    confirm_password = forms.CharField(label='تکرار کلمه عبور', widget=forms.PasswordInput,
                                       validators=[validators.MaxLengthValidator(100)])
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('پسورد باید یکی باشد')
        return confirm_password

class LoginForm(forms.Form):
    email = forms.EmailField(label='ایمیل',widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
                             validators=[validators.MaxLengthValidator(100), validators.EmailValidator])
    password = forms.CharField(label=' کلمه عبور',widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                               validators=[validators.MaxLengthValidator(100)])

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label='ایمیل',widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
                             validators=[validators.MaxLengthValidator(100), validators.EmailValidator])

class ResetPasswordForm(forms.Form):
    password = forms.CharField(label=' کلمه عبور',widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                               validators=[validators.MaxLengthValidator(100)])
    confirm_password = forms.CharField(label='تکرار کلمه عبور', widget=forms.PasswordInput,
                                       validators=[validators.MaxLengthValidator(100)])