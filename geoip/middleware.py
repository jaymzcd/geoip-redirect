from django.template.loader import render_to_string
from geoip.models import GeoIPRecord
from django.utils.encoding import smart_str

class GeoIPMiddleWare(object):

    def __init__(self):
        self.redirect_inject = render_to_string('geoip/redirect.html')

    def process_response(self, request, response):
        response.content = smart_str(response.content) + smart_str(self.redirect_inject)
        user_code = GeoIPRecord.get_code('92.52.69.82')
        
        return response

