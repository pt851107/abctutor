from django.contrib import admin
from .models import Gallery

# Register your models here.


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('id', 'name')
    list_per_page = 20


admin.site.register(Gallery, GalleryAdmin)
