from django.contrib import admin
from .models import Members

# Register your models here.
class MemberData(admin.ModelAdmin):
    list_display = ('accountNo','accountName','accountType','accountCurrency','firstName','lastName','accountStatus','balance')
    search_fields =('accountNo','accountName','accountType','firstName','accountCurrency','lastName','regDate','accountStatus','balance')
    list_per_page = 10

admin.site.register(Members,MemberData)