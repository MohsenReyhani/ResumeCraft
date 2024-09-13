from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import debug_toolbar

urlpatterns = [
    # path('/', admin.site.urls),
    path('app/', include('dashboard.urls')),
    path('app/admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    # urlpatterns = [path('__debug__/', include('debug_toolbar.urls')),] + urlpatterns
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls)), ] + urlpatterns