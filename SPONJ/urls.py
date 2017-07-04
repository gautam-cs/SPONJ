from django.contrib import admin
from django.conf.urls import include, url
from django.conf import settings
from django.views import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('ACCOUNTS.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^site_media/media/(?P<path>.*)$', include(static.serve),{'document_root': settings.MEDIA_ROOT}),
    # url(r'^site_media/static/(?P<path>.*)$', include(static.serve),{'document_root': settings.STATIC_ROOT}),
]

