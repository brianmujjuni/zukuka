from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json
from django.http import  JsonResponse, request, response,HttpResponse
from members.models import Members
from transactions.models import Transaction
from accountCharges.models import accountCharges
import csv
import xlwt
import datetime


# Create your views here.
@login_required(login_url='/authentication/login')
def index(request):
    accountcharges = accountCharges.objects.order_by('-regDate').all()
    context ={
        'accountcharges': accountcharges,
    }
    return render(request,'accountCharges/index.html',context)

@login_required(login_url='/authentication/login')
def add_charges(request):

    member = Members.objects.all()
    transaction = Transaction.objects.all()
    context ={

        'member': member,
        'values': request.POST
    }

    if request.method =='GET':
        return render(request,'accountCharges/add-charges.html',context)
    if request.method =='POST':
        transactionId = request.POST['transactionId']
        accountNo = request.POST['accountNo']
        accountName = request.POST['accountName']
        accountType =  request.POST['accountType']
        chargeType = request.POST['chargeType']
        oldBalance = request.POST['oldBalance']
        chargeAmount = request.POST['chargeAmount']
        newBalance = request.POST['newBalance']

        if not chargeType:
            messages.error(request,'Please Charge Description Is Required')
            return render(request,'accountCharges/add-charges.html',context)
        if not accountType:
            messages.error(request,'Please Account Type Is Required Cant Be Blank')
            return render(request,'accountCharges/add-charges.html',context)
        if not accountName:
            messages.error(request,'Please Account Name Field Is Required To Continue Charge')
            return render(request,'accountCharges/add-charges.html')

        accountCharges.objects.create(transactionId = transactionId,accountNo=accountNo,accountName=accountName,accountType=accountType,
        chargeType=chargeType,oldBalance=oldBalance,chargeAmount=chargeAmount,newBalance=newBalance,regBy= request.user)

        transaction.objects.create(transactionId = transactionId,accountNo=accountNo,accountName=accountName,accountType=accountType,transactionType=chargeType,
        transactionAmount=chargeAmount,balanceAmount=newBalance,)

        messages.success(request,'Account Charge Transaction Has Successfully Been Made')
        return redirect('accountCharges')

@login_required(login_url='/authentication/login')
def update_charges(request,transactionId):

    member = Members.objects.all()
    accountcharge =accountCharges.objects.get(pk=transactionId)
    
    context ={
        'accountcharge': accountcharge,
        'values': accountcharge
    }

    if request.method == 'GET':
        return render(request,'accountCharges/update-charges.html',context)
    if request.method == 'POST':
       
        accountNo = request.POST['accountNo']
        accountName = request.POST['accountName']
        accountType =  request.POST['accountType']
        chargeType = request.POST['chargeType']
        oldBalance = request.POST['oldBalance']
        chargeAmount = request.POST['chargeAmount']
        newBalance = request.POST['newBalance']

        if not accountNo:
            messages.error(request,'Please Account Number Field Is Missing')
            return render(request,'accountCharges/update-charges.html',context)
        if not accountName:
            messages.error(request,'Please Account Name Is Missing And Cant Continue')
            return render(request,'accountCharges/update-charges.html',context)
        if not accountType:
            messages.error(request,'Please Account Type Field Is Missing')
            return render(request,'accountCharges/update-charges.html',context)
        if  not chargeType:
            messages.error(request,'Please Indicate Charge Type To Contionue ')
            return render(request,'accountCharges/update-charges.html',context)
        if not chargeAmount:
            messages.error(request,'Please Include Charge Amount To Complete Transaction')
            return render(request,'accountCharges/update-charges.html',context)
        
        if not newBalance:
            messages.error(request,'Please Account New Balance Cant Be Blank')
            return render(request,'accountCharges/update-charges.html',context)

        accountcharge.accountNo = accountNo
        accountcharge.accountName = accountName
        accountcharge.accountType = accountType
        accountcharge.chargeType = chargeType
        accountcharge.chargeAmount = chargeAmount
        accountcharge.oldBalance = oldBalance
        accountcharge.newBalance = newBalance
        accountcharge.save()

        memb = Members.objects.get(accountNo = accountNo)
        memb.balance = newBalance
        memb.save()

        transaction = Transaction.objects.get(transactionId = transactionId)
        transaction.accountNo = accountNo
        transaction.accountName = accountName
        transaction.accountType = accountType
        transaction.transactionType = chargeType
        transaction.transactionAmount = chargeAmount
        transaction.balanceAmount = newBalance
        transaction.save()

        messages.success(request,'Account Charge SuccessFully Saved')
        return redirect('accountCharges')

@login_required(login_url='/authentication/login')
def delete_accountCharge(request,transactionId):
    accountCharge = accountCharges.objects.get(pk=transactionId)
    transaction = Transaction.objects.get(pk=transactionId)
    accountCharge.delete()
    transaction.delete()
    messages.success(request,'Account Charge Transaction Has SuccessFully Been Deleted')
    return redirect('accountCharges')

@login_required(login_url='/authentication/login')  
def search_accountCharges(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        charges = accountCharges.objects.order_by('-regDate').filter(
            accountNo__icontains=search_str) | accountCharges.objects.order_by('-regDate').filter(accountName__istartswith=search_str) | accountCharges.objects.order_by('-regDate').filter(
                accountType__icontains=search_str) | accountCharges.objects.order_by('-regDate').filter(transactionId__icontains=search_str) | accountCharges.objects.filter(
                    regDate__icontains=search_str) | accountCharges.objects.order_by('-regDate').filter(chargeType__icontains=search_str)
        data = charges.values()
        return JsonResponse(list(data),safe=False)

@login_required(login_url='/authentication/login')
def charges_excell(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename = Account Charges-'+ str(datetime.datetime.now())+ '.xls'
    wb = xlwt.Workbook(encoding = 'utf-8')
    ws = wb.add_sheet('Account Charges')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns =['Transaction Id','Account No','Account Name','Account Type','Charge Type','Old Balance','Charge Amount','Account Balance','Charge Date']
    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)
    
    font_style = xlwt.XFStyle()

    rows = accountCharges.objects.order_by('-regDate').all().values_list('transactionId','accountNo','accountName','accountType','chargeType','oldBalance','chargeAmount','newBalance','regDate')

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)
    wb.save(response)
    return response

@login_required(login_url='/authentication/login')
def charges_csv(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename = Account Charges-'+ str(datetime.datetime.now())+'.csv'

    writer = csv.writer(response)
    writer.writerow(['Transaction Id','Account No','Account Name','Account Type','Charge Type','Old Balance','Charge Amount','Account Balance','Charge Date'])

    charges = accountCharges.objects.order_by('-regDate').all()
    for charge in charges:
        writer.writerow([
            charge.transactionId,
            charge.accountNo,
            charge.accountName,
            charge.accountType,
            charge.chargeType,
            charge.oldBalance,
            charge.chargeAmount,
            charge.newBalance,
            charge.regDate
        ])

    return response

@login_required(login_url='/authentication/login')
def memberAccountName(request):
    if request.method =='GET':
        selectedAccount = request.GET['client_response']
        accountData =Members.objects.filter(accountNo = selectedAccount).first().accountName
        response_data = {}
        response_data['accountName'] = accountData
        print(accountData)

        return JsonResponse(response_data)