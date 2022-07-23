
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapi.urls'))
]
if settings.DEBUG: #settings.DEBUG is set to True
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

