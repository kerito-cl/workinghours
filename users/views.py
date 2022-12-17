from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import ListView, CreateView
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

@login_required

def home(request):
    
    return render(request, 'users/home.html')





#class HoursCreateView(LoginRequiredMixin, CreateView):
#    model = Profile
#    fields = ['hours', 'minutes']
#    template_name = 'users/home.html'

#    def form_valid(self, form):
#        form.instance.author = self.request.user
#        return super().form_valid(form)

@login_required

def profile(request):
     
    return render(request, 'users/profile.html')



