from django.contrib import admin
from .models import Camp
# Register your models here.

class CampAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','location', 'fees', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']

admin.site.register(Camp, CampAdmin)