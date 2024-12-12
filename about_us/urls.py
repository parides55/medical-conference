from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_us, name='about_us'),
    path('msg_from_president', views.msg_from_president, name='msg_from_president'),
]