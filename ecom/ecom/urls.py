from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sklep.urls')),
    path('koszyk/', include('koszyk.urls')),
    path('payment/', include('payment.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
