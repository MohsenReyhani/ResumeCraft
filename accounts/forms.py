from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UsernameField, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class PhoneNumberLoginForm(forms.Form):
    phone_number = forms.CharField(
        label="شماره تلفن",
        widget=forms.TextInput(attrs={"class": "form-control form-control-dg", "maxlength": "11", "type": "tel", 'placeholder': 'شماره تلفن خود را وارد نمایید'}),
        max_length=15, 
        required=True,
    )

class CustomUserCreationForm(UserCreationForm):

    phone_no = forms.CharField(
        label=_("شماره تلفن"),
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-control form-control-dg", "placeholder": "نام"}),
    ) 
    last_name = forms.CharField(
        label=_("نام خانوادگی"),
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "نام خانوادگی"}),
    )

    class Meta:
        model = CustomUser
        fields = ('first_name', 'phone_no', 'email')
    
    labels = {
        'first_name': 'نام',
        'email': 'ایمیل'
    }

    widgets = {
      'username': forms.TextInput(attrs={
          'class': 'form-control',
          'placeholder': 'نام کاربری'
      }),
      'email': forms.EmailInput(attrs={
          'class': 'form-control',
          'placeholder': 'example@company.com'
      })
    }

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser



class LoginForm(AuthenticationForm):
  username = UsernameField(label=_("نام کاربری"), widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "نام کاربری"}))
  password = forms.CharField(
      label=_("کلمه عبور"),
      strip=False,
      widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "کلمه عبور"}),
  )

class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))

class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'New Password'
    }), label="New Password")
    new_password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Confirm New Password'
    }), label="Confirm New Password")
    

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Old Password'
    }), label='Old Password')
    new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'New Password'
    }), label="New Password")
    new_password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Confirm New Password'
    }), label="Confirm New Password")

class UserSettingForm(forms.ModelForm):

    first_name = forms.CharField(
        label="نام",
        strip=False,
        widget=forms.TextInput(attrs={
            "placeholder": "نام",
            "class": "form-control"
        }),
    )
    last_name = forms.CharField(
        label="نام خانوادگی",
        strip=False,
        widget=forms.TextInput(attrs={
            "placeholder": "نام خانوادگی",
            "class": "form-control"
        }),
    )

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name')