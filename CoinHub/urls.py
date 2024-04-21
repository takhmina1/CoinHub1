from django.contrib import admin
from django.urls import path, include  
from .yasg import urlpatterns as yasg_urls
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('apps.users.urls')),
    path('api/finance/', include('apps.finance.urls')),
    path('api/faq', include('apps.faq.urls')),
    path('api/trading', include('apps.trading.urls')),

]

urlpatterns += yasg_urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
