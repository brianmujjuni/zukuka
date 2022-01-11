from django.http import  JsonResponse, response,HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from deposits.models import Deposits
from members.models import Members
from  accounts.models import Account
from transactions.models import Transaction
import json
import datetime 
import csv
import xlwt
# Create your views here.

@login_required(login_url='/authentication/login')
def index(request):
    deposits = Deposits.objects.order_by('-dateReg').all()

    context ={
        'deposits': deposits
    }
    return render(request,'deposits/index.html',context)

@login_required(login_url='/authentication/login')
def add_account_deposits(request):

    members = Members.objects.order_by('-regDate').filter(accountStatus='Active')

    context = {
        'members': members,
        'values': request.POST
    }

    if request.method =='GET':
        return render(request,'deposits/add-deposits.html',context)

    if request.method == 'POST':
        transactionId = request.POST['transactionId']
        accountNo = request.POST['accountNo']
        accountName = request.POST['accountName']
        accountType = request.POST['accountType']
        ninNumber = request.POST['ninNumber']
        contact = request.POST['contact']
        accountCurrency = request.POST['accountCurrency']
        oldBalance = request.POST['oldBalance']
        depositAmount = request.POST['depositAmount']
        newBalance = request.POST['newBalance']
        depositDate = request.POST['depositDate']
        transanctionType = 'Deposit'

        if not accountNo:
            messages.error(request,'Please Select Account Number To Continue')
            return render(request,'deposits/add-deposits.html',context)

        if not accountName:
            messages.error(request,'Please Account Name Field Is Required To  Continue')
            return render(request,'deposits/add-deposits.html',context)

        if not depositAmount:
            messages.error(request,'Please Deposit amount Field Is Required')
            return render(request,'deposits/add-deposits.html',context)

        if not newBalance:
            messages.error(request,'Please New Balance Not Reflecting')
            return render(request,'deposits/add-deposits.html',context)

        if depositDate =='mm/dd/yyyy':
            messages.error(request,'Please Select Transaction Date To Continue')
            return render(request,'deposits/add-deposits.html',context)

        Deposits.objects.create(deposit_id=transactionId,accountNo=accountNo,accountName=accountName,
            accountType=accountType,ninNumber=ninNumber,contact=contact,accountCurrency=accountCurrency,
            oldBalance=oldBalance,depositAmount=depositAmount,newBalance=newBalance,depositDate=depositDate,regBy =request.user )
        
        #Save the transaction in the transactions Model
        Transaction.objects.create(transactionId=transactionId,accountNo=accountNo,accountName=accountName,accountType=accountType,transanctionType=transanctionType,
        transactionAmount=depositAmount,balanceAmount=newBalance,regBy =request.user)

        #calling the members balance to update amount
        memberBalance = Members.objects.get(pk = accountNo)
        memberBalance.balance = newBalance
        memberBalance.save()
        messages.success(request,'Deposit Transaction Of Transaction Id'+str(transactionId)+'Has Been Saved')
        return redirect('deposits')

@login_required(login_url='/authentication/login')
def delete_deposit(request,deposit_id):
    deposit = Deposits.objects.get(pk=deposit_id)
    deposit.delete()
    messages.success(request,'Deposit Transaction SuccessFully Deleted')
    return redirect('deposits')

@login_required(login_url='/authentication/login')
def update_deposit(request,deposit_id):
    deposit = Deposits.objects.get(pk=deposit_id)
    
    context = {
        'deposit': deposit,
        'values': deposit
    }

    if request.method == 'GET':
        return render(request,'deposits/update-deposits.html',context)
    if request.method =='POST':
        transactionId = request.POST['transactionId']
        accountNo = request.POST['accountNo']
        accountName = request.POST['accountName']
        accountType = request.POST['accountType']
        ninNumber = request.POST['ninNumber']
        contact = request.POST['contact']
        accountCurrency = request.POST['accountCurrency']
        oldBalance = request.POST['oldBalance']
        depositAmount = request.POST['depositAmount']
        newBalance = request.POST['newBalance']
        depositDate = request.POST['depositDate']

        if not accountNo:
            messages.error(request,'Please Account Number Field Is Missing')
            return render(request,'deposits/update-deposit.html',context)
        if not accountName:
            messages.error(request,'Please Account Name Is Required')
            return render(request,'deposits/update-deposit.html',context)
        if not accountType:
            messages.error(request,'Please Account Type Is Missing')
            return render(request,'deposits/update-deposit.html',context)
        if not accountCurrency:
            messages.eror(request,'Please Account Currency Is Missing')
            return render(request,'deposits/update-deposit.html',context)
        if not oldBalance:
            messages.error(request,'Please Account Old Balance Is Missing ')
            return render(request,'deposits/update-deposit.html',context)
        if not depositAmount:
            messages.error(request,'Please Deposit Amount Is Required')
            return render(request,'deposits/update-deposit.html',context)
        if not newBalance:
            messages.error(request,'Please Account New Balance Is Missing')
            return render(request,'deposits/update-deposit.html',context)

        deposit.accountNo = accountNo
        deposit.accountName = accountName
        deposit.accountType = accountType
        deposit.ninNumber = ninNumber
        deposit.contact = contact
        deposit.accountCurrency =accountCurrency
        deposit.oldBalance = oldBalance
        deposit.depositAmount =depositAmount
        deposit.newBalance =newBalance
        deposit.depositDate = depositDate
        
        deposit.save()
        messages.success(request,'Deposit Transaction SuccessFully Updated')
        return redirect('deposits')

@login_required(login_url='/authentication/login')
def memberAccountType(request):
    if request.method == 'GET':
        selectedAccount = request.GET['client_response']
        accountData = Members.objects.filter(accountNo = selectedAccount).first().accountType
        response_data ={}
        response_data['accountType'] = accountData
       
        return JsonResponse(response_data)

@login_required(login_url='/authentication/login')
def memberCurrency(request):
    if request.method =='GET':
        selectedAccount = request.GET['client_response']
        accountData =Members.objects.filter(accountNo = selectedAccount).first().accountCurrency
        response_data = {}
        response_data['accountCurrency'] = accountData

        return JsonResponse(response_data)

@login_required(login_url='/authentication/login')
def memberName(request):
    if request.method =='GET':
        selectedAccount = request.GET['client_response']
        accountData = Members.objects.filter(accountNo = selectedAccount).first().accountName
        response_data = {}
        response_data['accountName'] = accountData

        return JsonResponse(response_data)

@login_required(login_url='/authentication/login')
def memberninNumber(request):
    if request.method =='GET':
        selectedAccount = request.GET['client_response']
        accountData =Account.objects.filter(accountNo = selectedAccount).first().ninNumber
        response_data = {}
        response_data['ninNumber'] = accountData
        return JsonResponse(response_data)

def memberContact(request):
    if request.method =='GET':
        selectedAccount = request.GET['client_response']
        accountData =Account.objects.filter(accountNo = selectedAccount).first().phoneNo1
        response_data = {}
        response_data['phoneNo1'] = accountData
        print(accountData)
        return JsonResponse(response_data)


@login_required(login_url='/authentication/login')
def memberBalance(request):
    if request.method =='GET':
        selectedAccount = request.GET['client_response']
        accountData =Members.objects.filter(accountNo = selectedAccount).first().balance
        response_data = {}
        response_data['balance'] = accountData
        
        return JsonResponse(response_data)

@login_required(login_url='/authentication/login')
def deposit_excel(request):
    response = HttpResponse(content_type = 'application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename = Deposits' + str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding = 'utf-8')
    ws = wb.add_sheet('Deposits')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Deposit Id','Account No','Account Name','Account Type','Currency','Old Balance','Deposit','New Balance','Deposit Date']

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)
    font_style = xlwt.XFStyle()
    rows = Deposits.objects.all().values_list('deposit_id','accountNo','accountName','accountType','accountCurrency','oldBalance','depositAmount','newBalance','depositDate')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)
    wb.save(response)
    return response

@login_required(login_url='/authentication/login')
def deposit_csv(request):
    response = HttpResponse(content_type ='text/csv')
    response['Content-Disposition'] = 'attachment; filename = Withdraws'+str(datetime.datetime.now())+'.csv'
    writer = csv.writer(response)
    writer.writerow(['Deposit Id','Account No','Account Name','Account Type','Currency','Old Balance','Deposit','New Balance','Deposit Date'])
    deposits = Deposits.objects.all()

    for deposit in deposits:
        writer.writerow([deposit.deposit_id,deposit.accountNo,deposit.accountName,deposit.accountType,
        deposit.accountCurrency,deposit.oldBalance,deposit.depositAmount,deposit.newBalance,deposit.depositDate])
    return response

@login_required(login_url='/authentication/login')
def search_deposit(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        deposits = Deposits.objects.order_by('-dateReg').filter(accountNo__istartswith=search_str) | Deposits.objects.order_by('-dateReg').filter(
            accountName__icontains=search_str) | Deposits.objects.order_by('-dateReg').filter(
                deposit_id__istartswith=search_str) | Deposits.objects.order_by('-dateReg').filter(newBalance__istartswith=search_str)
        data = deposits.values()
        return JsonResponse(list(data),safe=False)
