from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<slug:meetup_slug>/success', views.confirm_registration, name='confirm_registration'),
    path('<slug:meetup_slug>', views.meetup_detail, name='meetup_detail')
]
