"""abc_tots URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')),
    path('summercamp/', include('summercamp.urls')),
    path('lessons/', include('lessons.urls')),
    path('activities/', include('activities.urls')),
    path('daycare/', include('daycare.urls')),
    path('teachers/', include('teachers.urls')),
    path('gallerys/', include('gallerys.urls')),
    path('shopping_cart/', include('shopping_cart.urls',namespace='shopping_cart')),
    path('shopping_cart/', include('shopping_cart.urls',namespace='cart_detail')),
    path('admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
