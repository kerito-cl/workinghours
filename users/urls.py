from django.urls import path
from . import views
from .views import HoursCreateView,HoursUpdateView, HoursDetailView


urlpatterns = [
    path('',HoursCreateView.as_view() , name='users-home'),
    path('hours/<int:pk>',HoursDetailView.as_view() , name='detail-work'),
    path('hours/<int:pk>/',HoursUpdateView.as_view() , name='stop-work')


]
