from django.urls import path
from .import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
    path('',views.index,name='branches'),
    path('add-branch',views.add_branch,name='add-branch'),
    path('delete-branch/<int:id>', views.delete_branch, name="delete-branch"),
    path('edit-branch/<int:id>',views.edit_branch,name='edit-branch'),

    path('view-branch-currencies',views.view_branchCurrency,name='view-branch-currencies'),
    path('add-branch-currencies',views.add_branchCurrency,name='add-branch-currencies'),
    path('delete-branchCurrency/<int:id>', views.delete_branchCurrencies, name="delete-branchCurrency"),
    path('edit-branch-currency/<int:id>',views.edit_branchCurrency,name='edit-branch-currency'),
    
    
]