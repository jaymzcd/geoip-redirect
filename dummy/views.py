# Create your views here.
from django.shortcuts import render_to_response

def sample_view(request):
    return render_to_response('master.html')
