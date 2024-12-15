from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Speaker

# Create your views here.
def conference_info(request):
    try:
        return render(request, 'conference/conference_info.html')

    except Exception as e:
        messages.error(request, f"The following error occurred: {str(e)}")
        return redirect('conference_info')


def conference_schedule(request):
    try:
        return render(request, 'conference/conference_schedule.html')

    except Exception as e:
        messages.error(request, f"The following error occurred: {str(e)}")
        return redirect('conference_schedule')


def speakers(request):
    
    try:
        speakers = Speaker.objects.all()
        
        context = {
            'speakers': speakers
        }
        
        return render(request, 'conference/speakers.html', context)

    except Speaker.DoesNotExist:
        messages.info(request, 'News not found.')
        return redirect('speakers')

    except Exception as e:
        messages.error(request, f"The following error occurred: {str(e)}")
        return redirect('speakers')
        


def sponsors(request):
    try:
        return render(request, 'conference/sponsors.html')

    except Exception as e:
        messages.error(request, f"The following error occurred: {str(e)}")
        return redirect('sponsors')