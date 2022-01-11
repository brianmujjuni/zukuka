
from django import urls
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',include('dashboard.urls')),
    path('authentication/',include('authentication.urls')),
    path('accounts/',include('accounts.urls')),
    path('branch/',include('branch.urls')),
    path('withdraws/',include('withdraws.urls')),
    path('deposits/',include('deposits.urls')),
    path('members/',include('members.urls')),
    path('transactions/',include('transactions.urls')),
    path('currency/',include('currency.urls')),
    path('account_types/',include('account_types.urls')),
    path('accountCharges/',include('accountCharges.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
