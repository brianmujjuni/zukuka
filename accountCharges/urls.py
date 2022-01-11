from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .import views

urlpatterns=[
    path('',views.index,name='accountCharges'),
    path('add-accountCharges/',views.add_charges,name='add-accountCharges'),
    path('update_charges/<str:transactionId>',views.update_charges,name='update_charges'),
    path('delete_charge/<str:transactionId>',views.delete_accountCharge,name='delete_charge'),
    path('search_charges', csrf_exempt(views.search_accountCharges),name="search_charges"),
    path('charge_name/',views.memberAccountName,name='accountchargeName'),
    path('charges_excell',views.charges_excell,name='charges_excell'),
    path('charges_csv',views.charges_csv,name='charges_csv'),
   
   
]