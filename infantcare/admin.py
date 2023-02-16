from django.contrib import admin
from .models import Infantcare
# Register your models here.


class InfantcareAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]
    list_filter = ['id', 'name']


admin.site.register(Infantcare, InfantcareAdmin)
