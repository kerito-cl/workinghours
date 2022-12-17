from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Profile(models.Model):

    author = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.author.username} Profile'

    
class Hours(models.Model):
    worker = models.ForeignKey(User, on_delete=models.CASCADE)
    start = models.TimeField(default=timezone.now)
    end = models.TimeField(default=timezone.now)



    def get_absolute_url(self):
      return reverse('users-home')
