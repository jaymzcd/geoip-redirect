from django.shortcuts import render_to_response
from geoip.decorators import redirect_geoip

@redirect_geoip
def sample_view(request):
    return render_to_response('master.html')
