from django.shortcuts import render, get_object_or_404
from .models import Activity
# Create your views here.

def index(request):
    activities = Activity.objects.all()
    context = {'activities':activities}
    return render(request,'activities/activities.html',context)

def activity_detail(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    return render(request, 'activities/activity_detail.html',{'activity':activity})