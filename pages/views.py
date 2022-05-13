from email import message
from django.shortcuts import redirect, render

from pages.forms import CustomerForm, TransferForm
from .models import Customer, Transfer
from django.contrib import messages
from django.contrib.auth import authenticate
# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def viewCustomers(request):
    return render(request, 'pages/view customers.html', {'customers': Customer.objects.all()})

def transfer(request, id):
    sender = Customer.objects.get(id = id)
    if request.method == 'POST':
        transfer_form = TransferForm(request.POST)
        if transfer_form.is_valid():
            transfer_form = transfer_form.save(commit=False)
            reciever = Customer.objects.get(name = transfer_form.reciever)
            check = True
            transfer_form.sender = sender.name
            if transfer_form.sender == transfer_form.reciever:
                messages.error(request, 'The sender can not transfer to himself')
                check = False
            if sender.balance < transfer_form.amount:
                messages.error(request, f'{sender.name} does not have enough balance for this transition')
                check = False
            if  transfer_form.amount <= 0:
                messages.error(request, 'The amount can not be less than or equal 0')
                check = False
            if check == False:
                return redirect('transfer')
            reciever.balance += transfer_form.amount
            sender.balance -= transfer_form.amount
            sender.save()
            reciever.save()
            transfer_form.save()
            return redirect('transfer')
    else:
        transfer_form = TransferForm
    context = {
        'customer' : sender,
        'transferForm': TransferForm,
    }
    return render(request, 'pages/transfer.html', context)

def trasferHistory(request):
    return render(request, 'pages/transfer history.html', {'transfers': Transfer.objects.all()})

def createCustomer(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST) 
        if customer_form.is_valid():
            customer_form = customer_form.save(commit=False)
            customer_form.save()
    else:
        customer_form = CustomerForm
    context = {
        'customerForm': CustomerForm,
    }
    return render(request, 'pages/create customer.html', context)