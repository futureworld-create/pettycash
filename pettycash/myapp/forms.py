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

class RegisterModelForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']





