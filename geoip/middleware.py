from django.template.loader import render_to_string
from geoip.models import GeoIPRecord, IPRedirectEntry
from geoip.conf import geo_setting
from django.conf import settings
from django.utils.encoding import smart_str

class GeoIPMiddleWare(object):

    def __init__(self):
        self.redirect_inject = render_to_string('geoip/base_redirect.html')
        if geo_setting('DEBUG_IP'):
            self.DEBUG_IP = geo_setting('DEBUG_IP')
        else:
            self.DEBUG_IP = False

    def process_response(self, request, response):
        """ Read in the users IP address from the request object. If we
        find a matching GeoIPRecord for it and that country code has an
        active redirect then inject the HTML into the template to show
        a lightbox to the user """

        # The following is for inplace debugging forcing a particular IP
        if settings.DEBUG and self.DEBUG_IP:
            inbound_ip = self.DEBUG_IP
        else:
            inbound_ip = request.META['REMOTE_ADDR']

        user_code = GeoIPRecord.get_code(inbound_ip)
        redirect_list = IPRedirectEntry.objects.all()

        ccodes = redirect_list.values_list('incoming_country_code', flat=True)
        if user_code in ccodes and r'/admin' not in request.path:
            # Slight hack above to avoid hooking into admin
            code_index = list(ccodes).index(user_code) # use this to grab the template data
            redirect_data = redirect_list[code_index] # in theory this is the right one
            context = dict(redirect=redirect_data)

            if redirect_data.custom_message is not None:
                inject_data = render_to_string('geoip/custom_redirect.html', context)
            else:
                inject_data = self.redirect_inject # use one from __init__ time

            response.content = smart_str(response.content) + \
                smart_str(inject_data)

        return response
