from django.shortcuts import render
from .models import Daycare

# Create your views here.


def index(request):
    daycares = Daycare.objects.all()
    context = {'daycares': daycares}
    return render(request, 'daycare/daycare.html', context)
