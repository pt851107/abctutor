from django.contrib import admin
from .models import Daycare

# Register your models here.


class DaycaresAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]
    list_filter = ['id', 'name']


admin.site.register(Daycare, DaycaresAdmin)
