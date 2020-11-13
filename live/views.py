from description.models import *
from django.shortcuts import render

from .models import *


# Create your views here.
def main(request):
    events = False if LiveVideos.objects.count() == 0 else True

    try:
        desc = Description.objects.get()
    except Description.DoesNotExist:
        desc = {}
    
    return render(
        request,
        'index.html',
        {
            'page': 'Home',
            'events':events,
            'desc': desc
        }
    )
