from django.contrib import admin
from django.urls import path, include  
from .yasg import urlpatterns as yasg_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('apps.users.urls')),
    path('api/finance/', include('apps.finance.urls')),
    path('api/', include('apps.trading.urls')),

]

urlpatterns += yasg_urls


