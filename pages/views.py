from django.shortcuts import render
from django.http import HttpResponse
from teachers.models import Teacher
from gallerys.models import Gallery
from summercamp.models import Camp
from lessons.models import Lesson
from activities.models import Activity

# Create your views here.


def index(request):
    teachers = Teacher.objects.all()
    gallerys = Gallery.objects.all()
    summercamp = Camp.objects.all()
    lessons = Lesson.objects.all()
    activities = Activity.objects.all()
    context = {
        'teachers': teachers,
        'gallerys': gallerys,
        'summercamp': summercamp,
        'lessons': lessons,
        'activities': activities
    }
    return render(request, 'pages/index.html', context)

def daycare(request):
    return render(request, 'pages/daycare.html')

def infantcare(request):
    return render(request, 'pages/infantcare.html')


def summercamp(request):
    summercamp = Camp.objects.all()
    context = {
        'summercamp': summercamp
    }
    return render(request, 'summercamp/summercamp.html', context)


def lessons(request):
    lessons = Lesson.objects.all()
    context = {
        'lessons': lessons
    }    
    return render(request, 'lessons/lessons.html', context)

def activities(request):
    activities = Activity.objects.all()
    context = {
        'activities': activities
    }    
    return render(request, 'activities/activities.html', context)


def contact(request):
    return render(request, 'pages/contact.html')


def teachers(request):
    return render(request, 'pages/teachers.html')
