from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .import views

urlpatterns=[
    path('',views.index,name='accounts'),
    path('add-accounts',views.add_accounts,name='add-accounts'),
    path('update-account/<str:accountNo>',views.update_accounts,name='update-account'),
    path('delete-account/<str:accountNo>', views.delete_account, name="delete-account"),
    path('search_accounts', csrf_exempt(views.search_accounts),name="search_accounts"),
    path('accounts-excell',views.accounts_excell,name='accounts-excell'),
    path('accounts-csv',views.accounts_csv,name='accounts-csv'),

    path('add-standin',views.add_standin,name='add-standin'),
    path('view-standins',views.view_accountStandIn,name='view-standins'),
    path('delete-standIn/<int:id>', views.delete_accountStandIn, name="delete-standIn"),
    path('update-standIn/<int:id>', views.update_standIn, name="update-standIn"),
    path('standInaccountName/',views.standInaccountName,name='standInaccountName'),
    path('standin-excell',views.standin_excell,name='standin-excell'),
    path('standin-csv',views.standin_csv,name='standin-csv'),
    path('search_standin', csrf_exempt(views.search_standIns),name="search_standin"),
]