from django.core import paginator
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from account_types.models import Account_Types
from currency.models import Currency
from .models import Account, individual_standin
from accountCharges.models import accountCharges
import json
from django.http import  JsonResponse, response,HttpResponse
from members.models import Members
import csv
import xlwt
import datetime

# Create your views here.
@login_required(login_url='/authentication/login')
def index(request):


    accounts = Account.objects.order_by('-regDate','accountName').all()
    context={
        'accounts': accounts
    }
    return render(request,'accounts/index.html',context)

@login_required(login_url='/authentication/login')
def add_accounts(request):
    accountTypes =Account_Types.objects.order_by('-regDate').filter(accountStatus = 'True')
    currencyCode = Currency.objects.all()
    context ={
        'currencyCode': currencyCode,
        'accountTypes': accountTypes,
        'values': request.POST,
    }
    
    if request.method == 'GET':
        return render(request,'accounts/add_account.html',context)
    
    if request.method == 'POST':
        accountNo = request.POST['accountNo']
        accountType = request.POST['accountType']
        currency = request.POST['currency']
        accountName = request.POST['accountName']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        otherName = request.POST['otherName']
        gender =request.POST['gender']
        dob = request.POST['dob']
        nationality = request.POST['nationality']
        religion = request.POST['religion']
        ninNumber = request.POST['ninNumber']
        ninImage = request.POST['ninImage']
        phoneNo1 = request.POST['phoneNo1']
        phoneNo2 = request.POST['phoneNo2']
        email =request.POST['email']
        occupation = request.POST['occupation']
        companyName = request.POST['companyName']
        nextOfKinName = request.POST['nextOfKinName']
        relationship = request.POST['relationship']
        contact = request.POST['contact']
        profilePic = request.POST['profilePic']
        openingFees = request.POST['openingFees']
        accountStatus = request.POST['accountStatus']
        regDate = request.POST['date1']
        
        
        if not accountNo:
            messages.error(request, 'Please account Number cant be Blank')
            return render(request,'accounts/add_account.html',context)

        if not accountName:
            messages.error(request, 'Please Asign Account a name')
            return render(request,'accounts/add_account.html',context)

        if not firstName and lastName:
            messages.error(request,'Please first name and last name are required')
            return render(request,'accounts/add_account.html',context)
        if not accountStatus :
            messages.error(request,'Please Select Account Status')
            return render(request, 'accounts/add_account.html', context)

        if not currencyCode:
            messages.error(request,'Please Account Currency Field Cant Be Blank')
            return render(request, 'accounts/add_account.html', context)

        if not accountType:
            messages.error(request,'Please Select Account Type Field To Continue')
            return render(request, 'accounts/add_account.html', context)

        if not nationality:
            messages.error(request,'Please Nationality Field Is Required To Continue')
            return render(request, 'accounts/add_account.html', context)

        if not phoneNo1:
            messages.error(request,'Please Client Phone Number One Is Required')
            return render(request, 'accounts/add_account.html', context)

        if not relationship:
            messages.error(request,'Please Provide Account Relationship To Next Of Kin')
            return render(request, 'accounts/add_account.html', context)

        if not nextOfKinName:
            messages.error(request,'Please Provide Account Next Of Kin Name To Continue')
            return render(request, 'accounts/add_account.html', context)

        if not contact:
            messages.error(request,'Please Provide Account Next Of Kin Contact To Continue')
            return render(request, 'accounts/add_account.html', context)

        if not openingFees:
            messages.error(request,'Opening Fees must be Paid ')
            return render(request, 'accounts/add_account.html', context)

        Account.objects.create(accountNo=accountNo,accountName=accountName,accountType=accountType,
        currency=currency,firstName=firstName,lastName=lastName,otherName=otherName,gender=gender,dob=dob,
        nationality=nationality,religion=religion,ninNumber=ninNumber,ninImage=ninImage,phoneNo1=phoneNo1,
        phoneNo2=phoneNo2,email=email,occupation=occupation,companyName=companyName,nextOfKinName=nextOfKinName,
        relationship=relationship,contact=contact,profilePic=profilePic,openingFees=openingFees,
        accountStatus=accountStatus,regDate=regDate,regBy =request.user,)

        Members.objects.create(accountNo=accountNo,accountName=accountName,accountType=accountType,
        accountCurrency=currency,firstName=firstName,lastName=lastName,otherName=otherName,accountStatus=accountStatus)
       
        messages.success(request,'Individual Account saved successfully')

        return redirect('add-standin')

    
@login_required(login_url='/authentication/login')
def update_accounts(request,accountNo):
    account =Account.objects.get(pk=accountNo)
    member = Members.objects.get(pk = accountNo)

    context ={
        'account': account,
        'values': account
    }

    if request.method == 'GET':
        return render(request,'accounts/update_account.html',context)
    if request.method == 'POST':
       
        accountType = request.POST['accountType']
        currency = request.POST['currency']
        accountName = request.POST['accountName']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        otherName = request.POST['otherName']
        gender =request.POST['gender']
        dob = request.POST['dob']
        nationality = request.POST['nationality']
        religion = request.POST['religion']
        ninNumber = request.POST['ninNumber']
        ninImage = request.POST['ninImage']
        phoneNo1 = request.POST['phoneNo1']
        phoneNo2 = request.POST['phoneNo2']
        email =request.POST['email']
        occupation = request.POST['occupation']
        companyName = request.POST['companyName']
        nextOfKinName = request.POST['nextOfKinName']
        relationship = request.POST['relationship']
        contact = request.POST['contact']
        profilePic = request.POST['profilePic']
        openingFees = request.POST['openingFees']
        accountStatus = request.POST['accountStatus']
        
        if not openingFees:
            messages.error(request,'Opening Fees Must Be Paid Before Regestration')
            return render(request,'accounts/update_account.html',context)

        account.accountType = accountType
        account.currency = currency
        account.accountName = accountName
        account.firstName = firstName
        account.lastName = lastName
        account.otherName = otherName
        account.gender = gender
        account.dob = dob
        account.nationality = nationality
        account.religion = religion
        account.ninNumber = ninNumber
        account.ninImage = ninImage
        account.phoneNo1 = phoneNo1
        account.phoneNo2 = phoneNo2
        account.email = email
        account.occupation = occupation
        account.companyName = companyName
        account.nextOfKin = nextOfKinName
        account.relationship =relationship
        account.contact = contact
        account.profilePic = profilePic 
        account.openingFees = openingFees
        account.accountStatus =accountStatus
        member.accountName = accountName
        member.accountType = accountType
        member.accountCurrency = currency
        member.firstName = firstName
        member.lastName = lastName
        member.otherName = otherName
        member.accountStatus = accountStatus
        member.save()
        account.save()
        messages.success(request,'Account Updated Successfully')
        return redirect('accounts')

@login_required(login_url='/authentication/login')
def delete_account(request,accountNo):
    account = Account.objects.get(pk=accountNo)
    members = Members.objects.get(pk = accountNo)
    members.delete()
    account.delete()
    messages.success(request,'Account deleted Successfully')
    return redirect('accounts')

@login_required(login_url='/authentication/login')
def add_standin(request):
    
    accounts = Members.objects.order_by('-regDate').all()
    context ={
        'accounts': accounts,
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request,'accounts/add_account_standin.html',context)
    if request.method == 'POST':
        accountNo = request.POST['accountNo']
        accountName = request.POST['accountName']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        gender = request.POST['gender']
        dob =  request.POST['dob']
        ninNumber = request.POST['ninNumber']
        contact = request.POST['contact']
        email = request.POST['email']
        if  not accountNo:
            messages.error(request,'Please Account Number Is Required ')
            return render(request,'accounts/add_account_standin.html',context)
        if not accountName:
            messages.error(request,'Please Account Name Is Required')
            return render(request,'accounts/add_account_standin.html',context)
        if not firstName:
            messages.error(request,'Please First Name Field Is Required')
            return render(request,'accounts/add_account_standin.html',context)
        if not  lastName:
            messages.error(request,'Please Last Name Field Is Required')
            return render(request,'accounts/add_account_standin.html',context)
        if not ninNumber:
            messages.error(request,'Please National Id Number Is Required')
            return render(request,'accounts/add_account_standin.html',context)
        if not contact:
            messages.error(request,'Please Mobile Contact Number Is Required')
            return render(request,'accounts/add_account_standin.html',context)
        if not gender:
            messages.error(request,'Please Gender Field Is Required')
            return render(request,'accounts/add_account_standin.html',context)
        individual_standin.objects.create(accountNo= accountNo,accountName=accountName,firstName=firstName,
        lastName=lastName,gender=gender,dob=dob,ninNumber=ninNumber,contact=contact,email=email,regBy=request.user)
        messages.success(request,'Account Stand In SuccessFully Registered')
            
        return redirect('view-standins')
        
@login_required(login_url='/authentication/login')
def view_accountStandIn(request):
    accountStandIns = individual_standin.objects.all()
    context={
        'accountStandIns': accountStandIns
    }
    return render(request,'accounts/view-account-standin.html',context)

@login_required(login_url='/authentication/login')
def delete_accountStandIn(request,id):
    standin = individual_standin.objects.get(pk=id)
    standin.delete()
    messages.success(request,'Individual Account Stand In SuccessFully Deleted')
    return redirect('view-standins')

@login_required(login_url='/authentication/login')
def update_standIn(request,id):

    standIn = individual_standin.objects.get(pk=id)
    context = {
        'standIn': standIn,
        'values': standIn
    }
    if  request.method =='GET':
        return render(request,'accounts/update-standIn.html',context)
    if request.method =='POST':
        accountNo = request.POST['accountNo']
        accountName = request.POST['accountName']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        gender = request.POST['gender']
        dob =  request.POST['dob']
        ninNumber = request.POST['ninNumber']
        contact = request.POST['contact']
        email = request.POST['email']

        if  not accountNo:
            messages.error(request,'Please Account Number Is Required ')
            return render(request,'accounts/update-standIn.html',context)
        if not accountName:
            messages.error(request,'Please Account Name Is Required')
            return render(request,'accounts/update-standIn.html',context)
        if not firstName:
            messages.error(request,'Please First Name Field Is Required')
            return render(request,'accounts/update-standIn.html',context)
        if not  lastName:
            messages.error(request,'Please Last Name Field Is Required')
            return render(request,'accounts/update-standIn.html',context)
        if not ninNumber:
            messages.error(request,'Please National Id Number Is Required')
            return render(request,'accounts/update-standIn.html',context)
        if not contact:
            messages.error(request,'Please Mobile Contact Number Is Required')
            return render(request,'accounts/update-standIn.html',context)
        if not gender:
            messages.error(request,'Please Gender Field Is Required')
            return render(request,'accounts/update-standIn.html',context)
        
        standIn.accountNo = accountNo
        standIn.accountName = accountName
        standIn.firstName = firstName
        standIn.lastName = lastName
        standIn.gender = gender
        standIn.dob = dob
        standIn.ninNumber = ninNumber
        standIn.contact = contact
        standIn.email = email
        standIn.save()
        messages.success(request,'Individual  Account Stand In Updated Successfully')
        return redirect('view-standins')

@login_required(login_url='/authentication/login')
def standInaccountName(request):
    if request.method =='GET':
        selectedAccount = request.GET['client_response']
        accountData =Account.objects.filter(accountNo = selectedAccount).first().accountName
        response_data = {}
        response_data['accountName'] = accountData
       
        return JsonResponse(response_data)

@login_required(login_url='/authentication/login')
def search_accounts(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        accounts = Account.objects.order_by('date1').filter(
            accountNo__icontains=search_str) | Account.objects.order_by('-date1').filter(accountName__istartswith=search_str) | Account.objects.order_by('-date1').filter(
                accountType__icontains=search_str) | Account.objects.order_by('-date1').filter(date1__icontains=search_str) | Account.objects.order_by('-date1').filter(accountStatus__icontains=search_str)
        data = accounts.values()
        return JsonResponse(list(data),safe=False)

@login_required(login_url='/authentication/login')
def accounts_excell(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename = Accounts'+ str(datetime.datetime.now())+ '.xls'
    wb = xlwt.Workbook(encoding = 'utf-8')
    ws = wb.add_sheet('Accounts')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns =['Account No','Account Name','Account Type','Currency','First Name','Last Name','Other Name','Gender','DOB','Nationality','Religion','Nin Number','Phone No1','Phone No2',
    'Email','Occupation','Company Name','Next Of Kin','Relationship','Contact','Opening Fees','Account Status','Reg Date']
    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)
    
    font_style = xlwt.XFStyle()

    rows = Account.objects.order_by('-regDate').all().values_list('accountNo','accountName','accountType','currency','firstName','lastName','otherName','gender','dob','nationality','religion','ninNumber','phoneNo1','phoneNo2',
    'email','occupation','companyName','nextOfKinName','relationship','contact','openingFees','accountStatus','regDate')

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)
    wb.save(response)
    return response

@login_required(login_url='/authentication/login')
def accounts_csv(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename = Accounts-'+ str(datetime.datetime.now())+'.csv'

    writer = csv.writer(response)
    writer.writerow(['Account No','Account Name','Account Type','Currency','First Name','Last Name','Other Name','Gender','DOB','Nationality','Religion','Nin Number','Phone No1','Phone No2',
    'Email','Occupation','Company Name','Next Of Kin','Relationship','Contact','Opening Fees','Account Status','Reg Date'])

    accounts = Account.objects.order_by('-date1').all()
    for account in accounts:
        writer.writerow([
            account.accountNo,account.accountName,account.accountType,account.currency,account.firstName,account.lastName,account.otherName,account.gender,account.dob,account.nationality,account.religion,account.ninNumber,
            account.phoneNo1,account.phoneNo2,account.email,account.occupation,account.companyName,account.nextOfKinName,account.relationship,account.contact,account.openingFees,account.accountStatus,account.regDate
        ])

    return response

@login_required(login_url='/authentication/login')
def standin_excell(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename = Accounts Stand Ins-'+ str(datetime.datetime.now())+ '.xls'
    wb = xlwt.Workbook(encoding = 'utf-8')
    ws = wb.add_sheet('Accounts Stand Ins')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns =['Account No','Account Name','First Name','Last Name','Gender','DOB','Nin Number','Contact','Email','Registered On']
    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)
    
    font_style = xlwt.XFStyle()

    rows = individual_standin.objects.order_by('-regDate').all().values_list('accountNo','accountName','firstName','lastName','gender','dob','ninNumber','contact','email','regDate')

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)
    wb.save(response)
    return response

@login_required(login_url='/authentication/login')
def standin_csv(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename = Accounts Stand Ins-'+ str(datetime.datetime.now())+'.csv'

    writer = csv.writer(response)
    writer.writerow(['Account No','Account Name','First Name','Last Name','Gender','DOB','Nin Number','Contact','Email','Registered On'])

    standins = individual_standin.objects.order_by('-regDate').all()
    for standin in standins:
        writer.writerow([
            standin.accountNo,standin.accountName,standin.firstName,standin.lastName,
            standin.gender,standin.dob,standin.ninNumber,standin.contact,standin.email,standin.regDate
        ])

    return response

@login_required(login_url='/authentication/login')
def search_standIns(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        accounts = individual_standin.objects.order_by('-regDate').filter(
            accountNo__icontains=search_str) | individual_standin.objects.order_by('-regDate').filter(
                accountName__istartswith=search_str) | individual_standin.objects.order_by('-regDate').filter(ninNumber__istartswith = search_str)
        data = accounts.values()
        return JsonResponse(list(data),safe=False)