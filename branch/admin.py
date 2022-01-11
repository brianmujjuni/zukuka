from django.contrib import admin

from branch.models import Branch_Currency, Branches

# Register your models here.
class Branch(admin.ModelAdmin):
    list_display=('branchName','phoneNo1','phoneNo2','email','country','location','regBy','date1')
    search_fields=('branchName','email','country','location','date')
    list_per_page = 20

class BranchCurrency(admin.ModelAdmin):
    list_display=('branchName','currencyCode','exchangeRate','regBy','regDate')
    search_fields=('branchName','currencyCode')

admin.site.register(Branches,Branch),
admin.site.register(Branch_Currency,BranchCurrency),
