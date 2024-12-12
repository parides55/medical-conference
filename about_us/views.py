from django.shortcuts import render

# Create your views here.
def about_us(request):
    return render(request, 'about_us/about_us.html')


def msg_from_president(request):
    return render(request, 'about_us/msg_from_president.html')