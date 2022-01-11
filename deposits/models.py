from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from account_types.models import Account_Types
from accounts.models import Account
from members.models import Members
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Deposits(models.Model):
    deposit_id = models.CharField(primary_key=True,editable=False,max_length=266)
    accountNo = models.CharField(max_length=266,blank=False)
    accountName = models.CharField(max_length=266,null=False)
    accountType = models.CharField(max_length=100,blank=False)
    accountCurrency = models.CharField(max_length=10)
    ninNumber = models.CharField(max_length=266,blank=True)
    contact = models.CharField(max_length=20)
    oldBalance = models.FloatField(blank=False,default=0)
    charges = models.IntegerField(blank=True,default=0)
    depositAmount = models.FloatField()
    newBalance = models.FloatField()
    depositDate = models.DateField()
    transactionType = models.CharField(max_length=50,default='deposit')
    regBy = models.ForeignKey(to=User,on_delete=DO_NOTHING)
    dateReg = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.accountNo
    
    class Meta:
       ordering = ('-dateReg',)