from django.urls import path
from . import views
#from .views import HoursCreateView


urlpatterns = [
    path('',views.home , name='users-home')

]
