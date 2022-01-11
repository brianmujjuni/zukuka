from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import branch
from branch.admin import BranchCurrency
from branch.models import Branch_Currency, Branches
from currency.models import Currency

# Create your views here.
@login_required(login_url='/authentication/login')
def index(request):
    branches = Branches.objects.all()

    context = {
        'branches': branches,
    }

    return render(request,'branch/index.html',context)

@login_required(login_url='/authentication/login')
def add_branch(request):

    
    context = {
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request,'branch/add-branch.html',context)
    if request.method =='POST':
        branchName = request.POST['branchName']
        phoneNo1 = request.POST['phoneNo1']
        phoneNo2 = request.POST['phoneNo2']
        email = request.POST['email']
        country = request.POST['country']
        location = request.POST['location']

        if not branchName:
            messages.error(request,'Please Branch Name Field Is Required')
            return render(request,'branch/add-branch.html',context)
        if not phoneNo1:
            messages.error(request,'Please All Phone Contacts Are Required')
            return render(request,'branch/add-branch.html',context)
        if not email:
            messages.error(request,'Please All Email Field Is Required')
            return render(request,'branch/add-branch.html',context)
        if not country:
            messages.error(request,'Please Country Field Is Required')
            return render(request,'branch/add-branch.html',context)
        if not location:
            messages.error(request,'Please Location Field Is Required')
            return render(request,'branch/add-branch.html',context)

        Branches.objects.create(branchName=branchName,phoneNo1=phoneNo1,phoneNo2=phoneNo2,
        email=email,country=country,location=location,regBy=request.user)
        messages.success(request,'Branch Successfully Saved ')
        return redirect('branches')

@login_required(login_url='/authentication/login')
def delete_branch(request,id):
    branch = Branches.objects.get(pk=id)
    branch.delete()
    messages.success(request,'Branch deleted Successfully')
    return redirect('branches')

@login_required(login_url='/authentication/login')
def edit_branch(request,id):

    branch = Branches.objects.get(pk=id)
    context = {
        'branch': branch,
        'values': branch,
    }
    if request.method =='GET':
        return render(request,'branch/edit-branch.html',context)
    if request.method == 'POST':


        branchName = request.POST['branchName']
        phoneNo1 = request.POST['phoneNo1']
        phoneNo2 = request.POST['phoneNo2']
        email = request.POST['email']
        country = request.POST['country']
        location = request.POST['location']

        if not branchName:
            messages.error(request,'Please Branch Name Field Is Required')
            return render(request,'branch/edit-branch.html',context)
        if not phoneNo1:
            messages.error(request,'Please All Phone Contacts Are Required')
            return render(request,'branch/edit-branch.html',context)
        if not email:
            messages.error(request,'Please All Email Field Is Required')
            return render(request,'branch/edit-branch.html',context)
        if not country:
            messages.error(request,'Please Country Field Is Required')
            return render(request,'branch/edit-branch.html',context)
        if not location:
            messages.error(request,'Please Location Field Is Required')
            return render(request,'branch/edit-branch.html',context)
        branch.branchName = branchName
        branch.phoneNo1 = phoneNo1
        branch.phoneNo2 = phoneNo2
        branch.email = email
        branch.country = country
        branch.location = location

        branch.save()
        messages.success(request,'Branch Details Successfully Updated')
        return redirect('branches')
       
   
@login_required(login_url='/authentication/login')
def view_branchCurrency(request):
    branchCurrency = Branch_Currency.objects.all()

    context ={
        'branchCurrency':  branchCurrency
    }
    return render(request,'branch/view-branch-currencies.html',context)

@login_required(login_url='/authentication/login')
def add_branchCurrency(request):
    currencies = Currency.objects.all()
    branch =Branches.objects.all()
    context ={

        'branch': branch,
        'currencies': currencies
    }
    if request.method == 'GET':
        return render(request,'branch/add-branch-currencies.html',context)
    if request.method == 'POST':
        branchName = request.POST['branchName']
        currencyCode = request.POST['currencyCode']
        exchangeRate = request.POST['exchangeRate']
        
        if currencyCode =='Please Select Currency':
            messages.error(request,'Please Select Currecny')
            return render(request,'branch/add-branch-currencies.html',context) 
        

        Branch_Currency.objects.create(branchName=branchName,currencyCode=currencyCode,
        exchangeRate=exchangeRate,regBy=request.user)
        messages.success(request,'Branch Currency SuccessFully Saved')
        return redirect('view-branch-currencies')
   
@login_required(login_url='/authentication/login')
def delete_branchCurrencies(request,id):
    branchCurrency = Branch_Currency.objects.get(pk=id)
    branchCurrency.delete()
    messages.success(request,'Branch Currency deleted Successfully')
    return redirect('view-branch-currencies')

@login_required(login_url='/authentication/login')
def edit_branchCurrency(request,id):
    branchCurrency = Branch_Currency.objects.get(pk=id)
    branch = Branches.objects.all()
    currencies = Currency.objects.all()

    context = {

        'branchCurrency': branchCurrency,
        'branch': branch,
        'currencies': currencies,
        'values': branchCurrency
    }
    if request.method ==  'GET':
        return render(request,'branch/edit-currency.html',context)
    if request.method == 'POST':
        branchName = request.POST['branchName']
        currencyCode = request.POST['currencyCode']
        exchangeRate = request.POST['exchangeRate']

        if not branchName:
            messages.error(request,'Please Branch Name Field Is Required')
            return render(request,'branch/edit-currency.html',context)
        if not currencyCode:
            messages.error(request,'Please Currency Field Is Required')
            return render(request,'branch/edit-currency.html',context)

        branchCurrency.branchName = branchName
        branchCurrency.currencyCode = currencyCode
        branchCurrency.exchangeRate = exchangeRate
        branchCurrency.save()
        messages.success(request,'Branch Currency SuccessFully Updated')
        return redirect('view-branch-currencies')

        





