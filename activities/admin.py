from django.contrib import admin
from .models import Activity
# Register your models here.

class ActivityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location', 'fees', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    
admin.site.register(Activity, ActivityAdmin)