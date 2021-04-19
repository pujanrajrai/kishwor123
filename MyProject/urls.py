from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('autoshop/', include('autoshop.urls')),
    path('travel/', include('travel.urls')),
    path('vehicle/', include('vehicle.urls')),
    path('accounts/', include('accounts.urls')),
    path('profiles/', include('profiles.urls')),
    path('contact/', include('contact.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
