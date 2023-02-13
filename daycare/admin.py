from django.contrib import admin
from .models import Price

# Register your models here.


class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('id', 'name')
    list_per_page = 20


admin.site.register(Price, PriceAdmin)
