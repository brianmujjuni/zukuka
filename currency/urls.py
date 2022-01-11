from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='view-curreny'),
    path('add-currency',views.add_currency,name='add-currency'),
    path('delete-currency/<int:id>', views.delete_currency, name="delete-currency"),
    path('edit-currency/<int:id>',views.edit_currency,name='edit-currency'),
    
]