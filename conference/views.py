from django.shortcuts import render
from .models import Speaker

# Create your views here.
def conference_info(request):
    return render(request, 'conference/conference_info.html')


def conference_schedule(request):
    return render(request, 'conference/conference_schedule.html')


def speakers(request):
    
    speakers = Speaker.objects.all()
    
    context = {
        'speakers': speakers
    }
    
    return render(request, 'conference/speakers.html', context)


def sponsors(request):
    return render(request, 'conference/sponsors.html')