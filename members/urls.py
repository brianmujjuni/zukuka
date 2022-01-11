from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .import views

urlpatterns =[
    path('',views.index,name='members'),
    path('delete-member/<str:accountNo>', views.delete_member, name="delete-member"),
    path('view-pending-accounts/',views.view_pendingAccounts,name='view-pending-accounts'),
    path('view-dormant-accounts/',views.view_dormantAccounts,name='view-dormant-accounts'),
    path('update-status/<str:accountNo>',views.update_status,name='update-status'),
    path('members_active/',views.members_active,name='members_active'),
    path('members_active_csv/',views.members_active_csv,name='members_active_csv'),
    path('members_pending/',views.members_pending,name='members_pending'),
    path('members_pending_csv/',views.members_pending_csv,name='members_pending_csv'),
    path('members_dormant/',views.members_dormant,name='members_dormant'),
    path('members_dormant_csv/',views.members_dormant_csv,name='members_dormant_csv'),
    path('search-activeMembers', csrf_exempt(views.search_activeMembers),name="search-activeMembers"),
    path('search-dormantMembers', csrf_exempt(views.search_dormantMembers),name="search-dormantMembers"),
    path('search-pendingMembers', csrf_exempt(views.search_PendingMembers),name="search-pendingMembers"),
]
