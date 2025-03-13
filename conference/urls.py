from django.urls import path
from . import views

urlpatterns = [
    path('', views.conference_info, name='conference_info'),
    path('conference_schedule', views.conference_schedule, name='conference_schedule'),
    path('speakers', views.speakers, name='speakers'),
]
