from django.contrib import admin
from .models import Teacher

# Register your models here.


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('id', 'title', 'description')
    list_per_page = 20


admin.site.register(Teacher, TeacherAdmin)
