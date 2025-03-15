from django.shortcuts import render, redirect
from django.contrib import messages

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
