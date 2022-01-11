from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING

from django.contrib.auth.models import User

from members.models import Members

# Create your models here.
class Account(models.Model):
    accountNo = models.CharField(max_length=266,primary_key=True)
    accountType = models.CharField(max_length=266,blank=False)
    currency = models.CharField(max_length=10,null=False)
    accountName = models.CharField(max_length=266,blank=False)
    firstName = models.CharField(max_length=266)
    lastName = models.CharField(max_length=266)
    otherName = models.CharField(max_length=266,blank=True)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    nationality = models.CharField(max_length=266)
    religion = models.CharField(max_length=20)
    ninNumber = models.CharField(max_length=266,blank=True)
    ninImage = models.ImageField(upload_to='nin_images/%Y/%m/%d/')
    phoneNo1 = models.CharField(max_length=20)
    phoneNo2 = models.CharField(max_length=20,blank=True)
    email =models.EmailField(blank=True)
    occupation = models.CharField(max_length=100)
    companyName = models.CharField(max_length=266)
    nextOfKinName = models.CharField(max_length=266)
    relationship = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    profilePic = models.ImageField(upload_to='photos/%Y/%m/%d/')
    openingFees = models.FloatField()
    accountStatus = models.CharField(max_length=20,default='Pending')
    regDate = models.DateField()
    date1 = models.DateTimeField(auto_now_add=True)
    regBy = models.ForeignKey(to=User,on_delete = DO_NOTHING)

    def __str__(self):
        return self.accountNo
    
    class Meta:
       ordering = ('-date1',)

    class Meta:
        verbose_name_plural = 'Individual Accounts'


class individual_standin(models.Model):
    accountNo = models.CharField(max_length=266,unique=True,blank=False,default='MZ-000-D')
    accountName = models.CharField(max_length=266)
    firstName = models.CharField(max_length=266,blank=False)
    lastName = models.CharField(max_length=266,blank=False)
    gender = models.CharField(max_length=10,default='Male')
    dob = models.DateField()
    ninNumber = models.CharField(max_length=266)
    contact = models.CharField(max_length=20,default='000,0000')
    email = models.EmailField(default='example@gmail.com')
    regDate = models.DateTimeField(auto_now=True)
    regBy = models.ForeignKey(to=User,on_delete=DO_NOTHING,default='1')

    def __str__(self):
        return self.accountNo

    class Meta:
       ordering = ('-regDate','accountNo',)
    
    class Meta:
        verbose_name_plural = 'Individual Account Standins'

    


