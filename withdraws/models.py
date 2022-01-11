from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields import TextField
from accounts.models import Account
import uuid
from currency.models import Currency
from account_types.models import Account_Types

from members.models import Members

# Create your models here.
class Withdraws(models.Model):
    withdraw_id = models.CharField(primary_key=True,max_length=266,unique=True)
    accountNo = models.CharField(max_length=266,blank=False,db_index=True)
    accountName = models.CharField(max_length=266,blank=False,db_index=True)
    accountType = models.CharField(max_length=50,blank=False,db_index=True)
    ninNumber = models.CharField(max_length=266,blank=False)
    contact = models.CharField(max_length=20)
    accountCurrency= models.CharField(max_length=50,blank=False)
    oldBalance = models.IntegerField()
    charges = models.IntegerField()
    withdrawAmount = models.IntegerField()
    newBalance = models.FloatField()
    withdrawDate = models.DateField()
    transactionType = models.CharField(max_length=50,default='withdraw',db_index=True)
    regBy = models.ForeignKey(to=User,on_delete = DO_NOTHING)
    dateReg = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.accountNo
    
    class Meta:
       ordering = ('-dateReg',)

    class Meta:
        verbose_name_plural = 'Withdraws'


