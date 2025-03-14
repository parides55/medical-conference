from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def sponsors(request):
    try:
        return render(request, 'sponsors/sponsors.html')

    except Exception as e:
        messages.error(request, f"The following error occurred: {str(e)}")
        return redirect('sponsors')


def sponsorships(request):
    try:
        return render(request, 'sponsors/sponsorships.html')

    except Exception as e:
        messages.error(request, f"The following error occurred: {str(e)}")
        return redirect('sponsors')