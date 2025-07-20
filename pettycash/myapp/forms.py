from django import forms
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['description', 'category', 'amount']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter expense details'}),
            'category': forms.Select(),
            'amount': forms.NumberInput(attrs={'step': '0.01'}),
        }
  # your custom user model

from django import forms
from .models import User  # your custom AbstractUser-based model

class RegisterModelForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        
        return cleaned_data





