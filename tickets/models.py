from django.db import models


# Create your models here.

class Notification(models.Model):
    nickname = models.CharField(max_length=255)
    state = models.BooleanField(default=False)
    email = models.EmailField()
    to_date = models.DateField()
    start_station = models.CharField(max_length=16)
    end_station = models.CharField(max_length=16)
    memo = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
