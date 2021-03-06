from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^geoipredirect/', include('geoipredirect.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'example/ignore-me/', 'dummy.views.sample_view'),
    (r'example/', 'dummy.views.sample_view'),
    (r'^$', 'dummy.views.sample_view'),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
