from django.http import HttpResponse

def save_target(request):
    response = HttpResponse()
    if request.POST['save']:
        response.set_cookie('geoip-target', request.POST['target'])
    else:
        unset(request.COOKIES['geoip-target'])
    return response
