from django.shortcuts import render
from .models import Transaction
from django.contrib.auth.decorators import login_required
from django.http import  JsonResponse, response,HttpResponse
import datetime 
import json
import csv
import xlwt
# Create your views here.

@login_required(login_url='/authentication/login')
def index(request):
    transactions = Transaction.objects.all()

    context ={
        'transactions':transactions
    }
    return render(request,'transactions/index.html',context)

@login_required(login_url='/authentication/login')
def members_transactions(request):
    response = HttpResponse(content_type = 'application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename = Account Transactions-'+ str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding = 'utf-8')
    ws = wb.add_sheet('Account Transaction')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Transaction Id','Account No','Account Name','Account Type','Transaction Type','Transaction Amount','Account Balance','Registered By','Transaction Date']

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)
    font_style = xlwt.XFStyle()
    rows = Transaction.objects.all().values_list('transactionId','accountNo','accountName','accountType','transanctionType','transactionAmount','balanceAmount','transactionDate')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)
    wb.save(response)
    return response

@login_required(login_url='/authentication/login')
def transaction_csv(request):
    response = HttpResponse(content_type ='text/csv')
    response['Content-Disposition'] = 'attachment; filename =Account Transactions-'+str(datetime.datetime.now())+'.csv'
    writer = csv.writer(response)
    writer.writerow(['Transaction Id','Account No','Account Name','Account Type','Transaction Type','Transaction Amount','Account Balance','Registered By','Transaction Date'])
    transactions = Transaction.objects.order_by('-transactionDate').all()

    for transaction in transactions:
        writer.writerow([
            transaction.transactionId,
            transaction.accountNo,
            transaction.accountName,
            transaction.accountType,
            transaction.transanctionType,
            transaction.transactionAmount,
            transaction.balanceAmount,
            transaction.regBy,
            transaction.transactionDate,

        ])
    return response

@login_required(login_url='/authentication/login')
def search_transactions(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        transactoins = Transaction.objects.order_by('-transactionDate').filter(transactionId__istartswith=search_str) | Transaction.objects.order_by('-transactionDate').filter(
            accountNo__icontains=search_str) | Transaction.objects.order_by('-transactionDate').filter(
                accountName__icontains=search_str) | Transaction.objects.filter(transactionDate__istartswith=search_str) | Transaction.objects.filter(transactionDate__icontains=search_str)
            
        data = transactoins.values()
        return JsonResponse(list(data),safe=False)