from django.contrib import admin

from currency.models import Currency

# Register your models here.
class Currencies(admin.ModelAdmin):
    list_display=('currencyName','currencyCode','currencyStatus','regBy','date1')
    search_fields=('currencyName','currencyCode','currencyStatus')
    list_per_page = (20)
    
admin.site.register(Currency,Currencies),