from django.db import models
from django.contrib.auth.models import User
from hours.models import Totaltime

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    hours = models.IntegerField()
    minutes = models.IntegerField()
    days_work = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} Profile'
