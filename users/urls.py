from django.urls import path
from . import views
from .views import HoursCreateView, EndCreateView


urlpatterns = [
    path('',HoursCreateView.as_view() , name='users-home'),
    path('',EndCreateView.as_view() , name='users-home'),

]
