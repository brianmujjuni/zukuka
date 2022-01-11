from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from withdraws.models import Withdraws

# Create your models here.
class Transaction(models.Model):
    transactionId = models.CharField(max_length=266,primary_key=True,default='000-00-D')
    accountNo = models.CharField(max_length=266,blank=False)
    accountName = models.CharField(max_length=266,blank=False)
    accountType = models.CharField(max_length=50,blank=False)
    transanctionType = models.CharField(max_length=30,blank=False)
    transactionAmount = models.FloatField()
    balanceAmount = models.FloatField()
    transactionDate = models.DateTimeField(auto_now_add=True)
    regBy = models.ForeignKey(to=User,on_delete=DO_NOTHING)

    def __str__(self):
        return self.accountNo
    
    class Meta:
       ordering = ('-transactionDate',)