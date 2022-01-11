from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING

# Create your models here.
class accountCharges(models.Model):
    transactionId = models.CharField(max_length=266,primary_key=True)
    accountNo = models.CharField(max_length=266,blank=False,db_index=True)
    accountName = models.CharField(max_length=266,blank=False,db_index=True)
    accountType = models.CharField(max_length=266,blank=False)
    chargeType = models.CharField(max_length=100,blank=False)
    oldBalance = models.FloatField()
    chargeAmount = models.FloatField()
    newBalance = models.FloatField()
    regDate = models.DateTimeField(auto_now_add=True)
    regBy = models.ForeignKey(to=User,on_delete=DO_NOTHING)

    def __str__(self):
            return self.transactionId
        
    class Meta:
        ordering = ('-regDate',)

    class Meta:
            verbose_name_plural = 'Account Charges'


