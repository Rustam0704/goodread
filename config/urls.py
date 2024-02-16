from config import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name="home"),
    path('users/', include("apps.users.urls")),
    # path('books/', include("books.urls")),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
