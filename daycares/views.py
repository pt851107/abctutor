from django.shortcuts import render, get_object_or_404
from .models import Daycare
from shopping_cart.forms import CartAddProductForm

# Create your views here.


def index(request):
    daycare = Daycare.objects.all()
    context = {'daycare': daycare}
    return render(request, 'daycare/daycare.html', context)
