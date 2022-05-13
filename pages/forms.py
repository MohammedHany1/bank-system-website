from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import Customer, Transfer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'balance',]
class TransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = ['sender', 'reciever', 'amount',]