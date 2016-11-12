from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns(
    url(r'^admin/', admin.site.urls),
    url(r'', include('ACCOUNTS.urls')),
)

urlpatterns += patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # Static files url.
    (r'^site_media/media/(?P<path>.*)$', 'django.views.static.serve',
                                   {'document_root': settings.MEDIA_ROOT}),
    (r'^site_media/static/(?P<path>.*)$', 'django.views.static.serve',
                                {'document_root': settings.STATIC_ROOT}),
)
