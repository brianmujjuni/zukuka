from django.db import models
from django.db.models.fields.related import ForeignKey

from account_types.models import Account_Types
from currency.models import Currency

# Create your models here.
class Members(models.Model):
    
    accountNo = models.CharField(primary_key=True,max_length=266,unique=True)
    accountName = models.CharField(max_length=266,blank=False)
    accountType = models.CharField(max_length=266,blank=False)
    accountCurrency = models.CharField(max_length=50,default='UGX',blank=False)
    firstName = models.CharField(max_length=266,blank=False)
    lastName = models.CharField(max_length=266,blank=False)
    otherName = models.CharField(max_length=266,blank=True)
    accountStatus = models.CharField(max_length=20,null=False)
    balance = models.FloatField(default=0)
    regDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.accountNo
    
    class Meta:
       ordering = ('-regDate',)

    class Meta:
        verbose_name_plural = 'Member Accounts'


