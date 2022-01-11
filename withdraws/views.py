
from django.db.models.query_utils import select_related_descend
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from withdraws.models import Withdraws
from transactions.models import Transaction
from members.models import Members
from accounts.models import Account
from account_types.models import Account_Types
from accountCharges.models import accountCharges
import json
from django.http import  JsonResponse, response,HttpResponse
import datetime 
import csv
import xlwt

# Create your views here.
@login_required(login_url='/authentication/login')
def index(request):
    
    withdraws = Withdraws.objects.all()

    context = {
        'withdraws': withdraws
    }
    return render(request,'withdraws/index.html',context)

@login_required(login_url='/authentication/login')
def add_withdraws(request):

    members = Members.objects.order_by('-regDate').filter(accountStatus='Active')
    context ={
        'members':members,
        'values': request.POST
    }

    if request.method =='GET':
        return render(request,'withdraws/add-withdraw.html',context)
    if request.method =='POST':
       
        withdraw_id =request.POST['withdraw_id']
        accountNo = request.POST['accountNo']
        accountName = request.POST['accountName']
        accountType = request.POST['accountType']
        ninNumber = request.POST['ninNumber']
        contact = request.POST['contact']
        accountCurrency = request.POST['accountCurrency']
        oldBalance = request.POST['oldBalance']
        charges = request.POST['charges']
        withdrawAmount = request.POST['withdrawAmount']
        newBalance =request.POST['newBalance']
        withdrawDate = request.POST['withdrawDate']
        transactionType = 'Withdraw'

        if accountType == 'PakaPaka' or accountType == 'Saving':
            messages.error(request,'Please Your Going To be Charged 10,000/=')
            charges = 10000
            return  render(request,'withdraws/add-withdraw.html',context)
       
        if not accountNo:
            messages.error(request,'Please Account Number Is Required')
            return render(request,'withdraws/add-withdraw.html',context)
        if not accountName:
            messages.error(request,'Please Account Name Field Is Required')
            return render(request,'withdraws/add-withdraw.html',context)

        if not accountCurrency:
            messages.error(request,'Please Account Currency Is Required')
            return render(request,'withdraws/add-withdraw.html',context)

        if not withdrawAmount:
            messages.error(request,'Please Withdraw Amount Is Required To Continue')
            return render(request,'withdraws/add-withdraw.html',context)

        if not newBalance:
            messages.error(request,'Please Account Current Balance Is Required')
            return render(request,'withdraws/add-withdraw.html',context)

        if withdrawAmount <= '0':
            messages.error(request,'Please You Have Zero Account Balance')
            return render(request,'withdraws/add-withdraw.html',context)


        if withdrawDate == 'mm/dd/yyyy':
            messages.error(request,'Please Select Withdraw Date To Continue')
            return render(request,'withdraws/add-withdraw.html',context)

        Withdraws.objects.create(withdraw_id=withdraw_id,accountNo=accountNo,accountName=accountName,accountType=accountType,ninNumber=ninNumber,
        contact=contact,accountCurrency=accountCurrency,oldBalance=oldBalance,charges=charges,withdrawAmount=withdrawAmount,
        newBalance=newBalance,withdrawDate=withdrawDate,transactionType=transactionType,regBy=request.user)

        Transaction.objects.create(transactionId=withdraw_id,accountNo=accountNo,accountName=accountName,accountType=accountType,transanctionType=transactionType,
        transactionAmount=withdrawAmount,balanceAmount=newBalance,regBy =request.user)
        #save the withdraw charge to count total revenue
        accountCharges.objects.create(transactionId = withdraw_id,accountNo=accountNo,accountName=accountName,accountType=accountType,
        chargeType=transactionType,oldBalance=oldBalance,chargeAmount=charges,newBalance=newBalance,regBy= request.user)

         #calling the members balance to update amount
        memberBalance = Members.objects.get(pk = accountNo)
        memberBalance.balance = newBalance
        memberBalance.save()

        messages.success(request,'Withdraw Transaction SuccessFully Saved')
        return redirect('withdraws')
        
        
#function to delete withdraw transaction
@login_required(login_url='/authentication/login')
def delete_withdraw(request,withdraw_id):
    withdraw = Withdraws.objects.get( pk = withdraw_id)
    withdraw.delete()
    messages.success(request,'Withdraw Transaction Successfully  Deleted')
    return redirect('withdraws')

@login_required(login_url='/authentication/login')
def update_withdraw(request,withdraw_id):

    withdraw = Withdraws.objects.get( pk = withdraw_id)
    context={
        'withdraw': withdraw,
        'values': withdraw,

    }
    if request.method  == 'GET':
        return render(request,'withdraws/update-withdraw.html',context)

    if request.method == 'POST':
        accountNo = request.POST['accountNo']
        accountName = request.POST['accountName']
        accountType = request.POST['accountType']
        accountCurrency = request.POST['accountCurrency']
        ninNumber = request.POST['ninNumber']
        contact = request.POST['contact']
        oldBalance = request.POST['oldBalance']
        charges = request.POST['charges']
        withdrawAmount = request.POST['withdrawAmount']
        newBalance = request.POST['newBalance']
        withdrawDate = request.POST['withdrawDate']

        if accountNo =='Please Select Account No':
            messages.error(request,'Please Select account No')
            return render(request,'withdraws/update-withdraw.html',context)

        if not withdrawAmount:
            messages.error(request,'Please Withdraw Amount Field Is Required')
            return render(request,'withdraws/update-withdraw.html',context)

        if not withdrawDate:
            messages.error(request,'Please Select Transaction Date !!!')
            return render(request,'withdraws/update-withdraw.html',context)

        withdraw.accountNo = accountNo
        withdraw.accountName = accountName
        withdraw.accountType = accountType
        withdraw.accountCurrency = accountCurrency
        withdraw.ninNumber = ninNumber
        withdraw.contact = contact
        withdraw.oldBalance =oldBalance
        withdraw.charges = charges
        withdraw.withdrawAmount = withdrawAmount
        withdraw.newBalance = newBalance
        withdraw.withdrawDate = withdrawDate
        withdraw.save()
        messages.success(request,'Withdraw Transaction Updated SuccessFully')
        return redirect('withdraws')

#function to fetch memeber data
@login_required(login_url='/authentication/login')
def memberAccountType(request):
    if request.method == 'GET':
        selectedAccount = request.GET['client_response']
        accountData = Members.objects.filter(accountNo = selectedAccount).first().accountType
        response_data ={}
        response_data['accountType'] = accountData
       
        return JsonResponse(response_data)

@login_required(login_url='/authentication/login')
def memberAccountName(request):
    if request.method =='GET':
        selectedAccount = request.GET['client_response']
        accountData =Members.objects.filter(accountNo = selectedAccount).first().accountName
        response_data = {}
        response_data['accountName'] = accountData
        print(accountData)

        return JsonResponse(response_data)

@login_required(login_url='/authentication/login')
def memberAccountBalance (request):
    if request.method =='GET':
        selectedAccount = request.GET['client_response']
        accountData =Members.objects.filter(accountNo = selectedAccount).first().balance 
        response_data = {}
        response_data['balance'] = accountData
        print(accountData)

        return JsonResponse(response_data)

@login_required(login_url='/authentication/login')
def memberAccountCurrency(request):
    if request.method =='GET':
        selectedAccount = request.GET['client_response']
        accountData =Members.objects.filter(accountNo = selectedAccount).first().accountCurrency
        response_data = {}
        response_data['accountCurrency'] = accountData
        print(accountData)

        return JsonResponse(response_data)

@login_required(login_url='/authentication/login')
def memberNinNumber(request):
    if request.method =='GET':
        selectedAccount = request.GET['client_response']
        accountData =Account.objects.filter(accountNo = selectedAccount).first().ninNumber
        response_data = {}
        response_data['ninNumber'] = accountData
   

        return JsonResponse(response_data)

@login_required(login_url='/authentication/login')
def memberContact(request):
    if request.method =='GET':
        selectedAccount = request.GET['client_response']
        accountData =Account.objects.filter(accountNo = selectedAccount).first().phoneNo1
        response_data = {}
        response_data['phoneNo1'] = accountData
        

        return JsonResponse(response_data)
#select account Charges per withdraw account Type
@login_required(login_url='/authentication/login')
def withdrawCharge(request):
    if request.method =='GET':
        selectedAccount = request.GET['client_response']
        accountData =Account_Types.objects.filter(accountType = selectedAccount).first().withdrawCharge
        response_data = {}
        response_data['withdrawCharge'] = accountData
        print(accountData)

        return JsonResponse(response_data)

@login_required(login_url='/authentication/login')
def withdraw_excel(request):
    response = HttpResponse(content_type = 'application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename = Withdraws'+ str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding = 'utf-8')
    ws = wb.add_sheet('Withdraws')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Withdraw Id','Account No','Account Name','Account Type','Currency','Old Balance','Withdraw','New Balance','Withdraw Date']

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)
    font_style = xlwt.XFStyle()
    rows = Withdraws.objects.all().values_list('withdraw_id','accountNo','accountName','accountType','accountCurrency','oldBalance','withdrawAmount','newBalance','dateReg')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)
    wb.save(response)
    return response

@login_required(login_url='/authentication/login')
def withdraw_csv(request):
    response = HttpResponse(content_type ='text/csv')
    response['Content-Disposition'] = 'attachment; filename = Withdraws'+str(datetime.datetime.now())+'.csv'
    writer = csv.writer(response)
    writer.writerow(['Withdraw Id','Account No','Account Name','Account Type','Currency','Old Balance','Withdraw','New Balance','Withdraw Date'])
    withdraws = Withdraws.objects.all()

    for withdraw in withdraws:
        writer.writerow([withdraw.withdraw_id,withdraw.accountNo,withdraw.accountName,
        withdraw.accountType,withdraw.accountCurrency,withdraw.oldBalance,withdraw.withdrawAmount,
        withdraw.newBalance,withdraw.dateReg])
    return response


@login_required(login_url='/authentication/login')
def search_withdraw(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        withdraws = Withdraws.objects.filter(accountNo__istartswith=search_str) | Withdraws.objects.filter(
            accountName__icontains =search_str) | Withdraws.objects.filter(newBalance__icontains = search_str) | Withdraws.objects.filter(
                accountType__istartswith=search_str) | Withdraws.objects.filter(newBalance__istartswith = search_str) | Withdraws.objects.filter(
                    accountCurrency__icontains=search_str) | Withdraws.objects.filter(withdrawDate__istartswith=search_str)
                
        data = withdraws.values()
        return JsonResponse(list(data), safe=False)
        
