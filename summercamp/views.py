from django.shortcuts import render, get_object_or_404
from .models import Camp
# Create your views here.

def index(request):
    summercamp = Camp.objects.all()
    context = {'summercamp':summercamp}
    return render(request,'summercamp/summercamp.html',context)

def camp_detail(request, camp_id):
    camp = get_object_or_404(Camp,pk=camp_id)
    return render(request, 'summercamp/camp_detail.html',{'camp':camp})