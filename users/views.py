from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView
from .models import Profile, Hours
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UserWorkForm
from django.contrib import messages

@login_required

def home(request):
#    if request.method == 'POST':
#        form = UserWorkForm(request.POST)
#
#        if form.is_valid():
#            form.save()            
#            messages.success(request, f'Your worked has finished')
#            return redirect('profile')

    return render(request, 'users/home.html')





class HoursCreateView(LoginRequiredMixin, CreateView):
    model = Hours
    fields = ['start', 'end']
    

    template_name = 'users/home.html'

    def form_valid(self, form):
        form.instance.worker = self.request.user
        return super().form_valid(form)

#class HoursUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#    model = Hours
#    fields = ['end']
#    template_name = 'users/home.html'
#
#    def form_valid(self, uform):
#        uform.instance.worker = self.request.user
#        return super().form_valid(form)
#
#    def test_func(self):
#        post = self.get_object()
#        if self.request.user == post.worker:
#            return True
#        return False


@login_required

def profile(request):

        return render(request, 'users/profile.html')



