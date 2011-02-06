from geoip.middleware import GeoIPMiddleware
from django.utils.decorators import decorator_from_middleware

redirect_geoip = decorator_from_middleware(GeoIPMiddleware)
