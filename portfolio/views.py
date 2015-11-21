from django.shortcuts import render

from .models import *


def portfolio(request):

    return render(request, 'portfolio/_portfolio.html')
