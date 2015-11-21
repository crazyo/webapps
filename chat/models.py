from django.db import models


class Message(models.Model):
    author = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
