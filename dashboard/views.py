from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
import datetime
from django.db.models.functions import TruncMonth
from accountCharges.models import accountCharges
from accounts.models import Account
from deposits.models import Deposits
from members.models import Members
from withdraws.models import Withdraws

# Create your views here.
@login_required(login_url='/authentication/login')
def index(request):
    todays_date = datetime.date.today()
    accounts =Members.objects.all()
    pendingAccounts = Members.objects.filter(accountStatus = 'Pending')
    pendingCount = pendingAccounts.count()
    account_count = accounts.count()

    dormantAccounts = Members.objects.filter(accountStatus = 'Dormant')[:5]
    dormantCount  = dormantAccounts.count()

    hugeBalance= Members.objects.order_by('-balance').all()[:5]

    withdraws = Withdraws.objects.filter(dateReg__date = todays_date)
    withdraw_count = withdraws.aggregate(Sum('withdrawAmount'))
   
    deposits =Deposits.objects.filter(dateReg__date = todays_date )
    deposits_count = deposits.aggregate(Sum('depositAmount'))

    accountBalances = Members.objects.all()
    accountBalance_count = accountBalances.aggregate(Sum('balance'))

    totalunit=deposits.aggregate(Sum('depositAmount'))

    totalCharges = accountCharges.objects.filter(regDate__date = todays_date)
    totalrevenueCount = totalCharges.aggregate(Sum('chargeAmount'))

   

    context = {
        'dormantCount': dormantCount,
        'dormantAccounts': dormantAccounts,
        'pendingAccounts': pendingAccounts,
        'hugeBalance': hugeBalance,
        'totalunit': totalunit['depositAmount__sum'],
        'pendingCount': pendingCount,
        'account_count':account_count,
        'withdraw_count': withdraw_count['withdrawAmount__sum'],
        'deposits_count': deposits_count['depositAmount__sum'],
        'accountBalance_count': accountBalance_count['balance__sum'],
         'totalrevenueCount': totalrevenueCount['chargeAmount__sum']
    }
    return render(request,'dashboard/index.html',context)
