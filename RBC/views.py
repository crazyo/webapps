from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'dashborad/pages/index.html')

def flot(request):
    return render(request, 'dashborad/pages/flot.html')