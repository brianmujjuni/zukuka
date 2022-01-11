from django.contrib import admin

from accounts.models import Account, individual_standin

# Register your models here.
class IndividualAccount(admin.ModelAdmin):

    list_display=('accountNo','accountName','accountType','firstName','lastName','accountStatus','date1')
    search_fields=('accountNo','accountName','accountType','firstName','lastName','accountStatus','date1','gender')
    list_per_page = 20

class Standin(admin.ModelAdmin):
    list_display=('accountName','firstName','lastName','gender','dob','regBy','regDate')
    search_fields=('accountNo','accountName','ninNumber','firstName','lastName','gender','regDate')

admin.site.register(Account,IndividualAccount),
admin.site.register(individual_standin,Standin)