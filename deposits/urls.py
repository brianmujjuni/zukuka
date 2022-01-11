from django.urls import path
from .import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns =[

    path('',views.index,name='deposits'),
    path('add-deposits',views.add_account_deposits,name='add-deposits'),
    path('delete-deposit/<str:deposit_id>', views.delete_deposit, name="delete-deposit"),
    path('update-deposit/<str:deposit_id>', views.update_deposit, name="update-deposit"),
    path('Maccounttype/',views.memberAccountType,name='Maccounttype'),
    path('Maccountcurrency/',views.memberCurrency,name='Maccountcurrency'),
    path('Maccountname/',views.memberName,name='Maccountname'),
    path('MaccountNinNUmber/',views.memberninNumber,name='MaccountNinNUmber'),
    path('MBalance/',views.memberBalance,name='MBalance'),
    path('memberContact/',views.memberContact,name='memberContact'),
    path('deposit_excel',views.deposit_excel,name='deposit_excel'),
    path('deposit_csv',views.deposit_csv,name='deposit_csv'),
    path('search-deposit', csrf_exempt(views.search_deposit),name="search_deposit"),
    
]