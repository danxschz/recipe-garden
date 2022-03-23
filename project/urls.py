from django.contrib import admin
from django.urls import include, path, re_path
from . import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('home.urls')),
    path('', include('recipes.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^home/media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]