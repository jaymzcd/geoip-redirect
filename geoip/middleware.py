from django.template.loader import render_to_string
from geoip.models import GeoIPRecord, IPRedirectEntry
from django.utils.encoding import smart_str

class GeoIPMiddleWare(object):

    def __init__(self):
        self.redirect_inject = render_to_string('geoip/redirect.html')

    def process_response(self, request, response):
        response.content = smart_str(response.content) + smart_str(self.redirect_inject)
        user_code = GeoIPRecord.get_code('92.52.69.82')
        redirect_list = IPRedirectEntry.objects.all().values_list('incoming_country_code', flat=True)
        print user_code
        print redirect_list
        return response

