from django.urls import path
from . import views
from .views import HoursCreateView 


urlpatterns = [
    path('',HoursCreateView.as_view() , name='users-home'),
]
