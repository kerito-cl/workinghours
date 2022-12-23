from django.urls import path
from . import views
from .views import HoursCreateView,HoursUpdateView


urlpatterns = [
    path('',HoursCreateView.as_view() , name='users-home'),
    path('',HoursUpdateView.as_view() , name='users-home'),


]
