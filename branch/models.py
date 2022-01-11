from datetime import datetime
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields import CharField, DateField
from django.db.models.fields.related import ForeignKey
from django.http import request
from django.utils.timezone import now
from django.contrib.auth.models import User

from currency.models import Currency



# Create your models here.
class Branches(models.Model):
    branchName = models.CharField(max_length=266,blank=False)
    phoneNo1 = models.CharField(max_length=20)
    phoneNo2 = models.CharField(max_length=20)
    email = models.EmailField(blank=False)
    country = models.CharField(max_length=50,blank=False)
    location = models.CharField(max_length=266,blank=False)
    date = models.DateField(default=now)
    date1 = models.DateTimeField(auto_now_add=True)
    regBy = models.ForeignKey(to=User,on_delete=DO_NOTHING)

    def __str__(self):
        return self.branchName
    
    class Meta:
        ordering = ('-date',)

    class Meta:
        verbose_name_plural = 'Branches'

class Branch_Currency(models.Model):
    branchName = models.CharField(max_length=50,blank=False)
    currencyCode = models.CharField(max_length=10,blank=False)
    exchangeRate = models.IntegerField(default=0,blank=True)
    regBy =models.ForeignKey(to=User,on_delete=DO_NOTHING)
    regDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.branchName
    
    class Meta:
        ordering = ('-regDate','branchName',)

    class Meta:
        verbose_name_plural = 'Branch Currencies'
