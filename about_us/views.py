from django.shortcuts import render
from .models import PresidentMessage

# Create your views here.
def about_us(request):
    return render(request, 'about_us/about_us.html')


def msg_from_president(request):

    try:
        message = PresidentMessage.objects.get(is_active=True)
    except PresidentMessage.DoesNotExist:
        message = None
    
    return render(request, 'about_us/msg_from_president.html', {'message': message})