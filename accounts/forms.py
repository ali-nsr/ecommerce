from django import forms
from django.core import validators
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import authenticate
from .models import *


# this form is for adding user in admin panel
class UserCreateForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone']

    def clean_password2(self):
        data = self.cleaned_data
        if data['password2'] and data['password1'] and data['password2'] != data['password1']:
            raise forms.ValidationError('check password please')
        return data['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField

    class Meta:
        model = User
        fields = ['phone']

    def clean_password(self):
        return self.initial['password']


class RegisterForm(forms.Form):
    phone = forms.CharField(
        label='Phone',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '09*********'
            }
        ),
        validators=[
            validators.MaxLengthValidator(11),
        ]
    )
    # password = forms.CharField(
    #     label='Password',
    #     widget=forms.PasswordInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Password'
    #         }
    #     ),
    #     validators=[
    #         validators.MinLengthValidator(8)
    #     ]
    #
    # )
    # confirm_password = forms.CharField(
    #     label='Confirm Password',
    #     widget=forms.PasswordInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Confirm Password'
    #         }
    #     ),
    #     validators=[
    #         validators.MinLengthValidator(8)
    #     ]
    # )

    def clean_phone(self):
        phone_number = self.cleaned_data['phone']
        if User.objects.filter(phone__exact=phone_number):
            raise forms.ValidationError('Phone Is Exists')
        return phone_number

    # def clean_confirm_password(self):
    #     password = self.cleaned_data['password']
    #     confirm_password = self.cleaned_data['confirm_password']
    #
    #     if password != confirm_password:
    #         raise forms.ValidationError('Passwords Are Not Match')
    #     return confirm_password


class CheckOtpForm(forms.Form):
    code = forms.CharField(
        label='code',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter code'
            }
        ),
        validators=[
            validators.MaxLengthValidator(4),
        ]
    )

class LoginForm(forms.Form):
    phone = forms.CharField(
        label='Phone',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Phone'
            }
        ),
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        ),
    )

    def clean(self):
        if self.is_valid():
            phone = self.cleaned_data['phone']
            password = self.cleaned_data['password']
            if not authenticate(phone=phone, password=password):
                raise forms.ValidationError("Phone Or Password Is Wrong")
