from django.contrib import messages
from django.shortcuts import redirect, render
import members
from members.models import Members
from accounts.models import Account
from django.http import  JsonResponse, response,HttpResponse
from django.contrib.auth.decorators import login_required
import json
import datetime 
import csv
import xlwt



# Create your views here.
@login_required(login_url='/authentication/login')
def index(request):
    members = Members.objects.filter(accountStatus='Active')
    context = {
        'members':members
    }
    return render(request,'members/index.html',context)

@login_required(login_url='/authentication/login')
def view_pendingAccounts(request):
    members = Members.objects.filter(accountStatus = 'Pending')
    context ={
        'members': members
    }
    return render(request,'members/view-pending.html',context)

@login_required(login_url='/authentication/login')
def view_dormantAccounts(request):
    members = Members.objects.filter(accountStatus='Dormant')
    context ={
        'members': members
    }
    return render(request,'members/view-dormant.html',context)

@login_required(login_url='/authentication/login')
def delete_member(request, accountNo):
    members = Members.objects.get(pk = accountNo)
    individualAccount = Account.objects.get(pk = accountNo)
    individualAccount.delete()
    members.delete()
    messages.success(request,'Member Account Number Successfully Deleted')
    return redirect('members')

@login_required(login_url='/authentication/login')
def update_status(request,accountNo):
    members = Members.objects.get(pk=accountNo)
    individualAccount = Account.objects.get(pk=accountNo)
    context={
        'members':members,
        'values': members
    }
    if request.method =='GET':
        return render(request,'members/update-status.html',context)
    if request.method == 'POST':
        accountStatus = request.POST['accountStatus']

        
        if not accountStatus:
            messages.error(request,'Please Account Status Field Is Rquired To Perform Update')
            return render(request,'members/update-status.html',context)
        if accountStatus =='Please Select Account Status':
            messages.error(request,'Please Select Account Status To Continue')
            return render(request,'members/update-status.html',context)

        members.accountStatus = accountStatus
        individualAccount.accountStatus = accountStatus
        members.save()
        individualAccount.save()
        if accountStatus =='Active':
            messages.success(request,'Account Status SuccessFully Update')
            return redirect('members')
        elif accountStatus =='Pending':
            messages.success(request,'Account Status Successfully Updated')
            return redirect('view-pending-accounts')
        else:
            messages.success(request,'Account Status SuccessFully Update')
            return redirect('view-dormant-accounts')

    messages.success(request,'Account Status SuccessFully Update')
    return redirect('members')

@login_required(login_url='/authentication/login')      
def members_active(request):
    response = HttpResponse(content_type = 'application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename = Active Member'+ str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding = 'utf-8')
    ws = wb.add_sheet('Members')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Account No','Account Name','Account Type','Account Currency','First Name','Last Name','Balance','regDate']

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)
    font_style = xlwt.XFStyle()
    rows = Members.objects.filter(accountStatus='Active').values_list('accountNo','accountName','accountType','accountCurrency','firstName','lastName','balance','regDate')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)
    wb.save(response)
    return response

@login_required(login_url='/authentication/login')
def members_active_csv(request):
    response = HttpResponse(content_type ='text/csv')
    response['Content-Disposition'] = 'attachment; filename = Active Members'+str(datetime.datetime.now())+'.csv'
    writer = csv.writer(response)
    writer.writerow(['Account No','Account Name','Account Type','Account Currency','First Name','Last Name','Balance','regDate'])
    members= Members.objects.filter(accountStatus='Active')

    for members in members:
        writer.writerow([members.accountNo,members.accountName,members.accountType,members.accountCurrency,
        members.firstName,members.lastName,members.balance,members.regDate])
    return response

@login_required(login_url='/authentication/login')
def members_pending(request):
    response = HttpResponse(content_type = 'application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename = Pending Member'+ str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding = 'utf-8')
    ws = wb.add_sheet('Pending Members')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Account No','Account Name','Account Type','Account Currency','First Name','Last Name','Balance','regDate']

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)
    font_style = xlwt.XFStyle()
    rows = Members.objects.filter(accountStatus='Pending').values_list('accountNo','accountName','accountType','accountCurrency','firstName','lastName','balance','regDate')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)
    wb.save(response)
    return response

@login_required(login_url='/authentication/login')
def members_pending_csv(request):
    response = HttpResponse(content_type ='text/csv')
    response['Content-Disposition'] = 'attachment; filename = Pending Members'+str(datetime.datetime.now())+'.csv'
    writer = csv.writer(response)
    writer.writerow(['Account No','Account Name','Account Type','Account Currency','First Name','Last Name','Balance','regDate'])
    members= Members.objects.filter(accountStatus='Active')

    for members in members:
        writer.writerow([members.accountNo,members.accountName,members.accountType,members.accountCurrency,
        members.firstName,members.lastName,members.balance,members.regDate])
    return response

@login_required(login_url='/authentication/login')
def members_dormant(request):
    response = HttpResponse(content_type = 'application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename = Dormant Member'+ str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding = 'utf-8')
    ws = wb.add_sheet('Dormant Members')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Account No','Account Name','Account Type','Account Currency','First Name','Last Name','Balance','regDate']

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)
    font_style = xlwt.XFStyle()
    rows = Members.objects.filter(accountStatus='Dormant').values_list('accountNo','accountName','accountType','accountCurrency','firstName','lastName','balance','regDate')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)
    wb.save(response)
    return response

@login_required(login_url='/authentication/login')
def members_dormant_csv(request):
    response = HttpResponse(content_type ='text/csv')
    response['Content-Disposition'] = 'attachment; filename = Dormant Members' + str(datetime.datetime.now())+'.csv'
    writer = csv.writer(response)
    writer.writerow(['Account No','Account Name','Account Type','Account Currency','First Name','Last Name','Balance','regDate'])
    members= Members.objects.filter(accountStatus='Active')

    for members in members:
        writer.writerow([members.accountNo,members.accountName,members.accountType,members.accountCurrency,
        members.firstName,members.lastName,members.balance,members.regDate])
    return response

@login_required(login_url='/authentication/login')
def search_activeMembers(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        members = Members.objects.order_by('-regDate').filter(accountStatus ='Active',accountNo__icontains=search_str) | Members.objects.order_by('-regDate').filter(accountStatus = 'Active',accountName__icontains=search_str)
            
        data = members.values()
        return JsonResponse(list(data),safe=False)

@login_required(login_url='/authentication/login')
def search_dormantMembers(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        members = Members.objects.order_by('-regDate').filter(accountStatus ='Dormant',accountNo__icontains=search_str) | Members.objects.order_by('-regDate').filter(accountStatus = 'Dormant',accountName__icontains=search_str)
            
        data = members.values()
        return JsonResponse(list(data),safe=False)

@login_required(login_url='/authentication/login')
def search_PendingMembers(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        members = Members.objects.order_by('-regDate').filter(accountStatus ='Pending',accountNo__icontains=search_str) | Members.objects.order_by('-regDate').filter(accountStatus = 'Pending',accountName__icontains=search_str)
            
        data = members.values()
        return JsonResponse(list(data),safe=False)