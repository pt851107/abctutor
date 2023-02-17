from django.contrib import admin
from .models import Lesson
# Register your models here.

class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','location','created', 'updated']
    list_filter = ['id','name']
    
admin.site.register(Lesson, LessonAdmin)