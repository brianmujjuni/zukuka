from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .import views

urlpatterns =[
    path('',views.index,name='transactions'),
    path('search-transactions',csrf_exempt(views.search_transactions),name='search-transactions'),
    path('members_transactions',views.members_transactions,name='members_transactions'),
    path('transaction-csv',views.transaction_csv,name='transaction-csv'),
    
]