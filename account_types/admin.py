from django.contrib import admin

from account_types.models import Account_Types

# Register your models here.
class AccountType(admin.ModelAdmin):
    list_display=('branchName','accountType','currencyCode','minimumBalance','withdrawCharge','accountStatus','regBy','regDate')
    search_fields =('accountType','branchName','regDate','accountStatus')
    list_per_page = 10
    
admin.site.register(Account_Types,AccountType),
