from django.shortcuts import render
from .models import PresidentMessage

# Create your views here.
def about_us(request):
    return render(request, 'about_us/about_us.html')


def msg_from_president(request):

    try:
        messages = PresidentMessage.objects.filter(is_active=True)
        print(messages)
    except PresidentMessage.DoesNotExist:
        messages = None
    
    return render(request, 'about_us/msg_from_president.html', {'messages': messages})