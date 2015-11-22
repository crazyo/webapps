from django.shortcuts import render

from .models import *


def feed(request):
    activities = Activity.objects.all()
    trimmed = []

    count = 0
    initiators = []
    dates = []
    for activity in activities:
        if activity.is_important:
            if count:
                dates.sort()
                trimmed.append({'initiator': ','.join(initiators),
                                'text': str(count) + ' activities...',
                                'date': dates[-1]})
                count = 0
                initiators = []
                dates = []
            trimmed.append(activity)
        else:
            count += 1
            if str(activity.initiator) not in initiators:
                initiators.append(str(activity.initiator))
            dates.append(activity.date)
    if count:
        dates.sort()
        trimmed.append({'initiator': ','.join(initiators),
                        'text': str(count) + ' activities...',
                        'date': dates[-1]})
    context = {'activities': trimmed}
    return render(request, 'feed/_feed.html', context)


def raw_feed(request):
    activities = Activity.objects.all()
    context = {'activities': activities}
    return render(request, 'feed/_feed_raw.html', context)
