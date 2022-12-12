from django.db import models
from django.contrib.auth.models import User

class Totaltime(models.Model):
    
    hours = models.IntegerField()
    minutes = models.IntegerField()
    days_work = models.IntegerField()
    worker = models.ForeignKey(User, on_delete=models.CASCADE)


