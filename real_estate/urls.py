from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('supersecret/', admin.site.urls),
]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MRDIA_ROOT)