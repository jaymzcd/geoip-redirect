from django.template.loader import render_to_string
from geoip.models import GeoIPRecord, IPRedirectEntry
from django.utils.encoding import smart_str

class GeoIPMiddleWare(object):

    def __init__(self):
        self.redirect_inject = render_to_string('geoip/redirect.html')

    def process_response(self, request, response):
        """ Read in the users IP address from the request object. If we
        find a matching GeoIPRecord for it and that country code has an
        active redirect then inject the HTML into the template to show
        a lightbox to the user """

        inbound_ip = request.META['REMOTE_ADDR']
        user_code = GeoIPRecord.get_code(inbound_ip)
        redirect_list = IPRedirectEntry.objects.all().values_list('incoming_country_code', flat=True)

        if user_code in redirect_list and r'/admin' not in request.path:
            # Slight hack above to avoid hooking into admin
            response.content = smart_str(response.content) + smart_str(self.redirect_inject)
        return response
