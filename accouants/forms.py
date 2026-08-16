from django import forms
from django.core.exceptions import ValidationError
from .models import User
class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput)
class SignupForm(forms.Form):
    phone_number = forms.CharField(max_length=15)
    password=forms.CharField(widget=forms.PasswordInput)
    password_confirmation = forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        if self.cleaned_data.get('password')==self.cleaned_data.get('password_confirmation'):
            return self.cleaned_data
        else : 
            raise ValidationError('the password do not match ')
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name","profile_image"]