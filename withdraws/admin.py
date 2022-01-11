from django.contrib import admin

from .models import Withdraws

# Register your models here.
class withdrawData(admin.ModelAdmin):
    list_display=('withdraw_id','accountNo','accountName','accountType','oldBalance','charges','withdrawAmount','newBalance','withdrawDate')
    search_list =('withdraw_id','accountNo','accountName','newBalance','dateReg')
    list_per_page = 10
admin.site.register(Withdraws,withdrawData)