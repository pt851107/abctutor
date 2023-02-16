from django.contrib import admin
from .models import Lesson
# Register your models here.

class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','location', 'fees', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    
admin.site.register(Lesson, LessonAdmin)