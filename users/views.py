from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from hours.models import Totaltime
from .models import Profile


@login_required

def profile(request):
     
    context = {"test": hours.objects.all()
               }
    return render(request, 'users/profile.html', context)

