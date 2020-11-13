from description.models import *
from django.shortcuts import render

from .models import *


# Create your views here.
def main(request):
    #LiveVideos Model
    events = False if LiveVideos.objects.count() == 0 else True
    try:
        event = LiveVideos.objects.latest('id')
    except LiveVideos.DoesNotExist:
        event = {}
    
    #Description model
    try:
        desc = Description.objects.get()
    except Description.DoesNotExist:
        desc = {}
    
    return render(
        request,
        'index.html',
        {
            'events':events,
            'event':event,
            'desc': desc
        }
    )
