from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    hours = models.IntegerField(default=0)
    minutes = models.IntegerField(default=0)
    days_work = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.author.username} Profile'

    def get_absolute_url(self):

        return reverse('users-home')
