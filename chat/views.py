from django.shortcuts import render
from django.http import HttpResponse

from .models import *


def messages(request):
    if request.method == 'GET':
        msgs = Message.objects.all()
        context = {'messages': msgs}
        # print(context['messages'][0].text)
        return render(request, 'chat/_messages.html', context)

    if request.method == 'POST':
        msg = Message(author=str(request.user), text=request.POST.get('text'))
        msg.full_clean()
        msg.save()
        return HttpResponse()
