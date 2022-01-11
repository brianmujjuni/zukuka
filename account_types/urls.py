from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='account-types'),
    path('add-account-types',views.add_account_types,name='add-account-types'),
    path('delete-accountTypes/<int:id>',views.delete_accountType,name='delete-accountTypes'),
    path('edit-account-types/<int:id>',views.edit_accountType,name='edit-account-types'),
   
]