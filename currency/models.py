from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING
# Create your models here.
class Currency(models.Model):
    currencyName = models.CharField(max_length=100,blank=False,)
    currencyCode = models.CharField(max_length=10,blank=False,default='UGX',unique=True)
    currencyStatus = models.CharField(max_length=20,blank=False)
    regBy = models.ForeignKey(to=User,on_delete=DO_NOTHING)
    regDate = models.DateField(default=now)
    date1 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.CurrencyCode

    class Meta:
        ordering = ('date1',)

    class Meta:
        verbose_name_plural ='Currencies'