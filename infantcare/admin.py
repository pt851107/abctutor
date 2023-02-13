from django.contrib import admin
from .models import Infantcare
# Register your models here.


class InfantcareAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'location',
                    'fees', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Infantcare, InfantcareAdmin)
