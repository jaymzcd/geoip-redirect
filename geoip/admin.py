from django.contrib import admin
from geoip.models import GeoIPRecord, IPRedirectEntry, IgnoreURL

admin.site.register(GeoIPRecord)
admin.site.register(IPRedirectEntry)
admin.site.register(IgnoreURL)
