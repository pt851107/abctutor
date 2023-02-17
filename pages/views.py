from django.shortcuts import render
from django.http import HttpResponse
from teachers.models import Teacher
from gallerys.models import Gallery
from summercamp.models import Camp
from lessons.models import Lesson
from activities.models import Activity
from contacts.models import Comment
from django.contrib import messages


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
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        title = request.POST['subject']
        message = request.POST['message']
        comment = Comment(
            name=name, email=email, title=title, message=message)
        comment.save()
        messages.success(request, 'Comment send!')
        return render(request, 'pages/contact.html')


def teachers(request):
    teachers = Teacher.objects.all()
    context = {'teachers': teachers}
    return render(request, 'teachers/teachers.html', context)


def daycare(request):
    return render(request, 'daycare/daycare.html')


def infantcare(request):
    return render(request, 'infantcare/infantcare.html')
