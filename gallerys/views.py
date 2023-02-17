from django.shortcuts import render, get_object_or_404
from .models import Gallery

# Create your views here.


def index(request):
    gallerys = Gallery.objects.all()
    context = {'gallerys': gallerys}
    return render(request, 'index.html', context)