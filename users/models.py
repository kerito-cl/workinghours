from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone, dateformat
from datetime import timedelta

class Profile(models.Model):

    author = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.author.username} Profile'

    
class Hours(models.Model):
    worker = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    start = models.TimeField(default=timezone.now)
    end = models.TimeField(default=timezone.now)
     
    date_time = dateformat.format(timezone.now(), 'm-d-Y') 
   
#    @property
#    def duration(self):
#        if self.end is not None and self.start is not None:
#        return self.end - self.start

    def __str__(self):

        return self.date_time

    def get_absolute_url(self):
        return reverse('stop-work', kwargs={'pk':self.pk})

#class EndWork(models.Model):
#    worker = models.ForeignKey(User, on_delete=models.CASCADE)
#    finish_work = models.TimeField(default=timezone.now)

#class StartWork(models.Model):
#    worker = models.ForeignKey(User, on_delete=models.CASCADE)
#    start_work = models.TimeField(default=timezone.now)

