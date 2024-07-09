from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from user.models import UserBalance
from user.forms import UserBalanceForm
from transaction.service import TransactionService
from transaction.models import Transaction
from django.db import transaction
from user.services import UserService
from django.contrib import messages

# Create your views here.
@login_required
@transaction.atomic
def admin_add_balance(request):
    form = UserBalanceForm()
    if request.method == "POST":
        form = UserBalanceForm(request.POST)
        if form.is_valid():
            form.save()
            TransactionService.create_transaction(
                "Top up",
                request.POST['user'],
                request.POST['balance'],
                Transaction.Transactionstatus.COMPLETED,
                Transaction.PaymentMethod.ADMIN,
                Transaction.TransactionType.INCOME
            )
            messages.success(request,"Updated balance")
            return redirect('/users/userbalance')
    context = {
        'form':form
    }
    return render(request, 'user/balance-create.html',context)

@login_required
def list_user_balance(request):
    user_balance = UserBalance.objects.all()
    context = {
        'user_balance':user_balance
    }
    return render(request, 'user/balance-list.html',context)

@login_required
@transaction.atomic
def update_balance(request,id):
    user_balance = UserBalance.objects.get(id=id)
    error = {}
    if request.method == "POST":
        if int(request.POST['balance'])<0:
            error['form']="Value must be positive" 
        UserService.add_balance(user_balance, int(request.POST['balance']))
        TransactionService.create_transaction(
                "Update balance",
                user_balance.user.id,
                request.POST['balance'],
                Transaction.Transactionstatus.COMPLETED,
                Transaction.PaymentMethod.ADMIN,
                Transaction.TransactionType.INCOME

            )
        
        return redirect('/users/userbalance')
    
    context = {
        "error":error
    }
    return render(request, 'user/update_balance.html',context)

