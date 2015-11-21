from django.shortcuts import render

from .models import *


def feed(request):
    activities = Activity.objects.all()
    context = {'activities': activities}
    return render(request, 'feed/_feed.html', context)
