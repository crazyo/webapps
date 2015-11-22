from django.db import models
from django.contrib.auth.models import User


class Activity(models.Model):
    initiator = models.ForeignKey(User)
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    is_important = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']


class Comment(models.Model):
    author = models.ForeignKey(User)
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    activity = models.ForeignKey(Activity)
