

from django.urls import path, include

urlpatterns = [
    path('livestocks/', include('livestocks.urls')),
    path('admins/', include('admins.urls')),
    path('', include('accounts.urls'))
]
