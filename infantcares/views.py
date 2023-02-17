from django.shortcuts import render, get_object_or_404
from .models import Infantcare
# Create your views here.

def index(request):
    infantcares = Infantcare.objects.all()
    context = {'infantcares': infantcares}
    return render(request, 'infantcare/infantcare.html', context)
