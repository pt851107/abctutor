from django.contrib import admin
from .models import Camp
# Register your models here.

class CampAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','location','created', 'updated']
    list_filter = ['id', 'name']

admin.site.register(Camp, CampAdmin)