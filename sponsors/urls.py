from django.urls import path
from . import views


urlpatterns = [
    path('', views.sponsors, name='sponsors'),
    path('/sponsorships/', views.sponsorships, name='sponsorships'),
]