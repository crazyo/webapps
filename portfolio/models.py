from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class TopCategory(models.Model):

    user = models.ForeignKey(User)
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    revenue = models.DecimalField(max_digits=5, decimal_places=2)

class SubCategory(models.Model):
    user = models.ForeignKey(User)
    top_category = models.ForeignKey(TopCategory)
    name = models.CharField(max_length=20)
    revenue = models.DecimalField(max_digits=5, decimal_places=2)


class ReturnRate(models.Model):
    user = models.ForeignKey(User)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    date= models.DateTimeField('Date', blank=True, null=True)


    def __unicode__(self):
        if len(self.title) >= 30:
            return self.title[:27] + '...'
        return self.title