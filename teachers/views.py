from django.shortcuts import render, get_object_or_404
from .models import Teacher

# Create your views here.


def index(request):
    teachers = Teacher.objects.order_by('name')
    context = {'teachers': teachers}
    return render(request, 'teachers/teachers.html', context)


def teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    context = {'teacher': teacher}
    return render(request, 'teachers/teacher.html', context)
