from django.shortcuts import render

# Create your views here.
def conference_info(request):
    return render(request, 'conference/conference_info.html')


def conference_schedule(request):
    return render(request, 'conference/conference_schedule.html')


def speakers(request):
    return render(request, 'conference/speakers.html')


def sponsors(request):
    return render(request, 'conference/sponsors.html')