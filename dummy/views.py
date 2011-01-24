# Create your views here.
from django.http import HttpResponse

def sample_view(request):
    return HttpResponse('I am a sample response')
