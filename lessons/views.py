from django.shortcuts import render, get_object_or_404
from .models import Lesson
# Create your views here.

def index(request):
    lessons = Lesson.objects.all()
    context = {'lessons':lessons}
    return render(request,'lessons/lessons.html',context)

def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'lessons/lesson_detail.html',{'lesson':lesson})