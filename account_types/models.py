from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields.related import ForeignKey
from branch.models import Branches
from currency.models import Currency


# Create your models here.
class Account_Types(models.Model):
    branchName= models.CharField(max_length=50,blank=False)
    accountType = models.CharField(max_length=266)
    description = models.TextField(blank=True)
    currencyCode = models.CharField(max_length=20,blank=False)
    minimumBalance = models.FloatField(blank=False)
    withdrawCharge = models.IntegerField(default=0)
    accountStatus = models.BooleanField(default=False)
    regBy = models.ForeignKey(to=User,on_delete=DO_NOTHING)
    regDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.accountType
    
    class Meta:
       ordering = ('-regDate','branchName','accountStatus')

    class Meta:
        verbose_name_plural = 'Account Types'

