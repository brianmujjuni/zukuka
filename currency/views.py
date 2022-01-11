from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from currency.models import Currency

# Create your views here.
@login_required(login_url='/authentication/login')
def index(request):
    currencies = Currency.objects.all()

    context = {
        'currencies': currencies
    }
    return render(request,'currency/index.html',context)

@login_required(login_url='/authentication/login')
def add_currency(request):

    context = {
        'values': request.POST
    }
    if request.method =='GET':
        return render(request,'currency/add-currency.html',context)
    if request.method =='POST':
        currencyName = request.POST['currencyName']
        currencyCode = request.POST['currencyCode']
        currencyStatus = request.POST['currencyStatus']
        regDate =request.POST['regDate']

        if not currencyName:
            messages.error(request,'Please Currency Name Field Is Required ')
            return render(request,'currency/add-currency.html',context)
        if not currencyCode:
            messages.error(request,'Please Currency Code Field Is Required ')
            return render(request,'currency/add-currency.html',context)

        Currency.objects.create(currencyName=currencyName,currencyCode=currencyCode,
        currencyStatus=currencyStatus,regDate=regDate,regBy=request.user)
        messages.success(request,'Currency Successfully Saved ')
        return redirect('view-curreny')

@login_required(login_url='/authentication/login')
def delete_currency(request,id):
    currency = Currency.objects.get(pk=id)
    currency.delete()
    messages.success(request,'Currency deleted Successfully')


@login_required(login_url='/authentication/login')
def edit_currency(request,id):

    currency = Currency.objects.get(pk=id)
    context ={
        'currency': currency,
        'values': currency

    }

    if request.method == 'GET':
        return render(request,'currency/edit-currency.html',context)
    if  request.method == 'POST':
        currencyName = request.POST['currencyName']
        currencyCode = request.POST['currencyCode']
        currencyStatus = request.POST['currencyStatus']

        if not  currencyName:
            messages.error(request,'Please Fill In Currency Name')
            return render(request,'currency/edit-currency.html',context)
        if not currencyCode:
            messages.error(request,'Please  Select Currency Code Field')
            return render(request,'currency/edit-currency.html',context)
        if not currencyStatus:
            messages.error(request,'Please Select Currency Status To Continue ')
            return render(request,'currency/edit-currency.html',context)

        currency.currencyName = currencyName
        currency.currencyCode = currencyCode
        currency.currencyStatus = currencyStatus
        currency.save()
        messages.success(request,'Currency Successfully Updated ')
        return redirect('view-curreny')

   