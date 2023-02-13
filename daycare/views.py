from django.shortcuts import render
from .models import Price

# Create your views here.


def index(request):
    prices = Price.objects.order_by('name')
    context = {'prices': prices}
    return render(request, 'pages/daycare.html', context)
