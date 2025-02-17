from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from movie_site import settings
from movies.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    # path(''.include('movies.urls')),
    path('', index)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)