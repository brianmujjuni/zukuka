from django.contrib import admin

from .models import Deposits

# Register your models here.
class DepositData(admin.ModelAdmin):
    list_display =('deposit_id','accountNo','accountName','accountType','oldBalance','depositAmount','depositDate')
    search_fields =('deposit_id','accountNo','accountName','accountType','depositDate','newBalance')
    list_per_page =10
admin.site.register(Deposits,DepositData)