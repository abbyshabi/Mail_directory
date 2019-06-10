from django import forms
from .models import User
from django.core.validators import validate_email



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('First_Name', 'Last_Name', 'Email')

    