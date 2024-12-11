from django.shortcuts import render

# Create your views here.
def conference(request):
    return render(request, 'conference/conference.html')