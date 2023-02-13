from django.shortcuts import render, get_object_or_404
from .models import Gallery

# Create your views here.


def index(request):
    gallerys = Gallery.objects.all()
    context = {'gallerys': gallerys}
    return render(request, 'index.html', context)

#def gallery(request, gallery_id):
#    gallery = get_object_or_404(Gallery,pk=gallery_id)
#    context = {'gallery' : gallery}
#    return render(request, 'pages/gallery.html', context)