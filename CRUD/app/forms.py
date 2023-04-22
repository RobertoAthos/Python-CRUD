from django import forms
from .models import User

# model forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nome', 'telefone', 'email']