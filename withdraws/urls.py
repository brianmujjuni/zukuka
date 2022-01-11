from django.urls import path

from .import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns =[
    path('',views.index,name='withdraws'),
    path('add-withdraws',views.add_withdraws,name='add-withdraws'),
    path('delete-withdraw/<str:withdraw_id>',views.delete_withdraw,name='delete-withdraw'),
    path('update-withdraw/<str:withdraw_id>',views.update_withdraw,name='update-withdraw'),
    path('search-withdraw', csrf_exempt(views.search_withdraw),name="search_withdraw"),
    path('memberAccountType/',views.memberAccountType,name="memberAccountType"),
    path('memberAccountName/',views.memberAccountName,name='memberAccountName'),
    path('memberAccountCurrency/',views.memberAccountCurrency,name='memberAccountCurrency'),
    path('memberAccountBalance/',views.memberAccountBalance,name='memberAccountBalance'),
    path('memberNinNumber/',views.memberNinNumber,name='memberNinNumber'),
    path('memberContact/',views.memberContact,name='memberContact'),
    path('withdrawCharge/',views.withdrawCharge,name='withdrawCharge'),
    path('withdraw_excel',views.withdraw_excel,name='withdraw_excel'),
    path('withdraw_csv',views.withdraw_csv,name='withdraw_csv'),
   
]