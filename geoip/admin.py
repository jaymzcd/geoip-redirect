from django.contrib import admin
from geoip.models import GeoIPRecord, IPRedirectEntry

admin.site.register(GeoIPRecord)
admin.site.register(IPRedirectEntry)
