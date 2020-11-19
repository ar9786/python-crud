from django.core import validators
from django import forms
from .models import User1
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User1
        fields = ['name','email','password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(render_value = True,attrs={'class':'form-control'})
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']