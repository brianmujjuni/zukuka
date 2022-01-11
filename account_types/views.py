from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from branch.models import Branches
from currency.models import Currency
from account_types.models import Account_Types

# Create your views here.
@login_required(login_url='/authentication/login')
def index(request):
    Acctypes = Account_Types.objects.all()
    context = {
        'Acctypes':Acctypes
    }

    return render(request,'account-types/index.html',context)

@login_required(login_url='/authentication/login')
def add_account_types(request):
    branches =Branches.objects.all()
    currency = Currency.objects.all()
    context={
        'branches': branches,
        'currency': currency,
        'values': request.POST
    }
    if request.method =='GET':
        return render(request,'account-types/add-types.html',context)
    if request.method =='POST':
        branchName = request.POST['branchName']
        accountType = request.POST['accountType']
        description = request.POST['description']
        currencyCode = request.POST['currencyCode']
        minimumBalance = request.POST['minimumBalance']
        accountStatus = request.POST['accountStatus']

        if branchName == "Please Select Branch" :
            messages.error(request,'Please Branch Field Is Required')
            return render(request,'account-types/add-types.html',context)

        if not accountType:
            messages.error(request,'Please Account Type Field Is Required')
            return render(request,'account-types/add-types.html',context)

        if  currencyCode == "Please Select Currency" :
            messages.error(request,'Please Select Currency Field')
            return render(request,'account-types/add-types.html',context)

        if not minimumBalance:
            messages.error(request,'Please Fill In Minimum Balance For Account Types')
            return render(request,'account-types/add-types.html',context)

        if  accountStatus =="Please Select Account Status":
            messages.error(request,'Please Fill In Account Status')
            return render(request,'account-types/add-types.html',context)

        Account_Types.objects.create(branchName=branchName,accountType=accountType,description=description,
        currencyCode=currencyCode,minimumBalance=minimumBalance,accountStatus=accountStatus,regBy=request.user)
        messages.success(request,'Account Type Successfully Saved')
        return redirect('account-types')
    
@login_required(login_url='/authentication/login')
def delete_accountType(request,id):
    accountType =Account_Types.objects.get(pk=id)
    accountType.delete()
    messages.success(request,'Account Type Successfully Deleted')
    return redirect('account-types')
    
@login_required(login_url='/authentication/login')
def edit_accountType(request,id):
    accountTypes = Account_Types.objects.get(pk=id)
    context={
        'accountTypes': accountTypes,
        'values': accountTypes
    }
    if request.method  == 'GET':
        return render(request,'account-types/edit-account-type.html',context)
    if request.method == 'POST':
        branchName = request.POST['branchName']
        accountType = request.POST['accountType']
        description = request.POST['description']
        currencyCode = request.POST['currencyCode']
        minimumBalance = request.POST['minimumBalance']
        accountStatus = request.POST['accountStatus']
        if not branchName:
            messages.error(request,'Please Branch Name Is Required ')
            return redirect(request,'account-types/edit-account-type.html',context)

    
    
